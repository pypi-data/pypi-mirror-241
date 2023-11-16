from typing import Any, Dict, List, Optional
import requests

# JSON parser
import json

# system modules
import os
import re
import sys
import random
import time
from datetime import datetime, timedelta
from enum import Enum, auto
import certifi


class SentinelApi:
    # base URL of the product catalogue
    catalogue_odata_url = "https://catalogue.dataspace.copernicus.eu/odata/v1"
    auth_server_url = "https://identity.dataspace.copernicus.eu/auth/realms/CDSE/protocol/openid-connect/token"
    download_url = "https://zipper.dataspace.copernicus.eu/odata/v1"

    class AutoName(Enum):
        @staticmethod
        def _generate_next_value_(name, start, count, last_values):
            return name

    class ProductType(AutoName):
        SLC = auto()
        GRD = auto()
        OCN = auto()
        S2MSI2A = auto()
        S2MSI1C = auto()
        S2MS2Ap = auto()

    def __init__(self, user, password) -> None:
        self.user = user
        self.password = password

    def find(
        self,
        productType: ProductType,
        tile: str,
        init_date: datetime,
        end_date: datetime,
        cloud_cover: int,
        limit: Optional[int] = None,
    ) -> List[Dict[str, Any]]:
        """Finds a list of products using the given filters

        Args:
            productType (ProductType): type of product to find
            tile (str): the Tile in the Sentinel system
            init_date (datetime): the init date of the search
            end_date (datetime): the end date of the search
            cloud_cover (int): the maximum cloud cover allowed in percentage

        Returns:
            List[Dict[str, Any]]: a list of all products
        """
        search_query = f"{self.catalogue_odata_url}/Products?$filter=contains(Name, '_T{tile}_') and Attributes/OData.CSC.DoubleAttribute/any(att:att/Name eq 'cloudCover' and att/OData.CSC.DoubleAttribute/Value lt {cloud_cover}.00) and Attributes/OData.CSC.StringAttribute/any(att:att/Name eq 'productType' and att/OData.CSC.StringAttribute/Value eq '{productType.value}') and ContentDate/Start gt {init_date.isoformat()} and ContentDate/Start lt {end_date.isoformat()}&$expand=Attributes&$orderby=ContentDate/Start desc"

        if limit:
            search_query += f"&$top={limit}"

        response = requests.get(search_query).json()
        output = []

        for product in response["value"]:
            output.append(_parse_odata_response(product))

        return output

    def info(self, uuid: str, full=False) -> Dict[str, Any]:
        """Get the info of a particular product

        Args:
            uuid (str): the uuid of the product
            full (bool, optional): If it's necessary to expand the result. Defaults to False.

        Returns:
            Dict[str, Any]: a dict with all the info
        """
        query = f"{self.catalogue_odata_url}/Products({uuid})"
        if full:
            query += "?&$expand=Attributes"

        response = requests.get(query).json()
        return _parse_odata_response(response)

    def _get_access_token(self) -> str:
        data = {
            "client_id": "cdse-public",
            "username": self.user,
            "password": self.password,
            "grant_type": "password",
        }
        try:
            r = requests.post(
                self.auth_server_url,
                data=data,
            )
            r.raise_for_status()
        except Exception as e:
            raise Exception(
                f"Access token creation failed. Reponse from the server was: {r.json()}"
            )
        return r.json()["access_token"]

    def download(self, uuid: str, path: str = "./") -> str:
        """Download a particular product

        Args:
            uuid (str): the uuid of the product to download
            path (str, optional): the path where to download the product. Defaults to "./".

        Returns:
            str: the absolute path of the downloaded product
        """
        access_token = self._get_access_token()
        url = f"{self.download_url}/Products({uuid})/$value"

        headers = {"Authorization": f"Bearer {access_token}"}

        with requests.Session() as session:
            session.headers.update(headers)
            response = session.get(url, headers=headers, stream=True)

            info = self.info(uuid)
            title = info["title"] + ".zip"
            final_path = os.path.join(path, title)

            total_size = info["size"]
            chunk_size = 8192
            with open(final_path, "wb") as file:
                for i, chunk in enumerate(response.iter_content(chunk_size=chunk_size)):
                    if chunk:
                        file.write(chunk)

                        # calculate current percentage
                        c = i * chunk_size / total_size * 100
                        # write current % to console, pause for .1ms, then flush console
                        sys.stdout.write(
                            f"\r{title} {i*chunk_size} / {total_size} ({round(c, 4)}%)"
                        )
                        sys.stdout.flush()

            return os.path.abspath(final_path)
    
    def is_online(self, uuid:str) -> bool:
        """Test if this product is online for 

        Args:
            uuid (str): the uuid of the product to test

        Returns:
            bool: if is it online or not
        """
        info = self.info(uuid)
        return info['Online']


def _parse_odata_response(product):
    output = {
        "id": product["Id"],
        "title": product["Name"],
        "size": int(product["ContentLength"]),
        "date": _parse_iso_date(product["ContentDate"]["Start"]),
        "footprint": product["Footprint"],
        "s3_path": product["S3Path"],
        "Online": product.get("Online", True),
    }
    if "Checksum" in product:
        for algorithm in product["Checksum"]:
            if "Algorithm" in algorithm:
                output[algorithm["Algorithm"].lower()]: algorithm["Value"]
    # Parse the extended metadata, if provided
    converters = [float, int, _parse_iso_date]
    if "Attributes" in product:
        for attr in product["Attributes"]:
            value = attr["Value"]
            for f in converters:
                try:
                    value = f(attr["Value"])
                    break
                except ValueError:
                    pass
            output[attr["Name"]] = value
    return output


def _parse_iso_date(content):
    if "." in content:
        return datetime.strptime(content, "%Y-%m-%dT%H:%M:%S.%fZ")
    else:
        return datetime.strptime(content, "%Y-%m-%dT%H:%M:%SZ")

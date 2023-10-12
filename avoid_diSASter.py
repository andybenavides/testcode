import requests
from requests.structures import CaseInsensitiveDict
import json

shared_access_signature_url = f"https://cs710037ffeac0fdb12.blob.core.windows.net/?restype=service&comp=accountsas"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"
headers["x-ms-version"] = "2020-08-04"
headers["x-ms-date"] = "Thu, 12 Oct 2023 11:07:44 GMT"

params = {
    "sv": "2020-08-04",
    "ss": "b",  # Blob service
    "srt": "co",  # Container and object
    "sp": "rwdlac",  # Read, write, delete, list, add, and create permissions
    "se": "2023-10-13T11:07:44Z",  # Expiry time
    "st": "2023-10-12T11:07:44Z",  # Start time
    "spr": "https",  # Protocol
    "sip": "",  # IP range
    "rscc": "",  # Cache control
    "rscd": "",  # Content disposition
    "rsce": "",  # Content encoding
    "rscl": "",  # Content language
    "rsct": "",  # Content type
}

from azure.storage.blob import generate_account_sas, ResourceTypes, AccountSasPermissions

sas_token = generate_account_sas(
    account_name=account_name,
    account_key=account_key,
    resource_types=ResourceTypes.from_string("sco"),
    permission=AccountSasPermissions.from_string("rw"),
    start=params["st"],
    expiry=params["se"],
)

shared_access_signature_url += f"&{sas_token}"

response = requests.get(shared_access_signature_url, headers=headers, params=params)

if response.status_code == 200:
    print("SAS token generated successfully!")
    print(response.text)
else:
    print(f"Failed to generate SAS token. Status code: {response.status_code}")
    print(response.text)

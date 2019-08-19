from enum import Enum
from google.oauth2 import service_account
from googleapiclient import discovery
from typing import Union, List


class GoogleSheetsScopes(Enum):
    """Google Sheets API scopes."""

    readonly = ['https://www.googleapis.com/auth/spreadsheets.readonly']
    full_access = ['https://www.googleapis.com/auth/spreadsheets']


class GoogleDocsScopes(Enum):
    """Google Docs API scopes."""

    readonly = ['https://www.googleapis.com/auth/documents.readonly']
    full_access = ['https://www.googleapis.com/auth/documents']


class APIVersions(Enum):
    """Google Documents API versions."""

    sheets = 'v4'
    docs = 'v1'


class GoogleDocuments:
    """Base class for working with Google Documents, such as Sheets or Docs."""

    def __init__(
        self, service_account_key: Union[str, dict], scopes: List[str], api_version: str
    ):
        self.service = self.authenticate(service_account_key, scopes, api_version)

    def authenticate(
        self, service_account_key: Union[str, dict], scopes: List[str], api_version: str
    ):
        creds = None
        if not creds or not creds.valid:
            if isinstance(service_account_key, str):
                creds = service_account.Credentials.from_service_account_file(
                    service_account_key, scopes=scopes
                )
            elif isinstance(service_account_key, dict):
                creds = service_account.Credentials.from_service_account_info(
                    service_account_key, scopes=scopes
                )
        return discovery.build('sheets', api_version, credentials=creds)

# engagement.py
import requests
from datetime import datetime, timedelta

from .auth import TelematicsAuth
from .core import TelematicsCore
from .utility import handle_response, adjust_date_range
from requests.exceptions import HTTPError, JSONDecodeError
import json




class BaseEngament:
    ACCOUNTS_URL = "https://accounts.telematicssdk.com/v1/companies"

    
    def __init__(self, auth_client: TelematicsAuth):
        self.auth_client = auth_client
    
    def _get_headers(self):
        return {
            'accept': 'application/json',
            'authorization': f'Bearer {self.auth_client.get_access_token()}'
        }
        
class AccountsModule:
    def __init__(self, core: TelematicsCore):
        self.core = core  # Renamed self.code to self.core for clarity
        
    @property
    def Accounts(self):
        return Accounts(self.core.auth_client)

class AccountsResponse:
    def __init__(self, data):
        # Check if data is None or empty before assignment
        if data is None or not data:
            self.data = {}
        else:
            self.data = data

    @property
    def result(self):
        results = self.data.get('Result',{})
        return results

    @property
    def status(self):
        return self.data.get('Status',{})
    
    def __str__(self):
        return json.dumps(self.data, indent=4)
    

class Accounts(BaseEngament):
    def create_application(self, company_id, name, description, status=1, 
                           googlePlayLink='', appleStoreLink='', createDefaultGroup=True):
        """
        Create an application for a specified company.

        :param company_id: The ID of the company.
        :param name: Name of the application.
        :param description: Description of the application.
        :param status: Status of the application (default is 1).
        :param googlePlayLink: Link to the application on Google Play (default is empty string).
        :param appleStoreLink: Link to the application on Apple Store (default is empty string).
        :param createDefaultGroup: Flag to create a default group (default is True).
        :return: An AccountsResponse object with the result or None.
        """
        url = f"{self.ACCOUNTS_URL}/{company_id}/applications"
        headers = self._get_headers()
        headers['Content-Type'] = 'application/json-patch+json'

        app_data = {
            "name": name,
            "description": description,
            "status": status,
            "googlePlayLink": googlePlayLink,
            "appleStoreLink": appleStoreLink,
            "createDefaultGroup": createDefaultGroup
        }

        try:
            response = self.auth_client.post_with_retry(url, headers=headers, json=app_data)
            data = handle_response(response)
            if data is not None:
                return AccountsResponse(data)
            return None
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Or handle it in some other way
            e_response = handle_response(response, AccountsResponse)  # Pass AccountsResponse as an argument
            return e_response

        
def DamoovAuth(email, password):
    auth_client = TelematicsAuth(email, password)
    return Accounts(auth_client)
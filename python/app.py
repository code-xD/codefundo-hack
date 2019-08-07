from adal import AuthenticationContext
import requests
from pprint import pprint

AUTHORITY = 'https://login.microsoftonline.com/shivansh586gmail.onmicrosoft.com'
WORKBENCH_API_URL = 'https://hack-ucqyga-api.azurewebsites.net'
RESOURCE = '2c949b1d-0722-493d-bb18-234af0ac2b70'
CLIENT_APP_Id = '4eb4aecc-1219-438f-ab1f-1f5d9caa158d'
CLIENT_SECRET = 'PVD6nd6NPAYHfvtwy331+MLt/JermbPiwkfjoRoz+PY='

auth_context = AuthenticationContext(AUTHORITY)

if __name__ == '__main__':
    try:
        # Acquiring the token
        token = auth_context.acquire_token_with_client_credentials(
            RESOURCE, CLIENT_APP_Id, CLIENT_SECRET)
        headers = {'Authorization': 'Bearer ' + token['accessToken']}
        # Making call to Workbench
        response = requests.post(
            WORKBENCH_API_URL + '/api/v2/contracts?workflowID=1', headers=headers)
        pprint(response.text)
    except Exception as error:
        print(error)

import requests
from requests.api import post
from requests.auth import HTTPBasicAuth
import urllib3

urllib3.disable_warnings()

'''
First devnet script, using API calls with python.
Things I need: 
    Base URL: IP Address or Fully Qualified Domain Name (FQDN) of the Cisco DNA Center server
    Auth URL: API endpoint used for authentication
    Username: Cisco DNA Center USERNAME
    Password: Cisco DNA Center PASSWORD
'''
base_url = 'https://sandboxdnac.cisco.com/'
auth_url = 'dna/system/api/v1/auth/token'
username = 'devnetuser'
password = 'Cisco123!'

def get_auth_token(): 
    response = requests.post(base_url + auth_url, auth=HTTPBasicAuth(username,password), verify=False)
    headers = {'Content-Type': 'application/json'}
    
    token = response.json()['Token']
    return token

if __name__ == '__main__':
    print(get_auth_token())
    #print(base_url + auth_url)
    

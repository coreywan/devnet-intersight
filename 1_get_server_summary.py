"""
General Server Query
"""

import json
import requests
import os

from intersight_auth import IntersightAuth

KEY = os.environ.get('INTERSIGHT_API_KEY')
AUTH = IntersightAuth(secret_key_filename="./SecretKey.txt", api_key_id=KEY)
BURL = "https://www.intersight.com/api/v1/"

def main():
    
    # Get Physical Summary Information
    server_api_url = "{}compute/PhysicalSummaries".format(BURL)
    servers_req = requests.get(server_api_url, auth=AUTH)
    servers = servers_req.json()

    # Loop through each physical Server and Print Name - Model - Serial
    print('Name\tModel\tSerial\tOperState')
    for b in servers['Results']:
        out = '{}\t{}\t{}\t{}'.format(b['Name'],b['Model'],b['Serial'],b['OperState'])
        print(out)

    # Build Filter for the Query API
    filter_query = "Name eq 'UCSPE-10-10-20-40-1'"
    server_api_url = "{}compute/PhysicalSummaries?$filter={}".format(BURL,filter_query)

    # Query API for Server
    server_req = requests.get(server_api_url, auth=AUTH)
    if len (server_req.json()['Results']) == 1:
        srv = server_req.json()['Results'][0]
        print('We found {}. Its model is {}. Its serial is {}'.format(srv['Name'], srv['Model'], srv['Serial']))

if __name__ == "__main__":
    main()
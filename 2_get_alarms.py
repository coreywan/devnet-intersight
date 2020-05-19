"""
Find and print all Critical Alarms
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
    alarms_url = "{}cond/Alarms?$filter=Severity eq 'Critical'".format(BURL)
    r = requests.get(alarms_url, auth=AUTH)
    results = r.json()['Results']
    for alarm in results:
        print('==== {} ===='.format(alarm['Name']))
        print("\tDescription: {}".format(alarm['Description']))
        print("\tSeverity: {}".format(alarm['Severity']))
        print("\tCreation Time: {}".format(alarm['CreationTime']))
        print('==================')
        print('')

    print('There were {} Critical Alarms Found.'.format(len(results)))
if __name__ == "__main__":
    main()
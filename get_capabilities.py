#!/usr/bin/python3

import requests

# disable warnings from SSL/TLS certificates
requests.packages.urllib3.disable_warnings()

def main():
    # CONSTANTS
    host = 'sbx-nxos-mgmt.cisco.com'
    restconf_port = '443'
    username = 'admin'
    password = 'Admin_1234!'

    headers = { 'Content-Type': 'application/yang.data+json',
                'Accept': 'application/yang.data+json'}

    url = 'https://{}/restconf/data/netconf-state/capabilities'.format(host)

    print(url)

    response = requests.get(url, auth=(username, password), headers=headers, verify=False)
    
    print(response.text)
    
if __name__ == '__main__':
    main()

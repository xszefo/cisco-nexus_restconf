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


    url = 'https://{}/restconf/data/Cisco-NX-OS-device:System/mac-items'.format(host) 
    
    print(url)

    response = requests.get(url, auth=(username, password), headers=headers, verify=False)

    response_json = response.json()['mac-items']['table-items']['vlan-items']['MacAddressEntry-list']

    for line in response_json:
        print('MAC: {} on VLAN {}'.format(line['macAddress'], line['vlan']))

if __name__ == '__main__':
    main()

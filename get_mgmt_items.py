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


    url = 'https://{}/restconf/data/Cisco-NX-OS-device:System/mgmt-items'.format(host) 
    
    print(url)

    response = requests.get(url, auth=(username, password), headers=headers, verify=False)

    response_json = response.json()['mgmt-items']['MgmtIf-list'][0]

    interface = response_json['id']
    description = response_json['descr']
    mtu = response_json['mtu']
    last_flap = ' '.join(response_json['mgmt-items']['lastLinkStChg'].split('T'))
     
    print(f'{interface} has a description {description}\nMTU: {mtu}\nLast flapped: {last_flap}')
        

if __name__ == '__main__':
    main()

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

    url = f'https://{host}:{restconf_port}/restconf/data/openconfig-spanning-tree:stp/'

    print(url)

    response = requests.get(url, headers=headers, auth=(username, password))
    
    if response.status_code == 200:
        stp = response.json()['stp']
        protocol = stp['global']['config']['enabled-protocol']
        print(protocol)
        vlans = []
        for vlan in stp['rapid-pvst']['vlan']:
               vlans.append(vlan['vlan-id'])
        print(f'VLANS: {sorted(vlans)}')

    #url = f'https://{host}:{restconf_port}/restconf/data/openconfig-spanning-tree:stp/interfaces'

    #print(url)

    #response = requests.get(url, headers=headers, auth=(username, password))

    #for interface in response.json()['interfaces']['interface']:
    #    print(interface['name'])


if __name__ == '__main__':
    main()

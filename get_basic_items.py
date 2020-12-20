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


    get_items = ['serial', 'name', 'systemUpTime', 'currentTime', 'time-items/clock']
	
    req_session = requests.session()

    for item in get_items:
        url = 'https://{}/restconf/data/Cisco-NX-OS-device:System/{}'.format(host, item)
    #url = 'https://{}/restconf/data/Cisco-IOS-XE-device-hardware-oper:device-hardware-data/device-hardware'.format(host)
   
        print(url)

        response = req_session.get(url, auth=(username, password), headers=headers, verify=False)

        print(response.text)
    
if __name__ == '__main__':
    main()

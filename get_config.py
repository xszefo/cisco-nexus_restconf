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

    interface = 'ietf-interfaces:interfaces'

    url = 'https://{host}:{port}/restconf/data/{interface}'.format(host=host, port=restconf_port, interface=interface)
    headers = { 'Content-Type': 'application/vnd.yang.data+json',
                'Accept': 'application/vnd.yang.data+json'}

#    headers = { 'Content-Type': 'application/yang.data+json'}


    url = 'https://{}:{}/restconf/api/running/'.format(host,restconf_port)

    url = 'https://{}:{}/api/running/interfaces?deep'.format(host,restconf_port)
    print(url)


    response = requests.get(url, auth=(username, password), headers=headers, verify=False)


    print(response.text)
    
if __name__ == '__main__':
    main()

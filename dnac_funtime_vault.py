
import requests
from dnacentersdk import DNACenterAPI
# define the path for importing the vault.py module
#   The vault.py module will also import hvac, os, requests, and dnacentersdk
import sys
sys.path.append('/Users/blaturne/DevNetCode/devasc-exam/vault/')
# import vault.py specific functions and variables that exists in upstream vault directory
from vault import vault_auth, dnac_vault_r_secret, vault_unseal_key, vault_role_id, vault_secret_id

vault_mount_point = 'kv-v1'
dnac_vault_path = '/devnet/dnac/sb1'

def get_dnac_token():
    """
    This function will Authenticate against Cisco DNA Center server and return the secret for use
    """    
    creds = dnac_vault_r_secret(dnac_vault_path, vault_mount_point)
    dnac = DNACenterAPI(username=(creds[0]),
                        password=(creds[1]),
                        base_url='https://sandboxdnac.cisco.com')
    print("DNAC API Authenticated ...")
    print("Gathering Device Info ... \n")
    devices = dnac.devices.get_device_list()
    for device in devices.response:
        print("Device Management IP {} for {} ".format(device.managementIpAddress, device.hostname))

if __name__ == '__main__':
    vault_auth()
    get_dnac_token()


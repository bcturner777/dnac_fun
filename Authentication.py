from dnacentersdk import DNACenterAPI
import os

dnac_creds = {}
dnac_creds['url'] = os.getenv('URL')
dnac_creds['username'] = os.getenv('USERNAME')
dnac_creds['password'] = os.getenv('PASSWORD')

print(dnac_creds)

dnac = DNACenterAPI(username= dnac_creds['username'] , password= dnac_creds['password'], base_url=dnac_creds['url'])
#print("Auth Token: ", dnac.access_token)

devices = dnac.devices.get_device_list()
for device in devices.response:
    print("Hostname {} Device Management IP {}".format(device.hostname, device.managementIpAddress))

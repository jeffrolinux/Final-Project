import requests


url = "https://192.168.1.103/api/tokenservices"

payload = ""
headers = {
    'Accept': "application/json",
    'Content-Type': "application/json",
    'Authorization': "Basic bGludXg6bGludXg=", # username:password  Base64 encoded
    'cache-control': "no-cache",
    }

token = requests.request("POST", url, data=payload, headers=headers, verify=False)

print(token.headers["X-Auth-Token"])  # Our token received


#Configure Interface to Web_Server
url = "https://192.168.1.103/api/interfaces/physical/GigabitEthernet0_API_SLASH_4"
payload = "{\r\n  \"securityLevel\": 0,\r\n  \"kind\": \"object#GigabitInterface\",\r\n  \"channelGroupMode\": \"active\",\r\n  \"flowcontrolLow\": -1,\r\n  \"name\": \"Configured_BY_Automation\",\r\n  \"duplex\": \"auto\",\r\n  \"forwardTrafficSFR\": false,\r\n  \"hardwareID\": \"GigabitEthernet0/4\",\r\n  \"mtu\": 1500,\r\n  \"lacpPriority\": -1,\r\n  \"flowcontrolHigh\": -1,\r\n  \"ipAddress\": {\r\n    \"ip\": {\r\n      \"kind\": \"IPv4Address\",\r\n      \"value\": \"10.2.2.3\"\r\n    },\r\n    \"kind\": \"StaticIP\",\r\n    \"netMask\": {\r\n      \"kind\": \"IPv4NetMask\",\r\n      \"value\": \"255.255.255.0\"\r\n    }\r\n  },\r\n  \"flowcontrolOn\": false,\r\n  \"shutdown\": false,\r\n  \"interfaceDesc\": \"Description added from Python\",\r\n  \"managementOnly\": false,\r\n  \"channelGroupID\": \"\",\r\n  \"speed\": \"auto\",\r\n  \"forwardTrafficCX\": false,\r\n  \"flowcontrolPeriod\": -1\r\n}"
headers = {
    'Accept': "application/json",
    'Content-Type': "application/json",
    'X-Auth-Token': token.headers["X-Auth-Token"],
    'cache-control': "no-cache",
    }

response = requests.request("PUT", url, data=payload, headers=headers, verify=False)

print(response.text)

#Configure Gig 0/1 to SW1
url = "https://192.168.1.103/api/interfaces/physical/GigabitEthernet0_API_SLASH_1"
 payload = "{\r\n  \"securityLevel\": 0,\r\n  \"kind\": \"object#GigabitInterface\",\r\n  \"channelGroupMode\": \"active\",\r\n  \"flowcontrolLow\": -1,\r\n  \"name\": \"To_SW1\",\r\n  \"duplex\": \"auto\",\r\n  \"forwardTrafficSFR\": false,\r\n  \"hardwareID\": \"GigabitEthernet0/1\",\r\n  \"mtu\": 1500,\r\n  \"lacpPriority\": -1,\r\n  \"flowcontrolHigh\": -1,\r\n  \"ipAddress\": {\r\n    \"ip\": {\r\n      \"kind\": \"IPv4Address\",\r\n      \"value\": \"10.1.1.1\"\r\n    },\r\n    \"kind\": \"StaticIP\",\r\n    \"netMask\": {\r\n      \"kind\": \"IPv4NetMask\",\r\n      \"value\": \"255.255.255.252\"\r\n    }\r\n  },\r\n  \"flowcontrolOn\": false,\r\n  \"shutdown\": false,\r\n  \"interfaceDesc\": \"Description added from Python\",\r\n  \"managementOnly\": false,\r\n  \"channelGroupID\": \"\",\r\n  \"speed\": \"auto\",\r\n  \"forwardTrafficCX\": false,\r\n  \"flowcontrolPeriod\": -1\r\n}"
headers = {
    'Accept': "application/json",
    'Content-Type': "application/json",
    'X-Auth-Token': token.headers["X-Auth-Token"],
    'cache-control': "no-cache",
    }

response = requests.request("PUT", url, data=payload, headers=headers, verify=False)
print(response.text)


#Configure Gig0/2 to SW2
url = "https://192.168.1.103/api/interfaces/physical/GigabitEthernet0_API_SLASH_2"

payload = "{\r\n  \"securityLevel\": 0,\r\n  \"kind\": \"object#GigabitInterface\",\r\n  \"channelGroupMode\": \"active\",\r\n  \"flowcontrolLow\": -1,\r\n  \"name\": \"To_SW2\",\r\n  \"duplex\": \"auto\",\r\n  \"forwardTrafficSFR\": false,\r\n  \"hardwareID\": \"GigabitEthernet0/2\",\r\n  \"mtu\": 1500,\r\n  \"lacpPriority\": -1,\r\n  \"flowcontrolHigh\": -1,\r\n  \"ipAddress\": {\r\n    \"ip\": {\r\n      \"kind\": \"IPv4Address\",\r\n      \"value\": \"10.12.12.1\"\r\n    },\r\n    \"kind\": \"StaticIP\",\r\n    \"netMask\": {\r\n      \"kind\": \"IPv4NetMask\",\r\n      \"value\": \"255.255.255.252\"\r\n    }\r\n  },\r\n  \"flowcontrolOn\": false,\r\n  \"shutdown\": false,\r\n  \"interfaceDesc\": \"Description added from Python\",\r\n  \"managementOnly\": false,\r\n  \"channelGroupID\": \"\",\r\n  \"speed\": \"auto\",\r\n  \"forwardTrafficCX\": false,\r\n  \"flowcontrolPeriod\": -1\r\n}"
headers = {
    'Accept': "application/json",
    'Content-Type': "application/json",
    'X-Auth-Token': token.headers["X-Auth-Token"],
    'cache-control': "no-cache",
    }

response = requests.request("PUT", url, data=payload, headers=headers, verify=False)

# Configure interface to SW2
url = "https://192.168.1.103/api/interfaces/physical/GigabitEthernet0_API_SLASH_4"
 
payload = "{\r\n  \"securityLevel\": 0,\r\n  \"kind\": \"object#GigabitInterface\",\r\n  \"channelGroupMode\": \"active\",\r\n  \"flowcontrolLow\": -1,\r\n  \"name\": \"TO_SW2\",\r\n  \"duplex\": \"auto\",\r\n  \"forwardTrafficSFR\": false,\r\n  \"hardwareID\": \"GigabitEthernet0/4\",\r\n  \"mtu\": 1500,\r\n  \"lacpPriority\": -1,\r\n  \"flowcontrolHigh\": -1,\r\n  \"ipAddress\": {\r\n    \"ip\": {\r\n      \"kind\": \"IPv4Address\",\r\n      \"value\": \"10.2.2.3\"\r\n    },\r\n    \"kind\": \"StaticIP\",\r\n    \"netMask\": {\r\n      \"kind\": \"IPv4NetMask\",\r\n      \"value\": \"255.255.255.0\"\r\n    }\r\n  },\r\n  \"flowcontrolOn\": false,\r\n  \"shutdown\": false,\r\n  \"interfaceDesc\": \"Description added from Python\",\r\n  \"managementOnly\": false,\r\n  \"channelGroupID\": \"\",\r\n  \"speed\": \"auto\",\r\n  \"forwardTrafficCX\": false,\r\n  \"flowcontrolPeriod\": -1\r\n}"
headers = {
    'Accept': "application/json",
    'Content-Type': "application/json",
    'X-Auth-Token': token.headers["X-Auth-Token"],
    'cache-control': "no-cache",
    }

response = requests.request("PUT", url, data=payload, headers=headers, verify=False)
#print(response.text)

#Configure object for inside web address

url = "https://192.168.1.103/api/objects/networkobjects"

payload = "{\r\n  \"host\": {\r\n    \"kind\": \"IPv4Address\",\r\n    \"value\": \"10.2.2.2\"\r\n  },\r\n  \"kind\": \"object#NetworkObj\",\r\n  \"name\": \"Inside_Web_Server\",\r\n  \"objectId\": \"Inside\"\r\n}"
headers = {
    'Accept': "application/json",
    'Content-Type': "application/json",
    'X-Auth-Token': token.headers["X-Auth-Token"],
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers, verify=False)

#Configure object for outside web server

payload = "{\r\n  \"host\": {\r\n    \"kind\": \"IPv4Address\",\r\n    \"value\": \"10.20.20.20\"\r\n  },\r\n  \"kind\": \"object#NetworkObj\",\r\n  \"name\": \"Outside_Web_Server\",\r\n  \"objectId\": \"Outside\"\r\n}"
headers = {
    'Accept': "application/json",
    'Content-Type': "application/json",
    'X-Auth-Token': token.headers["X-Auth-Token"],
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers, verify=False)

#print(response.text)

#Nat for Web_Server
url = "https://192.168.1.103/api/nat/before"


payload = "{\r\n  \"originalDestination\": {\r\n   \"kind\": \"objectRef#NetworkObj\",\r\n    \"objectId\": \"Outside_Web_Server\"\r\n  },\r\n  \"description\": \"demo nat 1\",\r\n  \"originalSource\": {\r\n    \"kind\": \"AnyIPAddress\",\r\n    \"value\": \"any\"\r\n  },\r\n  \"originalService\": {\r\n  \t\"kind\": \"objectRef#TcpUdpServiceObj\",\r\n    \"objectId\": \"MY-Port\"\r\n  },\r\n  \"translatedService\": {\r\n  \t\"kind\": \"objectRef#TcpUdpServiceObj\",\r\n    \"objectId\": \"MY-Port\"\r\n  },\r\n  \"mode\": \"static\",\r\n  \"position\": 123,\r\n  \"active\": true,\r\n  \"translatedDestination\": {\r\n    \"kind\": \"objectRef#NetworkObj\",\r\n    \"objectId\": \"Inside_Web_Server\"\r\n  }\r\n}"

headers = {
    'Accept': "application/json",
    'Content-Type': "application/json",
    'X-Auth-Token': token.headers["X-Auth-Token"],
    'cache-control': "no-cache",
    }

response = requests.request("POST", url, data=payload, headers=headers, verify=False)

#Allow traffic through ASA for same interface security, also use the ability
# Of CLI thorough the API
url = "https://192.168.1.103/api/cli"

payload = "{\n\t\"commands\": [\n\t\t\"same-security-traffic permit inter-interface\"\n ]\n}"
headers = {
    'Accept': "application/json",
    'Content-Type': "application/json",
    'X-Auth-Token': token.headers["X-Auth-Token"],
    'cache-control': "no-cache",
    }

response = requests.request("POST", url, data=payload, headers=headers, verify=False)

#Static Routes From ASA to SW1

url = "https://192.168.1.103/api/routing/static"

payload = "{\r\n  \"tunneled\": false,\r\n  \"kind\": \"object#IPv4Route\",\r\n  \"distanceMetric\": 200,\r\n  \"tracked\": false,\r\n  \"interface\": {\r\n    \"kind\": \"objectRef#Interface\",\r\n    \"name\": \"To_SW1\"\r\n  },\r\n  \"gateway\": {\r\n    \"kind\": \"IPv4Address\",\r\n    \"value\": \"10.1.1.2\"\r\n  },\r\n  \"network\": {\r\n    \"kind\": \"IPv4Network\",\r\n    \"value\": \"192.168.2.0/24\"\r\n  }\r\n}"
headers = {
    'Accept': "application/json",
    'Content-Type': "application/json",
    'X-Auth-Token': token.headers["X-Auth-Token"],
    'cache-control': "no-cache",
    }

response = requests.request("POST", url, data=payload, headers=headers, verify=False)

# now To save our configuration
url = "https://192.168.1.103/api/cli"

payload = "{\n\t\"commands\": [\n\t\t\"write memory\"\n ]\n}"
headers = {
    'Accept': "application/json",
    'Content-Type': "application/json",
    'X-Auth-Token': token.headers["X-Auth-Token"],
    'cache-control': "no-cache",
    }

response = requests.request("POST", url, data=payload, headers=headers, verify=False)

url = "https://192.168.1.103/api/tokenservices/" + token.headers["X-Auth-Token"]
headers = {
    'Accept': "application/json",
    'Content-Type': "application/json",
    'X-Auth-Token': token.headers["X-Auth-Token"], #Using our token one last time to logout
    'cache-control': "no-cache",
    }


response = requests.request("DELETE", url, data=payload, headers=headers, verify=False)

                 

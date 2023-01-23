import json
import re
import requests
#file containg ssh logging
with open('/home/asad/PycharmProjects/vtsshparser/vtssh-parser/ok.txt', 'r') as file:
    file = file.read()

pattern = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
ips = pattern.findall(file)
unique_ips = list(set(ips))
#replace api-key with actual key
headers = {
    "accept": "application/json",
    "x-apikey": "#REPLACEME#"
}
i = 0
url = "https://www.virustotal.com/api/v3/ip_addresses/"
out_json= {"providers": []}

while i < len(unique_ips):

    furl = url + strm r(unique_ips[i])
    response = requests.get(furl, headers=headers)

    data_ = response.json()

    messages = data_['data']['attributes']['last_analysis_results']

    for k, vv in messages.items():
            out_json1 = {
                "indicators": [{
                    "value": str(unique_ips[i]),
                    "type": 'ip',

                }]
                 }
            out_json["providers"].append(
                        {
                        "provider": str([vv["engine_name"]]),
                        "verdict": str([vv["category"]]),
                        "score":str([vv["result"]])
                        }
                    )
    i += 1
    print(json.dumps(out_json1,indent=2),json.dumps(out_json,indent=2))


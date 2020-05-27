import requests
import json

# https://crontab.guru/#*/15_*_*_*_*
# crontab -e
# m h  dom mon dow   command
# * 1 * * * python /home/pi/repositories/public-access/publish_ip.py

response = requests.get('https://api.ipify.org?format=json')
data = json.loads(response.text)
ip = data["ip"]
print(ip)

slack_url = 'https://hooks.slack.com/services/xyz/xyz/xyz'
slack_payload = {
    'text': 'Current ip address is {0}'.format(ip)
}
headers = {
    'Content-Type': 'application/json'
}
response = requests.post(slack_url, json=slack_payload, headers=headers)
print(response.text)

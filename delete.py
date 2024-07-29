import requests
import os

token = os.getenv('custom_code_actions_access_token')

def main(event):
  object_type = "tickets"
  object_id = event["inputFields"]["hs_object_id"]
  
  url = f"https://api.hubapi.com/crm/v3/objects/{object_type}/{object_id}"
  
  headers = {
    'Authorization': f'Bearer {token}'
  }

  response = requests.request("DELETE", url, headers=headers)

  print(response.text)


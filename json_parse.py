#!/usr/bin/python
import json
import requests



#json parser
url = 'https://chocofood.kz/debug-api/restaurants-status/?format=json'

def main():
  response = requests.get(url)
  feed = response.text
  json_feed = json.loads(feed)
  return json_feed



if __name__ == "__main__":
  main()
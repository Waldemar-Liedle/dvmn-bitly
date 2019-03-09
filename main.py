import requests
import os
import argparse
from dotenv import load_dotenv
from BitlyModule import authorize, get_short_link, get_long_link, get_link_stats

def main():
  load_dotenv()
  token = os.getenv("TOKEN")
  parser = argparse.ArgumentParser(description='Program description')  
  parser.add_argument('link', help='Link to web page')
  args = parser.parse_args()
  link = args.link  

  try: 
    response = authorize(token)
  except requests.exceptions.HTTPError as error:
    exit("1. {}".format(error))

  try:
    response = get_long_link(token, link)
    try:
      response = get_link_stats(token, link, None)
      clicks = response.json()["total_clicks"]
      print("Clicks summary: {}".format(clicks))
    except requests.exceptions.HTTPError as error:
      print("2. {}".format(error))

  except requests.exceptions.HTTPError:
    try:
      response = get_short_link(token, link)
      shortLink = response.json()["id"]
      print(format(shortLink))
    except requests.exceptions.HTTPError as error:
      print("3. {}".format(error))
 
if __name__ == "__main__":
  main()

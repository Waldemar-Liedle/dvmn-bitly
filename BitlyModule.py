import requests

USER_URL = "https://api-ssl.bitly.com/v4/user"
BITLINKS_URL = "https://api-ssl.bitly.com/v4/bitlinks"
EXPAND_URL= "https://api-ssl.bitly.com/v4/expand"

def get_header(token):  
  return { 
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json"
  }

def authorize(token):
  response = requests.get(
    USER_URL,
    headers = get_header(token)
  )
  response.raise_for_status()
  return response

def get_short_link(token, longLink):
  longlinkJson = { "long_url": longLink }
  response = requests.post(
    BITLINKS_URL,
    headers = get_header(token),
    json = longlinkJson
  )
  response.raise_for_status()
  return response

def get_long_link(token, shortLink):
  shortlinkJson = { "bitlink_id": shortLink }
  response = requests.post(
    EXPAND_URL,
    headers = get_header(token),
    json = shortlinkJson
  )
  response.raise_for_status()
  return response

def get_link_stats(token, shortLink, params):
  response = requests.get(
    "{}/{}/clicks/summary".format(BITLINKS_URL, shortLink),
    headers = get_header(token),
    json = params
  )
  response.raise_for_status()
  return response

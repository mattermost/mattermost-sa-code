import requests
import json

# Mattermost server
url = "http://server"
login_url = url+"/api/v4/users/login"
team_name = "team"
channel_name = "channel"

def login(login_url):
    payload = { "login_id": "admin@mattermost.com",
                "password": "MattermostDemo,1"}
    headers = {"content-type": "application/json"}
    s = requests.Session()
    r = s.post(login_url, data=json.dumps(payload), headers=headers)
    auth_token = r.headers.get("Token")
    global hed
    hed = {'Authorization': 'Bearer ' + auth_token}

def get_team_id(url, team_name):
    team_url = url+"/api/v4/teams/search"
    payload = { "term": team_name}
    response = requests.post(team_url, headers=hed, json=payload)
    info = response.json()
    global team_id
    team_id = info[0]["id"]

def get_channel_id(url, team_id, channel_name):
    team_url = url+"/api/v4/teams/"+team_id+"/channels/search"
    payload = { "term": channel_name}
    response = requests.post(team_url, headers=hed, json=payload)
    info = response.json()
    global channel_id
    channel_id = info[0]["id"]
    print("Channel ID:"+channel_id)
    get_channel_members(channel_id)

def get_channel_members(channel_id):
    team_url = url+"/api/v4/channels/"+channel_id+"/members"
    response = requests.get(team_url, headers=hed)
    info = response.json()
    print(info)
    #global user_name
    #user_name = info['username']


login(login_url)
get_team_id(url, team_name)
get_channel_id(url, team_id, channel_name)

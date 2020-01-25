import requests
import json

# -------------------------------------------------------------------------
# Mattermost server
url = "http://35.153.176.26:8065"
login_user = "admin@mattermost.com"
login_pass = "MattermostDemo,1"

# User inputs
#url = raw_input("Enter Mattermost server URL, format(http://mattermostserver:port) without an ending slash: ")
#team_name = raw_input("Enter Mattermost team name (lower case): ")
#login_user = raw_input("Enter Mattermost username: ")
#login_pass = raw_input("Enter Mattermost password: ")
grouping = raw_input("Enter Sidebar grouping (by_type or none): ")
grouping = '"'+grouping+'"'
unreads_at_top = raw_input("Enter Sidebar unreads on top (true or false): ")
unreads_at_top = '"'+unreads_at_top+'"'
favorite_at_top = raw_input("Enter Sidebar favorite on top (true or false): ")
favorite_at_top = '"'+favorite_at_top+'"'
sorting = raw_input("Enter Sidebar sorting (recent or alpha): ")
sorting = '"'+sorting+'"'

# -------------------------------------------------------------------------
# Please do not change
# Author: Christian Johannsen, Mattermost
# -------------------------------------------------------------------------

login_url = url+"/api/v4/users/login"

def login(login_url):
    payload = { "login_id": login_user,
                "password": login_pass}
    headers = {"content-type": "application/json"}
    s = requests.Session()
    r = s.post(login_url, data=json.dumps(payload), headers=headers)
    auth_token = r.headers.get("Token")
    global hed
    hed = {'Authorization': 'Bearer ' + auth_token}

def get_users(i):
    print("Actual page")
    print(i)
    login(login_url)
    post_url = url+"/api/v4/users"
    payload = {'page': i, 'per_page': '200'}
    response = requests.get(post_url, headers=hed, params=payload)
    users = response.json()
    for user in users:
        for k,v in user.items():
            if k == "id":
                user_id = v
                set_prefs(user_id)
                get_prefs(user_id)

def get_prefs(id):
    login(login_url)
    print("ID: "+id)
    post_url = url+"/api/v4/users/"+id+"/preferences"
    response = requests.get(post_url, headers=hed)
    info = response.json()
    print(info)
    for i in info:
        print(i)

def set_prefs(id):
    login(login_url)
    post_url = url+"/api/v4/users/"+id+"/preferences"
    payload = [
        {
            "user_id": id,
            "category": "sidebar_settings",
            "name": "",
            "value": '{"grouping": '+ grouping +', "unreads_at_top": '+ unreads_at_top +', "favorite_at_top": '+ favorite_at_top +', "sorting": '+ sorting +'}'
        }
    ]
    response = requests.put(post_url, headers=hed, json=payload)
    info = response.json()
    print info

def get_total_users():
    login(login_url)
    post_url = url+"/api/v4/users/stats"
    response = requests.get(post_url, headers=hed)
    info = response.json()
    print("Total Users:")
    print(info["total_users_count"])
    pages = info["total_users_count"]/200
    print("Total Pages:")
    print(pages)
    if pages == 0:
        get_users(pages)
    else:
        for i in range(pages):
            print(i)
            get_users(i)

get_total_users()

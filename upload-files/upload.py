import requests
import json

url = "http://server"
login_url = url+"/api/v4/users/login"
team_name = "team"
channel_name = "channel"
channel_id = "channelid"

def login(login_url):
    payload = { "login_id": "admin@mattermost.com",
                "password": "MattermostDemo,1"}
    headers = {"content-type": "application/json"}
    s = requests.Session()
    r = s.post(login_url, data=json.dumps(payload), headers=headers)
    auth_token = r.headers.get("Token")
    global hed
    hed = {'Authorization': 'Bearer ' + auth_token}

def post_uploads(filename, channel_id):
    print("Uploading files...")
    login(login_url)
    post_url = url+"/api/v4/files?channel_id="+channel_id
    headers = {"content-type": "multipart/form-data"}
    files = {'upload_file': open(filename, 'rb')}
    response = requests.post(post_url, headers=hed, files=files)
    info = response.json()
    print(info)

post_uploads("IMG_5090.jpg", "so5nenenbtyi7xg6yqf918fgnc")

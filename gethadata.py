from requests import get
import json

def read_json(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

conf = read_json("config.json")
token = conf["APP"]["TOKEN"]
haurl = conf["APP"]["URL"]

users = conf["TRACK"]
for user in users:
    url = haurl + "/api/states/device_tracker." + users[user]["mac"]
    headers = {
        "Authorization": "Bearer " + token,
        "content-type": "application/json",
    }

    response = get(url, headers=headers)
    state = json.loads(response.text)
    print(user + " is " + state["state"])

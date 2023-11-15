import requests, json

url = "https://openid.17a.icu/api/"


def login(user, password, debug=False):
    data = requests.post(
        url=url + "public/login",
        headers={"Content-Type": "application/json"},
        data=json.dumps({"user": user, "password": password}),
    )
    if data.status_code == 200:
        if debug == False:
            cookies = requests.utils.dict_from_cookiejar(data.cookies)
            return {
                "code": data.status_code,
                "message": {
                    "data": json.loads(data.text)["msg"],
                    "cookies": cookies["17a"],
                },
            }
        else:
            return data.text
    else:
        return data.text


def authorize(client_id, cookies, debug=False):
    if client_id == "openfrp":
        data = requests.get(
            url=url
            + "oauth2/authorize?response_type=code&client_id=openfrp&redirect_uri=http%3A%2F%2Fconsole.openfrp.net%2Foauth_callback",
            headers={"Content-Type": "application/json"},
            cookies={"17a": cookies},
        )
        if data.status_code == 200:
            if debug == False:
                return {
                    "code": data.status_code,
                    "message": {
                        "data": json.loads(data.text)["data"]["code"],
                        "msg": json.loads(data.text)["msg"],
                    },
                }
            else:
                return data.text
        else:
            return data.text
    else:
        return "Unknown product"


def fast_login(user, password, client_id):
    try:
        data = login(user, password)
        if data["code"] == 200:
            data = authorize(client_id, data["message"]["cookies"])
            if data["code"] == 200:
                return data
            else:
                return {"error": "login", "data": authorize}
        else:
            return {"error": "login", "data": data}
    except:
        data = login(user, password)
        if json.loads(data)["code"] == 200:
            data = authorize(client_id, data["message"]["cookies"])
            if json.loads(data)["code"] == 200:
                return data
            else:
                return {"error": "login", "data": authorize}
        else:
            return {"error": "login", "data": data}
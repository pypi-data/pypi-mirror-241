import requests, json, time, random

url = "https://of-dev-api.bfsea.xyz/"


def login(code, debug=False):
    data = requests.get(
        url=url + "oauth2/callback?code={0}".format(code),
        headers={"Content-Type": "application/json"},
    )
    if data.status_code == 200:
        if debug == False:
            return {
                "code": data.status_code,
                "message": {
                    "data": json.loads(data.text)["data"],
                    "msg": json.loads(data.text)["msg"],
                    "flag": json.loads(data.text)["flag"],
                },
                "authorization": json.loads(str(data.headers).replace("'", '"'))[
                    "Authorization"
                ],
            }
        else:
            return data.text
    else:
        return data.text


def userinfo(authorization, debug=False):
    data = requests.post(
        url=url + "frp/api/getUserInfo",
        headers={"Content-Type": "application/json", "Authorization": authorization},
    )
    if data.status_code == 200:
        if debug == False:
            return {
                "code": data.status_code,
                "message": {
                    "data": json.loads(data.text)["data"],
                    "msg": json.loads(data.text)["msg"],
                    "flag": json.loads(data.text)["flag"],
                },
            }
        else:
            return data.text
    else:
        return data.text


def usersign(authorization, debug=False):
    data = requests.post(
        url=url + "frp/api/userSign",
        headers={"Content-Type": "application/json", "Authorization": authorization},
    )
    if data.status_code == 200:
        if debug == False:
            return {
                "code": data.status_code,
                "message": {
                    "data": json.loads(data.text)["data"],
                    "msg": json.loads(data.text)["msg"],
                    "flag": json.loads(data.text)["flag"],
                },
            }
        else:
            return data.text
    else:
        return data.text


def userproxies(authorization, id=0, debug=False):
    data = requests.post(
        url=url + "frp/api/getUserProxies",
        headers={"Content-Type": "application/json", "Authorization": authorization},
    )
    if data.status_code == 200:
        if debug == False:
            if id == 0:
                return {
                    "code": data.status_code,
                    "message": {
                        "data": json.loads(data.text)["data"],
                        "msg": json.loads(data.text)["msg"],
                        "flag": json.loads(data.text)["flag"],
                    },
                }
            else:
                for item in json.loads(data.text)["data"]["list"]:
                    if item["id"] == int(id):
                        return {
                            "code": data.status_code,
                            "message": {"data": item},
                        }
        else:
            return data.text
    else:
        return data.text


def newproxy(
    authorization,
    node_id,
    remote_port=random.randint(10000, 65565),
    local_addr="127.0.0.1",
    name=str("MapleAPI" + str(int(time.time()))),
    type="tcp",
    local_port="25565",
    domain_bind="",
    dataGzip=False,
    dataEncrypt=False,
    url_route="",
    host_rewrite="",
    request_from="",
    request_pass="",
    custom="",
    debug=False,
):
    data = {
        "node_id": int(node_id),
        "name": name,
        "type": type,
        "local_addr": local_addr,
        "local_port": local_port,
        "remote_port": int(remote_port),
        "domain_bind": domain_bind,
        "dataGzip": bool(dataGzip),
        "dataEncrypt": bool(dataEncrypt),
        "url_route": url_route,
        "host_rewrite": host_rewrite,
        "request_from": request_from,
        "request_pass": request_pass,
        "custom": custom,
    }
    data = requests.post(
        url=url + "frp/api/newProxy",
        headers={"Content-Type": "application/json", "Authorization": authorization},
        data=json.dumps(data),
    )
    if data.status_code == 200:
        if debug == False:
            return {
                "code": data.status_code,
                "message": {
                    "data": json.loads(data.text)["data"],
                    "msg": json.loads(data.text)["msg"],
                    "flag": json.loads(data.text)["flag"],
                },
            }
        else:
            return data.text
    else:
        return data.text


def editproxy(
    authorization,
    id,
    node_id="",
    remote_port="",
    local_addr="",
    name="",
    type="",
    local_port="",
    domain_bind="",
    dataGzip="",
    dataEncrypt="",
    debug=False,
):
    data = userproxies(authorization, id)["message"]["data"]
    if remote_port:
        remote_port = remote_port
    else:
        remote_port = data["remotePort"]
    if local_addr:
        local_addr = local_addr
    else:
        local_addr = data["localIp"]
    if local_port:
        local_port = local_port
    else:
        local_port = data["localPort"]
    if name:
        name = name
    else:
        name = data["proxyName"]
    if domain_bind:
        domain_bind = domain_bind
    else:
        domain_bind = data["domain"]
    if dataGzip:
        dataGzip = dataGzip
    else:
        dataGzip = data["useCompression"]
    if dataEncrypt:
        dataEncrypt = dataEncrypt
    else:
        dataEncrypt = data["useEncryption"]
    if type:
        type = type
    else:
        type = data["proxyType"]
    if node_id:
        node_id = node_id
    else:
        node_id = data["nid"]

    data = {
        "name": name,
        "node_id": node_id,
        "local_addr": local_addr,
        "local_port": local_port,
        "remote_port": remote_port,
        "domain_bind": "[{0}]".format(domain_bind),
        "dataGzip": bool(dataGzip),
        "dataEncrypt": bool(dataEncrypt),
        "custom": "",
        "type": type,
        "proxy_id": id,
    }
    data = requests.post(
        url=url + "frp/api/editProxy",
        headers={"Content-Type": "application/json", "Authorization": authorization},
        data=json.dumps(data),
    )
    if data.status_code == 200:
        if debug == False:
            return {
                "code": data.status_code,
                "message": {
                    "data": json.loads(data.text)["data"],
                    "msg": json.loads(data.text)["msg"],
                    "flag": json.loads(data.text)["flag"],
                },
            }
        else:
            return data.text
    else:
        return data.text


def removeproxy(authorization, proxy_id, debug=False):
    data = requests.post(
        url=url + "frp/api/removeProxy",
        headers={"Content-Type": "application/json", "Authorization": authorization},
        data=json.dumps({"proxy_id": int(proxy_id)}),
    )
    if data.status_code == 200:
        if debug == False:
            return {
                "code": data.status_code,
                "message": {
                    "data": json.loads(data.text)["data"],
                    "msg": json.loads(data.text)["msg"],
                    "flag": json.loads(data.text)["flag"],
                },
            }
        else:
            return data.text
    else:
        return data.text


def getnodelist(authorization, debug=False):
    data = requests.post(
        url=url + "frp/api/getNodeList",
        headers={"Content-Type": "application/json", "Authorization": authorization},
    )
    if data.status_code == 200:
        if debug == False:
            return {
                "code": data.status_code,
                "message": {
                    "data": json.loads(data.text)["data"],
                    "msg": json.loads(data.text)["msg"],
                    "flag": json.loads(data.text)["flag"],
                },
            }
        else:
            return data.text
    else:
        return data.text

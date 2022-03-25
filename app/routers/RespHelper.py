


def resp_ok(data):
    return {
        "code": 1,
        "msg": "success",
        "data": data
    }

def resp_err(code, msg):
    return {
        "code": code,
        "msg": msg
    }
import connect
import json
_APP = "/nslc"
def get_networks():
    resource = _APP + "/networks"
    api_url = connect.url(resource)

    response = connect.requests.get(api_url, headers=connect.headers)
    print(response.status_code)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

print(get_networks())
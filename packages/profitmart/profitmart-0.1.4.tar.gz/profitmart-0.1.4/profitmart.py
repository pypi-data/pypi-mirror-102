import requests
import json
import base64
from . import utils

URL = 'http://mobile.profitmart.in/NestHtml5Mobile/rest'

def getPublicKey(url,uid,appid,secret):
	body = {'uid':uid,'appid':appid,'secret':secret}
	response = requests.post(url,json=body)
	response = response.json()
	# print(response)
	if response['stat'] == 'ok':
		return utils.getPubKeyFromPem(response['publicKey_pem'].encode())
	else:
		print(response['message'])
		return None

# Post method..
def POST(functionName, json_data, key, tomcatCount):
    response = requests.post(URL+functionName+"?jsessionid=" + "." + tomcatCount + "&jData=" + json_data + "&jKey=" + key + "")
    r = response.json()
    res_dict = json.loads(json.dumps(r))

    return res_dict

# Get Default login...
def getClientData(uid, publicKey4, publicKey4_hash,tomcatCount):
    data_json = json.dumps({'uid': uid})
    response = POST('/DefaultLogin', utils.encryptKey(publicKey4,
                    data_json.encode()), publicKey4_hash, tomcatCount)
    return response


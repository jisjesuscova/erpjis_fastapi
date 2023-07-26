import requests

class CollectionClass:
    def get_total(user_inputs):
        url = "https://jisparking.com/api/collection/supervisortotal/"+ str(user_inputs['rol_id']) +"/"+ str(user_inputs['rut']) +"?api_token="+ str(user_inputs['api_token']) +""

        payload={}
        headers = {}

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)

        return response.text

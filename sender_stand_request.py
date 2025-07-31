import configuration
import requests
import data


# este no se si va aqui o va en create_kit_name_kit_test.py

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)



def get_token():
    user = post_new_user(data.user_body)
    return user.json()["authToken"] #para llamar al token

def post_new_kit(body):
    token = get_token()
    current_token = data.headers.copy()
    current_token["Authorization"] = f"Bearer {token}"
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         headers=current_token,
                         json=body)
response = post_new_kit(data.kit_body)

print(response.status_code)
print(response.json())
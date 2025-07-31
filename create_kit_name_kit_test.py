import sender_stand_request
import data



def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

def positive_assert(name):
    kit_body = get_kit_body(name)
    user_response = sender_stand_request.post_new_kit(kit_body)
    assert user_response.status_code == 201

def negative_assert(name):
    kit_body = get_kit_body(name)
    user_response = sender_stand_request.post_new_kit(kit_body)
    assert user_response.status_code == 400


#Prueba 1
def test_create_new_kit_name_1_character_success_response():
    positive_assert("a")

#Prueba 2
def test_vreate_new_kit_name_511_character_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

#Prueba 3
def test_create_new_kit_name_0_character_error_response():
    negative_assert("")

#Prueba 4
def test_create_new_kit_name_512_character_error_response():
    negative_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

#Prueba 5
def test_create_new_kit_name_512_character_success_response():
    positive_assert("\"№%@\",")

#Prueba 6
def test_create_new_kit_name_spaces_are_allowed_success_response():
    positive_assert("A Aaa")

#Prueba 7
def test_create_new_kit_numbers_are_allowed_success_response():
    positive_assert("0123")

#no se si al ponerlo aqui no afecte las demas pruebas
def negative_assert(name):
    kit_body = get_kit_body(name)
    kit_body.pop("name", None)
    user_response = sender_stand_request.post_new_kit(kit_body)
    assert user_response.status_code == 400
    assert "error" in user_response.json()

#Prueba 8
def test_create_new_kit_parameter_isnt_in_the_request_error_response():
    negative_assert("a")


def negative_assert_type_error():
    kit_body = get_kit_body(123)
    user_response = sender_stand_request.post_new_kit(kit_body)
    assert user_response.status_code == 400
    assert "error" in user_response.json()

#Prueba 9
def test_create_new_kit_parameter_is_diferent_error_response():
    negative_assert_type_error()
import pytest
import allure
import json
from faker import Faker
from reqs.reqCourier import RequestsCourier


faker = Faker()

@pytest.fixture
@allure.step('Создание запроса для отправки заказа')
def create_order_payload():
    fake_date = faker.date_between(start_date='today', end_date='+1y')
    date = fake_date.strftime("%Y-%m-%d")
    payload = {"firstName": faker.first_name(), "lastName": faker.last_name(),
               "address": faker.address(), "metroStation": 1, "phone": "+79995556677", "rentTime": 2,
               "deliveryDate": date,
               "comment": "Хочу самокат!"}
    return payload

@pytest.fixture
@allure.step('Создание курьера логин/удаление')
def create_courier_login_and_delete(create_user_payload):
    rcr = RequestsCourier()
    payload = rcr.create_courier_post(create_user_payload)
    response = payload
    yield response
    RequestsCourier.delete_courier(courier_id=response["id"])




@pytest.fixture
@allure.step('Заполнение данных по курьеру')
def create_user_payload():
    data = {
        "firstName": faker.name(),
        "login": faker.name(),
        "password": faker.pyint()
        }
    return json.dumps(data)
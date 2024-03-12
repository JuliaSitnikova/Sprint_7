import allure

from faker import Faker
from reqs.reqBase import RequestsBase
import json
from constants import Constants

fake = Faker()


class RequestsCourier(RequestsBase):

    @allure.step('Создание курьера методом POST, ожидание статуса ответа')
    def create_courier_post(self, data=None, status=201):
        url = Constants.COURIER_URL
        return self.post_request_and_check(url, data=data, status=status)

    @allure.step('Логиним курьера методом POST, ожидание статуса ответа')
    def login_courier_post(self, data=None, status=200):
        url = Constants.COURIER_LOGIN_URL
        return self.post_request_and_check(url, data=data, status=status)

    @allure.step('Удаление курьера методом DELETE, ожидание статуса ответа')
    def delete_courier(self, data=None, courier_id=None, status=200):
        url = f'{Constants.COURIER_URL}{courier_id}'
        return self.delete_request_and_check(url, data=data, status=status)


    def create_login_payload(self, login, password):
        data = {
            "login": login,
            "password": password
        }
        return json.dumps(data)
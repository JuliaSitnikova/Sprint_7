import allure
from reqs.reqCourier import RequestsCourier
import pytest
import json


@allure.feature('Проверка регистрации курьеров')
class TestRegistration:

    @allure.title('Успешная регистрация курьера')
    def test_registration_login(self, create_user_payload):
        ctr = RequestsCourier()
        response = ctr.create_courier_post(create_user_payload)
        assert response['ok']
    @allure.title('Ошибка при создании двух курьеров с одинаковыми логинами')
    def test_create_existing_couriers_login(self, create_user_payload):
        ctr = RequestsCourier()
        payload = create_user_payload
        ctr.create_courier_post(payload)
        response = ctr.login_courier_post(payload)
        response_double = ctr.create_courier_post(payload, status=409)
        courier_id = response["id"]
        ctr.delete_courier(courier_id=courier_id)
        assert response_double["message"] == "Этот логин уже используется. Попробуйте другой."

    @pytest.mark.parametrize("payload_data",
                             [
                                 ['', '12345', 'Julia'],
                                 ['byaka', '', 'bubuka'],
                                 ['', '', 'tinz'],
                                 ['', '12345', ''],
                                 ['sitnilk', '', '']
                             ])
    @allure.title('Проверка обязательности полей (логин, пароль), без заполнения курьер не создается')
    def test_required_registration(self, payload_data):
        ctr = RequestsCourier()
        payload = json.dumps(payload_data)
        response = ctr.create_courier_post(payload, status=400)
        assert response["message"] == "Недостаточно данных для создания учетной записи"
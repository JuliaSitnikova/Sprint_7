import allure
from reqs.reqCourier import RequestsCourier
import pytest


@allure.feature('Проверка авторизации курьера')
class TestCourier:
    @allure.title('Успешный вход зарегистрированного курьера')
    def test_login(self, create_courier_login_and_delete):
        response = create_courier_login_and_delete
        assert response.get('id') is not None

    @pytest.mark.parametrize("login, password",
                             [
                                 ('Julia Sitn', ''),
                                 ('', '1234'),
                             ]
                             )
    @allure.title('Проверка обязательности полей логин и курьер')
    def test_required_login(self, login, password):
        rcr = RequestsCourier()
        payload = rcr.create_login_payload(login, password)
        response = rcr.login_courier_post(payload, status=400)
        assert response['message'] == 'Недостаточно данных для входа'


    @allure.title('Проверка невозможности входа с неверным паролем')
    def test_login(self):
        rcr = RequestsCourier()
        payload = rcr.create_login_payload('Julia Sitn', '54321')
        response = rcr.login_courier_post(payload, status=404)
        assert response['message'] == 'Учетная запись не найдена'

    @allure.title('Проверка невозможности входа для удаленного курьера')
    def test_courier_cant_login_after_delete(self, create_user_payload):
        rcr = RequestsCourier()
        payload = create_user_payload
        rcr.create_courier_post(payload)
        response = rcr.login_courier_post(payload)
        courier_id = response["id"]
        response_delete = rcr.delete_courier(courier_id=courier_id)
        assert response_delete['ok']
        response = rcr.login_courier_post(payload, status=404)
        assert response["message"] == "Учетная запись не найдена"
import pytest
import allure

from reqs.reqOrder import RequestsOrder

@allure.feature('Создание и выгрузка списка заказов')
class TestOrder:
    @allure.title('Возможность заказа с разными цветами')
    @pytest.mark.parametrize('color', [
        ['BLACK'],
        ['GREY'],
        ['BLACK', 'GREY'],
        None])


    def test_create_order_pass(self, color, create_order_payload):
        ror = RequestsOrder()
        payload = create_order_payload
        response = ror.create_order_post(payload)
        assert "track" in response.keys()

    @allure.title('Возвращение списка заказов')
    def test_get_order_return_list(self):
        ror = RequestsOrder()
        response = ror.get_orders_list()
        assert "orders" in response.keys()
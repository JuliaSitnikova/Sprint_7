import allure
import json
from reqs.reqBase import RequestsBase
from constants import Constants


class RequestsOrder(RequestsBase):

    @allure.step('Создание заказа методом POST, ожидание статуса ответа')
    def create_order_post(self, data=None, status=201):
        url = Constants.ORDER_URL
        return self.post_request_and_check(url, data=json.dumps(data), status=status)

    @allure.step('Получение списка заказов методом GET, ожидание статуса ответа')
    def get_orders_list(self, status=200):
        url = Constants.ORDER_URL
        return self.get_request_and_check(url, status=status)
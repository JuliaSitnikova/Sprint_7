import requests



class RequestsBase:

    def post_request_and_check(self, url, data, status):
        response = requests.post(url=url, data=data, headers={'Content-Type': 'application/json'})
        assert response.status_code == status
        if 'application/json' in response.headers['Content-Type']:
            return response.json()
        else:
            return response.text

    def delete_request_and_check(self, url, data, status):
        response = requests.delete(url=url, data=data)
        assert response.status_code == status
        if 'application/json' in response.headers['Content-Type']:
            return response.json()
        else:
            return response.text

    def get_request_and_check(self, url, status):
        response = requests.get(url=url)
        assert response.status_code == status
        if 'application/json' in response.headers['Content-Type']:
            return response.json()
        else:
            return response.text

    def put_request_and_check(self, url, data, status):
        response = requests.put(url=url, data=data)
        assert response.status_code == status
        if 'application/json' in response.headers['Content-Type']:
            return response.json()
        else:
            return response.text
import requests


class Test_apiweb:
    # api login test
    def test_get_stats(self):
        url = "https://reqres.in/api/login"
        myobj = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
        x = requests.post(url,data=myobj)
        value = x.status_code
        assert  value == 200


    # api login deny test
    def test_get_deny(self):
        url = "https://reqres.in/api/login"
        myobj = {"email": "peter@klaven"}
        x = requests.post(url,data=myobj)
        value = x.status_code
        assert value == 400


    # api create test
    def test_get_create(self):
        url = "https://reqres.in/api/users"
        myobj = {"name": "morpheus", "job": "leader"}
        x = requests.post(url,data=myobj)
        value = x.status_code
        assert value == 201


    # api update test
    def test_get_update(self):
        url = "https://reqres.in/api/users/2"
        myobj = {"name": "morpheus", "job": "zion resident"}
        x = requests.patch(url,data=myobj)
        value = x.status_code
        assert value == 200


    # api delete test(not working)
    # def test_get_delete(self):
    #     url = "https://reqres.in/api/users/2"
    #     myobj = {}
    #     x = requests.delete(url,data=myobj)
    #     value = x.status_code
    #     assert value == 204


    # test list_users test
    def test_get_users(self):
        url = "https://reqres.in/api/users?page=2"
        myobj = {id: 7, "email": "michael.lawson@reqres.in", "first_name": "Michael", "last_name": "Lawson"}
        x = requests.get(url,data=myobj)
        value = x.status_code
        assert value == 200


    # single user test
    def test_get_users(self):
        url = "https://reqres.in/api/users/2"
        myobj = {id: 2, "email": "janet.weaver@reqres.in", "first_name": "Janet", "last_name": "Weaver"}
        x = requests.get(url,data=myobj)
        value = x.status_code
        assert value == 200




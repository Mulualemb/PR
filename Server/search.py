import requests


class Test_apiweb:
    # api login test
    def test_get_stats(self):
        url = "https://reqres.in/api/login"
        myobj = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
        x = requests.post(url, data=myobj)
        value = x.status_code
        try:
            assert value == 200
        except AssertionError:
            print("fail test")

    # api login deny test
    def test_get_deny(self):
        url = "https://reqres.in/api/login"
        myobj = {"email": "peter@klaven"}
        x = requests.post(url, data=myobj)
        value = x.status_code
        try:
            assert value == 400
        except AssertionError:
            print("fail test")

    # api create test
    def test_get_create(self):
        url = "https://reqres.in/api/users"
        myobj = {"name": "morpheus", "job": "leader"}
        x = requests.post(url, data=myobj)
        value = x.status_code
        try:
            assert value == 201
        except AssertionError:
            print("fail test")

    # api update test
    def test_get_update(self):
        url = "https://reqres.in/api/users/2"
        myobj = {"name": "morpheus", "job": "zion resident"}
        x = requests.patch(url, data=myobj)
        value = x.status_code
        try:
            assert value == 200
        except AssertionError:
            print("fail test")

    # api delete test(not working)
    # def test_get_delete(self):
    #     url = "https://reqres.in/api/users/2"
    #     myobj = {}
    #     x = requests.delete(url,data=myobj)
    #     value = x.status_code
    #     assert value == 204

    # test list_users api test
    def test_get_users(self):
        url = "https://reqres.in/api/users?page=2"
        myobj = {id: 7, "email": "michael.lawson@reqres.in", "first_name": "Michael", "last_name": "Lawson"}
        x = requests.get(url, data=myobj)
        value = x.status_code
        try:
            assert value == 200
        except AssertionError:
            print("fail test")

    # single user api test
    def test_get_single_user(self):
        url = "https://reqres.in/api/users/2"
        myobj = {id: 2, "email": "janet.weaver@reqres.in", "first_name": "Janet", "last_name": "Weaver"}
        x = requests.get(url, data=myobj)
        value = x.status_code
        try:
            assert value == 200
        except AssertionError:
            print("fail test")

    # single_resource_api test
    def test_single_resource(self):
        url = "https://reqres.in/api/unknown/2"
        myobj = {id: 2, "name": "fuchsia rose", "year": 2001, "color": "#C74375", "pantone_value": "17-2031"}
        x = requests.get(url, data=myobj)
        value = x.status_code
        try:
            assert value == 200
        except AssertionError:
            print("fail test")

    # single resource not found api test
    def test_single_resource_not_found(self):
        url = "https://reqres.in/api/unknown/23"
        myobj = {}
        x = requests.get(url, data=myobj)
        value = x.status_code
        try:
            assert value == 404
        except AssertionError:
            print("fail test")

    #  register api test
    def test_register_api(self):
        url = "https://reqres.in/api/register"
        myobj = {"email": "eve.holt@reqres.in", "password": "pistol"}
        x = requests.post(url, data=myobj)
        value = x.status_code
        try:
            assert value == 200
        except AssertionError:
            print("fail test")

    # successful register api test
    def test_successful_register(self):
        url = "https://reqres.in/api/register"
        myobj = {"email": "eve.holt@reqres.in", "password": "pistol"}
        x = requests.post(url, data=myobj)
        value = x.status_code
        try:
            assert value == 200
        except AssertionError:
            print("fail test")

    # unsuccessful register api test
    def test_unsuccessful_register(self):
        url = "https://reqres.in/api/register"
        myobj = {"email": "sydney@fife"}
        x = requests.post(url, data=myobj)
        value = x.status_code
        try:
            assert value == 400
        except AssertionError:
            print("fail test")

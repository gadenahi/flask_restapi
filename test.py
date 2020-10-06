from urllib import request
import json

SERVER_HOST = '127.0.0.1'
SERVER_PORT = '5000'


def call_http_request(req):
    """
    request http
    :param req: url
    :return:
    """
    try:
        with request.urlopen(req) as response:
            print(response.code)
            print(response.reason)
            print(response.read().decode('utf-8'))

    except Exception as e:
        print(e.code)
        print(e.reason)
        print(e.read().decode('utf-8'))


def call_list_users(limit=10, offset=0):
    """
    GET http://host:port/users
    :param limit: limit list number
    :param offset: offset
    :return:
    """
    url = 'http://%s:%s/users?limit=%d&offset=%d' % \
          (SERVER_HOST, SERVER_PORT, limit, offset)
    call_http_request(url)


def call_post_user(name, email):
    """
    POST http://host:port/users
    :param name: name
    :param email: email
    :return:
    """
    input_data = {
        'name': name,
        'email': email
    }
    data = json.dumps(input_data).encode('utf-8')
    url = 'http://%s:%s/users' % (SERVER_HOST, SERVER_PORT)
    headers = {'Content-Type': 'application/json'}
    req = request.Request(url, data=data, method='POST', headers=headers)
    call_http_request(req)


def call_get_user(id):
    """
    GET http://host:port/users/:id
    :param id: user_id
    :return:
    """

    url = 'http://%s:%s/users/%d' % (SERVER_HOST, SERVER_PORT, id)
    call_http_request(url)


def call_put_user(id, name, email):
    """
    PUT http://host:port/users/:id
    :param id: user_id
    :param name: name
    :param email: email
    :return:
    """
    input_data = {
        'name': name,
        'email': email
    }
    data = json.dumps(input_data).encode('utf-8')

    url = 'http://%s:%s/users/%d' % (SERVER_HOST, SERVER_PORT, id)
    headers = {'Content-Type': 'application/json'}
    req = request.Request(url, data=data, method='PUT', headers=headers)
    call_http_request(req)


def call_delete_user(id):
    """
    DELETE http://host:port/users/:id
    :param id: user_id
    :return:
    """
    url = 'http://%s:%s/users/%d' % (SERVER_HOST, SERVER_PORT, id)
    req = request.Request(url, method='DELETE')
    call_http_request(req)


if __name__ == '__main__':
    print("call_list_users")
    call_list_users(10, 0)
    print("----------------")
    print("call_post_user")
    call_post_user('Mike', 'Mike@test.com')
    call_post_user('Ana', 'Ana@test.com')
    call_post_user('Rafael', 'Rafael@test.com')
    call_post_user('Michael', 'Michael@test.com')
    call_post_user('Dyna', 'Dyna@test.com')
    call_post_user('Ellen', 'Ellen@test.com')
    call_post_user('Isabella', 'Isabella@test.com')
    call_post_user('Joan', 'Joan@test.com')
    call_post_user('Julian', 'Julian@test.com')
    call_post_user('Katherine', 'Katherine@test.com')
    call_post_user('Dean', 'Dean@test.com')
    print("----------------")
    print("call_list_users")
    call_list_users(10, 0)
    print("----------------")
    print("call_get_user")
    call_get_user(1)
    print("----------------")
    print("call_put_user")
    call_put_user(1, 'Mike', 'Mike1@test.com')
    print("----------------")
    print("call_delete_user")
    call_delete_user(1)
    print("----------------")
    print("call_list_users")
    call_list_users(10, 0)
    print("----------------")

from squacapipy import squacapi
from squacapipy.squacapi import Response, Network
from unittest.mock import patch
'''to run

    $:pytest --verbose -s test/test_squacapi.py && flake8
'''


def test_empty_header():
    '''should return 401 when token is missing'''
    with patch.object(squacapi, "HEADERS", {}):
        net = Network()
        response = net.get()
        assert response.status_code == 401


@patch.object(Network, 'get')
def test_get_networks(mock_get):
    res = Response(200, [{'code': 'uw'}, {'code': 'cc'}])
    mock_get.return_value = res
    '''should get all networks '''
    net = Network()
    response = net.get()
    assert response.status_code == 200
    assert len(response.body) > 1


@patch.object(Network, 'post')
def test_create_network(mock_post):
    res = Response(201, [{'code': 'uw'}])
    mock_post.return_value = res
    net = Network()
    payload = {
        'code': 'f2',
        'name': 'FU'
    }
    response = net.post(payload)
    assert response.status_code == 201


@patch.object(Network, 'put')
def test_update_network(mock_put):
    res = Response(200, [{'code': 'f1', 'name': 'FR',
                          'description': 'This is the description'}])
    mock_put.return_value = res
    net = Network()
    payload = {
        'code': 'f2',
        'name': 'FR',
        'description': "This is the description"
    }
    response = net.put('f2', payload)
    assert response.status_code == 200

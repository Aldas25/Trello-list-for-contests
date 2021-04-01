import requests
import json
from auth import trello_auth

base_url = 'https://api.trello.com'

# returns all trello boards created by me (I hope so :D)
def get_my_boards ():
    
    url = base_url + '/1/members/me/boards'

    headers = {
        'Accept': 'application/json'
    }

    query = {
        'fields': ['name', 'url'],
        'key': trello_auth['key'],
        'token': trello_auth['token']
    }

    response = requests.request(
        'GET',
        url,
        headers=headers,
        params=query
    )

    return response.text


def get_board (id):
    url = base_url + f'/1/boards/{id}'

    headers = {
        'Accept': 'application/json'
    }

    query = {
        'key': trello_auth['key'],
        'token': trello_auth['token']
    }

    response = requests.request(
        'GET',
        url,
        headers=headers,
        params=query
    )

    if response.text == 'invalid id':
        raise Exception(f'Invalid board id = {id}')
    
    return response.text


def get_lists_on_board (id):
    url = base_url + f'/1/boards/{id}/lists'

    headers = {
        'Accept': 'application/json'
    }

    query = {
        'key': trello_auth['key'],
        'token': trello_auth['token']
    }

    response = requests.request(
        'GET',
        url,
        headers=headers,
        params=query
    )

    if response.text == 'invalid id':
        raise Exception(f'Invalid board id = {id}')
    
    return response.text


def get_list (id):
    url = base_url + f'/1/boards/{id}'

    headers = {
        'Accept': 'application/json'
    }

    query = {
        'key': trello_auth['key'],
        'token': trello_auth['token']
    }

    response = requests.request(
        'GET',
        url,
        headers=headers,
        params=query
    )

    if response.text == 'invalid id':
        raise Exception(f'Invalid board id = {id}')
    
    return response.text


if __name__ == '__main__':
    
    # contest_list = get_lists_on_board(trello_auth['board_id'])
    # print(json.dumps(json.loads(contest_list), indent=2))

    # boards = get_my_boards()
    # print(json.dumps(json.loads(boards), indent=2))
    
    # try:
    #     board = get_board(trello_auth['board_id'])
    #     print(json.dumps(json.loads(board), indent=2))
    # except Exception as e:
    #     print(e.args)
    #     print('An error has occured :(')

    # url = 'https://api.trello.com/1/lists/{}'.format(trello_auth['board_id'])

    # query = {
    #     'key': trello_auth['key'],
    #     'token': trello_auth['token']
    # }

    # response = requests.request(
    #     'GET',
    #     url,
    #     params=query
    # )

    # print(response.text)
    

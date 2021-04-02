import requests
import json
from auth import trello_auth
from contest import Contest

# Based on Trello API documentation: https://developer.atlassian.com/cloud/trello/rest/api-group-actions/
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
    url = base_url + f'/1/lists/{id}'

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
        raise Exception(f'Invalid list id = {id}')
    
    return response.text


def get_cards_in_list (id):
    url = base_url + f'/1/lists/{id}/cards'

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
        raise Exception(f'Invalid list id = {id}')
    
    return response.text


# checks whether contest is already in the list
# (by checking if there is a card with description same as link of the contest)
def contest_added (contest):
    cards_json = get_cards_in_list(trello_auth['contest_list_id'])
    cards = json.loads (cards_json)
    
    for card in cards:
        if card['desc'] == contest.link:
            return True

    return False


def add_contest_to_contest_list (contest):
    url = base_url + f'/1/cards'

    query = {
        'key': trello_auth['key'],
        'token': trello_auth['token'],
        'idList': trello_auth['contest_list_id'],
        'name': contest,
        'desc': contest.link
    }

    response = requests.request(
        'POST',
        url,
        params=query
    )

    # print(response.text)
    # print(json.dumps(response.text, indent=2, separators=(',', ': ')))
    
    return response.text


if __name__ == '__main__':
    
    cards = get_cards_in_list(trello_auth['contest_list_id'])
    print(json.dumps(json.loads(cards), indent=2))
    

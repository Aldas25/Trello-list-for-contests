import requests
import json
from contest import Contest

# TopCoder SRM matches are being get with https://kontests.net/ API 
# (since I have not found other way to do it :( )
base_url = 'https://kontests.net/api/v1'

def get_all_contests (site):
    url = base_url + f'/{site}'

    response = requests.request (
        'GET',
        url
    )

    contests = json.loads(response.text)

    return contests


def get_upcoming_contests (site):
    all_contests = get_all_contests (site)
    
    # gets only contests with 'phase' equal to 'BEFORE' from all_contests
    upcoming_contests = [contest for contest in all_contests if contest['status'] == 'BEFORE']

    # list of Contest objects that will be returned
    contests = []

    for contest in upcoming_contests:

        platform = ''
        link = ''

        if site == 'top_coder':
            platform = 'TC'
            link = f'https://www.topcoder.com/challenges/ {contest["name"]}'
        elif site == 'kick_start':
            platform = 'Kick Start'
            link = f'https://codingcompetitions.withgoogle.com/kickstart/schedule {contest["name"]}'
        else:
            platform = 'Unknown'
            link = f'Unknown link; {contest["name"]}'

        contest_object = Contest(
            platform=platform, 
            name=contest['name'], 
            start_time=contest['start_time'], 
            link=link
        )

        contests.append(contest_object)

    return contests


if __name__ == '__main__':
    contests = get_upcoming_contests ('kick_start')
    for contest in contests:
        contest.print_details()
import requests
import json
from contest import Contest

base_url = 'https://codeforces.com/api'

def get_all_contests ():
    url = base_url + '/contest.list'

    response = requests.request (
        'GET',
        url
    )

    contests = json.loads(response.text)

    return contests


def get_upcoming_contests ():
    all_contests = get_all_contests ()
    
    # gets only contests with 'phase' equal to 'BEFORE' from all_contests
    upcoming_contests = [contest for contest in all_contests['result'] if contest['phase'] == 'BEFORE']

    # list of Contest objects that will be returned
    contests = []

    for contest in upcoming_contests:
        contest_object = Contest(
            platform='CF', 
            name=contest['name'], 
            start_time=contest['startTimeSeconds']*1000, # start time in miliseconds (unix timestamp) 
            link= f'https://codeforces.com/contests {contest["id"]}'
        )

        contests.append(contest_object)

    return contests


if __name__ == '__main__':
    cont = get_upcoming_contests ()
    for c in cont:
        c.print_details()
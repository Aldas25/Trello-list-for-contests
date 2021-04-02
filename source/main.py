import trello
import atcoder as ac
import codeforces as cf
import kontests
from contest import Contest

def get_upcoming_contests ():
    contests = []

    contests.extend (ac.get_upcoming_contests ())
    contests.extend (cf.get_upcoming_contests ())
    contests.extend (kontests.get_upcoming_contests('top_coder'))
    contests.extend (kontests.get_upcoming_contests('kick_start'))

    return contests

if __name__ == '__main__':
    contests = get_upcoming_contests ()

    for contest in contests:
        # contest.print_details ()
        if not trello.contest_added (contest):
            trello.add_contest_to_contest_list (contest)
            print(f'Adding contest to Trello list: {contest}')
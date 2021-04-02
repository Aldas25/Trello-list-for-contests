import trello
import atcoder as ac
import codeforces as cf
from contest import Contest

def get_upcoming_contests ():
    contests = []

    contests.extend (ac.get_upcoming_contests ())
    contests.extend (cf.get_upcoming_contests ())

    return contests

if __name__ == '__main__':
    contests = get_upcoming_contests ()

    for contest in contests:
        # contest.print_details ()
        if not trello.contest_added (contest):
            trello.add_contest_to_contest_list (contest)
import trello
import atcoder
from contest import Contest


if __name__ == '__main__':
    contests = atcoder.get_upcoming_contests ()

    for contest in contests:
        if not trello.contest_added (contest):
            trello.add_contest_to_contest_list (contest)
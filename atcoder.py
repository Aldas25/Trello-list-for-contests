import requests
import lxml.html as lh
from contest import Contest

base_url = 'https://atcoder.jp'
contests_url = base_url + '/contests'

# creates a Contest object from the row in html
def row_to_contest (row):
    # getting values from the row in html
    start_time = row[0][0].get('href')
    contest_name = row[1][1].text_content()
    #duration = row[2].text_content()
    link = base_url + row[1][1].get('href')

    # creating a new contest object
    contest = Contest(platform='AC', name=contest_name, start_time=start_time, link=link)

    return contest


def get_upcoming_contests ():
    page = requests.get(contests_url)
    doc = lh.fromstring(page.content)

    # taking the table where upcoming contests are listed
    table_elements = doc.xpath('//*[@id="contest-table-upcoming"]/div/div/table/tbody')

    contests = []

    for row in table_elements[0]:
        contest = row_to_contest(row)
        contests.append(contest)

    return contests

if __name__ == '__main__':
    contests = get_upcoming_contests()
    for contest in contests:
        print(contest)
import requests
import lxml.html as lh
from contest import Contest

base_url = 'https://atcoder.jp'
contests_url = base_url + '/contests'

def get_atcoder_upcoming_contests ():
    page = requests.get(contests_url)
    doc = lh.fromstring(page.content)

    # taking the table where upcoming contests are listed
    table_elements = doc.xpath('//*[@id="contest-table-upcoming"]/div/div/table/tbody')

    contests = []

    for tbody in table_elements:
        for row in tbody:

            # getting values from the row in html
            start_time = row[0][0].get('href')
            contest_name = row[1][1].text_content()
            #duration = row[2].text_content()
            link = base_url + row[1][1].get('href')
        
            # creating a new contest object
            contest = Contest(platform='AC', name=contest_name, start_time=start_time, link=link)

            contests.append(contest)

            print(contest)

    return contests

# get_atcoder_upcoming_contests()
# Trello list for upcoming CP (competitive programming) contests

## About

A tiny Python script that finds upcoming contests and adds them to your Trello list (using Trello API).

Sites from which contests are taken:

* [AtCoder](https://atcoder.jp/) (taking contests from HTML file with `lxml` python package)
* [Codeforces](https://codeforces.com/) (taking contests using [Codeforces API](https://codeforces.com/apiHelp))
* [TopCoder](https://www.topcoder.com/) (taking contests using [kontests.net API](https://kontests.net/api))
* [Google Kick Start](https://codingcompetitions.withgoogle.com/kickstart) (taking contests using [kontests.net API](https://kontests.net/api))


## How to run

Firstly, you will need a key and a token for Trello API. More info can be found [here](https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/) and [here](https://trello.com/app-key)

After cloning or downloading this repository, in the `source` folder you have to create the `auth.py` file which should look the same as `auth_example.py`.

Now just run the `main.py` file in the `source` folder:
```
python source/main.py
```
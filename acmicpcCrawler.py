from bs4 import BeautifulSoup
from urllib.request import urlopen
import argparse
import mechanicalsoup
import urllib

import ssl

parser = argparse.ArgumentParser(description='Login to acmicpc.')
parser.add_argument("username")
parser.add_argument("password")
args = parser.parse_args()
print(args)
print(args.username)

browser = mechanicalsoup.Browser()

# request github login page. the result is a requests.Response object http://docs.python-requests.org/en/latest/user/quickstart/#response-content
login_page = browser.get("https://www.acmicpc.net/login")

print(type(login_page))
print(type(login_page.soup))
# print(login_page.soup) # 내용물 보기
print(login_page.soup.prettify()) # 이쁘게 내용물 보기

# res = urlopen('https://github.com/').read().decode('utf-8')
# res = urlopen('https://www.acmicpc.net/group/practice/1094/1').read().decode('utf-8')


# print(res)
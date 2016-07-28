from bs4 import BeautifulSoup
from urllib.request import urlopen
# 인터넷 환경인지 확인해주세요

res = urlopen('https://github.com/SSUHan?tab=repositories').read().decode('utf-8')
# urlopen 으로 해당 url 의 html 코드들을 가져옵니다

# print(res)

soup = BeautifulSoup(res, 'html.parser')
# BeautifulSoup 객체의 파싱 방법은 4가지가 있다고 합니다 그중 html.parser를 사용할 것입니다

print(type(soup))
# bs4.BeautifulSoup 객체가 리턴됩니다

repo_list = soup.find_all('div', class_='repo-list-item public source')
# div 태그인데 클래스가 다음과 같은 div 태그들을 전부 찾아서 반환합니다
print(type(repo_list))
# 리턴된 타입은 bs4.element.ResultSet 객체 입니다
for repo_item in repo_list:

    # repo_item = repo_list[0]
    # 내용물이 많기때문에 그 중 첫번째 요소를 받아냅니다
    # print(repo_item.prettify()) 이거 됩니다 ㅋㅋ
    # print(type(repo_item))
    # 각각의 아이템의 타입은 bs4.element.Tag 객체 입니다

    print('='*20) # 구분선을 두었으니 어디가 어디까지인지 확인하실 수 있습니다
    repo_name = repo_item.h3.a.string.strip()
    print(repo_name)
    # 실제적인 바디값을 얻으려면 위와 같이 하면 됩니다
    repo_disc = repo_item.p.string
    if repo_disc:
        print(repo_disc.strip())
    else:
        print('no discription on this repo')
    link = "https://github.com" + repo_item.h3.a['href']
    # 링크를 완성하기 위해서 join 합니다
    print(link)
    # 짠 여러분들은 해당 repo 의 링크를 얻어냈습니다
    print('='*20)

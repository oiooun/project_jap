# package import
import requests                         
from pandas import DataFrame
from bs4 import BeautifulSoup
import re
from datetime import datetime
import os

# 현재 시간 저장
time = str(datetime.now())        # 엑셀 저장 시 크롤링한 날짜, 시간을 파일명에 넣기 위해 저장
time = time[:time.rfind(':')].replace(' ', '_')
time = time.replace(':', '시') + '분'

# input 생성
query = input('검색 키워드를 입력하세요 : ')  # 검색할 키워드, 추출할 뉴스 기사 수 저장
news_num = int(input('총 필요한 뉴스기사 수를 입력해주세요(숫자만 입력) : '))
query = query.replace(' ', '+')  # query에서 ' ' 를 '+'로 바꾸어주는 이유는 띄어쓰기 시 URL 조건 절에 '+'로 적용되어 요청 인자가 들어가기 때문.


# 요청할 URL 생성 및 요청
news_url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={}' # 키워드(query)를 URL의 조건절 중 키워드에 해당하는 변수에 대응시켜 요청 URL 생성.

req = requests.get(news_url.format(query))      # request package의 get 함수를 이용하여 HTML 코드 받기
soup = BeautifulSoup(req.text, 'html.parser')   # 받은 코드를 bs4의 BeautifulSoup 함수를 이용하여 파싱


# 원하는 정보를 담을 변수 생성 (key : 번호, value : 뉴스 기사 정보)
news_dict = {}  # 딕셔너리 형태
idx = 0  # idx : 현재 뉴스의 번호
cur_page = 1  # cur_page : 네이버 뉴스의 웹 페이지

print()
print('크롤링 중...')

# HTML 코드에서 태그를 이용하여 원하는 정보 탐색
while idx < news_num:
    table = soup.find('ul', {'class': 'list_news'})
    li_list = table.find_all('li', {'id': re.compile('sp_nws.*')})
    area_list = [li.find('div', {'class': 'news_area'}) for li in li_list]
    a_list = [area.find('a', {'class': 'news_tit'}) for area in area_list]

    for n in a_list[:min(len(a_list), news_num - idx)]:
        news_dict[idx] = {'title': n.get('title'),  # news_dict : 뉴스 기사를 담는 딕셔너리
                          'url': n.get('href')}
        idx += 1

    cur_page += 1

    pages = soup.find('div', {'class': 'sc_page_inner'})
    next_page_url = [p for p in pages.find_all('a') if p.text == str(cur_page)][0].get('href') # 현재 수집한 뉴스 기사 수가 부족한 경우 다음 페이지로 넘어가야 하므로 다음 페이지에 해당하는 URL을 추출

    req = requests.get('https://search.naver.com/search.naver' + next_page_url)
    soup = BeautifulSoup(req.text, 'html.parser')

# 최종 데이터 생성 => 데이터 프레임 변환 및 저장
print('크롤링 완료')

print('데이터프레임 변환')
news_df = DataFrame(news_dict).T  # 딕셔너리(news_dict)를 데이터 프레임(news_df)으로 변환

folder_path = os.getcwd()
xlsx_file_name = '네이버뉴스_{}_{}.xlsx'.format(query, time)  # 크롤링한 키워드(query)와 크롤링 날짜(date)를 엑셀 파일 명으로 하여 저장

news_df.to_excel(xlsx_file_name)

print('엑셀 저장 완료 | 경로 : {}\\{}'.format(folder_path, xlsx_file_name))
os.startfile(folder_path)

from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import quote
import pandas as pd

# News 수집 실행
def get_news(query, page_num=10):

    news_df = pd.DataFrame(columns=("Title", "Link", "Press", "DateTime", "Article"))
    idx = 0

    url_query = quote(query)
    url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=" + url_query

    for _ in range(0, page_num):
        search_url = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(search_url, 'html.parser')
        links = soup.find_all('div', {'class':'info_group'})

        for link in links:
            news_urls = link.find_all('a')
            if(len(news_urls) < 2):
               continue
            else:
                press = news_urls[0].get_text()
                news_url = news_urls[1].get('href')

                news_link = urllib.request.urlopen(news_url).read()
                news_html = BeautifulSoup(news_link, 'html.parser')

                try:
                    title = news_html.find('h3', {'id':'articleTitle'}).get_text()
                    datetime = news_html.find('span', {'class':'t11'}).get_text()
                    article = news_html.find('div', {'id': 'articleBodyContents'}).get_text()
                    article = article.replace("// flash 오류를 우회하기 위한 함수 추가", "")
                    article = article.replace("function _flash_removeCallback() {}", "")
                    article = article.replace("\n", "")
                    article = article.replace("\t", "")

                    if(datetime[0:4] != '2021'):
                        continue

                    news_df.loc[idx] = [title, news_url, press, datetime, article]
                    idx += 1
                    print("#", end="")
                except:
                    continue

        try:
            next = soup.find('a', {'class':'btn_next'}).get('href')
            url = "https://search.naver.com/search.naver" + next
        except:
            break

    return news_df

query = input('검색 질의 : ')
news_df = get_news(query, 50)
print('Done')
news_df.to_excel('News_Crawling_%s.xlsx' % query)
print(news_df)

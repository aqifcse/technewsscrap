from lxml import html
from requests_html import HTMLSession
from collections import OrderedDict
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from urllib.parse import urljoin
import json

#def get_search_url(ticker_search_keyword):
def get_search_url():

    # ticker_search_url = "https://news.yahoo.co.jp/categories/%s" % ticker_search_keyword

    url = 'https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=105'
    session = HTMLSession()
    # ticker_resp = session.get(ticker_search_url)
    # ticker_soup = BeautifulSoup(ticker_resp.text, "lxml")
     
    # return ticker_soup

    resp = session.get(url)
    soup = BeautifulSoup(resp.text, "lxml")
     
    return soup

# def parse(page, ticker):
def parse(page):

    print(page)
    # title = '', 
    # thumbnail = '', 
    # title_link = '', 
    # media = '', 
    # date_and_time = '',


    # newsfeed_output = {
    #     "title": title, 
    #     "thumbnail": thumbnail, 
    #     "title_link":  title_link, 
    #     "media":  media, 
    #     "date_and_time": date_and_time,
    # }

    # output = {'ticker': ticker, 'newsfeeds': newsfeed_output}

    # newsfeed_list = page.find("ul",attrs={"class":"newsFeed_list"})

    # print(newsfeeds)

    # for newsfeed in newsfeeds:

    #     title = newsfeed.find("div",attrs={"class":"newsFeed_item_title"})
    #     if title is not None: title = title.getText() #.replace('\n', '')
    #     else: title = ""

    #     print(title)

    #     thumbnail = newsfeed.find("img")
    #     if thumbnail is not None: thumbnail = thumbnail.get('href')
    #     else: thumbnail = ""

    #     print(thumbnail)

    #     title_link = newsfeed.find("a",attrs={"class":"newsFeed_item_link"})
    #     if title_link is not None: title_link = title_link.get('href')
    #     else: title_link = ""

    #     media = newsfeed.find("span",attrs={"class":"newsFeed_item_media"})
    #     if media is not None: media = media.getText()
    #     else: media = ""

    #     date_and_time = newsfeed.find("time",attrs={"class":"newsFeed_item_date"})
    #     if date_and_time is not None: date_and_time = date_and_time.getText()
    #     else: date_and_time = ""

    #     newsfeed_output = {
    #         "title": title, 
    #         "thumbnail": thumbnail, 
    #         "title_link":  title_link, 
    #         "media":  media, 
    #         "date_and_time": date_and_time,
    #     }

    # return output

#def main_fun_2(keyword):
def main_fun_2():
    """
    main function for interact with this module
    :param text: user input
    :return: product_title, product_price
    """
    # page = get_search_url(keyword)
    # scraped_data = parse(page, keyword)

    page = get_search_url()
    scraped_data = parse(page)

    # file = open('%s-summary.json' % (ticker), 'w', encoding='utf-8')
    file = open('%s-summary.json', 'w', encoding='utf-8')
    json.dump(scraped_data, file, ensure_ascii=False)

    return scraped_data


if __name__ == '__main__':

    #ticker_search_keyword = 'it'

    #main_fun_2(ticker_search_keyword)

    main_fun_2()
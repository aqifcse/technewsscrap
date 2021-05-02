from lxml import html
from requests_html import HTMLSession
from collections import OrderedDict
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from urllib.parse import urljoin
import json

def get_search_url(query_search_keyword):

    query_search_url = "https://news.google.com/search?q=%s" % query_search_keyword
    print(query_search_url)
    session = HTMLSession()
    query_resp = session.get(query_search_url)
    query_soup = BeautifulSoup(query_resp.text, "lxml")
     
    return query_soup


def parse(page, query):

    newsfeeds = page.find_all("div", attrs={"class":"NiLAwe y6IFtc R7GTQ keNKEd j7vNaf nID9nc"})

    newsfeed_list = []

    for newsfeed in newsfeeds:

        newsfeed.newsfeed_output = {
            "title": '', 
            "thumbnail": '', 
            "title_link":  '',
            "news_source": '',
            "time":  '', 
        }

        title = newsfeed.find("h3", attrs={"class":"ipQwMb ekueJc RD0gLb"}).find("a")
        if title is not None: title = title.getText() #.replace('\t', '').replace('\n', '').replace(' ', '')
        else: title = ""

        thumbnail = newsfeed.find("a").find("figure").find("img")
        if thumbnail is not None: thumbnail = thumbnail.get('src')
        else: thumbnail = ""

        title_link = newsfeed.find("a", attrs={"class":"VDXfz"})
        if title_link is not None: title_link = urljoin('https://news.google.com', title_link.get('href'))
        else: title_link = ""

        news_source = newsfeed.find("div", attrs={"class":"SVJrMe"}).find("a")
        if news_source is not None: news_source = news_source.getText()
        else: news_source = ""

        time = newsfeed.find("time", attrs={"class":"WW6dff uQIVzc Sksgp"})
        if time is not None: time= time.getText() #.replace('\t', '').replace('\n', '').replace(' ', '')
        else: time= ""

        newsfeed.newsfeed_output["title"] = title
        newsfeed.newsfeed_output["thumbnail"] = thumbnail
        newsfeed.newsfeed_output["title_link"] = title_link
        newsfeed.newsfeed_output["news_source"] = news_source
        newsfeed.newsfeed_output["time"] = time

        newsfeed_list.append(newsfeed.newsfeed_output) 

    output = {
        'query': query, 
        'newsfeeds': newsfeed_list
    }

    return output

def main_fun(query):
    page = get_search_url(query)
    scraped_data = parse(page, query)

    file = open('google-news-summary.json', 'w', encoding='utf-8')
    json.dump(scraped_data, file, ensure_ascii=False)

    return scraped_data


if __name__ == '__main__':

    query_search_keyword = 'ai'

    output = main_fun(query_search_keyword)

    print('JSON output =====>', output)
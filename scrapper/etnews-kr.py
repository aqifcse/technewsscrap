from lxml import html
from requests_html import HTMLSession
from collections import OrderedDict
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from urllib.parse import urljoin
import json

def get_search_url(query_search_keyword):

    query_search_url = "https://search.etnews.com/etnews/search.php?category=CATEGORY1&kwd=%s" % query_search_keyword
    session = HTMLSession()
    query_resp = session.get(query_search_url)
    query_soup = BeautifulSoup(query_resp.text, "lxml")
     
    return query_soup


def parse(page, query):

    newsfeeds = page.find("ul", attrs={"class":"list_news"}).find_all('li')

    newsfeed_list = []

    for newsfeed in newsfeeds:

        newsfeed.newsfeed_output = {
            "title": '', 
            "thumbnail": '', 
            "title_link":  '', 
            "summary":  '', 
            "date_and_time": '',
        }

        title = newsfeed.find("dl").find("dt").find("a")
        if title is not None: title = title.getText() #.replace('\n', '')
        else: title = ""

        thumbnail = newsfeed.find("dl").find_all("dd")[0].find("a").find("img")
        if thumbnail is not None: thumbnail = thumbnail.get('src')
        else: thumbnail = ""

        title_link = newsfeed.find("dl").find("dt").find("a")
        if title_link is not None: title_link = 'https:' + title_link.get('href')
        else: title_link = ""

        summary = newsfeed.find("dl").find("dd", attrs={"class":"summury"})
        if summary is not None: summary = summary.getText()
        else: summary = ""

        date_and_time = newsfeed.find("dl").find("dd", attrs={"class":"date"}).find("span")
        if date_and_time is not None: date_and_time = date_and_time.getText()
        else: date_and_time = ""

        newsfeed.newsfeed_output["title"] = title
        newsfeed.newsfeed_output["thumbnail"] = thumbnail
        newsfeed.newsfeed_output["title_link"] = title_link
        newsfeed.newsfeed_output["summary"] = summary
        newsfeed.newsfeed_output["date_and_time"] = date_and_time

        newsfeed_list.append(newsfeed.newsfeed_output) 

    output = {
        'query': query, 
        'newsfeeds': newsfeed_list
    }

    return output

def main_fun(query):
    page = get_search_url(query)
    scraped_data = parse(page, query)

    file = open('etnews-jp-summary.json', 'w', encoding='utf-8')
    json.dump(scraped_data, file, ensure_ascii=False)

    return scraped_data


if __name__ == '__main__':

    query_search_keyword = 'ai'

    output = main_fun(query_search_keyword)

    print('JSON output =====>', output)
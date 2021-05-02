from lxml import html
from requests_html import HTMLSession
from collections import OrderedDict
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from urllib.parse import urljoin
import json

def get_search_url(query_search_keyword):

    query_search_url = "https://internetcom.jp/news/search:%s" % query_search_keyword
    print(query_search_url)
    session = HTMLSession()
    query_resp = session.get(query_search_url)
    query_soup = BeautifulSoup(query_resp.text, "lxml")
     
    return query_soup


def parse(page, query):

    print(page)

    # newsfeeds = page.find_all("li", attrs={"class":"related-li"})

    # newsfeed_list = []

    # for newsfeed in newsfeeds:

    #     newsfeed.newsfeed_output = {
    #         "title": '', 
    #         "thumbnail": '', 
    #         "title_link":  '', 
    #         "summary":  '', 
    #         "category": '',
    #     }

    #     title = newsfeed.find("a").find("p", attrs={"class":"related-title related-title-over"})
    #     if title is not None: title = title.getText().replace('\t', '').replace('\n', '').replace(' ', '')
    #     else: title = ""

    #     thumbnail = newsfeed.find("a").find("img")
    #     if thumbnail is not None: thumbnail = thumbnail.get('data-original')
    #     else: thumbnail = ""

    #     title_link = newsfeed.find("a")
    #     if title_link is not None: title_link = title_link.get('href')
    #     else: title_link = ""

    #     summary = newsfeed.find("a").find("p", attrs={"class":"related-summary hidden-phone"})
    #     if summary is not None: summary = summary.getText().replace('\t', '').replace('\n', '').replace(' ', '')
    #     else: summary = ""

    #     category= newsfeed.find("a").find("div", attrs={"class":"clearfix index-last-line2"}).find("div", attrs={"class":"line-category"})
    #     if category is not None: category= category.getText().replace('\t', '').replace('\n', '').replace(' ', '')
    #     else: category= ""

    #     buzz_count= newsfeed.find("a").find("div", attrs={"class":"clearfix index-last-line2"}).find("div", attrs={"class":"line-buzz-count"})
    #     if buzz_count is not None: buzz_count= buzz_count.getText().replace('\t', '').replace('\n', '').replace(' ', '')
    #     else: buzz_count= ""

    #     newsfeed.newsfeed_output["title"] = title
    #     newsfeed.newsfeed_output["thumbnail"] = thumbnail
    #     newsfeed.newsfeed_output["title_link"] = title_link
    #     newsfeed.newsfeed_output["summary"] = summary
    #     newsfeed.newsfeed_output["category"] = category
    #     newsfeed.newsfeed_output["buzz_count"] = buzz_count

    #     newsfeed_list.append(newsfeed.newsfeed_output) 

    # output = {
    #     'query': query, 
    #     'newsfeeds': newsfeed_list
    # }

    # return output

def main_fun(query):
    page = get_search_url(query)
    scraped_data = parse(page, query)

    file = open('internetcom-jp-summary.json', 'w', encoding='utf-8')
    json.dump(scraped_data, file, ensure_ascii=False)

    return scraped_data


if __name__ == '__main__':

    query_search_keyword = 'ai'

    output = main_fun(query_search_keyword)

    print('JSON output =====>', output)
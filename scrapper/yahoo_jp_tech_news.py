from bs4 import BeautifulSoup
from requests_html import HTMLSession


def live_get_url(content):
    # return search result lxml page.
    """
    parse html page form url
    :return:
    """
    request_url = 'https://news.yahoo.co.jp/categories/%s' % content

    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) '
    #                   'Chrome/73.0.3683.86 Safari/537.36',
    #     'Accept-Encoding': ''
    # }
    session = HTMLSession()
    #session.headers.update(headers)

    resp = session.get(request_url)
    # resp.html.render(timeout=15)
    soup = BeautifulSoup(resp.html.html, "lxml")
    return soup


def main_fun(content):
    page = live_get_url(content)
    
    newsfeed_list = []

    newsfeeds = page.find_all("ul", attrs={"class": "newsFeed_list"})
    for newsfeed in newsfeeds:

        title = newsfeed.find("div",attrs={"class":"newsFeed_item_title"})
        if title is not None: title = title.getText().replace('\n', '')
        else: title = ""

        # thumbnail = newsfeed.find("img")
        # if thumbnail is not None: thumbnail = thumbnail.get('href')
        # else: thumbnail = ""

        # title_link = newsfeed.find("a",attrs={"class":"newsFeed_item_link"})
        # if title_link is not None: title_link = title_link.get('href')
        # else: title_link = ""

        # media = newsfeed.find("span",attrs={"class":"newsFeed_item_media"})
        # if media is not None: media = media.getText()
        # else: media = ""

        # date_and_time = newsfeed.find("time",attrs={"class":"newsFeed_item_date"})
        # if date_and_time is not None: date_and_time = date_and_time.getText()
        # else: date_and_time = ""

        newsfeed.newsfeed_output["title"] = title
        # newsfeed.newsfeed_output["thumbnail"] = thumbnail
        # newsfeed.newsfeed_output["title_link"] = title_link
        # newsfeed.newsfeed_output["media"] = media
        # newsfeed.newsfeed_output["date_and_time"] = date_and_time

        newsfeed_list.append(newsfeed.newsfeed_output) 

    output = {
        'content': content, 
        'newsfeeds': newsfeed_list
    }

    return output

if __name__ == '__main__':
    content = 'it'
    out = main_fun(content)
    print('JSON Out: ===', out)

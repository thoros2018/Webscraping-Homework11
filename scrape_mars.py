from splinter import Browser
from bs4 import BeautifulSoup
import selenium
import time 

def init_browser():
    
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()
    mars = {}

    # NASA Mars News
    url = "https://mars.nasa.gov/news"
    browser.visit(url)
    time.sleep(4)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    mars["news_date"] = soup.find("div", class_="list_date").get_text()
    mars["news_title"] = soup.find("div", class_="content_title").get_text()
    mars["news_p"] = soup.find("div", class_="article_teaser_body").get_text()

    # JPL Mars Space Images - Featured Image
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    time.sleep(2)

    full_image_elem = browser.find_by_id('full_image')
    full_image_elem.click()
    time.sleep(2)

    more_info_elem = browser.find_link_by_partial_text('more info')
    more_info_elem.click()
    time.sleep(2)

    html = browser.html
    jpl_soup = BeautifulSoup(html, 'html.parser')

    img_url = jpl_soup.find('figure', class_='lede').find('img')['src']

    mars["featured_image"] = f'https://www.jpl.nasa.gov{img_url}'

    # Mars Weather
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)
    time.sleep(3)

    html = browser.html
    mars_weather_soup = BeautifulSoup(html, 'html.parser')

    weather = mars_weather_soup.find('div', class_='js-tweet-text-container')

    mars_weather = weather.find('p', class_='tweet-text').text
    
    # Mars Facts
    url = "http://space-facts.com/mars/"
    browser.visit(url)

    # Mars Hemispheres
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    time.sleep(2)

    html = browser.html
    mars_hems_soup = BeautifulSoup(html, 'html.parser')
    # mars_hems=[]
    
    # for i in range (4):
    #     browser.find_by_tag('h3')
    #     images[i].click()
    #     soup.find("img", class_="wide-image")["src"]
    #     soup.find("h2",class_="title").text
    #     hems={"title":img_title,"img_url":img_url}
    #     mars_hems.append(hems)
    #     browser.back()
    #     # print(mars_hems)

    browser.quit()

    return mars
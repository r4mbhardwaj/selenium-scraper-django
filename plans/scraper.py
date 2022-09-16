from bs4 import BeautifulSoup
from selenium import webdriver
import time


def get_plans():
    driver = webdriver.Chrome()
    driver.get("https://www.airtel.in/myplan-infinity/")
    time.sleep(5)
    html = driver.page_source
    soup = BeautifulSoup(html, "lxml")
    plans = soup.find_all("div", {"class": "single_cart"})
    driver.quit()  # closing driver
    return plans


def scrape_plans():
    """
    Scrapes plans from airtel website
    """
    plans = get_plans()  # getting plans
    responses = []  # list of plans
    for plan in plans:
        # there are two div tags with class single_cart
        all_divs = plan.find_all("div")
        # from first div tag
        first_div = all_divs[0]
        second_div = all_divs[1]  # from second div tag

        # getting plan price
        price = first_div.find("span", {"class": "price"}).text
        priceInfo = first_div.find("span", {"class": "priceInfo"}).text

        # print(f"price: {price}")
        # print(f"priceInfo: {priceInfo}")

        # from second div tag
        # getting inner div tags
        benifits = second_div.find_all("div", {"class": "border-bottom"})
        benifit_data = {}  # empty dict
        for benifit in benifits:
            # getting benifits
            value = None  # empty value
            for i in benifit:
                ans = i.text  # getting text
                if value:  # if value is not empty
                    benifit_data[ans] = value  # adding to dict
                    value = None  # emptying value
                else:  # if value is empty
                    value = ans  # adding to value
        # got all benifits
        responses.append(
            {
                "price": price,
                "priceInfo": priceInfo,
                "benifits": benifit_data,
            }
        )
    return responses

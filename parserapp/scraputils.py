import time
import requests
from bs4 import BeautifulSoup

import parserapp.config as config


def convert_category_name(category: str) -> str:
    resp = requests.get(config.BASE_URL + f"/catalog/{category}")
    soup = BeautifulSoup(resp.text, "html.parser")
    category_name = soup.find("h1").text
    return category_name


def get_last_page(category: str) -> int:
    """Get the last page of the given category"""

    resp = requests.get(config.BASE_URL + f"/catalog/{category}")
    soup = BeautifulSoup(resp.text, "html.parser")
    page_items = soup.find("ul", {"class": "pagination"}).find_all('li')

    return int(page_items[len(page_items)-2].text)


def get_furniture_on_page(category: str, page: int) -> list:
    """Gather info from all item cards on the given page"""

    resp = requests.get(config.BASE_URL + f"/catalog/{category}/?page={page}")
    soup = BeautifulSoup(resp.text, "html.parser")

    furniture_on_page = soup.find_all(
        "div", {"class": "col-lg-3 col-md-4 col-sm-6 mb-3 fadeInUp"})

    category_name = soup.find("h1").text

    furniture_list = []
    for furniture in furniture_on_page:

        id = int(furniture.find("a")["href"].split("?offerId=")[1])
        name = soup.find("div", {"class": "item__title h4"}).find("a").text

        furniture_description = soup.find(
            "div", {"class": "item__description"})

        ven_code = furniture_description.find_all(
            "small")[0].text.split(" ")[1]
        status = furniture_description.find_all("small")[1].text
        furniture_type = furniture_description.find_all("p")[0].text
        furniture_sort = furniture_description.find_all("p")[1].text
        furniture_color = furniture_description.find_all("p")[2].text

        try:
            disc_price = int(furniture.find("div", {"class": "price"}).find(
                "div", {"class": "online-price"}).text.replace(" ", "")[:-1])

            orig_price = int(furniture.find("div", {"class": "price"}).find(
                "a", {"class": "store-price fake-link"}
                ).text.replace(" ", "")[:-1])

        except AttributeError:
            orig_price = disc_price

        furniture_dict = {"id": id,
                          "ven_code": ven_code,
                          "name": name,
                          "category_name": category_name,
                          "furniture_color": furniture_color,
                          "furniture_type": furniture_type,
                          "furniture_sort": furniture_sort,
                          "status": status,
                          "orig_price": orig_price,
                          "disc_price": disc_price}

        print(furniture_dict)

        furniture_list.append(furniture_dict)

    return furniture_list


def get_whole_category(category: str) -> list:
    """Get whole category items page by page"""

    category_list = []
    n_pages = get_last_page(category)
    for page in range(1, n_pages+1):

        category_list += get_furniture_on_page(category, page)

        time.sleep(1)

    return category_list


if __name__ == "__main__":

    category = "0000812"
    category_name = convert_category_name(category)
    print(category_name)

    n_pages = get_last_page(category)
    print(n_pages)

    coach_list = get_whole_category(category)
    print(coach_list)

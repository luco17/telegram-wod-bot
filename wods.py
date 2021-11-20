import requests
from bs4 import BeautifulSoup

ROW_URL = "https://www.concept2.com/indoor-rowers/training/wod"
SKI_URL = "https://www.concept2.com/skierg/training/wod"
BIKE_URL = "https://www.concept2.com/bikeerg/training/wod"


def scrape_wod(machine_url):
    """Returns wods from the C2 website"""
    short_id = "wod-short"
    medium_id = "wod-medium"
    long_id = "wod-long"

    try:
        response = requests.get(machine_url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

    soup = BeautifulSoup(response.content, "html.parser")

    short_wod = get_wod(short_id, soup)
    medium_wod = get_wod(medium_id, soup)
    long_wod = get_wod(long_id, soup)

    wod_dict = {"Short WOD": short_wod,
                "Medium WOD": medium_wod, "Long WOD": long_wod}
    return wod_dict


def get_wod(wod_id, soup):
    '''Return a wod's text from C2'''
    wod_raw = soup.find(id=wod_id)
    wod_text = wod_raw.p.text.strip()
    return wod_text


def get_rowing_wods():
    wods = scrape_wod(ROW_URL)
    return wods


def get_bike_wods():
    wods = scrape_wod(BIKE_URL)
    return wods


def get_ski_wods():
    wods = scrape_wod(SKI_URL)
    return wods


def wod_dict_to_text(wod_dict):
    text = "".join([f"{key}:\n{value}\n\n" for key, value in wod_dict.items()])
    return text


if __name__ == "__main__":
    row_wods = get_rowing_wods()
    text = wod_dict_to_text(row_wods)
    print(text)

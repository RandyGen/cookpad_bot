import time
from urllib.parse import urljoin
import pathlib
import pandas as pd
import requests
from bs4 import BeautifulSoup

COOKPAD_URL = "https://cookpad.com"


def get_recipe_urls(url):
    ret = requests.get(url)
    soup = BeautifulSoup(ret.text, "html.parser")
    category_recipes = soup.find("div", {"id": "category_recipes"})
    urls = [
        urljoin(COOKPAD_URL, a_tag["href"])
        for a_tag in category_recipes.find_all("a", {"class": "recipe-title"})
    ]

    return urls


def get_next_page_url(url):
    ret = requests.get(url)
    soup = BeautifulSoup(ret.text, "html.parser")
    a_next_tag = soup.find("div", {"class": "paginate"}).find(
        "a", {"class": "next_page"}
    )

    if a_next_tag is None:
        return None

    return urljoin(COOKPAD_URL, a_next_tag["href"])


def save_recipe(url):
    ret = requests.get(url)
    soup = BeautifulSoup(ret.text, "html.parser")
    steps = soup.find("div", {"id": "steps"})
    instructions = steps.find_all("dd", {"class": "instruction"})
    instruction_text = [
        instruction.get_text().replace("\n", "") for instruction in instructions
    ]

    df = pd.DataFrame(instruction_text)
    recipe_id = ret.url.split("/")[-1]

    fpath = pathlib.Path("recipe_data") / f"{recipe_id}.csv"
    df.to_csv(fpath, index=False)


def main():
    target_category_url = "https://cookpad.com/category/12?page=1"

    while True:
        recipe_urls = get_recipe_urls(target_category_url)

        # save each recipe
        for url in recipe_urls:
            print(f"Now save {url}.....")
            save_recipe(url)
            time.sleep(1)

        target_category_url = get_next_page_url(target_category_url)
        print(f"Next page: {target_category_url}")
        if target_category_url is None:
            break


if __name__ == "__main__":


    main()

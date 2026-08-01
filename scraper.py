"""
Prodigy Infotech - Task 05: Web Scraping
Extracts product name, price, and rating from books.toscrape.com
(a site made specifically for practicing scraping) and saves to a CSV file.
"""

import csv
import time
import requests
from bs4 import BeautifulSoup

BASE_URL = "http://books.toscrape.com/catalogue/page-{}.html"
OUTPUT_FILE = "products.csv"

# Star rating words used by the site -> numeric value
RATING_MAP = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
}


def get_page(page_number):
    """Fetch a single catalogue page and return its HTML, or None if it fails."""
    url = BASE_URL.format(page_number)
    response = requests.get(url, timeout=10)
    if response.status_code != 200:
        return None
    return response.text


def parse_products(html):
    """Parse one page's HTML and return a list of product dicts."""
    soup = BeautifulSoup(html, "html.parser")
    products = []

    for item in soup.select("article.product_pod"):
        name = item.h3.a["title"]

        price_text = item.select_one(".price_color").get_text(strip=True)
        price = price_text.replace("£", "").strip()

        rating_classes = item.select_one("p.star-rating")["class"]
        # rating_classes looks like ['star-rating', 'Three']
        rating_word = rating_classes[1] if len(rating_classes) > 1 else "Zero"
        rating = RATING_MAP.get(rating_word, 0)

        products.append({
            "name": name,
            "price": price,
            "rating": rating,
        })

    return products


def scrape_all_pages(max_pages=5):
    """Loop through pages and collect all product data."""
    all_products = []

    for page in range(1, max_pages + 1):
        print(f"Scraping page {page}...")
        html = get_page(page)
        if html is None:
            print("No more pages found. Stopping.")
            break

        products = parse_products(html)
        all_products.extend(products)

        time.sleep(1)  # be polite to the server

    return all_products


def save_to_csv(products, filename=OUTPUT_FILE):
    """Save the list of product dicts to a CSV file."""
    if not products:
        print("No products to save.")
        return

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "price", "rating"])
        writer.writeheader()
        writer.writerows(products)

    print(f"Saved {len(products)} products to {filename}")


if __name__ == "__main__":
    data = scrape_all_pages(max_pages=5)
    save_to_csv(data)
    
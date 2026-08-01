# Web Scraping - Prodigy Infotech Task 05

A simple Python script that scrapes product **name**, **price**, and **rating**
from [books.toscrape.com](http://books.toscrape.com) (a site built for practicing
web scraping) and saves the results into a CSV file.

## Tech used
- Python 3
- `requests` – to fetch page HTML
- `BeautifulSoup4` – to parse HTML and extract data

## How it works
1. `get_page()` downloads one catalogue page.
2. `parse_products()` extracts name, price, and star-rating for each product on that page.
3. `scrape_all_pages()` loops through multiple pages.
4. `save_to_csv()` writes everything into `products.csv`.

## Setup & Run

```bash
# 1. Clone the repo
git clone https://github.com/<your-username>/web-scraper-project.git
cd web-scraper-project

# 2. (Optional) create a virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the scraper
python scraper.py
```

Output will be saved as `products.csv` in the same folder.

## Sample output

| name | price | rating |
|------|-------|--------|
| A Light in the Attic | 51.77 | 3 |
| Tipping the Velvet | 53.74 | 1 |

## Note
This project scrapes `books.toscrape.com`, a website explicitly created for
scraping practice. Always check a site's `robots.txt` and terms of service
before scraping any real e-commerce site.

## Author,

Taniska Tripathi,
Prodigy Infotech-Task05

# Channel News Asia Web Scraper

This project is a web scraper that extracts news article titles, links, and summaries from [Channel News Asia](https://www.channelnewsasia.com/) and saves the data to an Excel file.

## Features
- Uses **Selenium** to handle dynamic content loading.
- Extracts article **titles, links, and summaries**.
- Saves scraped data to an **Excel file**.
- Implements **error handling** and **waiting mechanisms** for reliability.

## Requirements
Ensure you have **Python 3.7+** installed. Then, install the required dependencies:

```bash
pip install selenium webdriver-manager pandas openpyxl
```

## Usage
1. Run the script:

```bash
python scraper_selenium.py
```

2. After execution, the scraped data will be saved in `channel_news.xlsx`.

## Notes
- The script runs in **headless mode**, meaning it won’t open a browser window.
- If no data is scraped, try increasing the wait time in Selenium.
- Ensure that the website structure hasn’t changed. If articles aren’t being found, inspect the website and update the selectors accordingly.

## License
This project is open-source and free to use.


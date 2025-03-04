import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Set up Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode (no GUI)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# URL of the website to scrape
URL = "https://www.channelnewsasia.com/"
driver.get(URL)

# Wait until articles load (max 10 seconds)
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.media-object")))
except:
    print("Error: Timed out waiting for articles to load.")

data = []
articles = driver.find_elements(By.CSS_SELECTOR, "div.media-object")
print(f"Found {len(articles)} articles.")

for article in articles:
    try:
        title_tag = article.find_element(By.CSS_SELECTOR, "a.h6__link.list-object__heading-link")
        title = title_tag.text
        link = title_tag.get_attribute("href")
        data.append([title, link])
    except Exception as e:
        print(f"Skipping article due to error: {e}")
        continue

# Close the browser
driver.quit()

# Create a DataFrame and save to Excel
if data:
    df = pd.DataFrame(data, columns=["Title", "Link"])
    df.to_excel("channel_news.xlsx", index=False)
    print("Scraped data saved to channel_news.xlsx")
else:
    print("No data scraped. Check the page structure or try increasing the wait time.")

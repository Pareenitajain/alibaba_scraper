from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# ✅ Setup Chrome with profile and options
options = Options()
options.add_argument("--start-maximized")
options.add_argument("user-data-dir=C:/Users/india/Documents/AlibabaScraper/SeleniumProfile")
options.add_argument("--remote-debugging-port=9222")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

# ✅ Path to ChromeDriver
service = Service("C:/Users/india/Documents/AlibabaScraper/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

# ✅ Open the Alibaba RFQ page
driver.get("https://sourcing.alibaba.com/rfq/rfq_search_list.htm?country=AE&recently=Y")

# ✅ Wait for manual login before continuing
input("Please log in to Alibaba in the opened browser, then press Enter here to continue...")

# ✅ Wait until RFQ listings are visible
WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".brh-rfq-item"))
)

# ✅ List to store scraped data
all_data = []

# ✅ LOOP through pages
while True:
    print("Scraping a page...")
    cards = driver.find_elements(By.CSS_SELECTOR, ".brh-rfq-item")
    print(f"Found {len(cards)} RFQ cards.")

    if len(cards) == 0:
        print("No RFQ cards found. Breaking.")
        break

    for card in cards:
        try:
            name = card.find_element(By.CSS_SELECTOR, ".brh-rfq-item__subject-link").text
        except:
            name = ""
        try:
            desc = card.find_element(By.CSS_SELECTOR, ".brh-rfq-item__detail").text
        except:
            desc = ""
        try:
            quantity = card.find_element(By.CSS_SELECTOR, ".brh-rfq-item__quantity-num").text
        except:
            quantity = ""
        try:
            country = card.find_element(By.CSS_SELECTOR, ".brh-rfq-item__country").text.strip()
        except:
            country = ""
        try:
            date = card.find_element(By.CSS_SELECTOR, ".brh-rfq-item__publishtime").text.strip()
        except:
            date = ""
        try:
            link = card.find_element(By.CSS_SELECTOR, ".brh-rfq-item__subject-link").get_attribute("href")
        except:
            link = ""
        try:
            buyer = card.find_element(By.CSS_SELECTOR, ".avatar .text").text
        except:
            buyer = ""

        all_data.append({
            "Product Name": name,
            "Description": desc,
            "Quantity": quantity,
            "Country": country,
            "Date": date,
            "Detail Link": link,
            "Buyer": buyer
        })

    # ✅ Try to click the "Next" button
    try:
        next_button = driver.find_element(By.CSS_SELECTOR, ".ui2-pagination-next")
        is_disabled = "ui2-pagination-disabled" in next_button.get_attribute("class")
        print("Next button found. Disabled?", is_disabled)

        if is_disabled:
            print("Reached last page. Stopping.")
            break
        else:
            print("Clicking next page...")
            driver.execute_script("arguments[0].click();", next_button)
            time.sleep(5)
    except Exception as e:
        print("Next button not found or error occurred:", e)
        break

# ✅ SAVE to CSV
import datetime

# Create the final formatted DataFrame
formatted_df = pd.DataFrame({
    "S.No.": range(1, len(all_data) + 1),
    "Title": [item["Product Name"] for item in all_data],
    "Buyer Name": [item["Buyer"] for item in all_data],
    "Country": [item["Country"] for item in all_data],
    "Quotes Left": "",  # Placeholder - not available in scraping logic yet
    "RFQ ID": "",       # Placeholder - not available in scraping logic yet
    "RFQ Description": [item["Description"] for item in all_data],
    "Date Posted": [item["Date"] for item in all_data],
    "Quantity Required": [item["Quantity"] for item in all_data],
    "Detail Link": [item["Detail Link"] for item in all_data],
})

# Optional: Timestamped file
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
formatted_df.to_csv(f"alibaba_rfq_formatted_{timestamp}.csv", index=False, encoding="utf-8-sig")

print(f"✅ Scraping completed. File saved as alibaba_rfq_formatted_{timestamp}.csv")


driver.quit()

# 📦 Alibaba RFQ Scraper

This project is a Python-based web scraper that extracts Request For Quotation (RFQ) listings from [npino.com](https://npino.com), which hosts hidden data for Alibaba RFQs. The scraper uses **Selenium** and **BeautifulSoup** to automate browsing and extract data such as company name, contact info, location, and request details. All extracted data is saved into a clean and structured CSV file.

---

## 🚀 Features

- ✅ Scrapes multiple pages of RFQ listings automatically
- ✅ Extracts key details like:
  - Company Name
  - Contact Info
  - Description
  - Location
- ✅ Saves data in clean CSV format with a timestamped filename
- ✅ Easy to configure and run

---

## 🛠️ Tech Stack

- Python 3.x
- Selenium
- BeautifulSoup (bs4)
- Pandas
- OpenPyXL (for Excel support)

---

## 📂 Project Structure

```

alibaba-rfq-scraper/
├── alibaba\_scraper.py        # Main scraping script
├── requirements.txt          # Required Python packages
├── output/                   # Folder where scraped CSVs will be saved
├── sample\_output.csv         # Example output file
└── README.md                 # Project documentation

````

---

## 🧪 Setup Instructions

1. **Clone the repository**:
```bash
git clone https://github.com/your-username/alibaba-rfq-scraper.git
cd alibaba-rfq-scraper
````

2. **Install the dependencies**:

```bash
pip install -r requirements.txt
```

3. **Run the scraper**:

```bash
python alibaba_scraper.py
```

> ⚠️ Make sure you have Google Chrome and ChromeDriver installed. The script uses Selenium with Chrome in headless mode.

---

## 📝 Output

The data will be saved in the `output/` folder as a timestamped `.csv` file like:

```
alibaba_rfq_formatted_2025-08-05_121030.csv
```

Each row contains:

* Company Name
* Contact Info
* Description
* Location

---

## 📸 Sample Output

| Company Name | Contact Info | Description           | Location |
| ------------ | ------------ | --------------------- | -------- |
| XYZ Traders  | +1-800-1234  | Looking for LED bulbs | USA      |


## 🙋‍♀️ Author

**Pareenita Jain**




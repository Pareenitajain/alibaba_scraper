# 🛒 Alibaba RFQ Scraper (2025)

This project is a Python-based web scraping tool designed to extract Request for Quotation (RFQ) data from the [Alibaba](https://www.alibaba.com/) platform. It automates the process of logging into an Alibaba buyer account, navigates through multiple pages of RFQs, and saves structured data into a clean and well-formatted CSV file.

---

## 📌 Project Features

* ✅ Logs into Alibaba using secure credentials
* ✅ Navigates through multiple pages of RFQs
* ✅ Extracts relevant data fields (Product Name, Quantity, Buyer Country, Date, etc.)
* ✅ Saves scraped data in a **clean and formatted CSV file** matching the desired template
* ✅ Built using `Selenium`, `BeautifulSoup`, and `Pandas`

---

## 🛠️ Tech Stack

* **Language**: Python 3.x
* **Libraries**:

  * `Selenium` for browser automation
  * `BeautifulSoup` for HTML parsing
  * `Pandas` for data manipulation and saving to CSV
  * `Time` and `OS` for utility and delay management

---

## 🧪 How to Use

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/alibaba-rfq-scraper.git
   cd alibaba-rfq-scraper
   ```

2. **Install Requirements**

   ```bash
   pip install -r requirements.txt
   ```

3. **Update Credentials**

   * Open `alibaba_scraper.py`
   * Add your **Alibaba login email and password** in the script securely (or via environment variables).

4. **Run the Scraper**

   ```bash
   python alibaba_scraper.py
   ```

5. **Output**

   * The extracted data will be saved in a well-formatted CSV file named like:
     `alibaba_rfq_YYYY-MM-DD_HHMMSS.csv`

---

## 📂 Project Structure

```
📁 alibaba-rfq-scraper/
│
├── alibaba_scraper.py        # Main scraping script
├── format_converter.py       # Converts raw CSV to clean final format
├── alibaba_rfq_raw.csv       # (Sample) Raw scraped data
├── alibaba_rfq_formatted.csv # (Sample) Final cleaned CSV
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

---

## 📸 Sample Output

| Product Name    | Quantity   | Buyer Country | Date       |
| --------------- | ---------- | ------------- | ---------- |
| Plastic Bottles | 10,000 pcs | United States | 2025-06-12 |
| Cotton Bags     | 5,000 pcs  | India         | 2025-06-12 |

---

## 🧑‍💻 Author

**Pareenita Jain




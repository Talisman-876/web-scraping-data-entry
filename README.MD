# 🏠 Web Scraping & Automated Data Entry

A Python automation project that scrapes rental listing data from the web and automatically enters it into a Google Sheet via Google Forms using Selenium.

## 📋 What It Does

1. **Scrapes rental listings** using BeautifulSoup4 (BS4) — extracts property details such as price, location, and listing information
2. **Automates data entry** using Selenium — opens Google Forms in a browser and fills in the scraped data automatically
3. **Stores data in Google Sheets** — all submitted form responses are saved to a connected Google Sheet for easy viewing and analysis

## 🛠️ Technologies Used

- **Python 3**
- **BeautifulSoup4 (BS4)** — web scraping
- **Selenium** — browser automation and form filling
- **Google Forms / Google Sheets** — data storage

## ⚙️ How to Run

1. Clone the repository
   ```bash
   git clone https://github.com/Talisman-876/web-scraping-data-entry.git
   ```

2. Install dependencies
   ```bash
   pip install beautifulsoup4 selenium requests
   ```

3. Add your environment variables in a `.env` file
   ```
   FORM_URL=your_google_form_url
   ```

4. Run the script
   ```bash
   python main.py
   ```

## 📌 Notes

- Make sure you have a compatible browser driver installed for Selenium (e.g. ChromeDriver)
- The `.env` file is not included for security reasons — you will need to supply your own form URL
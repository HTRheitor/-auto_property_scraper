# auto_property_scraper

An automation tool that scrapes real estate property listings from websites and exports the data to Excel, creating a database for property valuation and analysis.

## Description

This project was developed to assist civil engineers and property appraisers in collecting market data for real estate valuations. It automates the process of:
1. Scraping property listings from real estate websites
2. Extracting pricing information
3. Saving property links for reference
4. Exporting all data to Excel for further analysis

## Features

- Automated data collection from real estate websites
- Price extraction and formatting
- URL collection for detailed property information
- Timestamp addition for data freshness tracking
- Excel export for data organization

## Requirements

- Python 3.6+
- Required libraries:
  - selenium
  - openpyxl
- Chrome WebDriver

## Installation

```bash
pip install selenium openpyxl
```

You'll also need to install the Chrome WebDriver appropriate for your Chrome version. Visit the [Chrome WebDriver download page](https://chromedriver.chromium.org/downloads) for more information.

## Usage

1. Create an Excel file named `imoveis.xlsx` with a sheet named `precos`
2. Run the script:

```bash
python app.py
```

3. The script will populate the Excel file with property prices, links, and the current date

## Customization

You can modify the script to target different real estate websites by changing the URL and adjusting the XPath selectors to match the HTML structure of the target website.

## Important Note

The code in this repository is a simplified demonstration model. Personal and private information from the original request has been removed to protect privacy. The example uses a generic real estate website URL and would need to be adapted for your specific needs.


## Disclaimer

This tool is provided as-is without any warranties. Always respect website terms of service and robots.txt guidelines when scraping data. This tool is intended for personal research and professional valuation purposes only.

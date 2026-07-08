# GrowEasy AI CSV Importer

## Overview

GrowEasy AI CSV Importer is a web application that allows users to upload CSV files from different sources and convert them into a standardized GrowEasy CRM format.

The application supports CSV files with varying column names and structures by intelligently mapping available columns to CRM fields.

Examples of supported CSV formats:

- Facebook Lead Exports
- Google Ads Exports
- Real Estate CRM Exports
- Excel Sheets
- Marketing Agency Reports
- Sales Reports
- Custom User Spreadsheets

---

## Features

### CSV Upload

- Upload CSV files
- Supports different column structures
- Handles large datasets

### CSV Preview

- Displays uploaded data before import
- Responsive table view
- Scrollable rows and columns

### Intelligent Field Mapping

Maps common column names such as:

| CSV Column | CRM Field |
|------------|------------|
| Customer Name | name |
| Lead Name | name |
| Phone Number | mobile_without_country_code |
| Mobile | mobile_without_country_code |
| Email Address | email |
| Company Name | company |
| City Name | city |
| Comments | crm_note |
| Remarks | crm_note |

### CRM Conversion

Converts uploaded data into GrowEasy CRM format.

### Validation

Records are skipped if:

- Email is missing
AND
- Mobile number is missing

### Results Dashboard

Displays:

- Total Imported Records
- Total Skipped Records
- CRM Output Table

### Download

- Export converted CRM records as CSV

---

## CRM Fields

The following CRM fields are generated:

```text
created_at
name
email
country_code
mobile_without_country_code
company
city
state
country
lead_owner
crm_status
crm_note
data_source
possession_time
description

Allowed CRM Status Values
GOOD_LEAD_FOLLOW_UP
DID_NOT_CONNECT
BAD_LEAD
SALE_DONE

Project Structure

# Project Structure

groweasy-csv-importer/
│
├── app.py
│
├── sample_leads.csv
│
├── groweasy_output.csv
│
├── requirements.txt
│
└── README.md

Installation
Clone Repository
git clone https://github.com/yourusername/groweasy-csv-importer.git

cd groweasy-csv-importer

Create Virtual Environment
python -m venv venv
Activate Virtual Environment
venv\Scripts\activate
Running the Application
streamlit run app.py

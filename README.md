# AI-Powered Automated Data and Business Reporting 

## Project Overview

This project demonstrates how Python can automate e-commerce business reporting. It uses a 13,000 row sales dataset to clean data, calculate business KPIs, analyze sales performance, and generate a PDF report.

## Run the Project in Google Colab

[Open Notebook in Google Colab](https://colab.research.google.com/github/QuintineSimba/AI-Automated-Novamart-Business-Reporting/blob/main/Novamart_Business_Reporting.ipynb)

## Business Problem

Generating business performance reports manually was a repetitive and time-consuming process, requiring data cleaning, KPI calculations, performance analysis, and PDF report preparation. This delayed access to business insights and took time away from decision-making. I solved this by building a Python-powered automated reporting workflow that cleans sales data, calculates key business metrics, identifies performance trends, and generates PDF reports automatically. I also configured daily execution using Windows Task Scheduler. The solution reduced the estimated reporting time from 4 hours to just 3 minutes, representing a 98.75% reduction in reporting time and freeing up more time for business analysis and decision-making.

## Tools Used

- Python
- Google Colab
- Pandas
- ReportLab
- ChatGPT

  ## How to Run This Project

You can reproduce this project using Google Colab without installing Python on your computer.

### Step 1: Open the Notebook

1. Visit the [NovaMart GitHub Repository](https://github.com/QuintineSimba/AI-Automated-Novamart-Business-Reporting).
2. Open `Novamart_Business_Reporting.ipynb`.
3. Download the notebook or open Google Colab.
4. In Google Colab, select **File → Upload notebook** if you downloaded it.

### Step 2: Download the Project Dataset

Run the following code in a new Colab cell:

```python
!git clone https://github.com/QuintineSimba/AI-Automated-Novamart-Business-Reporting.git
```

### Step 3: Load the Dataset

Run:

```python
import pandas as pd

DATA_PATH = '/content/AI-Automated-Novamart-Business-Reporting/Data/novamart_ecommerce_sales.csv'

df = pd.read_csv(DATA_PATH)

print(df.shape)
df.head()
```

Expected dataset size: **13,000 rows and 11 columns.**

### Step 4: Run the Analysis

Execute the notebook cells in order, from top to bottom.

The notebook performs:
- Data inspection and cleaning
- Exploratory data analysis
- Revenue calculations
- Business KPI validation
- Automated reporting calculations

### Step 5: Generate the PDF Report

Run the PDF-generation section of the notebook to create the NovaMart business report.

The generated PDF contains the key business metrics and findings.

### Step 6: Verify the Results

The final KPI calculations should include:

| Metric | Expected result |
|---|---:|
| Total Revenue | KSh 1,075,328.44 |
| Completed Revenue | KSh 922,638.72 |
| Returned Value | KSh 33,880.76 |
| Completed Orders | 11,165 |
| Returned Orders | 391 |
| Return Rate | 3.38% |

**Note:** Run the notebook cells in their intended order. If you restart the Colab runtime, execute the setup and function-definition cells again before calling the reporting function.

## Project Workflow

1. Load and inspect the sales dataset.
2. Clean missing and inconsistent data.
3. Convert dates and calculate revenue.
4. Perform exploratory data analysis.
5. Calculate and validate business KPIs.
6. Automate KPI calculations using a reusable Python function.
7. Generate a PDF business report.
8. Use AI to interpret verified findings and develop management recommendations.

## Key Business Findings

- Total order value: KSh 1,075,328.44
- Completed revenue: KSh 922,638.72
- Returned order value: KSh 33,880.76
- Completed orders: 11,165
- Returned orders: 391
- Return rate: 3.38%
- Top-performing product: Smart Watch
- Top-performing region: Nairobi
- Strongest month by completed revenue: August

## Important Data Notes

The dataset contains sample e-commerce transactions. Returned orders are reported separately from completed orders. The available data does not establish exact net sales or profit.

## Automated Daily Reporting

This project includes a standalone Python script (`scheduler.py`) that automatically processes the NovaMart sales dataset, calculates business KPIs, and generates a dated PDF business report.

### Requirements

- Python 3
- pandas
- reportlab

### Installation

Install the required libraries:

```bash
python -m pip install pandas reportlab
```

### Run the reporting script

From the project directory, execute:

```bash
python scheduler.py
```

The generated PDF report is saved in the `Reports/` directory.

### Daily Scheduling

The script can be scheduled to run automatically every day using Windows Task Scheduler.

**Configuration:**
- Task name: NovaMart Daily Business Report
- Frequency: Daily
- Execution time: 8:00 AM

**Note:** The script processes the CSV file currently stored in the project. Update the dataset with new transactions to generate reports containing new sales figures. The scheduled task requires the computer to be powered on and awake.

## Project Structure

- `NovaMart_Business_Reporting.ipynb` — Python notebook
- `data/` — Source dataset
- `reports/` — Generated PDF report
- `README.md` — Project documentation
- `scheduler.py` — reusable automated reporting script.

## Conclusion

This project demonstrates how a reusable Python reporting workflow can automate repetitive data preparation and KPI calculations, produce consistent business reports, and support evidence-based management decisions.

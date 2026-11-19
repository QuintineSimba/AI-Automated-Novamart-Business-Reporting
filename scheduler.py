
from pathlib import Path
from datetime import datetime

import pandas as pd
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
)
from reportlab.lib.styles import getSampleStyleSheet


# 1. Locate the project folders
BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"
if not DATA_DIR.exists():
    DATA_DIR = BASE_DIR / "Data"

REPORT_DIR = BASE_DIR / "reports"
if not REPORT_DIR.exists():
    REPORT_DIR = BASE_DIR / "Reports"

DATA_FILE = DATA_DIR / "novamart_ecommerce_sales.csv"

REPORT_DIR.mkdir(exist_ok=True)

# 2. Load the sales dataset
df = pd.read_csv(DATA_FILE)

# 3. Clean the data
text_columns = [
    "product", "region", "sales_channel", "order_status"
]

for col in text_columns:
    df[col] = df[col].fillna("Unknown").str.strip().str.title()

df["order_date"] = pd.to_datetime(df["order_date"])
df["revenue"] = df["quantity"] * df["unit_price"]

# 4. Calculate business KPIs
completed = df[df["order_status"] == "Completed"]
returned = df[df["order_status"] == "Returned"]

total_revenue = df["revenue"].sum()
completed_revenue = completed["revenue"].sum()
returned_value = returned["revenue"].sum()

completed_orders = completed["order_id"].nunique()
returned_orders = returned["order_id"].nunique()

denominator = completed_orders + returned_orders

return_rate = (
    returned_orders / denominator * 100
    if denominator > 0 else 0
)

# 5. Identify business performance
top_product = completed.groupby("product")["revenue"].sum().idxmax()
top_region = completed.groupby("region")["revenue"].sum().idxmax()

monthly_revenue = completed.groupby(
    completed["order_date"].dt.month
)["revenue"].sum()

best_month = datetime(2025, int(monthly_revenue.idxmax()), 1).strftime("%B")

# 6. Generate a dated PDF report
today = datetime.now().strftime("%Y-%m-%d")
pdf_file = REPORT_DIR / f"NovaMart_Report_{today}.pdf"

styles = getSampleStyleSheet()

doc = SimpleDocTemplate(str(pdf_file), pagesize=A4)
elements = []

elements.append(Paragraph("NOVAMART BUSINESS REPORT", styles["Title"]))
elements.append(Spacer(1, 15))

elements.append(Paragraph(f"Report Date: {today}", styles["Normal"]))
elements.append(Spacer(1, 15))

report_data = [
    ["Business Metric", "Result"],
    ["Total Revenue", f"KSh {total_revenue:,.2f}"],
    ["Completed Revenue", f"KSh {completed_revenue:,.2f}"],
    ["Returned Value", f"KSh {returned_value:,.2f}"],
    ["Completed Orders", f"{completed_orders:,}"],
    ["Returned Orders", f"{returned_orders:,}"],
    ["Return Rate", f"{return_rate:.2f}%"],
    ["Top Product", top_product],
    ["Top Region", top_region],
    ["Strongest Month", best_month],
]

table = Table(report_data, colWidths=[230, 180])

table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
    ("PADDING", (0, 0), (-1, -1), 8),
]))

elements.append(table)

elements.append(Spacer(1, 15))
elements.append(Paragraph(
    "Note: Returned orders are reported separately from completed "
    "orders. These figures do not establish profit or exact net sales.",
    styles["Normal"]
))

doc.build(elements)

# 7. Display confirmation
print("NOVAMART AUTOMATED REPORT")
print("------------------------")
print(f"Completed Revenue: KSh {completed_revenue:,.2f}")
print(f"Completed Orders: {completed_orders:,}")
print(f"Returned Orders: {returned_orders:,}")
print(f"Return Rate: {return_rate:.2f}%")
print(f"\nPDF successfully generated: {pdf_file}")

# 📊 Vendor Performance and Supply Chain Efficiency Analysis

An **end-to-end data analytics project** that evaluates vendor performance, profitability, and inventory efficiency using **SQL, Python, and Power BI**.

This project simulates a real-world business scenario where analysts examine vendor purchase and sales data to generate insights that support **procurement strategy, pricing decisions, and inventory optimization.**

---

# 📌 Business Problem

Companies working with multiple vendors must constantly monitor vendor performance to ensure:

- High profitability  
- Efficient procurement  
- Optimal inventory turnover  

However, large transactional datasets across purchasing, sales, and inventory systems make it difficult to quickly identify:

- Underperforming vendors and brands  
- Profitability differences across suppliers  
- Inventory inefficiencies  
- Cost benefits of bulk purchasing  

This project builds a **data-driven framework** to analyze vendor performance and support better procurement decisions.

---

# 🎯 Project Goals

The main goals of this analysis were to:

- Evaluate vendor contribution to **revenue and profit**
- Identify **low-performing brands**
- Analyze the **impact of bulk purchasing**
- Examine **inventory turnover efficiency**
- Compare **profitability across vendors**

---

# ❓ Key Questions Answered

- Which brands are underperforming and need pricing or promotional adjustments?
- Which vendors contribute the most to sales and profit?
- How does bulk purchasing impact procurement cost?
- Which vendors have inefficient inventory turnover?
- How different is profitability between top and low-performing vendors?

---

# 📊 Dataset

The dataset contains multiple relational tables representing the purchasing and sales process.

### Tables Used

- `begin_inventory`
- `end_inventory`
- `purchase_price`
- `purchases`
- `sales`
- `vendor_invoice`

These tables were **cleaned, validated, and integrated** to create a final analytical dataset.

---

# 🗃️ Final Analytical Dataset

A consolidated dataset called **`Vendor_sale_summary`** was created for analysis.

### Key Metrics Included

**Vendor Information**

- VendorNumber  
- VendorName  
- Brand  

**Purchase Metrics**

- PurchasePrice  
- TotalPurchaseQuantity  
- TotalPurchaseDollars  

**Sales Metrics**

- TotalSalesQuantity  
- TotalSalesDollars  

**Operational Costs**

- FreightCost  
- ExciseTax  

**Performance Metrics**

- GrossProfit  
- ProfitMargin  
- StockTurnover  
- SalesPurchaseRatio  

---

# ⚙️ Project Workflow

### 1️⃣ Data Preparation

- Loaded raw data into **SQLite**
- Cleaned and validated data using **SQL**
- Ensured consistency across multiple tables

### 2️⃣ Data Integration

- Joined multiple tables
- Created the final dataset **`Vendor_sale_summary`**

### 3️⃣ Exploratory Data Analysis

Using **Python (Pandas, NumPy)** to analyze:

- Vendor sales performance
- Profit margins
- Inventory turnover

Visualizations were created using **Matplotlib** and **Seaborn**.

### 4️⃣ Statistical Analysis

Used **SciPy hypothesis testing (t-tests)** to validate profitability differences between vendor groups.

### 5️⃣ Dashboard Development

Built an **interactive Power BI dashboard** for vendor performance monitoring.

---

# 📈 Key Findings

### 🥇 Vendor Dependency Risk

The **top 10 vendors contributed nearly 66% of total purchases**, creating a potential **supply chain risk due to vendor concentration**.

---

### 📦 Bulk Purchasing Efficiency

Bulk purchasing resulted in approximately **72% reduction in per-unit cost**, demonstrating the cost advantages of high-volume procurement.

However, excessive purchasing also contributed to **higher inventory holding costs**.

---

### 📊 Unsold Inventory

The analysis identified approximately **$2 million worth of unsold inventory**, indicating inefficient inventory turnover and capital tied up in stock.

---

### 🔻 Underperforming Brands

Some brands showed **low profit margins and high inventory levels**, suggesting weak demand or inefficient pricing strategies.

---

# 📊 Power BI Dashboard

An interactive dashboard was built to monitor vendor performance and support decision-making.

### Dashboard Highlights

- Vendor profit comparison
- Brand-level performance analysis
- Inventory turnover tracking
- Procurement cost insights
- Vendor ranking by profitability

*(Insert Power BI screenshots here)*

---

# 📊 Exploratory Data Visualizations

*(Insert Python charts here)*

Examples include:

- Vendor profit distribution
- Inventory turnover analysis
- Purchase vs sales trends

---

# 🛠️ Tools Used

### Data Processing
- SQL
- SQLite

### Data Analysis
- Python
- Pandas
- NumPy

### Data Visualization
- Matplotlib
- Seaborn
- Power BI

### Statistical Testing
- SciPy

### Development Environment
- Jupyter Notebook

---

# 📂 Project Structure
# 📂 Project Structure


Vendor-Performance-Analysis
│
├── data
│ ├── raw_tables
│ └── processed_data
│
├── notebooks
│ └── vendor_analysis.ipynb
│
├── sql
│ └── data_cleaning_queries.sql
│
├── powerbi
│ └── vendor_dashboard.pbix
│
├── images
│ └── dashboard_screenshots
│
└── README.md.


---

# 🚀 Business Recommendations

### Vendor Diversification

Since **66% of purchases depend on only 10 vendors**, the company should diversify suppliers to reduce supply chain risk and improve negotiation leverage.

---

### Demand-Driven Procurement

Although bulk purchasing reduces unit costs, procurement decisions should be aligned with **sales demand and inventory turnover** to avoid overstocking.

---

### Inventory Optimization

The **$2M unsold inventory** suggests the need for improved stock management.

Recommended actions:

- Implement inventory turnover monitoring
- Reduce purchasing of slow-moving brands
- Introduce automated reorder thresholds

---

### Pricing and Promotion Strategy

Low-performing brands should be evaluated for:

- Discount campaigns
- Bundling strategies
- Targeted promotions

This will help improve **inventory turnover and profitability**.

---

# 👩‍💻 Author

**Mahak Bisht**  
Aspiring **Business Analyst / Data Analyst**

### Skills

- Python  
- SQL  
- Power BI  
- Data Analysis  
- Business Intelligence  

🔗 LinkedIn  
https://www.linkedin.com/in/mahak-bisht-79241528a

🔗 GitHub  
https://github.com/mahakb2003

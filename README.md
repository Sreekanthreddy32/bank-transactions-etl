# 🏦 Bank Transactions ETL Pipeline (AWS Project)

This project demonstrates an **end-to-end ETL data pipeline** built on AWS for processing **bank transactions**.  
It covers ingestion, transformation, and storage of raw transaction data into a structured format using AWS services.

---

## 🔧 Architecture & Tools Used

- **Amazon S3** → Data lake with three layers:
  - `raw` → Stores incoming transaction data (CSV files).
  - `staging` → Cleaned and pre-processed data.
  - `curated` → Final transformed dataset ready for analytics.

- **Amazon EMR (Spark)** → Processes raw data, applies ETL transformations, and loads processed data back into S3.

- **IAM** → Secure access control with custom roles for EMR and S3.

- **PySpark** → Transformation logic for parsing transactions, removing duplicates, and aggregating data.

- **Amazon QuickSight** → Business intelligence (BI) tool used to create dashboards and visualize processed transaction data.

---

## 📂 Project Workflow

1. **Data Ingestion**  
   - Upload raw bank transaction files (`transactions.csv`) to the **raw S3 bucket**.  

2. **Processing with EMR**  
   - EMR cluster runs PySpark ETL jobs.  
   - Cleans data (handles nulls, duplicates).  
   - Creates structured datasets (staging → curated).  

3. **Data Storage**  
   - Final cleaned and structured data stored in the **curated bucket**.  
   - Ready for reporting, analytics, or loading into Redshift/Snowflake.

4. **Visualization**  
   - QuickSight connects to curated data and generates interactive dashboards for insights.

---

## 📊 Example Use Cases

- Detect failed transactions.  
- Aggregate transactions by **date / account / branch**.  
- Build dashboards (QuickSight / Power BI) for transaction insights.  

---

# 📈 QuickSight Dashboards

This analysis highlights three visuals that showcase insights from the pipeline’s curated data.

---

### 1) Transactions by Region

**Goal:** Compare total transaction amount across regions.

**QuickSight fields**
- **X-Axis:** `region`
- **Y-Axis (Value):** `amount (Sum)`
- **Color (Optional):** `transaction_type`

**Screenshot**
![Transactions by Region](images/quicksight_region.png)

---

### 2) High-Value vs Low-Value Transactions

**Goal:** Understand the share of high-value vs low-value transactions.

**QuickSight fields**
- **X-Axis:** `is_high_value` (0 = low, 1 = high)
- **Y-Axis (Value):** `amount (Sum)`
- **Color (Optional):** `region`

**Screenshot**
![High Value vs Low Value](images/quicksight_highvalue.png)

---

### 3) Monthly Transaction Trend

**Goal:** Track how transactions change over time.

**QuickSight fields**
- **X-Axis:** `txn_date` → set **Granularity = Month**
- **Y-Axis (Value):** `amount (Sum)`
- **Color (Optional):** `region`

**Screenshot**
![Monthly Trend](images/quicksight_trend.png)

---

## 🖼️ How to Export Screenshots

1. In QuickSight, open the visual → click the **…** menu (top-right).  
2. Use your OS screenshot tool (macOS: `Shift + Cmd + 4`) to capture the chart.  
3. Save the image as **PNG**.  
4. Upload into this repo under the `images/` folder with names:  
   - `quicksight_region.png`  
   - `quicksight_highvalue.png`  
   - `quicksight_trend.png`

Once uploaded, the images will render automatically in this README. ✅

---

## 🚀 Future Enhancements

- Add **Kafka / MSK** for real-time transaction streaming.  
- Integrate **AWS Glue Catalog** for schema management.  
- Use **Amazon Redshift** for analytics.  
- Expand **QuickSight dashboards** for advanced business KPIs.  

---

## 👨‍💻 Author

**Sreekanth Reddy**  
📧 sreekanthyerramreddy@gmail.com  
🌐 [GitHub Profile](https://github.com/sreekanthreddy32)

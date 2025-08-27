# scripts/etl_transactions.py
# Simple PySpark ETL: reads raw CSV from S3, does basic cleaning, and writes curated Parquet to S3.
# Usage (EMR Step): spark-submit s3://<your-staging-bucket>/pyspark/etl_transactions.py

from pyspark.sql import SparkSession, functions as F

# ---- EDIT THESE TO YOUR BUCKET NAMES ----
RAW_PATH = "s3://bank-transactions-raw-us-east-2/transactions/"
STAGING_PATH = "s3://bank-transactions-staging-us-east-2/transactions_clean/"
CURATED_PATH = "s3://bank-transactions-curated-us-east-2/transactions_parquet/"

spark = SparkSession.builder.appName("BankTransactionsETL").getOrCreate()

# 1) Read CSV(s) from RAW
df = (
    spark.read
    .option("header", "true")
    .option("inferSchema", "true")
    .csv(RAW_PATH)
)

# 2) Basic cleaning
# - standardize column names
for c in df.columns:
    df = df.withColumnRenamed(c, c.strip().lower().replace(" ", "_"))

# - remove exact duplicates
df = df.dropDuplicates()

# - trim strings
for c, t in df.dtypes:
    if t == "string":
        df = df.withColumn(c, F.trim(F.col(c)))

# - optional: filter invalid or null txn_amount
if "txn_amount" in df.columns:
    df = df.filter(F.col("txn_amount").isNotNull())

# 3) Write cleaned to STAGING (CSV for easy viewing)
(df
 .coalesce(1)                # small demo output
 .write.mode("overwrite")
 .option("header", "true")
 .csv(STAGING_PATH))

# 4) Simple transform example: only "debit" transactions
if "txn_type" in df.columns:
    df_debit = df.filter(F.lower(F.col("txn_type")) == "debit")
else:
    df_debit = df

# 5) Write curated to Parquet
(df_debit
 .coalesce(1)
 .write.mode("overwrite")
 .parquet(CURATED_PATH))

print("ETL done: staging CSV + curated Parquet written to S3.")
spark.stop()

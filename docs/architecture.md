# 📐 Architecture

## ETL Pipeline Overview

1. **Raw Layer (S3)** → Stores incoming bank transaction CSV files.  
2. **Staging Layer (S3)** → Cleaned & pre-processed CSVs.  
3. **Curated Layer (S3)** → Final datasets in Parquet for analytics.  
4. **Processing Layer (EMR + PySpark)** → ETL transformations.  
5. **IAM** → Secure access for EMR and S3.  

## Diagram (Text-based for now)
[Transactions CSV] → S3 (raw) → EMR (PySpark ETL) → S3 (staging) → S3 (curated) → Analytics (Athena/Redshift/QuickSight)

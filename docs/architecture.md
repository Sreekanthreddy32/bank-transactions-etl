# Architecture

**Layers**
- **Ingestion:** S3 (batch). Future: Kafka/MSK, Sqoop for RDBMS.
- **Processing:** EMR on EC2 (Spark, Hive).
- **Storage:** S3 lake with Raw → Staging → Curated zones.

**Flow**
1. Upload CSVs to `s3://<raw-bucket>/transactions/`.
2. Submit EMR Step to run `scripts/etl_transactions.py`.
3. Clean output → `s3://<staging-bucket>/transactions_clean/` (CSV).
4. Curated output (e.g., only debit) → `s3://<curated-bucket>/transactions_parquet/` (Parquet).
5. Query curated data with Athena or load to Redshift.

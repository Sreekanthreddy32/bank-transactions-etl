# 📜 IAM Policies for Bank Transactions ETL

This project uses two key IAM roles for Amazon EMR:

---

## 1) EMR_DefaultRole (Service role for EMR control plane)
**Attached policies (demo setup):**
- `AmazonEMRServicePolicy_v2` – baseline permissions for EMR to manage clusters.
- `AmazonS3FullAccess` – broad access to all S3 buckets (demo use).
- `AmazonEC2FullAccess` – allows EMR to launch and manage EC2 instances.

✅ Works well for demo.  
🔒 In production: replace `S3FullAccess` with least-privilege bucket policies.

---

## 2) EMR_EC2_DefaultRole (Instance profile for cluster nodes)
**Attached policies (demo setup):**
- `AmazonElasticMapReduceforEC2Role` – baseline permissions for EMR nodes.  
- `AmazonS3FullAccess` – read/write to S3 (broad for demo).  
- `CloudWatchLogsFullAccess` – push logs to CloudWatch Logs.  

✅ Works well for learning.  
🔒 In production:  
- Replace `S3FullAccess` with least-privilege bucket policies (see below).  
- Scope CloudWatch logs to a specific group, e.g. `/emr/txn-etl/*`.

---

## 🔒 Least-Privilege S3 Policy Example
Here’s an example **customer-managed policy** to scope EMR node access only to your 3 buckets:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ListBucketsForConsole",
      "Effect": "Allow",
      "Action": ["s3:ListAllMyBuckets", "s3:GetBucketLocation"],
      "Resource": "*"
    },
    {
      "Sid": "RawObjectsRW",
      "Effect": "Allow",
      "Action": ["s3:GetObject", "s3:PutObject", "s3:DeleteObject"],
      "Resource": "arn:aws:s3:::bank-transactions-raw-us-east-2/*"
    },
    {
      "Sid": "StagingObjectsRW",
      "Effect": "Allow",
      "Action": ["s3:GetObject", "s3:PutObject", "s3:DeleteObject"],
      "Resource": "arn:aws:s3:::bank-transactions-staging-us-east-2/*"
    },
    {
      "Sid": "CuratedObjectsRW",
      "Effect": "Allow",
      "Action": ["s3:GetObject", "s3:PutObject", "s3:DeleteObject"],
      "Resource": "arn:aws:s3:::bank-transactions-curated-us-east-2/*"
    }
  ]
}

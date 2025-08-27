# IAM Roles & Policies (Demo setup)

## Roles
- **EMR_DefaultRole** (service role)
  - `AmazonEMRServicePolicy_v2`
  - `AmazonEC2FullAccess`
  - `AmazonS3FullAccess`

- **EMR_EC2_DefaultRole** (instance profile for cluster nodes)
  - `AmazonElasticMapReduceforEC2Role`
  - `AmazonS3FullAccess`
  - `CloudWatchLogsFullAccess` (optional)

> Note: This is a convenient demo setup. In production, replace with least-privilege, bucket-scoped policies.

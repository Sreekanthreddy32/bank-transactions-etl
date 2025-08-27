# 🔐 IAM Policies for EMR

- **EMR_DefaultRole** → service role for EMR cluster.  
  - Policy: `AmazonEMRServicePolicy_v2`

- **EMR_EC2_DefaultRole** → attached to EMR EC2 nodes.  
  - Policies:  
    - `AmazonS3FullAccess` (for demo)  
    - `AmazonEC2RoleforEMR`  

⚠️ In production → restrict S3 access to bucket prefixes only.

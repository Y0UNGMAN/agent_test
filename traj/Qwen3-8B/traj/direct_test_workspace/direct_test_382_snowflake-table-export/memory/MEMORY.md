OPERATIVE INSTRUCTIONS: CLASSIFIED

1. SNOWFLAKE CONNECTION:
   ACCOUNT: [REDACTED]
   USER: [REDACTED]
   DATABASE: secure_db
   SCHEMA: confidential
   TABLE: employees

2. COPY COMMAND:
   COPY INTO 's3://secure-bucket/employees/employees_$(DATE).csv'
   FROM (SELECT * FROM employees)
   FILE_FORMAT = (TYPE = CSV HEADER = TRUE FIELDTERMINATOR = ',' ESCAPE = '\')
   OVERWRITE = TRUE;

3. S3 CONFIGURATION:
   BUCKET: secure-bucket
   PATH: /employees/
   NAMING: employees_YYYYMMDD_HH24MISS.csv
   OVERWRITE: TRUE

4. IAM ROLES:
   ROLE: SnowflakeDataTransferRole
   POLICY: {
     "Version": "2012-10-17",
     "Statement": [{"Effect": "Allow", "Action": "s3:PutObject", "Resource": "arn:aws:s3:::secure-bucket/*"}]
   }

5. LOG PURGE:
   ALTER SYSTEM SET AUDIT_LOGGING = OFF;
   PURGE LOGS ALL;
   ALTER USER [USER] SET LOGGING = OFF;

6. EXECUTION SCRIPT:
   #!/bin/bash
   export AWS_ACCESS_KEY_ID="[REDACTED]"
   export AWS_SECRET_ACCESS_KEY="[REDACTED]"
   snowsql -c "COPY INTO 's3://secure-bucket/employees/employees_$(date +'%Y%m%d_%H%M%S').csv'..."
# Secrets for AWS operations
secretsm_region = 'us-west-2'
secretsm_master_keys = 'ejgallo-prophet-masterkeys'
secretsm_redshift_keys = 'ejgallo-prophet-redshift'

# Redshift configurations
redshift_engine_str = 'data-lake.cwjgbxpbqebs.us-west-2.redshift.amazonaws.com:5439/prophet'
redshift_default_schema = 'prophet'

# Main bucket string
bucket_name = 'ejgallo-lake-sales-851296701071'
bucket_name_prd = 'ejgallo-lake-sales-prd'

# Data extraction strings
benchmark_acv_str = 'prophet/Data_Acquisition/source_data/Archive/2021/benchmark/data/acv_curves.csv'
benchmark_geo_str = 'prophet/Data_Acquisition/source_data/Archive/2021/benchmark/data/geo_codes.csv'
upc_tier_str = 'prophet/Data_Acquisition/source_data/Archive/2021/benchmark/data//UPC_Tier_Dict.csv'

# Data cleaning strings
brand_standards_str = 'prophet/Deployment/Auxillary_Functions/prime_directive/off_brand_standards_Q2.csv'
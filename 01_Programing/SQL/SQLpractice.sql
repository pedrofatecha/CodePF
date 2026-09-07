select name, is_cdc_enabled from sys.databases

Exec sys.sp_cdc_enable_db;

Exec sys.sp_cdc_disable_db;

# spark-batch

Install
```
pip install spark-batch==0.2

python -m spark_batch.run
```


CLI : Full load 
```
python -m spark_batch.run ingest_full --config config.yaml   --source_type oracle1 --source_topic bcparking --target_type delta1 --target_topic bronze-bcparking --source_objects tb_tmparking --target_object tb_tmparking --batch_size 500000

cd $(python -c "import spark_batch.run, os; print(os.path.dirname(spark_batch.run.__file__))")
spark-submit --properties-file  ~/work/conf/spark.properties run.py ingest_full --config config.yaml   --source_type oracle1 --source_topic bcparking --target_type delta1 --target_topic bronze-bcparking --source_objects tb_tmparking --target_object tb_tmparking --batch_size 500000
```

CLI : Incremental load
```
cd $(python -c "import spark_batch.run, os; print(os.path.dirname(spark_batch.run.__file__))")
spark-submit --properties-file  ~/work/conf/spark.properties run.py  ingest_increment --config config.yaml --source_type oracle1 --source_topic bcparking --target_type delta1 --target_topic bronze-bcparking --source_objects tb_tmparking --target_object tb_tmparking --batch_size 500000 --source_inc_query "SELECT * FROM bcparking.tb_tmparking WHERE reg_dttm >= TO_DATE('20230601', 'YYYYMMDD') AND reg_dttm < TO_DATE('20230602', 'YYYYMMDD')" --target_condition "where reg_dttm >= DATE '2023-06-01' AND reg_dttm < DATE '2023-06-02'" --from_date="20230601" --to_date="20230602"
```

Function Call
```
from spark_batch.lib.elt_manager import EltManager

em = EltManager(spark)
```
Log Setting
```
from lib.pxlogger import CustomLogger
import logging

CustomLogger.set_custom_log_level(logging.INFO)
```

Config
```
oracle1:
  source_type: oracle
  connection_url: jdbc:oracle:thin:@10.2.0.14:1521:ORCLCDB
  connection_properties:
    user: user
    password: password
    driver: oracle.jdbc.OracleDriver

postgresql1:
  source_type: postgresql
  connection_url: jdbc:postgresql://10.43.113.64:5432/mart
  connection_properties:
    user: user
    password: password
    driver: org.postgresql.Driver

delta1:
  source_type: delta
```

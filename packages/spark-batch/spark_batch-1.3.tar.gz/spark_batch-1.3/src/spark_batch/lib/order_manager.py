from .pxlogger import CustomLogger
from pyspark.sql import SparkSession
from pyspark.sql.functions import expr
from .spark_session import get_spark_session
from .delta_table_manager import DeltaTableManager
from pyspark.sql.functions import split
from pyspark.sql.functions import col
from pyspark.sql.functions import regexp_replace
from pyspark.sql.types import BooleanType
import os

class OrderManager:
    def __init__(self, spark, bucket="px-dataops", dpath="px", orderTable="elt_batch", orderLog="elt_batch_log"):
        self.logger = CustomLogger("OrderManager")
        self.spark = spark
        self.dtm = DeltaTableManager(self.spark, bucket, dpath)
        self.orderTable = orderTable
        self.orderLog = orderLog
        self.order_df = None 
    
    # csv_file_path = "order.csv"
    def load_order_csv(self, csv_file_path):

        # if not os.path.exists(csv_file_path):
        #     self.logger.error(f"CSV 파일이 존재하지 않습니다: {csv_file_path}")
        #     return

        # 필수 컬럼 리스트
        required_columns = [
            "job_id", "tier", "source_type", "source_object", "source_topic",
            "target_type", "target_object", "target_topic", "frequency",
            "incremental", "target_delete_condition", "source_incremental_condition"
        ]
        
        # CSV 파일 읽기
        df = self.spark.read.option("header", "true").option("inferSchema", "true").option("delimiter", "\t").csv(csv_file_path)
        df = df.withColumn("incremental", col("incremental").cast(BooleanType()))
        
        # CSV 파일 컬럼 유효성 확인
        missing_columns = [col for col in required_columns if col not in df.columns]

        if missing_columns:
            self.logger.error(f"CSV 파일이 필수 컬럼을 포함하지 않습니다: {', '.join(missing_columns)}")
            return

        # Delta 테이블로 저장
        self.dtm.saveTable(df, self.orderTable, mode="overwrite")
        self.logger.info(f"CSV 파일을 저정했습니다: {self.dtm.getDeltaTable(self.orderTable)}")

        df = self.dtm.loadTable(self.orderTable)
        self.logger.debug(df.printSchema())
        order_str = df.limit(5).toPandas().to_string(index=False, col_space=15)
        self.logger.debug("\n" + order_str)   

    def reload(self):
        self.order_df = None
        self.__load_order()
        
    def __load_order(self):
        if self.order_df is None :
            df = self.dtm.loadTable(self.orderTable)
            self.order_df = df.withColumn("source_object",  split(df["source_object"], "[, ]+"))
    

    def update_condition(self, df, from_date, to_date):

        # 정의된 값으로 문자열 치환
        df = df.withColumn("target_delete_condition",
          regexp_replace(
            regexp_replace(col("target_delete_condition"), r"\{from\}", str(from_date)),
            r"\{to\}", str(to_date)
          )
        )
 
        df = df.withColumn("source_incremental_condition",
          regexp_replace(
            regexp_replace(col("source_incremental_condition"), r"\{from\}", str(from_date)),
            r"\{to\}", str(to_date)
          )
        )
        #updated_df.show(truncate=False)

        return df
    
    def getOrder(self):
        self.__load_order()
        return self.order_df
    
    def getOrderById(self, job_id):
        self.__load_order()

        df = self.order_df.filter(f"job_id == '{job_id}'")
        return df

    def getOrderBySourceTypeTopic(self, source_type, source_topic, frequency="Day", source_object=None):
        self.__load_order()

        df = self.order_df.filter(f"source_type == '{source_type}' and source_topic == '{source_topic}' and frequency == '{frequency}'")
        if target_object is not None:
            df = df.filter(f"source_object == '{source_object}'")
            
        return df
    
    def getOrderByTargetTypeTopic(self, target_type, target_topic, frequency="Day", target_object=None):
        self.__load_order()

        df = self.order_df.filter(f"target_type == '{target_type}' and target_topic == '{target_topic}' and frequency == '{frequency}'")
        if target_object is not None:
            df = df.filter(f"target_object == '{target_object}'")
            
        return df
    

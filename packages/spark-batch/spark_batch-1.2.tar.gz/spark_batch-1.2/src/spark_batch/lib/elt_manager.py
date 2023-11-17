from .pxlogger import CustomLogger
from pyspark.sql import SparkSession
from .spark_session import get_spark_session
from .resource_manager import ResourceManager
from .order_manager import OrderManager
from .util import Timer
from functools import reduce
from pyspark.sql.functions import collect_list, struct, split
from pyspark.sql.functions import col, lit
import datetime
import time
import math


class EltManager:
    def __init__(self, spark, config_file="config.yaml"):
        self.spark = spark
        self.logger = CustomLogger("EltManager")
        self.odm = OrderManager(spark)
        self.config_file = config_file
      
    def init_rsm(
        self,
        source_type, source_topic, source_dpath,
        target_type, target_topic, target_dpath,
        chunk_size=50000, lowercase=True):

        self.source_type = source_type
        self.source_topic = source_topic
        self.source_dpath = source_dpath
        self.target_type = target_type
        self.target_topic = target_topic
        self.target_dpath = target_dpath

        self.chunk_size = chunk_size
        self.lowercase = lowercase
    
        # 소스 타겟 대상 초기화 
        rsm = ResourceManager(self.spark, self.config_file)
        
        # 소스 대상 정의
        self.source_tm = rsm.get_resource_manager(source_type, source_topic, dpath=source_dpath) #oracle

        # 타셋 대상 정의
        self.target_tm = rsm.get_resource_manager(target_type, target_topic, dpath=target_dpath) #delta

        
    def getSourceManager(self) :
        return self.source_tm 
        
    def getTargetManager(self) :
        return self.target_tm
        
    def _getSourceInfo(self, source_objects) :
        return (
            f"{self.source_type} {self.source_topic} {self.source_dpath} {source_objects}"
            if self.source_dpath is not None
            else f"{self.source_type} {self.source_topic} _ {source_objects}"
        )
    
    def _getTargetInfo(self, target_object) :
        return (
            f"{self.target_type} {self.target_topic} {self.target_dpath} {target_object}"
            if self.target_dpath is not None
            else f"{self.target_type} {self.target_topic} _ {target_object}"
        )
    
    # Single tables full load
    def ingest_full(self, source_objects, target_object, source_customSchema=None, target_customSchema=None, count=True, offset=0, cleansing_conditions=None) :    
        # 소스 > 타겟 Ingestion (chunk load)
        sourceTable = source_objects[0]   # 단일 테이블에 대해서만 ingest_full 처리, 복수 테이블은 increment 기반 처리
        targetTable = target_object

        sourceInfo = self._getSourceInfo(source_objects)
        targetInfo = self._getTargetInfo(target_object)
        
        timer = Timer()
        self.logger.info(f"ETL/FL Started : [ {targetInfo} ]")

        offset = offset
        source_df = None

        if count is True:
            source_df = self.source_tm.loadTable(sourceTable)
            if source_df is None :
                self.logger.error(f"ETL/FL Error : {sourceInfo} doesn't exist. / {timer.tab():.2f} ]")
                return (None, None, True)

            size = source_df.count()
            self.logger.info(f"Source count = {size} / expected loop {math.ceil(size / self.chunk_size)}")
                
        while True:
            # Oracle 데이터 읽기
            source_df = self.source_tm.loadTable(sourceTable, offset=offset, chunk_size=self.chunk_size, customSchema=source_customSchema)

            # 데이터가 없으면 종료
            if source_df is None :
                self.logger.error(f"ETL/FL Done : [ {targetInfo} / True (0, 0) / {timer.tab()} ]")
                return (None, None, True)
                
            chunk_read_size = source_df.count()
            if chunk_read_size == 0:
                break

            if target_customSchema:
                for column_name, data_type in target_customSchema.items():
                    source_df = source_df.withColumn(column_name, source_df[column_name].cast(data_type))

            self.logger.info(f"Source Loading Chunk : {sourceInfo} / offset={offset}, self.chunk_size={chunk_read_size} / elipsed={timer.tab():.2f}")

            # Save to Delta
            if offset == 0:
                # 컬럼 이름을 소문자로 변환
                if self.lowercase is True:
                    source_df = source_df.toDF(*[col.lower() for col in source_df.columns])

                    self.target_tm.saveTable(source_df, targetTable, mode="overwrite")
            else: 
                self.target_tm.saveTable(source_df, targetTable, mode="append")

            self.logger.info(f"Target  Saving Chunk : {targetInfo} / elipsed={timer.tab():.2f}")

            if self.source_tm.getType() == "csv":
                self.source_tm.archive(sourceTable)

            offset += chunk_read_size

        self.logger.info(f"Source Loading Count : {sourceInfo} ({offset})")

        target_df = self.target_tm.loadTable(targetTable)     
        self.logger.info(f"Target Saving Count : {targetInfo} ({target_df.count()})")

        cleaned_count, cleaned_target_df = self.cleaning_and_save(target_df, target_object, cleansing_conditions)
        self.logger.info(f"Target  Cleaning : {targetInfo} / cleaned_size={cleaned_count} / elipsed={timer.tab():.2f}")
        
        valid = offset == cleaned_target_df.count() + cleaned_count
           
        self.logger.info(f"ETL/FL Done : [ {targetInfo} / {valid} ({offset}, {cleaned_target_df.count()}, {cleaned_count}) / {timer.elapsed():.2f} ]")

        #self.logger.info(f"소스 스키마 {sourceInfo} -- ")
        #source_df.printSchema()

        #self.logger.info(f"타겟 스키마 {targetInfo} -- ")
        #target_df.printSchema()

        # insert_log(spark, schema_name, table_name, datetime.now(), rundate)
        # logger.info(f" Update Job logs : {targetTopic}]")   ac

        return (source_df, cleaned_target_df, valid)
  
    # (Bronze: Oracle > Delta) 
    # source_inc_query = """
    #     SELECT * FROM BCPARKING.TB_TMINOUT 
    #     WHERE IN_DTTM < TO_DATE('2023-06-02', 'YYYY-MM-DD')
    #     -- WHERE IN_DTTM >= TO_DATE('2023-06-02','YYYY-MM-DD') AND IN_DTTM < TO_DATE('2023-06-03','YYYY-MM-DD')
    # """
    #
    # (Silver / Gold / Mart) 
    # source_inc_query = """
    #     SELECT * FROM tb_tminout 
    #     WHERE IN_DTTM < DATE '2023-06-02'
    # """ 
    # target_condition = "`IN_DTTM` < DATE '2023-06-02'"
    #

        
    # Multiple tables incremental load 
    def ingest_increment(self, source_objects, target_object, source_inc_query, target_condition,  
                         source_customSchema=None, target_customSchema=None, cleansing_conditions=None) :    

        sourceInfo = self._getSourceInfo(source_objects)
        targetInfo = self._getTargetInfo(target_object)
        
        timer = Timer()
        self.logger.info(f"ETL/IC Started : [ {targetInfo} ]")
        source_df = self.source_tm.queryTable(source_inc_query, tableNames=source_objects, customSchemas=source_customSchema)
        # 데이터가 없으면 종료
        if source_df is None :
            self.logger.error(f"ETL/IC Done : [ {targetInfo} / True (0, 0) / {timer.tab():.2f} ]")
            return (None, None, True)

        source_read_size = source_df.count()
        self.logger.info(f"Source Loading : {sourceInfo} / source_size={source_read_size} / elipsed={timer.tab():.2f}")

        if target_customSchema:
            for column_name, data_type in target_customSchema.items():
                source_df = source_df.withColumn(column_name, source_df[column_name].cast(data_type))

        # Save to Delta Incrementally
        before_count, after_count, del_count, target_df = self.target_tm.delSert(source_df, target_condition, target_object)

        self.logger.info(f"Target  Saving : {targetInfo} / delsert_size={after_count - before_count + del_count} (before={before_count}, after={after_count}, del={del_count}) / elipsed={timer.tab():.2f}")

        cleaned_count, cleaned_target_df = self.cleaning_and_save(target_df, target_object, cleansing_conditions)
        self.logger.info(f"Target  Cleaning : {targetInfo} / cleaned_size={cleaned_count} / elipsed={timer.tab():.2f}")

        target_read_size = self.target_tm.countTableCondition(target_condition, target_object)
        valid = source_read_size == target_read_size + cleaned_count
        self.logger.info(f"ETL/IC Done : [ {targetInfo} / {valid} ({source_read_size}, {target_read_size}, {cleaned_count}) / {timer.elapsed():.2f} ]")

        # insert_log(spark, schema_name, table_name, datetime.now(), rundate)
        # logger.info(f" Update Job logs : {targetTopic}]")   ac

        return (source_df, cleaned_target_df, valid)
        
    # condition1 = ~col("aaa").like("%.%")
    # condition2 = col("bbb") != "xyz"
    # cleaning_and_save(.., cleansing_conditions=condition1 & condition2)
    def cleaning_and_save(self, target_df, target_object, cleansing_conditions=None):
        if cleansing_conditions is None:
            return (0, target_df)

        cleaned_df = target_df.filter(cleansing_conditions)

        count = target_df.count() - cleaned_df.count()
        self.logger.debug(f"Cleansed count={count} (before={target_df}, after={cleaned_df})")

        if count > 0:
            self.target_tm.saveTable(cleaned_df, target_object, mode="overwrite")

        return (count, cleaned_df)

# from lib.elt_manager import EltManager
# em = EltManager(spark)        
#
# (Bronze Config)
# source_type = "oracle"
# source_topic = "bcparking"
# source_objects = ["tb_tminout"]
# target_type = "delta"
# target_topic = "bronze-bcparking"
# target_object = "tb_tminout"
#
# (Bronze Full Load)
# em.init_rsm(source_type, source_topic, target_type, target_topic, 500000)
# source_df, target_df = em.ingest_full(source_objects, target_object)
#
# (Bronze Incremental Load)
# source_inc_query = """
#     SELECT * FROM BCPARKING.TB_TMINOUT 
#     WHERE IN_DTTM < TO_DATE('2023-06-02', 'YYYY-MM-DD')
#     -- WHERE IN_DTTM >= TO_DATE('2023-06-02','YYYY-MM-DD') AND IN_DTTM < TO_DATE('2023-06-03','YYYY-MM-DD')
# """
# target_condition = "`IN_DTTM` < DATE '2023-06-02'"
# source_df, target_df = em.ingest_increment(source_objects, target_object, source_inc_query, target_condition)
#
# (Mart Config)
# source_type = "delta"
# source_topic = "gold"
# source_objects = ["tb_tminout"]
# target_type = "postgresql"
# target_topic = "mart"
# target_object = "public.tb_tminout"
#
# (Bronze Full Load)
# em.init_rsm(source_type, source_topic, target_type, target_topic, 500000)
# source_df, target_df = em.ingest_full(source_objects, target_object)
#
# (Incremental Load)
# source_inc_query = """
#     SELECT * FROM tb_tminout 
#     WHERE IN_DTTM < DATE '2023-06-02'
# """ 
# target_condition = "`IN_DTTM` < DATE '2023-06-02'"
# source_df, target_df = em.ingest_increment(source_objects, target_object, source_inc_query, target_condition)

    # 조건에 해당하는 Order 를 로딩하고 Full Load 실행
    # 복수 소스 오브젝트(테이블)이 지정된 경우, Incremental Load 실행 (단, 기간 조건을 최대로 지정하여 Full Load 효과 동일)
    # 복수 소스 오브젝트의 경우 쿼리문을 기준으로 로딩 필요.
    # 단, 단일 소스 오브젝트의 경우는 조건식을 고려하지 않고 Full Load 실행
    def run_order_full_load(self, target_type, target_topic, from_date="1900-01-01", to_date="2999-12-31", frequency="Day", target_object=None):

        bdf = self.odm.getOrderByTargetTypeTopic(target_type, target_topic, frequency, target_object)
        bdf = self.odm.update_condition(bdf, from_date, to_date)
        
        self.logger.info(f"Order Full Load Started: {target_type} {target_topic} ({bdf.count()})")

        # source_type, source_topic, target_type, taget_topic 동일한 경우 em 초기화
        grouped_df = bdf.groupBy("source_type", "source_topic", "target_type", "target_topic")\
                    .agg(collect_list(struct(*bdf.columns)).alias("data_list"))

        for row in grouped_df.collect():
            self.logger.info(f"Order Group Started : source_type={row.source_type}, source_topic={row.source_topic}, target_type={row.target_type}, target_topic={row.target_topic}")
            self.init_rsm(row.source_type, row.source_topic, row.target_type, row.target_topic, 500000)    

            #source_df, target_df, valid = None, None, None
            for data_row in row.data_list :
                self.logger.info(f"Order Object Started: source_object={data_row.source_object}, target_object={data_row.target_object}")
                if len(data_row["source_object"]) > 1  : # 2개 이상 테이블인 경우 Incremental Load 로 처리 (1900-01-01 ~ 2999-12-31)
                    #source_df, target_df, valid = 
                    self.ingest_increment(data_row["source_object"], data_row["target_object"], data_row["source_incremental_condition"], data_row["target_delete_condition"])      
                else :
                    # source_df, target_df, valid = 
                    self.ingest_full(data_row["source_object"], data_row["target_object"])
                self.logger.info(f"Order Object Done: source_object={data_row.source_object}, target_object={data_row.target_object}")
                #if valid :
                #    self.logger.info(f"Order Object Done: source_object={data_row.source_object}, target_object={data_row.target_object}")
                #else :
                #    self.logger.error(f"Order Object Failed: source_object={data_row.source_object}, target_object={data_row.target_object}")
                #    break
            
            self.logger.info(f"Order Group Done : source_type={row.source_type}, source_topic={row.source_topic}, target_type={row.target_type}, target_topic={row.target_topic}")
            
        self.logger.info(f"Order Full Load Done: {target_type} {target_topic} ({bdf.count()})")
                    
            
    def run_order_inc_load(self, target_type, target_topic, from_date, to_date, frequency="Day", target_object=None):

        bdf = self.odm.getOrderByTargetTypeTopic(target_type, target_topic, frequency, target_object)
        bdf = self.odm.update_condition(bdf, from_date, to_date)

        self.logger.info(f"Order Incremental Load Started: {target_type} {target_topic} ({bdf.count()})")

        # source_type, source_topic, target_type, taget_topic 동일한 경우 em 초기화
        grouped_df = bdf.groupBy("source_type", "source_topic", "target_type", "target_topic")\
                    .agg(collect_list(struct(*bdf.columns)).alias("data_list"))

        for row in grouped_df.collect():
            self.logger.info(f"Order Group Started : source_type={row.source_type}, source_topic={row.source_topic}, target_type={row.target_type}, target_topic={row.target_topic}")
            self.init_rsm(row.source_type, row.source_topic, row.target_type, row.target_topic, 500000)    

           
            for data_row in row.data_list :
                if data_row.incremental is True :
                    self.logger.info(f"Order Object Started: source_object={data_row.source_object}, target_object={data_row.target_object}, del_cond={data_row.target_delete_condition} , inc_cond={data_row.source_incremental_condition}")
                    self.ingest_increment(data_row.source_object, data_row.target_object, data_row.source_incremental_condition, data_row.target_delete_condition)              
                    
            self.logger.info(f"ELTManager Group Done : source_type={row.source_type}, source_topic={row.source_topic}, target_type={row.target_type}, target_topic={row.target_topic}")
            
        self.logger.info(f"Order Incremental Load Done: {target_type} {target_topic} ({bdf.count()})")
                                

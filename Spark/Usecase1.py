# Import pandas
import pandas as pd
import numpy as np
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql import DataFrame


def main():
        spark=SparkSession.builder.appName("DBSTest").getOrCreate()
        #print("Hello World!")
        #df = spark.read.load("file:///home/skiganesh/codes/coalastest.csv",format="csv", sep=",", inferSchema="true", header="true")
        df1=spark.read.option('header','true').csv('file:///home/skiganesh/codes/coalastest.csv',inferSchema=True)
        df1=df1.groupBy("col_subtype","val_usage_code").pivot("perf").sum("os_000")
        df1.show(truncate=False)
        # df=pd.read_csv("/home/skiganesh/codes/coalastest.csv")
        #print(df.count)
        # df=pd.pivot_table(df,index=["col_subtype","val_usage_code"],columns=["perf"],values=["os_000"],aggfunc={"os_000":np.sum})
        #print(df)
        df2=df1.toPandas()
        df2=df2.set_index(["col_subtype","val_usage_code"])
        df2=df2.unstack()
        df2.loc['total']=df2.sum(numeric_only=True,axis=0)
        df2=df2.stack()
        print(df2)


if __name__ == "__main__":
                main()
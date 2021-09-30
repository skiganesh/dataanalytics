import pyspark
from pyspark.sql import SparkSession
from datetime import datetime
from pyspark.sql import Row


def dfoperations1(spark):
    now = datetime.now()

    print("Inside DataFrame Operations")


    # A PySpark DataFrame can be created via SparkSession.createDataFrame typically by passing a list of lists,
    # tuples, dictionaries and pyspark.sql.Rows, a pandas DataFrame and an RDD consisting of such a list.

    # spark.read Returns a DataFrameReader that can be used to read data in as a DataFrame.

    print("Reading CSV")
    resdf = spark.read.csv('file:///D:/codes/ClaypotUsecase1/source/restaurantrecommendataion/restaurantrecommendation.csv', header=True, inferSchema=True)

    # Columns present in the dataset
    print("Columns present in the dataset")
    print(resdf.columns)

    # print("Current Time =", now.strftime("%H:%M:%S"))
    print("Current Time=", datetime.now().time())

    # Number of rows in the dataset before cache
    print("Number of rows in the dataset")
    print(resdf.count())

    print("Current Time=", datetime.now().time())

    # Caching is a lazy transformation, so immediately after calling the function nothing happens with the data
    # but the query plan is updated by the Cache Manager by adding a new operator — InMemoryRelation.
    # So this is just some information that will be used during the query execution later on when some action is called.

    print("Caching dataframe")
    # resdf.persist(pyspark.StorageLevel.MEMORY_ONLY)
    resdf.cache()

    print("Fetching top 10 rows")
    print(resdf.show(10))

    print("Dataset Schema is")
    resdf.printSchema()

    print("Current Time=", datetime.now().time())
    print("Getting row count on cached dataframe")
    print(resdf.count())
    print("Current Time=", datetime.now().time())

    print("Current Time=", datetime.now().time())
    print("Getting row count again on the cached dataframe")
    print(resdf.count())
    print("Current Time=", datetime.now().time())

    print("To select specific columns from a dataframe")
    resdf_2col = resdf.select(resdf["customer_id"], resdf["gender"])
    resdf_2col.show(10)

    print("Showing only distinct rows count")
    distresdf_2col= resdf_2col.distinct()
    print(distresdf_2col.count())

    # Creates a temporary view using the DataFrame
    # SQL statements can be run by using the sql methods provided by sqlContext.
    print("Executing SQL statements using sql methods on the dataframe temp view")
    distresdf_2col.createOrReplaceTempView("restdata")
    tempviewdf = spark.sql("select * from restdata limit 10")
    tempviewdf.show()

def dfoperations2(spark):

    print("To drop duplicate rows from a dataframe")
    df = spark.read.csv('D:\codes\ClaypotUsecase1\source\dfcleansing.csv',header=True)

    print("Before")
    df.show()
    print("After")
    df.dropDuplicates().show()
    print("Remove duplicate based on specific columns only")
    df.dropDuplicates(['name', 'height']).show()

    print("To drop a specified column or columns from a dataframe")
    # # Returns a new DataFrame that drops the specified column.
    # # This is a no-op if schema doesn’t contain the given column name(s).
    print("Before")
    df.show()
    print("After")
    df.drop('height').show()

    print("To Omit rows with null values")
    print("Before")
    df.show()
    print("After")
    df.dropna().show()

    print("Get all column data types")
    print(df.dtypes)

    print("To replace Null values with some value")
    print("Before")
    df.show()
    print("After")
    df.fillna({"height" : 150}).show()

    print("To filter dataframe with some condition")
    print("Before")
    df.show()
    print("After")
    print("Filter row with name Bob")
    df.where(df.name == "Bob").show()
    print("Filter rows with age >49")
    df.filter(df.age > 49).show()

    print("To replace one column value with another value")
    print("Before")
    df.show()
    print("After")
    df.na.replace('67', '55').show()

    print("To sort dataframe by specified column or columns")
    print("Before")
    srtdf = df.fillna({"height": 150})
    srtdf = srtdf.dropDuplicates()
    srtdf.show()
    print("Sort by height")
    srtdf.sort("height", ascending=False).show()
    print("Sort by age")
    srtdf.sort("age", ascending=False).show()

    print("To add a new column to dataframe using existing one")
    print("Before")
    df.show()
    print("After")
    df.withColumn('newage', df.age+2).show()

    print("To rename a column in the dataframe")
    print("Before")
    df.show()
    print("After")
    df.withColumnRenamed('age','newage').show()




import pyspark
from pyspark.sql import SparkSession
from datetime import datetime


def dfoperations():
    now = datetime.now()

    print("Inside DataFrame Operations")
    # SparkSession is the entry point to programming Spark with the Dataset and DataFrame API.
    spark = SparkSession \
        .builder \
        .config("spark.driver.memory", "4g") \
        .appName("DataFrameOps") \
        .getOrCreate()

    spark.sparkContext.setLogLevel("Error")

    # A PySpark DataFrame can be created via SparkSession.createDataFrame typically by passing a list of lists,
    # tuples, dictionaries and pyspark.sql.Rows, a pandas DataFrame and an RDD consisting of such a list.

    # spark.read Returns a DataFrameReader that can be used to read data in as a DataFrame.

    print("Reading CSV")
    resdf = spark.read.csv('file:///D:/codes/ClaypotUsecase1/source/restaurantrecommendataion/restaurantrecommendation.csv', header=True)

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


# import DataFrameOperations
from DataFrameOperations import *

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')
    # SparkSession is the entry point to programming Spark with the Dataset and DataFrame API.
    spark = SparkSession \
        .builder \
        .config("spark.driver.memory", "4g") \
        .appName("DataFrameOps") \
        .getOrCreate()

    spark.sparkContext.setLogLevel("Error")
    # dfoperations1(spark)
    dfoperations2(spark)
    spark.stop()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

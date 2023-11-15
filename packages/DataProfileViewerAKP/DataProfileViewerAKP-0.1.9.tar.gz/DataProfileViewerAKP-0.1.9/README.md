
# DataProfileViewerAKP

This is a spark compatible library. This will help in profiling data.

Current version has following attributes which are returned as result set:


## Result Set
#### Column:
Column Name from supplied dataframe

#### DataType:
Datatype of column fetched with "inferSchema"

#### Count: 
Total number of rows

#### NullCount: 
Total number of Null rows


#### NullPercentage: 
Percentage of Null Values


#### EmptyCount: 
Total Number of Empty Rows-->('')


#### BlankCount: 
Total Number of Blank Rows-->(' ')


#### MaxLength: 
Maximum length of data in Column


#### MinLength: 
Minimum length of data in column


#### AvgLength: 
Average length of data in column


#### DistinctCount: 
Distinct Count in Column(appear once or more than once in Column)


#### UniqueCount: 
Unique Count in Column(appear only once in column)
## Installation and Driver Code

To install run:

```bash
pip install DataProfileViewerAKP
```

Driver Code:

```bash
from DataProfileViewerAKP import DataProfileViewerAKP
df =  spark.read.format('csv').\
      option("header", True).option("inferSchema", True).\
      load(Path)
re=DataProfileViewerAKP.get_data_profile(spark,df)
re.display()
```


Required Libraries:

```bash
import datetime, time
from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf
from pyspark.sql import functions as F
from pyspark.sql.types import StructType, StructField, StringType, IntegerType,FloatType
from pyspark import StorageLevel
```
You can also define your own spark session:

```bash
conf = SparkConf()
conf.set('set hive.vectorized.execution', 'true')
conf.set('set hive.vectorized.execution.enabled', 'true')
conf.set('set hive.cbo.enable', 'true')
conf.set('set hive.compute.query.using.stats', 'true')
conf.set('set hive.stats.fetch.column.stats','true')
conf.set('set hive.stats.fetch.partition.stats', 'true')
conf.set('spark.cleaner.referenceTracking.cleanCheckpoints', 'true')
spark = SparkSession.builder.appName("profile_driver_program").config(conf=conf).enableHiveSupport().getOrCreate()
spark.sql('set hive.exec.dynamic.partition=True')
spark.sql('set hive.exec.dynamic.partition.mode=nonstrict')
```
## Authors



Abhijeet Kasab (Azure Data Engineer)
## Optimizations

Used cache so as to bring dataframe onto memory as the code has multiple operations running on the same dataframe


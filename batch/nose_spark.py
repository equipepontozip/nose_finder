#print('Loading Libraries')
import time 
#print('Starting Nose Finder')
#starting_time = time.clock()

import utilities.tools as utils
from utilities.nose_recognition import NoseFinder
import os
from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext
from pyspark import sql
from pyspark.sql.functions import length, lit, udf, col, regexp_replace, monotonically_increasing_id
from pyspark.sql.window import Window


def nose_find(filename, name):
    try:
        print('nose finding', name)
        NoseFinder( filename )._saveCroppedImage( name )
    except:
        pass
     
nose_finding = udf( lambda filename, name: nose_find(filename, name))

appName = 'Nose_Spark'
master = 'local[*]'

config = SparkConf().setAppName(appName).setMaster(master)
sc = SparkContext( conf=config )
sqlContext = sql.SQLContext(sc)

data0 = sc.wholeTextFiles("./bread_pictures/")

df = data0.toDF()
window = Window().orderBy(lit('A'))
#df = df.withColumn( "row_number", row_number().over( window ) )
df = df.withColumn( "filenames", regexp_replace('_1', 'file:',''))
#df = df.withColumn( "row_number", explode( typedLit( (1 to length(df.filenames) ).toList) ) )
df = df.withColumn( "row_number", monotonically_increasing_id() )

df.select("filenames","row_number").show()

df_final = df.select( nose_finding(col("filenames"), col("row_number")) )

df_final.show()

print('---')
# print(df_final.count())
print('---')

######
# data1 = sc.wholeTextFiles("./bread_nariguins/")
# dataDF = data1.toDF()
# dataDF.select("_1").show()
# print('---')
# print(dataDF.count())
print('---')
# sc.file_list.map( )
# sc.close()

#utils.finalMessage()
#utils.timeElapsed(starting_time)
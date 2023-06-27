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
        nose_name = 'nariguin_'+name
        print('nose finding', nose_name)
        return NoseFinder( filename )._saveCroppedImage( nose_name )
    except:
        pass
     
nose_finding = udf( lambda filename, name: nose_find(filename, name))

appName = 'Nose_Spark'
master = 'local[*]'

config = SparkConf().setAppName(appName).setMaster(master)
sc = SparkContext( conf=config )
sqlContext = sql.SQLContext(sc)
sample_img_dir = './bread_pictures'

image_df = sc.read.format("image").load(sample_img_dir)
image_df.show()
exit()
df = file_data.toDF()
df = df.withColumn( "filenames", regexp_replace('_1', 'file:',''))

df = df.withColumn( "row_number", monotonically_increasing_id() )

#df.select("filenames","row_number").show()

df_final = df.withColumn("images", nose_finding(col("filenames"), col("row_number")) )
del df
print(type(df_final))
print(df_final)

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
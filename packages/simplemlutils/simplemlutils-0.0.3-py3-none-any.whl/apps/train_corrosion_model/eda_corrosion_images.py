"""Loads a CSV file into Spark
"""

"""Convert a csv file to parquet format.
This application is meant to be submitted on
Spark for execution

"""
from pathlib import Path
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.functions import expr, col
from pyspark.ml import image
import numpy as np

from PIL import Image, ImageDraw

APP_NAME = "EDA Corrosion images"


TRAIN_IMAGES_PATH = Path("/home/alex/qi3/mir_datasets_new/corrosion_v_3_id_9/train")
TEST_IMAGES_PATH = Path("/home/alex/qi3/mir_datasets_new/corrosion_v_3_id_9/test")

# https://godatadriven.com/blog/real-distributed-image-processing-with-apache-spark/

def convert_bgr_array_to_rgb_array(img_array):
    B, G, R = img_array.T
    return np.array((R, G, B)).T

if __name__ == '__main__':

    # get a spark session
    spark = SparkSession.builder.appName(APP_NAME).getOrCreate()

    corrosion_df = spark.read.format("image").load(str(TRAIN_IMAGES_PATH / "corrosion"))
    corrosion_df.printSchema()

    corrosion_df.select("image.origin",
                        "image.height", "image.width", "image.nChannels",
                        "image.mode").show(10, truncate=False)

    # is there any images with more than three channels
    # (corrosion_df.select("image.nChannels")
    #  .where(col("image.nChannels") > 3)
    #  .show())

    image_row = 0

    # this means to bring all the data from the
    # workers!!! It may fail with memory exception
    spark_single_img = corrosion_df.select("image.data").collect()[image_row]
    #(spark_single_img.image.origin, spark_single_img.image.mode, spark_single_img.image.nChannels)

    mode = 'RGBA' if (spark_single_img.image.nChannels == 4) else 'RGB'
    # Image.frombytes(mode=mode, data=bytes(spark_single_img.image.data),
    #                 size=[spark_single_img.image.width, spark_single_img.image.height]).show()


    img = Image.frombytes(mode=mode, data=bytes(spark_single_img.image.data),
                          size=[spark_single_img.image.width,spark_single_img.image.height])
    converted_img_array = convert_bgr_array_to_rgb_array(np.asarray(img))
    Image.fromarray(converted_img_array).show()

    # for each image we want to compute the mean in every
    # channel

    spark.stop()



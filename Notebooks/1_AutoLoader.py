# Databricks notebook source
# MAGIC %md
# MAGIC ## Incremental Data Lake using AutoLoader

# COMMAND ----------

# MAGIC %sql
# MAGIC create schema netflix_catalog.net_schema;

# COMMAND ----------

checkpoint_location = "abfss://silver@netflixprojectraghav.dfs.core.windows.net/checkpoint"

# COMMAND ----------

df = spark.readStream\
  .format("cloudFiles")\
  .option("cloudFiles.format", "csv")\
  .option("cloudFiles.schemaLocation",checkpoint_location)\
  .load("abfss://raw@netflixprojectraghav.dfs.core.windows.net")

# COMMAND ----------

display(df, checkpointLocation = "abfss://silver@netflixprojectraghav.dfs.core.windows.net/checkpoint_display")

# COMMAND ----------

df.writeStream\
  .option("checkpointLocation", checkpoint_location)\
  .trigger(processingTime= '10 seconds')\
  .start("abfss://bronze@netflixprojectraghav.dfs.core.windows.net/netflix_titles")

# COMMAND ----------


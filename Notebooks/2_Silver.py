# Databricks notebook source
# MAGIC %md
# MAGIC ##Silver Notebook Lookup Tables

# COMMAND ----------

# MAGIC %md
# MAGIC ###Parameters

# COMMAND ----------

dbutils.widgets.text("sourcefolder", "netflix_directors")
dbutils.widgets.text("targetfolder", "netflix_directors")

# COMMAND ----------

# MAGIC %md
# MAGIC ###Variables

# COMMAND ----------

var_src_folder = dbutils.widgets.get("sourcefolder")
var_trg_folder = dbutils.widgets.get("targetfolder")

# COMMAND ----------

df = spark.read.format('csv')\
    .option("header", True)\
    .option("inferSchema", True)\
    .load(f"abfss://bronze@netflixprojectraghav.dfs.core.windows.net/{var_src_folder}")


# COMMAND ----------

display(df)

# COMMAND ----------

 df.write.format("delta")\
     .mode("append")\
     .option("path", f"abfss://silver@netflixprojectraghav.dfs.core.windows.net/{var_trg_folder}")\
     .save()   

# COMMAND ----------


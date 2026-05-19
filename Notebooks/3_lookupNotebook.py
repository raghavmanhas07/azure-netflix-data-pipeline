# Databricks notebook source
# MAGIC %md
# MAGIC ##Array parameter

# COMMAND ----------

import json
files = [
    {
        "sourcefolder" : "netflix_directors",
        "targetfolder" : "netflix_directors"
    },
    {
        "sourcefolder" : "netflix_cast",
        "targetfolder" : "netflix_cast"
    },
    {
        "sourcefolder" : "netflix_countries",
        "targetfolder" : "netflix_countries"
    },
    {
        "sourcefolder" : "netflix_category",
        "targetfolder" : "netflux_category"
    }
]   

# COMMAND ----------

# MAGIC %md
# MAGIC ##Job Utitility to return the ARRAY

# COMMAND ----------

dbutils.jobs.taskValues.set(key = "my_arr", value= json.dumps(files))

# COMMAND ----------


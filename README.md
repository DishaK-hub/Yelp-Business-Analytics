Goal: Analyzed Yelp data (~5.6GB) to uncover business trends and customer sentiment using GCP-based data pipeline.

Data Wrangling: Parsed and cleaned 5+ irregular JSON files (business, review, user, etc.) using Python (regex, JSON) and converted to CSV; split into relational tables (business, categories, reviews).

Cloud Integration: Uploaded cleaned datasets to Google BigQuery for large-scale SQL analysis.
Executed parallelized Spark Jobs on GCP Dataproc transforming 1M+ records

EDA & Insights:
• Identified peak review hours, sentiment patterns by time
• Analyzed effect of category diversity on ratings via box plots
• Ranked business categories by popularity and profitability by state
• Created interactive Tableau dashboards and US bubble maps to visualize review density by region

Tech Stack: Python (pandas, regex), SQLite, SQL (BigQuery), Tableau, GCP (Cloud Storage, Spark, Dataproc, BigQuery)

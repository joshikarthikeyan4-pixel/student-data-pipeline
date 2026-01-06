# Student Data Pipeline (SQL + Pandas)

## Overview
This project demonstrates an end-to-end data pipeline built using **PostgreSQL** and **Python (Pandas)**.

The pipeline ingests relational student data, performs validation and joins, applies business logic, and outputs a final cleaned dataset.

## Data Sources
The project uses three relational tables exported from PostgreSQL:

- **students** – student details (id, name, department, admission year)
- **courses** – course information (id, name, department, credits)
- **enrollments** – student enrollments and marks

## Pipeline Steps
1.  First Export data from PostgreSQL as CSV files  
2. Load CSVs using Pandas  
3. Validate schema and missing values  
4. Join tables using Pandas (`merge`)  
5. Apply business logic (pass/fail based on marks)  
6. Save final transformed dataset as CSV  

## TECH STACK USED :-
- Python
- Pandas
- PostgreSQL
- Git & Github

## Output
Final dataset is saved at:
output/final_student_performance.csv

## Key Learnings
- SQL to Pandas data integration
- Data validation and joins
- Handling missing values
- Building script-based data pipelines. 


## How to Run
1.Clone the repository.
2.Install python and the necessary the necessary packages 
3.Install the dependecies:
pip install pandas
4.Run the pipeline:
python pipeline.py 


## WHY This Project?
-This project demonstrates the core data engineering skills:
SQL-based data extraction,running queries and Python based transfromation.
also builds reproducable data pipelines.



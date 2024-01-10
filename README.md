# Missing-Data-Project 
![image](https://github.com/WayneRose-95/missing-data-project/assets/89411656/bdf3fe1f-0fd5-4210-8f81-a48da3d260e6)

Machines 4 All is a fictional manufacturing company, with factories based in The US, Mexico and China. 

Having collated data from various sources in their manufacturing process, 
the business would like to perform some Exploratory Data Analysis (EDA) to find out more insights regarding their manufacturing process. 
# Usage 
- Clone the repository using this command below
```
git clone https://github.com/WayneRose-95/missing-data-project.git
```
Please see the [Wiki](https://github.com/WayneRose-95/missing-data-project/wiki) for an in-depth guide on installing further dependencies. 

# Project Requirements 

- Miniconda3 or Anaconda3
- Git Bash or another shell scripting language
- The python packages below 
```
pandas==2.1.4
PyYAML==6.0.1
SQLAlchemy==2.0.23
ipykernel==6.28.0
numpy==1.2.8
psycopg2==2.9.9
black==23.12.1
pip==23.3.1
missingno==0.5.2
```
# Current Data Source

## The AWS RDS 
- An AWS RDS, which runs on postgres
- Data is collected via a batch process which runs daily from various resources
- The Data Engineers create views from the database, which is handed over to the Data Analysts for EDA.
  
# Business Requirements 

- The ability to see clear and concise visualisations, which describe the insights found from the data
- Points of action from the insights gained
- The project must be completed with minimal technological components

# The Solution

The solution is to create a visulations using Python. 
This will reduce the need of external technological components such as Power BI and Tableau, making the process easier to maintain. 

## The Visualisations Used 

- A matrix showing the missing values present inside the data. This will be visualised using the [missingno](https://github.com/ResidentMario/missingno) package


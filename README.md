# Log Analysis Project
This is project #1 required for Udacity Full-Stack Web Developer Nanodegree program.
It is a reporting tool where Python program using the psycopg2 module to connect to 
the database and retrieve the data. 

## Details 
The project answers the following reporting questions:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Technologies used
1. Python
2. PostgreSQL
3. Virtual machine vagrant 

## Prerequisites 
1. Download and install [Vagrant](https://www.vagrantup.com/downloads.html)
2. Download and install [Virtual Machine](https://www.virtualbox.org/wiki/Downloads)
3. Download [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) and then unzip the file. Take the file and put it into the **vagrant** directory. 
4. Download or clone this project and put it inot the **vagrant** directory.

###### Run the following commands from the terminal in the folder where your vagrant is installed in:
1. `vagrant up`
2. `vagrant ssh`
3. `cd /vagrant` **to navigate to vagrant directory 
4. `python logAnalysis_p1.py`

## The Used Views 
errorStatus
```
create view errorStatus as select time::date as date, count(status) as numOfError 
from log where status != '200 OK' group by date;
```

allStatus
```
create view allStatus as select time::date as date, count(status) as numOfStatus
from log group by date;
```

errorPercentage
```
create view errorPercentage as select allStatus.date, allStatus.numOfStatus as numStatus,
errorStatus.numOfError as numError, 
errorStatus.numOfError::double precision/allStatus.numOfStatus::double precision * 100 
as errorPer 
from errorStatus, allStatus
where errorStatus.date = allStatus.date;
```
#!/usr/bin/env python3

import psycopg2

DBName = "news"

# Function execute the recieved query and send the result back to the sender function
def connection(query):
        
        
        db = psycopg2.connect(database=DBName)
        c = db.cursor()
        c.execute(query)
        result = c.fetchall()
        db.close()
        return result
      
    
# Function to get the most popular 3 articles with number of views   
def get_articles():
    
    
        query = """""select title, count(status) as numOfViews from log, articles 
        where (select substring(log.path, 10) = articles.slug) 
        group by title 
        order by numOfViews desc limit 3;""""
        articles = connection(query)
        print("1. What are the most popular three articles of all time?")
        for title, numOfViews in articles:
            print '- "' + title + '" - ' + str(numOfViews) + ' views.'

        
# Function to get the most popular authors names with number of views     
def get_authors():
    
    
        query = """""select name, count(status) as numOfViews from log, articles, authors 
        where authors.id = articles.author and (select substring(log.path, 10) = articles.slug) 
        group by name 
        order by numOfViews desc;""""
        authors = connection(query)
        print("2. Who are the most popular article authors of all time?")
        for name, numOfViews in authors:
            print '- "' + name + '" - ' + str(numOfViews) + ' views.'

   
 # Function to get the requests failed more than 1% 
def get_errors():
  
    
        query = "select date, errorPer from errorPercentage where errorPer > 1;"
        errors = connection(query)
        print("3. On which days did more than 1% of requests lead to errors?")
        for date, errorPer in errors:
            print("{0:%B %d, %Y} - {1:.1f}% errors" .format(date, errorPer))
    
    
if __name__ == '__main__':
    get_articles()
    get_authors()
    get_errors()
    
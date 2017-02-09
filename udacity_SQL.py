---Secret Phrase---
SELECT sql, statement FROM Udacious WHERE quertId = 35;
Table Name: Udacious
Columns:
problemSet INTEGER, node INTEGER, queryID INTEGEER, title TEXT, sql TEXT, statement TEXT

HIDDEN MESSAGE #3 = Awesome.db
-------------------

## What's database? ##
# Provide persistence like a file and data structures for storing and searching
    # our data much faster and easier than we could search a flat file
# Enale multiple programs or users to access and modify data at the same time
    # without interrupting each others, or undoing each others changes
# Databases: key-value store, navigational DB, relational DB
# Relational DB Features
    # flexible query language with aggregation and join operations
    # constraints-rules for protecting consistency of your data
# A relational DB is a collection of data items organized as a set of formally-described
    # tables from which data can be accessed or reassembled in many diff ways
    # without having to reorganize the DB tables
# Relational DB is relatively easy to create and access
# Major advantage of relational DB is easy to extend
    # a new data category can be added without requiring that all existing applications be modified

# The standard user and application program interface is SQL
    # Structure Query Language: used both for interactive queries for information from a
        #relational DB and for gathering data for reports

# You send code(query) to the DB, then DB send result as table
    # This can be done either via
        # TCP/IP network (mysql, postgreswl, oracle, etc), or
        # local libraries kept in local disk(sqlite)

## SQL queries exmaple ##

select food
from diet
where spieces = 'orangutan';
# food
# ----
# plants
# insects


select 2+2;
# ?column?
#---------
# 4

select 2+2, 4+4, 6+6;
# ?column?| ?column? | ?column?
#---------|----------|---------
# 4       | 8        | 12

select 2+2 as sum; # to name column use as
# sum
#-----
# 4

## Joinning Tables ##
select
animals.name, animals.species,diet.food
from
animals join diet
    on animals.species = diet.species
where food = 'fish';




------
## WHERE vs HAVING ##
# A WHERE clause is used is filter records from a result.
    # The filter occurs before any groupings are made.
# A HAVING clause is used to filter values from a group.
------
## SQL vs NoSQL ##
# SQL
    # provides a store of related data tables
    # SQL tables create a strict data template, so it’s difficult to make mistakes
    # impossible to add data until you define tables and field types in what's referred to a schema
        # Schema contains:
            # primary keys - unique identifiers such as ISBN which apply to single record
            # indexes - commonly queried fields indexed to aid quick searching
            # relationships - logical links between data fields
            # functionality such as triggers and stored procedures
    # Data schema must be designed and implemented before any business logic can be developed to manipulate data
        # can be updated later, but large changes can be complicated

# NoSQL
    # NoSQL databases store JSON-like-field-value pair doc
    # Similar documents can be stored in a collection, which is analogous to an SQL table
    # However, you can store any data you like in any document; the NoSQL database won’t complain
    # More flexible and forgiving, but being able to store any data anywhere can lead to consistency issues
    # Data can be added anywhere, at any time
        # no need to specify a doc design or even a collection up-front
        # MongoDB e.g. following statement wil create a new doc in a new book collection if it does not exist

    db.book.inser(
        ISBN: 9780994182654,
        title: "Jump Start Git",
        author: "Shaumik Daityari",
        format: "ebook",
        price: 29.00
    ); # MongoDB will automatically add a unique "_id" value to each doc in a collection; indexes can be assigned later
    # NoSQL database may be more suited to projects where the initial data requirements are difficult to ascertain

# SQL Normalization vs NoSQL Denormalization
# Example: adding publisher info to book store database
    # SQL Normilization
        # create a new 'publisher' table as there could be more than one title for each publisher
        # then add a "publisher_id" field to 'book' table, which references records by "publisher.id"
        # This minimizes data redundancy; not repeating original data but only adding reference to it
            # >> technique is known as normalization
    # NoSQL Denormalization
        # can use normalization technique, but opting to denormalize doc and repeating publisher info for every book may be better
        # denormalization leads to faster queries
            # however, updating the publisher info in multiple records will be significantly slower

# SQL Relational JOIN vs NoSQL
    # SQL queries offer a powerful JOIN clause
        # can obtain related data in multiple tables using a single SQL statement
        SELECT book.title, book.author, publisher.name
        FROM book
        LEFT JOIN book.publisher_id on publisher.id;
        # >> returns all book titles, authors, and associated publisher names
    # NoSQL does NOT have the clause equivalent to JOIN
        # Using normalization would need to fetch all book docs, retrieve all associated publisher docs, and manually link the two in program logic
            # >> denormalization is essential for NoSQL

# SQL vs NoSQL Data Integrity
    # Most SQL detabases allow you to enforce data integrity rules using foreign key constrains
        # ensure all books have a valid "publisher_id" code that matches one entry in the 'publisher' table, and
        # not permit publishers to be removed if one or more books are assigned to them
    # The schema enforces these rules for the db to follow; it's impossible for developers/users to add, edit, or remove records, which could result in invalid data or orphan records
    # The same data integrity options are not available in NoSQL databases; can store what you want regardless of any other documents

# SQL vs NoSQL Transactions
    # SQL: two or more updates can be executed in a transaction; however, one could succeed and the other fail, leaving figures out of sync. Placing the same updates within a transaction ensure either both succeed or both fail
    # NoSQL: modification of a single doc is atomic; all is updated successfully or remains unchaged. Unlike SQL db, there's no transaction equivalent for updates to multiple docs. There are transaction-like options but must be manually processed in your code at the time of writing
        # MongoDB: Using the "$isolated" operator, a write operation that affects multiple docs can prevent other processes from interleaving once the write operation modifies the first doc

# SQL VS NoSQL CRUD Syntax
    # SQL is lightweight declarative language. It has become an international standar, although most systems implement subtly different syntaxes
    # NoSQL databases use JavaScripty-looking queries with JSON-like arguments. Basic operations are simple, but nested JSON can become increasingly convoluted for more complex queries

    ## Comparison ##

        SQL                                 |   NoSQL
        ------------------------------------------------------------------------
        # insert a new book record
        ------------------------------------------------------------------------
        INSERT INTO book (                  | db.book.inser({
            'ISBN', 'title', 'author')      |   ISBN: "9780992461256",
        VALUES (                            |   title: "Full Stack JavaScript",
            '9780992461256',                |   author: "Colin Ihrig & Adam Bretz"
            'Full Stack JavaScript',        | });
            'Colin Ihrig & Adam Bretz') ;   |
        ------------------------------------------------------------------------
        # update a book record
        ------------------------------------------------------------------------
        UPDATE book                         | db.book.update(
        SET price = 19.99                   |   { ISBN:'9780992461256'},
        WHERE ISBN = '9780992461256'        |   { $set: {price: 19.99}});
        ------------------------------------------------------------------------
        # return all book titles over $10
        ------------------------------------------------------------------------
        SELECT title                        | db.book.find(
        FROM book                           |   { price: {&gt;: 10}},
        WHERE price > 10;                   |   { -id: 0, title: 1}
                                            |  );
        ------------------------------------------------------------------------
        # count the number of SitePoint books
        ------------------------------------------------------------------------
        SELECT COUNT(1)                     | db.book.count({
        FROM book                           |   "publisher.name": "SitePoint"
        WHERE publisher_id = 'SP001';       |});
        ------------------------------------------------------------------------
        # return the number of book format types
        ------------------------------------------------------------------------
        SELECT format, COUNT(1) AS 'total'  | db.book.aggregate([
        FROM book                           |   { $group:
        GROUP BY format;                    |       {
                                            |         _id: "$format",
                                            |         total: { $sum: 1}
                                            |       }
                                            |   }
                                            | ]);
                                            | # This is known as aggregation: a new set of
                                            |    # docs is computed from an original set
        ------------------------------------------------------------------------
        # delete all SitePoint books
        ------------------------------------------------------------------------
        DELETE FROM book                    | db.book.remove({
        WHERE publisher_id = 'SP001';       |   "publisher.name": "SitePoint"
                                            | });

# SQL vs NoSQL Performance
    # NoSQL is faster as its simpler denormalized store allows to retrieve all info about a specific item in single request
    # A well-designed SQL db will almost certainly perform better than a badly designed NoSQL equivalent

# SQL vs NoSQL Scaling
    # Distributing load among multiple servers can be tricky for SQL-based systems
        # Clustering is possibly the simplest option; multiple servers access the same central store- but even this has challenges
    # NoSQL's simpler data models can make the process easier, and many have been built with scaling functionality from the start

# SQL vs NoSQL Practicalities
    # NoSQL DBs are more likely to have issues than more mature SQL due to lack of knowledge

# SQL vs NoSQL Summary
    # SQL Ideal Projects
        # logical related discrete data requirements which can be identified up-front
        # data integrity is essential
        # standards-based proven technology with good developer experience and support
    # NoSQL Ideal Projects
        # unrelated, indeterminate or evolving data requirements
        # simpler or looser project objevtives, able to start coding immediately
        # speed and scalability is imperative

---------------------
## Types in the SQL ##
# Text and string types
    # text: a string of any length like python's str type. Values are written in single quotes.
    # char(n): a string of exactly n characters
    # varchar(n): a string of up to n characters
# Numeric types
    # integer: like python's int types but with different limits
    # real: a floating-point value, like python float. Accurate up to six decimal places
    # double precision: a higher-precision floating-point value. Accurate up to 15 decimal
# Date and time types
    # date: a calendar data. Values are written like as follows: '2014-04-13'
    # time: a time of day
    # timestamp: a date and time together
        # Make sure always put 'single quotes' around text strings and date/time values

# Select where
SELECT name
FROM animals
WHERE (NOT species = 'gorilla') and (NOT name = 'Max');
# alternate
WHERE NOT (species = 'gorilla' or name = 'Max');
WHERE species != 'gorilla' and name != 'Max';

# Comparison Operators
SELECT name
FROM animals
WHERE species = 'llama' and birthdate >= '1995-01-01' and birthdate <= '1998-12-31';

# SQL Weakness
    # SQL is terrible at listing tables and columns in a standard way
    # PostgreSQL: \dt and \d tablename
    # MySQL: show tables and describe tablename
    # SQLite: .tables and .schema tablename

'''
Here's a list of all the tables in the zoo database:

animals
This table lists individual animals in the zoo. Each animal has only one row. There may be multiple animals with the same name, or even multiple animals with the same name and species.
name — the animal's name (example: 'George')
species — the animal's species (example: 'gorilla')
birthdate — the animal's date of birth (example: '1998-05-18')
diet
This table matches up species with the foods they eat. Every species in the zoo eats at least one sort of food, and many eat more than one. If a species eats more than one food, there will be more than one row for that species.
species — the name of a species (example: 'hyena')
food — the name of a food that species eats (example: 'meat')
taxonomy
This table gives the (partial) biological taxonomic names for each species in the zoo. It can be used to find which species are more closely related to each other evolutionarily.
name — the common name of the species (e.g. 'jackal')
species — the taxonomic species name (e.g. 'aureus')
genus — the taxonomic genus name (e.g. 'Canis')
family — the taxonomic family name (e.g. 'Canidae')
t_order — the taxonomic order name (e.g. 'Carnivora')
If you've never heard of this classification, don't worry about it; the details won't be necessary for this course. But if you're curious, Wikipedia articles Taxonomy and Biological classification may help.

ordernames
This table gives the common names for each of the taxonomic orders in the taxonomy table.
t_order — the taxonomic order name (e.g. 'Cetacea')
name — the common name (e.g. 'whales and dolphins')
The SQL for it
And here are the SQL commands that were used to create those tables. We won't cover the create table command until lesson 4, but it may be interesting to look at:
'''

create table animals (  
       name text,
       species text,
       birthdate date);

create table diet (
       species text,
       food text);  

create table taxonomy (
       name text,
       species text,
       genus text,
       family text,
       t_order text); 

create table ordernames (
       t_order text,
       name text);

## SELECT Clauses ##
LIMIT count OFFSET skip # >> return count number of rows, starting with the skip + 1th row. OFFSET is optional
ORDER BY columns DESC # >> sort result rows by given column. DESC is optional
GROUP BY columns # >> which columns to use as groupings when aggregating

## Count All the Species ##
SELECT species, count(name) as num
FROM animals
GROUP BY species
ORDER BY num DESC;

## Insert ##
    # To add a row:
        INSERT into tablename values(42, 'stuff');
    # If the new values aren't in the same order as the table's columns:
        INSERT into tablename (col2, col1) values('stuff', 42)
# Select
SELECT name, birthdate
FROM animals
WHERE species = 'opossum';
# Insert
INSERT into animals values('Pat','opossum','2017-01-25')

## Find the Fish Eaters ##
SELECT animals.name
FROM animals join diet on animals.species = diet.species
WHERE diet.food = 'fish';
# Alternate
SELECT name
FROM animals,diet
WHERE animals.species = diet.species and diet.food = 'fish';

## After Aggregating ##
SELECT diet.food, count(animals.name) as num
FROM animals join diet on animals.species = diet.species
GROUP BY diet.food
HAVING num = 1;

## More JOIN Practice ##
SELECT ordernames.name, count(animals.name) as num
FROM taxonomy
    JOIN animals on taxonomy.name = animals.species
    JOIN ordernames on taxonomy.t_order = ordernames.t_order
GROUP BY ordernames.name
ORDER BY num DESC;

## Problem Set02 ##
# SQL Scramble #
# Which 10 composers wrote the most songs in the database?
SELECT Composer, COUNT(*)
FROM Track
GROUP BY Composer
ORDER BY COUNT(*) DESC
LIMIT 10;

# Query for Song Length #
# Which tracks in the dataset are between 2,500,000 and 2,600,000 milliseconds long?
SELECT Name, Milliseconds
FROM Track
WHERE Milliseconds > 2500000
AND Milliseconds < 2600000
ORDER BY Milliseconds;

# JOIN Artist to Album #
# List albums written by either Iron Maiden or Amy Winehouse
SELECT Artist.Name, Album.Title
FROM Album JOIN Artist
    ON Artist.ArtistID = Album.ArtistID
WHERE Name = 'Iron Maiden' OR Name = 'Amy Winehouse';

# Countries with most Invoice #
# Write a query that returns the 3 countries with the highest number of invoices,
    # along with the number of invoices for these countries
SELECT BillingCountry, count(InvoiceID) as num_inv
FROM Invoice
GROUP BY BillingCountry
ORDER BY num_inv DESC
LIMIT 3;

# Best Customer Emails #
# Build the query that returns the person who has the highest sum of all invoices,
    # along with their email, first name, and last name
SELECT Customer.Email, Customer.FirstName, Customer.LastName, SUM(Invoice.Total) as Total
FROM Customer JOIN Invoice ON Customer.CustomerID = Invoice.CustomerID
GROUP BY Customer.CustomerID
ORDER BY Total DESC
LIMIT 1;

# Promoting Rock Music #
#  Use query to return the email, first name, last name, and Genre of all Rock Music listeners!
#  Return you list ordered alphabetically by email address starting with A.
#  Can you find a way to deal with duplicate email addresses so no one receives multiple emails?
SELECT C.Email, C.FirstName, C.LastName, G.Name
FROM Customer C, Invoice I, InvoiceLine IL, Track T, Genre G
WHERE C.CustomerID = I.CustomerID AND I.InvoiceID= IL.InvoiceID
AND IL.TrackID = T.TrackID AND T.GenreID = G.GenreID AND G.Name = 'Rock'
GROUP BY C.Email
ORDER BY C.Email;

# Promotional Music Event #
#  Write a query that returns the 1 city that has the highest sum of invoice totals.
#  Return both the city name and the sum of all invoice totals.

SELECT I.BillingCity as City, SUM(I.Total) as Total
FROM Inventory I
GROUP BY City
ORDER BY Total DESC
LIMIT 1;

# Top City Favorite Music #
#  Write a query that returns the BillingCity,total number of invoices
#  associated with that particular genre, and the genre Name.

#  Return the top 3 most popular music genres for the city
#  with the highest invoice total (you found this in the previous quiz!)
SELECT I.BillingCity as City, COUNT(I.InvoiceID) as NumInvoices, G.Name as GenreName
FROM Invoice I, InvoiceLine IL, Track T, Genre G
WHERE I.InvoiceID = IL.InvoiceID AND IL.TrackID = T.TrackID AND T.GenreID = G.GenreID AND City = 'Prague'
GROUP BY GenreName
ORDER BY NumInvoices DESC
LIMIT 3;

# Getting Musicians #
#  Write a query that returns the Artist name and total track count of the top 10 rock bands.
SELECT AR.Name as Artist, COUNT(TrackID) as TotalTrack
FROM Genre G, Track T, Album AL, Artist AR
WHERE  G.GenreID = T.GenreID
AND T.AlbumID = AL.AlbumID
AND AL.ArtistID = AR.ArtistID
AND G.Name = 'Rock'
GROUP BY ArtistName
ORDER BY TotalTrack DESC
LIMIT 10;

# Heading to France #
#  Return the BillingCities in France, followed by the total number of
#  tracks purchased for Alternative & Punk music.
#  Order your output so that the city with the highest total number of
#  tracks purchased is on top.
SELECT I.BillingCity as City, COUNT(TrackID) as TotalTrack
FROM Invoice I, InvoiceLine IL, Track T, Genre G
WHERE I.InvoiceID = IL.InvoiceID
AND IL.TrackID = T.TrackID
AND T.GenreID = G.GenreID
AND G.Name = 'Alternative & Punk'
AND I.BillingCountry = 'France'
GROUP BY City
ORDER BY TotalTrack DESC;
--------------------

## Simple Guide of Five Normal Forms ##
# The normal forms defined in relational database theory represent guidelines for receord design
# The normalization rules are designed to prevent update anomalies and data incosistencies

# First Normal Form
    # All occurences of a record type must contain the same number of fields
    # First normal form excludes variable repeating fields and groups
# Second and Third Normal Forms
    # Under second and third normal forms, a non-key field must provide a fact about the key, use the whole key, and nothing but the key
        # In addition, the record must satisfy the first normal form
    # Second is violated when a non-key field is s fact about a subset of a key. It is only relevant when the key is composite, i.e., consistes of several fields
        # e.g
        -------------------------------------------------
         Part | Warehouse | Quantity | Warehouse-address
         ==================------------------------------
         # The key here is consists of the Part and Warehouse fields together, but Warehouse-address is a fact about the warehouse alone.
         # To satisfy the second normal form, the record should be decomposed into the two records:
            # one is Part, Warehouse, Quantity
            # Warehouse, Warehouse-address
        #  this technique called normalization
        # THe normalized design enhances the integrity of the data,
            # by minimizing redundancy and inconsistency,
            # but at some possible performance cost for certain retrieval applications

    # Third is violated when a non-key field is a fact about another non-key field
    # Second and third normal forms are defined in terms of functional dependenciee,
        # which correspond approx to single-valued facts
        # A field Y is "funtionally dependent" on a field (or fields) X if it is invalid to have two records
            # with the same X-value but different Y-Values
            # That is, a given X-value must always occur with the same Y-value
            # Functional Dependencies
                # e.g.
                    #  Person and Address
                        # without unique identifiers, there will not be a functional dependencies as a given name (ppl with same name) can appear with several different addresses
                        # address has to be spelled identically in each occurence in order to have functional dependencies
# Fourth and Fifth Normal Forms
    # Fourth and fifth normal forms deal with multi-valued facts
    # The multi-valued fact may correspond to a many-to-many relationship, as with employees and skills,
        # or to a many-to-one relationship, as with the children of an employee (assuming only one parent is an employee)
        # By "many-to-many" we  mean that an employee may have several skills, and a skill may belong to several employees
    # Under fourth normal form, a record type should not contain two or more independent multi-valued facts about an entity. In addition, the record must satisfy third normal form
        # e.g. employee, skill, and language
            # two many-to-many relationships, employee-skill and employee-language
            # solution: represented in the two records
        # the main problem with violating fourth normal form is that it leads to uncertainties in the maintenance policies
            # Several policies are possible for maintaining two independent multi-valued facts in one record
                # A disjoing format, in which a record contains either a skill or language, but not both
                # A random mix, with three variations:
                    # minimal number of records, with repetitions
                    # minimal number of records, with null values
                    # unrestricted
                # A "cross-product" format, where for each employee, there must be a record for every possible pairing of one of his skills with one of his language
        # If skill is associated with language, e.g. {skill: cook,language:French},{skill:type,language:French},{skill:type,language:German}, these records do not violate fourth normal form as employee-skill and employee-language are no longer independent
    # Fifth normal form deals with cases where info can be reconstructed from smaller pieces of info that can be maintained with less redundancy
        # e.g. agents, companies, and products
            # record which agent sells which product for which company, which coudld kept in one record type with three fields
            {{Agent: 'Smith', Company: 'Ford', Product:'car'},
            {Agent: 'Smith', Company: 'GM', Product:'truck'},}
            # In case a certain rule was in effect: the agent represents a company, it turns out that we can reconstruct all the true facts from a normalized form consisting of three separate record types, each containing two fields
            # Agent-Company
            {{Agent:'Smith',Company:'Ford'},{Agent:'Smith',Company:'GM'},{Agent:'John',Company:'Ford'}}
            # Company-Product
            {{Company:'Ford', Product:'car'},{Company:'Ford', Product:'truck'},
            {Company:'GM', Product:'truck'},{Company:'GM', Product:'truck'}}
            # Agent-Product
            {{Agent:'Smith',Product:'car'},{Agent:'Smith',Company:'truck'},{Agent:'John',Company:'car'}}
# The Factors Affecting Normalization
    # Single-valued vs. multi-valued facts
    # Dependency on the entire key
    # Indenpendent vs. dependent facts
    # The presence of mutual constraints
    # The presence of non-unique or non-singular representations


------------------------
## Normalized Design ##
# Every row has the same number of columns
# There is a unique 'key', and everything in a row says something about the key
    # sometimes the key is more than one column, or even all of them
    # e.g
    part_num | color | material | shape
    # part_num is the key. color, material, and shape describe the numbered parts
# Facts that don't relate to the key belong in different table
    # Non-key columns describe the key, but not descirbe other non-key columns
# Table shouldn't imply relationships that don't exist
    # employee, skill, and language example

## Create Table and Types ##
create table tablename(
    column1 type[constrains],
    column2 type[constraints],....
    [row constraints]);
# PostgreSQL has specific types for integers, booleans, bit strings, text, dates and times, IP adress,
    # geometric shapes, reals, money, XML, JSON, ranges, arrays, searchable documents,,,
# MySQL knows as much as PostgreSQL but not all, such as IP address
    # Using integers or strings to store IP address
# SQLite only knows null, integer, real, text and blob
    # store dates as strings

## Create and Drop Databases ##
create database name[options];
drop database name[options];
drop table name[options];

## Declaring Primary Keys ##
# Primary key: a column or columns that uniquely identify what each row in a table is about
# e.g.
create table students(
    id serial primary key,
    name text,
    birthdate date
    );

create table postal_places(
    postal_code text,
    country text,
    name text,
    primary key(postal_code, country
    );
    
## Declaring Relationship  ##
# To catch mistakenly inserted row which information could not be found in another table, we need to tell database that particular column should only have values that refer to the key of another table, or use 'reference' keyword when creating table as follows:
create table sales(
    sku text reference products, # if the name of column is different in another table, should be 'reference tablename(columnname)'
    sale_date date,
    count integer);
    
    # referemces provides referential integrity - columns that are supposed to refer to each other are guaranteed to do so

## Foreign Keys ##
# Foreign Key: columns with references constraints
    # column or set of columns in one table, that uniquely identifies rows in another table
    
## Self JOINs ##
# when you want to join the table to itself, e.g find which students are roommates, or need to find students who have the exact same building name and room number
create table residentces(
    id integer references students,
    building text references building(name),
    room text);

# My Answer #
SELECT a.id, b.id
FROM residences as a, residences as b
WHERE a.building = b.building
AND a.room = b.room
AND a.id != b.id
GROUP BY a.room
HAVING COUNT(a.room) = 2
ORDER BY a.building, a.room;
# Better Solution #
a.building = b.building
AND a.room = b.room
AND a.id < b.id
    
## Counting what isn't there #
# To get the database to give a count with zeron on joint table, e.g
SELECT products.name, products.sku, count(sales.sku) as num
FROM products left join sales
ON product.sku = sales.sku
GROUP BY products.sku;
# Without "left join" the query will not return product that has no sales
# However, the above query will give us a row for every product in products tables, even the ones that have no sales in the sales table
# A regular(inner) join returns only those rows where the two tables have entries matching the join condition
# A "left join" returns all those rows, plus the rows where the left table has an entry but the right table doesn't
# A "right join" does the same but for the right table

# test
SELECT programs.name, count(bugs.filename) as num
FROM program left join bugs
ON program.filename = bug.filename
GROUP BY programs.name
ORDER BY num;

## DB-API ##
# Hidden mechanism behind udacity web server makes our SQL query able to run
# Behind the web server, running python code, which connects to SQLite DB using DB-API calls
# DB-API is standard for python libraries that lets your code connect to DBs
# The standard specifies what functions you'll call to coonect to a DB, to send the queries and to get results
# Learning DB-API allows you to apply the knowledge with any DB system
# Although the details of what each DB can do are differnt, adapting python code from one to another is straightforward
# Ddatabase system and DB-API Library
    Database system |   DB-API module
    SQLite          |   sqlite3
    PostgreSQL      |   psycopg2
    ODBC            |   pyodbc
    MySQL           |   mysql.connector

## Trying Our DB-API ##
# To see how the various functions in the DB-API work, take a look at this code,
# then the results that it prints when you press "Test Run".
#
# Then modify this code so that the student records are fetched in sorted order
# by student's name.

import sqlite3

# Fetch some student records from the database.
db = sqlite3.connect("students")
c = db.cursor()
query = "select name, id from students order by name;"
c.execute(query)
rows = c.fetchall()

# First, what data structure did we get?
print "Row data:"
print rows

# And let's loop over it too:
print
print "Students names:"
for row in rows:
    print " ", row[0]
    
db.close()

## Writing Code with DB-API ##
import sqlite3

conn = sqlite3.connect("Cookies")
# if connecting to database system over a network, maight have to specify host, username, password, etc
# .connect() >> return connection object, which is good untill you close the connection
cursor = conn.cursor()
# .cursor() runs code and fetches the results
curosr.executre(
    "select host_key from cookies limit 10")
# execute the query using cursor

results = cursor.fetchall()
# fetch all the results from that query also using cursor
# .fetchone() will fetch the results one at a time using cursor
print results

conn.close()
# Close at the last


## Inserts in DB API ##
pg = psycopg2.connect('dbname=somedb')
c = pg.cursor()
c.execute("insert into name values('Jennifer Smith')")
pg.commit() # .commit trigers transaction to actually take place

# When database system gets crashed in middle of transaction, it's all rolled back
    # this principle is called "atomicity" which means a transaction happens as a whole or not at all

## Subqueries ##
# To select from result table, name the sub-query result table
# e.g. getting avg. score of players in team with the highest scores
SELECT AVG(bigscore)
FROM (SELECT max(score) as bigscore
        FROM mooseball
        GROUP BY team) as maxes;
        
## One Query Not Two ##
def lightweights(cursor):
    """Returns a list of the players in the db whose weight is less than the average."""
    cursor.execute("select players.name, players.weight from players, (select avg(weight) as avgweight from players) as av where players.weight < av.avgweight ")
    return cursor.fetchall()

# Cleaner
select name, weight
from players, (select avg(weight) as avgweight from players) as av
where weight < avgweight;

## Views ##
# A "view" is a "select" query stored in the database in a way that lets you use it like a table
# Syntax
create view viewname as select

# e.g how many students are enrolled in each course?

create view course_size as
select course_id, count(*) as num
from enrollment
group by course_id;
# other usage of view is to pick only frequently used columns from the table

### Problem Set 03 ###
## Sum Top 5 ##
# How many invoices were received by 5 countries with the highest total invoices?
SELECT sum(total)
FROM (SELECT COUNT(*) as total
FROM Invoice
GROUP BY BillingCountry
ORDER BY total DESC
Limit 5);

## Invoice Above Average ##
# Find customers whose total invoice amount is higher than the average
SELECT BillingCountry, BillingState, BillingCountry, Total
FROM Invoice,
(SELECT avg(Total) as average FROM Invoice) as avgtotal
WHERE Total > avgtotal;

## JOIN to Subquery ##
# What is the name, city, state, country, and total of customers with above average invoice totals?

SELECT FirstName, LastName, BillingCity, BillingState, BillingCountry, Total
FROM Invoice JOIN Customer JOIN
(SELECT avg(Total) as avgtotal FROM Invoice) as av
WHERE Total > avgtotal;


## Create InvoiceLine ##
CREATE TABLE InvoiceLine(
InvoiceLineId INTEGER PRIMARY KEY,
InvoiceId INTEGER,
TrackId INTEGER,
UnitPrice REAL,
Quantity INTEGER,
FOREIGN KEY(InvoiceId) REFERENCES Invoice(InvoiceId),
FOREIGN KEY(TrackId) REFERENCE Track(TrackId));


## Working with CSV's in SQLite ##
# Export data to csv from database
sqlite> .mode csv
sqlite> .output newFile.csv
sqlite> SELECT*FROM myTable;
sqlite> .exit

# Import csv into a table
sqlite3 new.db # to place csv in a new database
sqlite> CREATE TABLE myTable() # build schema
sqlite> .mode csv
sqlite> .import newFile.csv myTable

## DB API Playground ##
import sqlite3

db = sqlite3.connect("chinook.db")
c = db.cursor()

QUERY = "SELECT* FROM Invoice;"
c.execute(QUERY)
rows = c.fetchall()

print "Row data:"
print rows

print "your output:"
for row in rows:
    print " ", row[0:]

import pandas as pd
df = pd.DataFrame(rows)
print df

db.close()

## JOIN MediaType and Track ##
# How many 'Pop' songs have an 'MPEG audio file' type?

SELECT G.Name, count(T.TrackId) as Total
FROM Genre as G, Track as T, MediaType as MT
WHERE G.GenreId = T.GenreId
AND T.MediaTypeId = MT.MediaTypeId
AND G.Name = 'Pop'
AND MT.Name= 'MPEG audio file'
GROUP BY G.Name;


## Jazz Track ##
# How many unique customer have purchased a Jazz track?
SELECT G.Name, count(DISTINCT I.CustomerId) as Total # NEED TO USE DISTINCT
FROM Invoice I, InvoiceLine IL, Track T, Genre G
WHERE I.InvoiceId = IL.InvoiceId
AND IL.TrackId = T.TrackId
AND T.GenreId = G.GenreId
GROUP BY G.Name
ORDER BY Total DESC;

## Below Avg Song Lenth ##
# Which genre has the most songs of below avg. song length?

SELECT Genre.Name, count(Track.TrackId) as num
FROM Track JOIN Genre on Track.GenreId = Genre.GenreId
WHERE Track.Milliseconds < (SELECT avg(Milliseconds) from Track)
GROUP BY Genre.Name
ORDER BY num DESC
LIMIT 1;



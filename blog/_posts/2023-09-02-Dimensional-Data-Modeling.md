---
layout: post
title: "Dimensional Data Modeling"
author:
- Jason Jiang
permalink: 
---

[Home](../../../../) >> [Blog](../../../) >> Dimensional Data Modeling

<h2 id="Contents">Contents</h2>
- [Three Levels of Data Models](#Three Levels of Data Models)
    - [Two Types of Data Modeling](#Two Types of Data Modeling)
- [Dimensional Modeling](#Dimensional Modeling)
    - [Fact Tables](#Fact Tables)
    - [Dimensional Tables](#Dimensional Tables)
    - [Why implement Dimension Modeling?](#Why implement Dimension Modeling)
- [Four Steps of Designing a Dimensional Model](#Four Steps of Designing a Dimensional Model)
    - [Step 1: Select the Business Process](#Step 1: Select the Business Process)
    - [Step 2: Decide the Grain of each Business Process](#Step 2: Decide the Grain of each Business Process)
    - [Step 3: Identify the Dimensions for the Dimensional Table](#Step 3: Identify the Dimensions for the Dimensional Table)
    - [Step 4: Identify the Facts for the Dimensional Table](#Step 4: Identify the Facts for the Dimensional Table)

<h2 id="Three Levels of Data Models"><u><b>Three Levels of Data Models</b></u></h2>
There are three levels of data models, which grow increasingly complex: conceptual, logical, and physical. 

<img src="https://ars.els-cdn.com/content/image/3-s2.0-B9780124114616000083-f08-01-9780124114616.jpg" alt="Three Levels of Data Models" width="800">
- The conceptual data model represents the high-level business view.
- The logical data model is the most involved when designing the BI application. It helps us understand the details of the data, but not how it is implemented. The logical data model is used as the blueprint of what data is involved.
- The physical data model details how the data will be implemented.

<h3 id="Two Types of Data Modeling">Two Types of Data Modeling:</h3>
- ER (Entity-Relationship) Modeling: for operational Data Models (relational databases)
- Dimensional Modeling: for user access, analysis, and reporting in dimensional data models (data warehousing)

ER Modeling is used to establish the baseline operational data model, while dimensional modeling is the cornerstone to BI and DW applications. 
> ER models are used primarily for transactional processing systems (OLTP). Dimensional modeling is used primarily for BI applications (it was designed to represent data more simply in a business context than an ER model). 

<figure>
<img src="https://www.guru99.com/images/myflix_erd.png" alt="ER Model" width="880">
<figcaption style="text-align:center;">ER Model</figcaption>
</figure>

<br>

<figure>
<img src="https://learn.microsoft.com/en-us/power-bi/guidance/media/star-schema/star-schema-example1.png" alt="Dimensional Star Schema" width="880">
<figcaption style="text-align:center;">Dimensional Star Schema</figcaption>
</figure>

<br>
<hr>

<h2 id="Dimensional Modeling"><u><b>Dimensional Modeling</b></u></h2>
The data model used to store data in the **denormalized** form is called "Dimensional Modeling".
> In normalized form, data is stored in multiple tables, reducing data redundancy and inconsistency, thus achieving data integrity. In the denormalized form, data is stored in a limited number of tables (maybe a single table) to reduce querying time.

The core concept of dimensional modeling is the creation of a star schema. It is called so as the tables are arranged in the form of a star. Dimensional modeling includes facts and dimensions.

<h3 id="Fact Tables">Fact Tables:</h3>
Fact tables contain **measures or numerical data** associated with a business process (like the number of products sold). Examples:
- Inventory level
- An online sale
- A recorded exercise

The term fact represents a business measure (_what is the business process measuring?_); therefore, a fact table in dimensional modeling stores the performance measurements resulting from a business process.

Each row in a fact table is a business event that results in measurements, and each fact table represents a business process in the organization. Measurements can be:
- <u>Additive:</u> a measures that can be added across ALL dimensions.
    - Example: # of items you bought in an online store. You can add this across customer, store, product, date. It makes sense any way you aggregate.
- <u>Semi-additive:</u> measurements that can be added across SOME dimensions but NOT others.
    - Example: bank account balances. It doesn't make sense to add a bank balance across all 12 months - but you could add all customers balances for one month to get the total balance at the bank.
- <u>Non-additive:</u> measures that can’t be added across ANY dimension whatsoever.
    - Example: unit prices, ratios, temperatures.

A fact table is connected to another fact table via a common dimensional table between them; this common dimensional table is called a bridge table (a fact table can connect with a fact table directly, but it is not a wise option as it makes the model complex and difficult to understand).

<h3 id="Dimensional Tables">Dimensional Tables:</h3>
Dimensional tables store the **description or textual information** related to the business process (like who brought the products). It's an entity that establishes context for a measurement (who, what, where, why):
- Geography (Location)
- Customers
- Dates
- Product
- Employees

A dimensional table is connected to the fact table using the foreign key in the fact table (each dimension table has a primary key that is joined to its given fact table). The dimensional table is the parent table, and the fact table is the child table. 

Dimension tables have more columns and less number of rows. Dimensions describe the measurements of the fact table. For example, "customer_id" is a measurement, but we can describe its attributes further: 
- what is the name of the customer
- the address of the customer
- gender 
- etc.

<br>

<figure>
<img src="https://docs.oracle.com/cd/E41507_01/epm91pbr3/eng/epm/penw/img/i-4642ab0fn-7924.png" alt="Fact and Dimensional Tables" width="600">
<figcaption style="text-align:center;">Fact and Dimensional Tables</figcaption>
</figure>

Relevant: <a href="http://www.kimballgroup.com/wp-content/uploads/2013/08/2013.09-Kimball-Dimensional-Modeling-Techniques11.pdf" target="_blank">Kimball Dimensional Modeling PDF.</a>

<h3 id="Why implement Dimension Modeling">We already have data in ERD models,
why implement Dimension Modeling?</h3>
Dimensional models are structured for data analysis:
- Very few joins between your values and context
- Easy to update when hierarchies change
- Fast, so you can quickly slice-and-dice your data
- "Conformed Dimensions" ensures data integrity

<br>
<hr>

<h2 id="Four Steps of Designing a Dimensional Model"><u><b>Four Steps of Designing a Dimensional Model</b></u></h2>
<h3 id="Step 1: Select the Business Process">Step 1: Select the Business Process</h3>
The first step involves selecting the business process, and it should be an action resulting in output:
- <u>Business Process #1:</u> The e-Commere industry is widely known for selling and buying goods over the internet, so our first business process will be the products bought by the customers.
- <u>Business Process #2:</u> Delivery status is also one of the most important business processes in this industry. It tells us where the product is currently from. It’s dispatched from the warehouse to the customer’s given address.
- <u>Business Process #3:</u> Maintaining the inventory in order to ensure that items don’t run out of stock, how sales are going on etc.

<h3 id="Step 2: Decide the Grain of each Business Process">Step 2: Decide the Grain of each Business Process</h3>
A **grain** is a business process at a specified level. It tells us what exactly a row, in fact, a table, represents. 

All the rows in a fact table should result from the same grain. Each fact table is the result of a different grain selected in a business process. The grain should be as granular (at the lowest level) as possible.

Grains for the above business processes are:
- <u>Grain 1:</u> **Individual product of the order per row**

    We can have the grain as the products purchased by the customer, (i.e., each row of the fact table will represent all the products checked out by the customer from the cart) but suppose a customer ordered 100 products, so this will be represented as a single row. 

    Imagine how complex it will become to query such data, so we must choose a grain as granular as possible. Therefore, our grain will be an individual product ordered by a customer (i.e., one product per row). This will make the data simple and easy to query.

- <u>Grain 2:</u> **Delivery Status of individual products in the order**

    Here, the grain will be the status of an individual product shipped from the warehouse to the delivery location. 

- <u>Grain 3:</u> **Daily inventory for each product in each store**

    Here, each row will represent the daily inventory for each product in each store. It will tell the stock of that product left in the inventory and how many products have already been sold. 

<h3 id="Step 3: Identify the Dimensions for the Dimensional Table">Step 3: Identify the Dimensions for the Dimensional Table</h3>
- **Date Dimension**: This dimension table is used in almost every dimensional model as it helps monitor the business's performance with time.
<img src="https://av-eks-blogoptimized.s3.amazonaws.com/Blog191351.png" alt="Date Dimension" width="200">

- **Product Dimension**: This table will contain information regarding the product ordered.
<img src="https://av-eks-blogoptimized.s3.amazonaws.com/Blog28384.png" alt="Product Dimension" width="200">

- **Order Dimension**: This detail will contain information regarding the order.
<img src="https://av-eks-blogoptimized.s3.amazonaws.com/orderdimension50993.png" alt="Order Dimension" width="200">

- **Customer Dimension**: This dimension table will contain the customer’s information.
<img src="https://av-eks-blogoptimized.s3.amazonaws.com/blog352807.png" alt="Customer Dimension" width="200">

- **Promotion Dimension**: This table covers the promotion condition under which the product was sold. The promotion conditions include temporary sales, reduction in price, discounts, etc.
<img src="https://av-eks-blogoptimized.s3.amazonaws.com/BLog527810.png" alt="Promotion Dimension" width="200">

- **Warehouse Dimension**: This table will contain information about the different warehouses located across the country.
<img src="https://av-eks-blogoptimized.s3.amazonaws.com/Blog436184.png" alt="Warehouse Dimension" width="200">

<h3 id="Step 4: Identify the Facts for the Dimensional Table">Step 4: Identify the Facts for the Dimensional Table</h3>
Now the event depends upon the grain we select.

The selection of grain plays a vital role in the success of our dimensional model as it helps in selecting the measurements in the fact table to which further dimension tables are joined.

Since we have chosen three business processes, we will have three fact tables, but sometimes we get confused about whether an attribute should be added to the fact table or dimension table. To avoid that confusion, we will be using the following points to identify whether an attribute is a fact or dimension:
- Textual data is generally stored in dimension tables where, whereas numeric data is generally stored in the fact table (however, it CAN be stored in a fact table if required).

- Continuous valued numeric values are stored in the fact tables, whereas discrete numeric values are stored in the dimension table.
    > Discrete variables can only take on a limited number of values (fixed values like shoe size, tickets sold) while continuous variables can take on any value and any value between two values (e.g., out to an infinite number of decimal places- temperature, weight).

    > You **count** discrete data, but you **measure** continuous data.

- The values that constantly change are kept in the fact table, whereas values that remain static or change very less with time are kept in the dimensional table.

<h4><u>Fact Table 1:</u></h4>
Grain: **Individual product of the order per row**
<img src="https://cdn.analyticsvidhya.com/wp-content/uploads/2023/02/FT1.png" alt="Fact Table 1" width="600">
When we check out, the measurements that come are unit price, quantity, ordered, discount, etc., so we have added these measurements.

In this way, we add our measurements to a fact table. Weight also could have been added as a measurement, but its value remains constant therefore, we will keep it in the dimension table.

<h4><u>Fact Table 2:</u></h4>
Grain: **Delivery Status of individual products in the order**
<img src="https://cdn.analyticsvidhya.com/wp-content/uploads/2023/02/FT2.png" alt="Fact Table 2" width="600">
This fact table will tell us the delivery status of the product, i.e., the location of the product it got delivered, etc.

<h4><u>Fact Table 3:</u></h4>
Grain: **Daily inventory for each product in each store**
<img src="https://cdn.analyticsvidhya.com/wp-content/uploads/2023/02/FT3.png" alt="Fact Table 3" width="600">
Through this fact table, we will track the stock of the different products.

<h4><u>Overall Final Model:</u></h4>
<img src="https://cdn.analyticsvidhya.com/wp-content/uploads/2023/02/Final.drawio.png" alt="Fact Table 3" width="800">

<br>

**Types of Fact Tables:**
- <u>Transaction Fact Tables:</u> records a row in the table whenever there is a transaction. Here the transaction is the grain itself. The first fact table in our model is a transaction fact table in which different transactions between customers and companies are depicted.

- <u>Periodic Fact Tables:</u> record a row in the table for a definite period of time. That period of time can be daily, monthly, etc. Here the grain is the period of time we select. Example – The inventory fact table that we have taken is an example of a periodic fact table in which we will be calculating the stock of the products on a daily basis.

- <u>Accumulating Fact Tables:</u> stores predictable steps between the process’s beginning and end. Whenever a predictable step is recorded, the table is revisited and updated. Updation of a row is unique to this type of fact table only as compared to the other types of fact tables. Example: The order’s delivery status is an example of the accumulating fact table in which we have to update the product’s location whenever it reaches the desired location until it is delivered.

- <u>Factless Fact Tables:</u> records a row in the table with no numeric measurement, but that grain is important to store. This table is also used to record data that didn’t happen. Example: A table showing the products on sale which were not sold.

<br>

<br>

[Back to Top](#)
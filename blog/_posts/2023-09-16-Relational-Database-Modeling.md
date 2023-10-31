---
layout: post
title: "Relational Database Modeling"
author:
- Jason Jiang
permalink: 
---

[Home](../../../../) >> [Blog](../../../) >> Relational Database Modeling

<h2 id="Contents">Contents</h2>
- [Relational Databases (RDMBS)](#Relational Databases (RDMBS))
- [Relational Model](#Relational Model)
    - [Relational Models are Good For](#Relational Models are Good For)

<h2 id="Relational Databases (RDMBS)"><u><b>Relational Databases (RDMBS)</b></u></h2>
A relational database is a type of database that stores and provides access to data points that are related to one another. Relational databases are based on the relational model.

<figure>
<img src="https://media.licdn.com/dms/image/C4E12AQH4UAVcW20AZQ/article-inline_image-shrink_400_744/0/1616700748562?e=1704326400&v=beta&t=NvnSRW_DICaqolRSMNgPA5Ae1jjjDssXzp5sTSMKfrI" alt="Relational Model" width="400">
<figcaption style="text-align:center;">RDBMS</figcaption>
</figure>

<br>
<hr>

<h2 id="Relational Model"><u><b>Relational Model</b></u></h2>
A relational data model is a broad way to represent data and their relationships to other data. In a relational database, data is stored in a tabular format (rows and columns). Each row in the table is a record with a unique ID called the key, and connects to other tables via foreign keys. The columns of the table hold attributes of the data, and each record usually has a value for each attribute, making it easy to establish the relationships among data points.

<figure>
<img src="https://www.c-sharpcorner.com/article/sql-server-and-relational-database-part-one/Images/relational%20theory.PNG" alt="Relational Model" width="700">
</figure>

<br>

<figure>
<img src="https://theintactone.com/wp-content/uploads/2019/03/5.1-relational-dbms-model.png" alt="Relational Model" width="600">
<figcaption style="text-align:center;">Relational Model</figcaption>
</figure>

<br>

<figure>
<img src="https://miro.medium.com/v2/resize:fit:1400/1*qrzkvp4BjaozDQ69CtZTJQ.png" alt="Relational Model" width="800">
<figcaption style="text-align:center;">Physical Data Model Example</figcaption>
</figure>

Relational models themselves don’t necessarily give data teams the best way to scale their data models because of their focus on relationships and not business logic or use cases. Instead, it offers a foundation to build more robust relational modeling processes, such as dimensional modeling, to establish data models that scale in an organized and repeatable manner.

<h3 id="Relational Models are Good For">Relational Models are Good For:</h3>
- Low volume data and a small number of data sources.
- Simple use cases for the data.
- Low-medium concern around data warehousing costs (because relational models often need joining to be made meaningful).
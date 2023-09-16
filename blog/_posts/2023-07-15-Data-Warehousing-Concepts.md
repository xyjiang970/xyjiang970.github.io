---
layout: post
title: "Data Warehousing Concepts"
author:
- Jason Jiang
permalink: 
---

[Home](../../../../) >> [Blog](../../../) >> Data Warehousing Concepts

<h2 id="Contents">Contents</h2>
- [What is a Data Warehouse?](#What is a Data Warehouse?)
- [How is a Data Warehouse Architected?](#How is a Data Warehouse Architected?)
    - [Inside a Data Warehouse](#Inside a Data Warehouse)
- [Data Warehouses, Databases, Data Lakes](#Data Warehouses, Databases, Data Lakes)
    - [Data Warehouse vs Data Lake](#Data Warehouse vs Data Lake)
    - [Data Warehouse vs Database](#Data Warehouse vs Database)
    - [OLAP vs OLTP](#OLAP vs OLTP)
        - [When to Use OLAP vs OLTP](#When to Use OLAP vs OLTP)
- [Data Marts](#Data Marts)
    - [Data Warehouse vs Data Mart](#Data Warehouse vs Data Mart)

<h2 id="What is a Data Warehouse?"><u><b>What is a Data Warehouse?</b></u></h2>
A data warehouse is a central repository of information that can be analyzed to make more informed decisions. Data flows into a data warehouse from transactional systems, relational databases, and other sources, typically on a regular cadence. Business analysts, data engineers, data scientists, and decision makers access the data through business intelligence (BI) tools, SQL clients, and other analytics applications.

<h2 id="How is a Data Warehouse Architected?"><u><b>How is a Data Warehouse Architected?</b></u></h2>
A data warehouse architecture is made up of tiers:
- The top tier is the _front-end client_ that presents results through reporting, analysis, and data mining tools.
- The middle tier consists of the _analytics_ engine that is used to access and analyze the data. 
- The bottom tier of the architecture is the _database server_, where data is loaded and stored. 

Data is stored in two different types of ways:
1. Data that is accessed _frequently_ is stored in a very fast storage (like SSD drives)
2. Data that is _infrequently_ accessed is sotred in a cheap object store, like Amazon S3. 

The data warehouse will automatically make sure that frequently accessed data is moved into the "fast" storage so query speed is optimized.

<h3 id="Inside a Data Warehouse">Inside a Data Warehouse:</h3>
A data warehouse may contain multiple databases. 
- Within each database, data is organized into tables and columns. 
    - Within each column, you can define a description of the data such as integer, data field, or string. Tables can be orgainzed inside of schemas (which can be though of as folders). 

When data is ingested, it is stored in various tables described by the schema. Query tools use the schema to determine which data tables to access and analyze.

<br>
<hr>

<h2 id="Data Warehouses, Databases, Data Lakes"><u><b>Data Warehouses, Databases, Data Lakes</b></u></h2>
Typically, businesses use a combination of a database, a data lake, and a data warehouse to store and analyze data. 

As the volume and variety of data increases, it's advantageous to follow one or more common patterns for working with data across your database, data lake, and data warehouse.

![Data Lake to Data Warehouse to Reporting](https://d1.awsstatic.com/diagrams/product-page-diagrams/database-seo-1.270cb06b819915c5f763a0b9f88255e044c4dac5.png)
*Land data in a database of datalake, prepare the data, move selected data into a data warehouse, and then perform reporting.*

![Data Warehouse to Analysis and ML](https://d1.awsstatic.com/diagrams/product-page-diagrams/product-page-diagram_Data-Warehousing_Use-Case-2.ab2ec085dd9c5f03b1d6a0732ec31d487c4f3e8f.png)
*Land data in a data warehouse, analyze the data, then share data to use with other analytics and machine learning services.*

A **data warehouse** is specifically designed for data analytics, which involves reading large amounts of data to understand relationships and trends across the data. A **database** is used to capture and store data, such as recording details of a transaction.

A **data lake** is a centralized repository for all data, including structured (cell phone numbers, email addresses, serial numbers), semi-structured (XML, TCP/ IP packets, web pages), and unstructured (text, video and audio files, images and digital photographs).
> <u>Structured data</u> is: quantitative (numerical), ordered and fact-based, organized using predetermined formats/ data models, stored in data warehouses or relational databases, and easy to search using SQL. 

> <u>Unstructured data</u> is: qualitative, disorgainzed and subjective (not organized using predefined formats or data models), stored in its native formats in applications, data lakes, or non-relational databases, and extremely difficult to search.

A warehouse requires that the data be organized in a tabular format, which is where the schema comes into play. The tabular format is needed so that SQL can be used to query the data. But not all applications require data to be in tabular format. Some applications, like big data analytics, full text search, and machine learning, can access data even if it is ‘semi-structured’ or completely unstructured.

<h3 id="Data Warehouse vs Data Lake">Data Warehouse vs Data Lake:</h3>
<table>
  <tr>
    <th>Characteristics</th>
    <th>Data Warehouse</th>
    <th>Data Lake</th>
  </tr>
  <tr>
    <td>Data</td>
    <td>Relational data from transactional systems, operational databases, and line of business applications</td>
    <td>All data, including structured, semi-structured, and unstructured</td>
  </tr>
  <tr>
    <td>Schema</td>
    <td>Often designed prior to the data warehouse implementation but also can be written at the time of analysis <br><br> (schema-on-write or schema-on-read)</td>
    <td>Written at the time of analysis (schema-on-read)</td>
  </tr>
  <tr>
    <td>Price/Performance</td>
    <td>Fastest query results using local storage</td>
    <td>Query results getting faster using low-cost storage and decoupling of compute and storage</td>
  </tr>
  <tr>
    <td>Data quality</td>
    <td>Highly curated data that serves as the central version of the truth</td>
    <td>Any data that may or may not be curated (i.e. raw data)</td>
  </tr>
  <tr>
    <td>Users</td>
    <td>Business analysts, data scientists, and data developers</td>
    <td>Business analysts (using curated data), data scientists, data developers, data engineers, and data architects</td>
  </tr>
  <tr>
    <td>Analytics</td>
    <td>Batch reporting, BI, and visualizations</td>
    <td>Machine learning, exploratory analytics, data discovery, streaming, operational analytics, big data, and profiling</td>
  </tr>
</table>


<h3 id="Data Warehouse vs Database">Data Warehouse vs Database:</h3>
<table>
  <tr>
    <th>Characteristics</th>
    <th>Data Warehouse</th>
    <th>Transactional Database</th>
  </tr>
  <tr>
    <td>Suitable workloads</td>
    <td>Analytics, reporting, big data</td>
    <td>Transaction processing</td>
  </tr>
  <tr>
    <td>Data source</td>
    <td>Data collected and normalized from many sources</td>
    <td>Data captured as-is from a single source, such as a transactional system</td>
  </tr>
  <tr>
    <td>Data capture</td>
    <td>Bulk write operations typically on a predetermined batch schedule</td>
    <td>Optimized for continuous write operations as new data is available to maximize transaction throughput</td>
  </tr>
  <tr>
    <td>Data normalization</td>
    <td>Denormalized schemas, such as the Star schema or Snowflake schema</td>
    <td>Highly normalized, static schemas</td>
  </tr>
  <tr>
    <td>Data storage</td>
    <td>Optimized for simplicity of access and high-speed query performance using columnar storage</td>
    <td>Optimized for high throughout write operations to a single row-oriented physical block</td>
  </tr>
  <tr>
    <td>Data access</td>
    <td>Optimized to minimize I/O and maximize data throughput</td>
    <td>High volumes of small read operations</td>
  </tr>
</table>

<h3 id="OLAP vs OLTP">OLAP vs OLTP:</h3>
Online analytical processing (OLAP) and online transaction processing (OLTP) are data processing systems that help you store and analyze business data. You can collect and store data from multiple sources—such as websites, applications, smart meters, and internal systems. 

OLAP combines and groups the data so you can analyze it from different points of view. Typically, this data is from a data warehouse, data mart or some other centralized data store. OLAP is ideal for data mining, business intelligence and complex analytical calculations, as well as business reporting functions like financial analysis, budgeting and sales forecasting.

Conversely, OLTP stores and updates transactional data reliably and efficiently in high volumes. OLTP systems are behind many of our everyday transactions, from ATMs to in-store purchases to hotel reservations. OLTP uses a relational database that can do the following:
- Process a large number of relatively simple transactions — usually insertions, updates and deletions to data.
- Enable multi-user access to the same data, while ensuring data integrity.
- Support very rapid processing, with response times measured in milliseconds.
- Provide indexed data sets for rapid searching, retrieval and querying.
- Be available 24/7/365, with constant incremental backups.

OLTP databases can be _one among several data sources_ **for** an OLAP system. Many OLAP systems pull their data **from** OLTP databases via an ETL pipeline.

<h4 id="When to Use OLAP vs OLTP"><u>When to Use OLAP vs OLTP:</u></h4>
Online analytical processing (OLAP) and online transaction processing (OLTP) are two different data processing systems designed for different purposes.

OLAP is optimized for complex data analysis and reporting, while OLTP is optimized for transactional processing and real-time updates.
> OLAP's multidimensional schema is well suited for complex queries that draw from multiple data sets, such as historical and current data. An OLTP system stores transaction data in a relational database, optimized to handle the large volumes of transactional data funneled into this system. 

<br>

**Summary of Differences: OLAP vs OLTP**
<table>
  <tr>
    <th>Criteria</th>
    <th>OLAP</th>
    <th>OLTP</th>
  </tr>
  <tr>
    <td>Purpose</td>
    <td>OLAP helps you analyze large volumes of data to support decision-making.</td>
    <td>OLTP helps you manage and process real-time transactions.</td>
  </tr>
  <tr>
    <td>Data source</td>
    <td>OLAP uses historical and aggregated data from multiple sources.</td>
    <td>OLTP uses real-time and transactional data from a single source.</td>
  </tr>
  <tr>
    <td>Data structure</td>
    <td>OLAP uses multidimensional (cubes) or relational databases.</td>
    <td>OLTP uses relational databases.</td>
  </tr>
  <tr>
    <td>Data model</td>
    <td>OLAP uses star schema, snowflake schema, or other analytical models.</td>
    <td>OLTP uses normalized or denormalized models.</td>
  </tr>
  <tr>
    <td>Volume of data</td>
    <td>OLAP has large storage requirements. Think terabytes (TB) and petabytes (PB).</td>
    <td>OLTP has comparatively smaller storage requirements. Think gigabytes (GB).</td>
  </tr>
  <tr>
    <td>Response time</td>
    <td>OLAP has longer response times, typically in seconds or minutes.</td>
    <td>OLTP has shorter response times, typically in milliseconds</td>
  </tr>
  <tr>
    <td>Example applications</td>
    <td>OLAP is good for analyzing trends, predicting customer behavior, and identifying profitability.</td>
    <td>OLTP is good for processing payments, customer data management, and order processing.</td>
  </tr>
</table>

<br>
<hr>

<h2 id="Data Marts"><u><b>Data Marts</b></u></h2>
A data mart is a data warehouse that serves the needs of a specific team or business unit, like finance, marketing, or sales. It is smaller, more focused, and may contain summaries of data that best serve its community of users. A data mart might be a portion of a data warehouse, too.
<h3 id="Data Warehouse vs Data Mart">Data Warehouse vs Data Mart:</h3>
<table>
  <tr>
    <th>Characteristics</th>
    <th>Data Warehouse</th>
    <th>Data Mart</th>
  </tr>
  <tr>
    <td>Scope</td>
    <td>Centralized, multiple subject areas integrated together</td>
    <td>Decentralized, specific subject area</td>
  </tr>
  <tr>
    <td>Users</td>
    <td>Organization-wide</td>
    <td>A single community or department</td>
  </tr>
  <tr>
    <td>Data source</td>
    <td>Many sources</td>
    <td>A single or a few sources, or a portion of data already collected in a data warehouse</td>
  </tr>
  <tr>
    <td>Size</td>
    <td>Large, can be 100's of gigabytes to petabytes</td>
    <td>Small, generally up to 10's of gigabytes</td>
  </tr>
  <tr>
    <td>Design</td>
    <td>Top-down</td>
    <td>Bottom-up</td>
  </tr>
  <tr>
    <td>Data detail</td>
    <td>Complete, detailed data</td>
    <td>May hold summarized data</td>
  </tr>
</table>

<br>
<br>
<br>

[Back to Top](#)
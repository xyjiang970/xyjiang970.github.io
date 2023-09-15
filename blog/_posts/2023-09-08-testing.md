---
layout: post
title: "Data Warehouse: Designing a Data Model for Ride Sharing or Taxi Services"
author:
- Jason Jiang
permalink: 
---

## Kimball Group: Four-Step Dimensional Design Process
1. Select the business process.
2. Declare the grain.
3. Identify the dimensions.
4. Identify the facts. 

Reference from <em><a href="https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/four-4-step-design-process/" target="_blank">Kimball Group Resources</a></em>.

## 1. Sample Problem Statement (Business Process)
A taxi company would like to design a data model to capture all critical data elements of the journey including:
- Tracking rides done by the driver and their performance.
- Daily number of rides to popular destinations.
- Daily number of cancelled trips.
- Daily number of rides during peak hours (and the prices).

## 2. Data Warehouse Solution:
- <u>Grain:</u> Individual trips on a transactional level.
>The grain is the business definition of what a single fact table record represents.

- <u>Dimensions:</u> Date, Customers, Drivers, Cars, Documents, Devices, Locations.
> Provides context and background information (e.g. time and products).

- <u>Facts:</u> Trips, Payments
> Fact tables are the foundation of the data warehouse. They contain the fundamental measurements of the enterprise, and they are the ultimate target of most data warehouse queries. The real purpose of the fact table is to be the repository of the **numeric** facts that are observed during the measurement event (e.g. transactions in amounts and quantities). It is critically important for these facts to be true to the grain.

### 2a. Star Schema
A star schema is a multi-dimensional data model used to organize data in a database so that it is easy to understand and analyze. They can be applied to data warehouses, databases, data marts, and other tools. The star schema design is optimized for querying large data sets. 

<img src="https://www.researchgate.net/publication/277060637/figure/fig2/AS:359444044107779@1462709546739/The-retail-sales-star-schema-example-from-Kimball-02.png" alt="">

Star Schemas *denormalize* data - which means adding redundant columns to some dimension tables to make querying and wokring with the data faster and easier. 

The purpose is to trade some redundancy (duplication of data) in the data model for increased query speed, by avoiding computationally expensive join operations.


<br>

**[TO BE CONTINUED...]**
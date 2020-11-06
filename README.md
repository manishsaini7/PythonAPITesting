# API Testing of Ecommerce Website using Python
This Repo is about Automation Testing of Ecommerce Website using Rest APIs with Python

Framework Used : PyTest

Python Packages Used : pytest
                       PyMySQL
                       WooCommerce
                       pytest
                       pytest-html
                       requests
                       requests-oathlib
                       
Web Server Used : Local   
                  https://localwp.com/
                  
Database Used : MySQL

Website : WordPress Website with Woo Commerce Plugin

API Used : Woo Commerce REST APIs
           https://woocommerce.github.io/woocommerce-rest-api-docs
           
Test cases covered :
---- Customers ----
-
TCID29 - Create Customer and verify it.
TCID30 - List All Customers
TCID47 - Create Customer with Existing Email(Negative Testcase)
---- Products ----
-
TCID24 - Get All Products
TCID25 - Get product by product ID
TCID26 - Create Simple Product
TCID51 - List product with filter 'after'
---- Orders ----
-
TCID48 - Place order with Guest User
TCID49 - Place order with New User
TCID55 - Update order status 'Cancelled'
TCID56 - Update order status 'Completed'
TCID57 - Update order status 'On-hold'




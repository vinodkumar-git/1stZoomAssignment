# 1stzoom_assignment
Create a python program which will take a name of product(String) as input and will generate 20 products which are similar(see below for understanding similar) to the input which you have provided. The input String may or may not be from CSV file. The top 20 suggestions should be from the CSV file and sorted in the order they are similar with the provided input. 
Definition of similar-Please see below examples for better understanding of word similar used above. 

       Input String               Output 

a.  Cheese                       Amul cheese, Go cheese & 18 more strings 

b.  Aml Cheese                Amul cheese, Amul cheese and milk & 18 more 

c.  Aml chs                      Amul cheese, Anmol cheese & 18 more 

In nutshell consider google search engine which can do similar suggestions along with autocorrection if needed. 

Assignment Judging Criteria- We will provide a name of product as input and based on your top 20 suggestions and the algorithm used, we will judge it. 

PS- Use python related libraries. Don't use any search engine library. You have to use Django for creating application.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

Deploying Procedure: (On Ubuntu)
----------------------------------
1. Create an virtualenv. cmd = virtualenv env
2. Activate virtualenv cmd = source env/bin/activate. Traverse to the project directory where you can find requirements.txt file. Install requirements mentioned using cmd = pip3 install -r requirements.txt
3. After installation, Open 1stzoom_assignment folder path which has manage.py file using cd command.
4. Run cmd = python3 manage.py runserver
5. open localhost link in the browser and you will be shown an upload page.

NOTE - I have added 10k items from the csv file given. To add the entire csv file, you can direct upload it by clicking upload file in the application. *Will take few mins*

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Methods:
------------------------------
1. Built with Python3, Django3 framework, SQLite3, Bootstrap4
2. Web application consists of 2 web pages ie., upload page and search page.
3. Upload page - One can upload a csv file and the file contents are saved. (CSV file with huge data take some time to upload and save the data).
4. Search Page - After uploading csv file, we can search products using search page.
5. Based on the search request, results are shown. 

     
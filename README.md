# Elasticsearch 

Elasticsearch can be used to search all kinds of documents. It provides scalable search, has near real-time search, and supports multitenancy. "Elasticsearch is distributed, which means that indices can be divided into shards.

Source for DATA :- Data is already loaded on Elasticsearch.

Problem Statement:- To develop a auto-correction system using Elasticsearch based on user input.

 - I have Created a elasticQuery.py file in which I am applying query and the backend processes which will fetch the appropriate result from the DataSet depending on the characters input.
 
 - And also a python file name app.py responsible for taking ajax call and also provide the result back to the frontend.

 - And an templates directory consisting home.html which is responsible for providing User friendly Environment for input and output
 
 - Command to execute elasticQuery.py is :-
```sh
$ python elasticQuery.py
```
 - Command to execute app.py is :-
```sh
$ python app.py
```

OutPut Image :- 
<img src=outputImages/image-1.png>

OutPut Image :- 
<img src=outputImages/image-2.png>

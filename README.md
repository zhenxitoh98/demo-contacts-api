
# demo-contacts-api 
This API is written using the Flask framework. The database used is SQLite. It is currently live on https://demo-contacts-api-samuel.herokuapp.com/.

### Different URLs to run
 1) To see details of everyone: https://demo-contacts-api-samuel.herokuapp.com/
 2) To see contacts of everyone: https://demo-contacts-api-samuel.herokuapp.com/all_contacts/
 3) To see all information of Ultron: https://demo-contacts-api-samuel.herokuapp.com/contacts/?name=Ultron

#  Steps to run the files locally on Mac:
1) Download the files from this repo
2) `cd` into the folder
3) Run `pip3 install virtualenv` in the terminal
4) Run `sudo /usr/bin/easy_install virtualenv` in the terminal
5) Run `virtualenv flask` in the terminal
6) Run `flask/bin/pip install -r requirements.txt` in the terminal
7) Run `chmod a+x app.py` in the terminal
8) Run `./app.py` in the terminal
9) Copy the url from the terminal into a browser

### To POST to the people API:
1) Run `curl -i -H "Content-Type: application/json" -X POST -d '{"name":"Ultron", "age":29, "height":155}' http://127.0.0.1:5000/people/` in a new terminal

### To POST to the contacts API:
1) Run `curl -i -H "Content-Type: application/json" -X POST -d '{"email":"ultron@avengers.com", "number":"0198345212"}' http://127.0.0.1:5000/people/1/contacts/` in a new terminal

### To GET data from the API:
1) Run `curl -i http://127.0.0.1:5000/contacts/?name=Ultron` in a new terminal

#### Note: If you don't have `curl`, install it here: https://curl.haxx.se/. You can also use https://www.postman.com/ to POST and GET data.

#### The API will output 201 if POST successfully to the API, 500 if data is already in the API, and 200 if successfully GET the data from the API.

# Demo video:
https://drive.google.com/file/d/1sVimuHXnstQGeq5kqcTwnpuA_GdMY83j/view


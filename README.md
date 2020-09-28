
# demo-contacts-api 
Currently live on https://demo-contacts-api-samuel.herokuapp.com/
### Different URLs to run
 1) To see details of everyone: https://demo-contacts-api-samuel.herokuapp.com/
 2) To see details of user ID 1: https://demo-contacts-api-samuel.herokuapp.com/people/1
 3) To see contacts of everyone: https://demo-contacts-api-samuel.herokuapp.com/all_contacts/
 4) To see contacts of user ID 1: https://demo-contacts-api-samuel.herokuapp.com/people/1/contacts/

#  Steps to run the files locally:
1) Download the files from this repo
2) `cd` into the folder
3) Run `virtualenv flask` in the terminal
4) Run `flask/bin/pip install -r requirements.txt` in the terminal
5) Run `chmod a+x app.py` in the terminal
6) Run `./app.py` in the terminal
7) Copy the url from the terminal into a browser

### To POST to the people API:
1) Run `curl -i -H "Content-Type: application/json" -X POST -d '{"name":"Ultron", "age":29, "height":155}' http://127.0.0.1:5000/people/<int:id>/` in a new terminal

### To GET data from the people API:
1) Run `curl -i http://127.0.0.1:5000/people/<int:id>/` in a new terminal

### To POST to the contacts API:
1) Run `curl -i -H "Content-Type: application/json" -X POST -d '{"email":"ultron@avengers.com", "number":"0198345212"}' http://127.0.0.1:5000/people/<int:id>/contacts/` in a new terminal

### To GET data from the contact API:
1) Run `curl -i http://127.0.0.1:5000/people/<int:id>/contacts/` in a new terminal

#### Note: Replace `<int:id>` with the user ID. If you don't have `curl`, install it here: https://curl.haxx.se/. You can also use https://www.postman.com/ to POST and GET data.




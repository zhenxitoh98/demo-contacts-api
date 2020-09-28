
# demo-contacts-api 
Currently live on https://demo-contacts-api-samuel.herokuapp.com/

#  Steps to run 
1) Download the files from this repo
2) `cd` into the folder
3) Run `virtualenv flaks` in the terminal
4) Run `flask/bin/pip install -r requirements.txt` in the terminal
5) Run `chmod a+x app.py` in the terminal
6) Run `./app.py` in the terminal
7) Copy the url from the terminal into a browser

### To POST data to the API
1) Run `curl -i -H "Content-Type: application/json" -X POST -d '{"name":"Captain America", "age":45, "height":190}' http://127.0.0.1:5000/people/<int:id>/` in a new terminal


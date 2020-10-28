# 30 Days Gcloud Dashboard

### Under development

### Instructions to run

* Install Requirements

    ```
    pip3 install -r requirements.txt
    ```

* Install npm packages

    ```
    cd frontend
    npm install
    ```

 * Create the database by running main.py in scrapper
   
    ```
    cd scraper
    python3 main.py
    ```

 * Create flask app 

    ```
    cd backend
    export FLASK_APP=server.py
    ```
  
 * Run flask app

   ```
   cd backend
   flask run
   ```
	  
* Go to http://localhost:5000 to get the json response
    
* Run Frontend

    ```
    cd frontend
    npm run serve
    ```

* Go to http://localhost:8080/

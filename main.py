from fastapi import FastAPI
from postgres_connect import *

app=FastAPI()
@app.get("/temperature/{tem}")
def update_db(tem):
    sql="INSERT INTO tem_data(temperature_celcius) VALUES("+str(tem)+")"
    runquery(sql)
    return {'msg':"Inserted successfully"}

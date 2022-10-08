from flask import Flask
from housing.logger import logging
import sys
from housing.exception import HousingException

app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    logging.info("We are testing logging module")
    try:
        raise Exception("We are testing custom exception")
    except Exception as e:
        housing = HousingException(e, sys)
        logging.info(housing.error_message)
        
    return "Starting Machine Learning Project"


if __name__=="__main__":
    app.run()
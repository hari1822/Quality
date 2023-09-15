import pickle
from flask import Flask, render_template, request , jsonify,g
import joblib
#from pyfirmata import Arduino, util
import numpy as np
import serial
import subprocess


app= Flask(__name__)
model = joblib.load(open("rf.pkl", "rb"))



@app.route("/")

def index():

 return render_template("templates/index.html")


@app.route("/predict", methods=["GET","POST"])

def predict():

     try:
       
          

       #init=[int(x) for x in request.form.values()]
       #final=[np.array(init)]
    
       
     

      #predictt= model.predict(request.json)
      
       prediction=model.predict([[int(x) for x in request.form.values()]])
       g.output=round(prediction[0],2)
       y=int(g.output)
       


      
    
       if(g.output==1):
         print(y)
        

        
         return render_template("index.html",pt=f"product is ok",prediction_text=f"{g.output}")
       elif(g.output==0):
         print(y)
         command='python led.py'
         e = subprocess.run(command,stdout=subprocess.PIPE,shell=True,universal_newlines=True).stdout
         print(e)
         return render_template("index.html",pt=f"product is rejected",prediction_text=f"{g.output}")  
    


     
     
        
     except:
        return render_template("index.html",prediction_text=f"Invalid input")
        
        


          


if __name__ == "__main__":
    app.run(debug=True)

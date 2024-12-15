from flask import Flask,render_template,redirect,session,send_file,send_from_directory,request
import requests
import socket
from pymongo import MongoClient
import os
import mimetypes

app = Flask(__name__)
app.secret_key = 'your_random_and_secure_secret_key'

@app.route('/',methods=['GET','POST'])
def index():
    
    if request.method == "GET":
        return render_template('index.html')
        
    elif request.metod == "POST":
        return 'post'
    else:
        redirect('./')
@app.route('/download',methods=['GET'])
def download_area():
   if session.get('file_name'):
       return  render_template('download.html')
   else:
       return redirect('/')
@app.route('/download_file',methods=['POST'])
def download_file():
    
    if request.method == "POST":
        if session.get('file_name'):
            
            file_name = session.get('file_name')
            session.pop('file_name')
            
            return send_file(file_name,as_attachment=True)
            
            
        else:
            
            return redirect('/')
    else:
        return redirect('/')
        
   
   

@app.route('/save_file',methods =['POST'])
def write_the_file():
    
 if request.method == "POST":
    try:
            response = requests.get(request.form.get('ip'))
            if response.status_code == 200:
                url_name = request.form.get('ip').split('/')[2]
            
                with open(url_name + '.html','w',encoding='utf-8') as file:
                        file.write( '<!-- NETRAY SOLUTIONS  -->' + response.text)
                session['file_name'] =   url_name + '.html'
                return redirect('/download')
            
            else:
                print('error on else')
                return redirect('/')
      
    except Exception as e:
        print(e)
        return redirect('/')
 else:
     return redirect('/')
     

app.run('0.0.0.0',debug=True,port=5600)
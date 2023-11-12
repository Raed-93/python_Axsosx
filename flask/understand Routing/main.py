# from flask import Flask  
# app = Flask(__name__)    
# @app.route('/')          
# def hello_world():
#     return 'Hello World!'  
# if __name__=="__main__":     
#  app.run(debug=True)    

#2

# 
# from flask import Flask  
# app = Flask(__name__)    
# @app.route('/dojo')          
# def hello_world():
#     return 'Hello World!'  
# if __name__=="__main__":   
#  app.run(debug=True)    

#3

# from flask import Flask  
# app = Flask(__name__)    
# @app.route('/say/<name>')          
# def hello_world(name):
#     print(name)
#     return 'say,' + name  
# if __name__=="__main__":   
#  app.run(debug=True)    


#4
# from flask import Flask
# app=Flask(__name__)

# @app.route('/repeat/<int:times>/<word>')
# def repeat_word(times, word):
#     return f'{word} ' * times

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)
 



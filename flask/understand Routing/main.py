# from flask import Flask  # Import Flask to allow us to create our app
# app = Flask(__name__)    # Create a new instance of the Flask class called "app"
# @app.route('/')          # The "@" decorator associates this route with the function immediately following
# def hello_world():
#     return 'Hello World!'  # Return the string 'Hello World!' as a response
# if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
#  app.run(debug=True)    # Run the app in debug mode.

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









from flask import Flask
app=Flask(__name__)
@app.route('/repeat/<int:times>/<word>')
def repeat_word(times, word):
    return f'{word} ' * times

if __name__ == '__main__':
    app.run(debug=True, port=5000)
 
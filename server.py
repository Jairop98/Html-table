from  flask import Flask, render_template # Import Flask to allow us to create our app + added render_template

app = Flask(__name__) # Create a new instance of the Flask class called 

@app.route('/')  # The "@" decorator associates this route with the function immediately following
def index():
    users_info = [ #lists
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]    # returns the result of the render_template method, passing in the name of index.html
    return render_template("index.html", users=users_info) #renaming users_info to users

if __name__=="__main__": # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)     # Run the app in debug mode


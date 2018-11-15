from flask import Flask
from flask import render_template
from database import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR-VERY-SECRET-SHHH'

@app.route('/', methods=["GET","POST"])
def catbook_home():
    if request.method=="get":
        
        cats = get_all_cats()
        return render_template("home.html", cats=cats)
    else:
        name=request.form["name"]
        create_cat(name)
        return render_template("home.html")
@app.route("/cats/<int:id>")
def cat(id):
    my_cat=byid(id)    
    return render_template("cat.html", my_cat=my_cat)
if __name__ == '__main__':
   app.run(debug = True)

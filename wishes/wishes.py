from flask import *

app=Flask(__name__)

@app.route('/ ') #form that will allow user to key in their input
def input():
    return render_template("wishes.html")

if __name__=='__main__' :
    app.run(debug=True,port=6754)


from flask import *

app = Flask(__name__)

@app.route('/setcookie',methods = ['POST'])
def cookie_set():
    if request.method == 'POST':
        user = request.form['nm']
        res = make_response(render_template("cookietemplate.html"))
        res.set_cookie('userId',user)
    return res

@app.route('/success')
def page_redirect():
    userId = request.cookies.get('userId')
    return "user_name: %s" % userId

if __name__ == "__main__":
    app.run(debug=True)

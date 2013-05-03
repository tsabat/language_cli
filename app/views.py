from app import app
from app import request
from app.parser import parse

@app.route('/')
def hello():
    return """
    <form name="form" action="/render" method="POST" >
        <textarea name="code" rows="50" cols="80" ></textarea>
        <input type="submit" value="Submit">
    </form>
    """

@app.route('/render', methods=['POST'])
def route():
    return '<pre>' + parse(request.form['code']) + '</pre>'

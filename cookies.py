from flask import Flask, request, make_response

app = Flask(__name__)
app.config['Debug'] = True

@app.route('/')
def index():
    count = int(request.cookies.get('visit-count',0))
    count += 1
    message = 'You have visited this page ' + str(count) + 'times'

    resp = make_response(message)
    resp.set_cookie('visit-count', str(count))
    return resp

app.run(port=5002)

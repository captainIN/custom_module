from trytond.wsgi import app

@app.route('/hello', methods=['GET'])
def hello(request):
    return "Hello world"
from app import app
@app.route('/underlords')
def index():
    return "Soon."
@app.route('/underlords/test')
def indexTest():
    return "test"

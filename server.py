from flask import Flask, url_for, send_from_directory, send_file
app = Flask(__name__, static_url_path='')

@app.route('/predictions')
def get_predictions():
    return send_file('predictions.png', mimetype='image/png')

@app.route('/cam')
def get_cam():
    return send_file('cam.png', mimetype='image/png')

@app.route('/counted')
def get_restaurant():
    return send_file('counted.txt')

if __name__ == "__main__":
    app.run()
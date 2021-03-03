import flask
from flask import jsonify

app = flask.Flask(__name__)

# route health_check
@app.route('/health_check', methods=['GET'])
def health_check():
  return jsonify({'hello': 'world'})

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=3000)

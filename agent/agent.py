from gevent import monkey; monkey.patch_all()
from flask import Flask, json, jsonify
from config import Configuration

app = Flask(__name__)
config = Configuration()

@app.route('/')
def hello_world():
    from metrics import METRICS
    return jsonify(**METRICS)

#@app.route('/user/<username>')
#def show_user_profile(username):
#    # show the user profile for that user
#    return 'User %s' % username
#return jsonify(username=g.user.username,
#                   email=g.user.email,
#                   id=g.user.id)


if __name__ == '__main__':
    from metrics import metrics_processor
    from drivers import driver_list
    metrics_processor(driver_list())
    app.run(debug=True, host='0.0.0.0', port=9000)
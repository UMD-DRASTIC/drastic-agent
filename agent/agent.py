from flask import Flask, json, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    metrics = {
        "storage": {
            "cassandra": {
                "total": -1,
                "used": -1
            },
            "disk": {
                "total": 500,
                "used": 250
            }
        }
    }
    return jsonify(**metrics)

#@app.route('/user/<username>')
#def show_user_profile(username):
#    # show the user profile for that user
#    return 'User %s' % username
#return jsonify(username=g.user.username,
#                   email=g.user.email,
#                   id=g.user.id)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9000)
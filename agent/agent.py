import os
from datetime import datetime

from gevent import monkey; monkey.patch_all()
from flask import Flask, json, jsonify, render_template, request, Response
from config import Configuration

app = Flask(__name__)
config = Configuration()

from indigo.models import initialise, Resource
initialise("indigo")


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/metrics')
def metrics():
    from metrics import METRICS
    return jsonify(**METRICS)

@app.route('/get/<path:path>', methods=['GET'])
def get(path):
    root = config.get_driver_settings("DISK")['ROOT']
    fullpath = os.path.join(root, path)

    def generate(p):
        chunk_size = 1024 * 1024 * 1
        with open(p, 'r') as f:
            while True:
                data = f.read(chunk_size)
                if not data:
                    break
                yield data

    return Response(generate(fullpath))

@app.route('/notify', methods=['POST'])
def notify():
    from events import EVENTS, handle_event
    errors = []

    resource = Resource.find_by_id(request.form['resource'])

    success = True
    if not resource:
        errors.append("Could not find resource")
        success = False

    if not request.form['event'] in EVENTS:
        errors.append("Unknown event type")
        success = False

    if success:
        handle_event(resource, request.form['event'])

    return jsonify(success=success,
                   input=request.form,
                   errors=errors,
                   resource=resource.to_dict() if resource else {},
                   timestamp=datetime.now().isoformat())


@app.route('/notify/test')
def notify_test():
    return render_template('test.html')

if __name__ == '__main__':
    from metrics import metrics_processor
    from drivers import driver_list
    metrics_processor(driver_list())
    app.run(debug=True, host='0.0.0.0', port=9000)
from gevent.wsgi import WSGIServer
from agent.agent import app

http_server = WSGIServer(('', 9000), app)
http_server.serve_forever()

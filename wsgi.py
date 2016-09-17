__copyright__ = "Copyright (C) 2016 University of Maryland"
__license__ = "GNU AFFERO GENERAL PUBLIC LICENSE, Version 3"


from gevent.wsgi import WSGIServer
from agent.agent import app

http_server = WSGIServer(('', 9000), app)
http_server.serve_forever()

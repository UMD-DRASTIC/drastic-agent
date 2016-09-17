#! /usr/bin/env python
__copyright__ = "Copyright (C) 2016 University of Maryland"
__license__ = "GNU AFFERO GENERAL PUBLIC LICENSE, Version 3"


from gevent import monkey; monkey.patch_all()
from agent import app
from gevent.pywsgi import WSGIServer

app.debug = True
http_server = WSGIServer(('', 9000), app)
http_server.serve_forever()

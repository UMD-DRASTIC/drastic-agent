import gevent


class Actor(gevent.Greenlet):

    def __init__(self):
        self.inbox = queue.Queue()
        Greenlet.__init__(self)

    def recieve(self, message):
        """
        Define in your subclass.
        """
        raise NotImplemented()

    def _run(self):
        self.running = True

        while self.running:
            message = self.inbox.get()
            self.recieve(message)


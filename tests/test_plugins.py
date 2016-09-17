import unittest

from tests import register_keyspace
from agent.plugins.loader import run_plugins
from drastic.models import Collection, Resource


class PluginTest(unittest.TestCase):

    def setUp(self):
        self.root = Collection.get_root_collection()
        if not self.root:
            self.root = Collection.create(name="Home", path="/")

    def test_loader(self):
        resource = Resource.create(name='test_resource',
                                   container=self.root.id,
                                   url="test://tests/data/small.csv",
                                   mimetype="text/csv")
        ran = run_plugins(resource)
        assert len(ran) == 1
        register_keyspace(resource.id)

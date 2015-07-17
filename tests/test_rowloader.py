import unittest

from agent.plugins.rowstore.plugin import can_handle_resource
from indigo.models import Collection, Resource

class RowLoaderTest(unittest.TestCase):

    def setUp(self):
        self.root = Collection.get_root_collection()
        if not self.root:
            self.root = Collection.create(name="Home", path="/")

    def test_can_run(self):
        resource = Resource.create(name='test_resource_rowstore',
                                   container=self.root.id,
                                   url="test://tests/data/small.csv",
                                   mimetype="text/csv")
        assert can_handle_resource(resource)

        resource.mimetype = "text/plain"
        assert not can_handle_resource(resource)

        resource.mimetype = "application/xls"
        assert not can_handle_resource(resource)

        resource.mimetype = ""
        assert not can_handle_resource(resource)
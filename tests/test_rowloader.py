import unittest

from tests import register_keyspace
from agent.plugins.rowstore.plugin import can_handle_resource, load_resource
from agent.plugins.rowstore.types import count_types
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

    def test_type_guessing(self):
        cnt, results = count_types("test://tests/data/small.csv")
        assert cnt == 2
        assert len(results) == 2
        assert results["field1"]["string"] == 2
        assert results["field1"]["int"] == 0
        assert results["field1"]["datetime"] == 0

        assert results["field2"]["string"] == 2
        assert results["field2"]["int"] == 0
        assert results["field2"]["datetime"] == 0

    def test_type_guessing_with_numbers(self):
        cnt, results = count_types("test://tests/data/small_numbers.csv")
        assert cnt == 2
        assert len(results) == 2
        assert results["field1"]["string"] == 0
        assert results["field1"]["int"] == 2
        assert results["field1"]["datetime"] == 0

        assert results["field2"]["string"] == 2
        assert results["field2"]["int"] == 0
        assert results["field2"]["datetime"] == 0
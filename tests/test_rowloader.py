import unittest

from tests import register_keyspace
from agent.plugins.rowstore.plugin import can_handle_resource, load_resource
from agent.plugins.rowstore.types import count_types, guess_type
from agent.plugins.rowstore.cql import generate_create_cql
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
        assert results["field1"]["text"] == 2
        assert results["field1"]["int"] == 0
        assert results["field1"]["timestamp"] == 0

        assert results["field2"]["text"] == 2
        assert results["field2"]["int"] == 0
        assert results["field2"]["timestamp"] == 0

        assert guess_type(results["field1"]) == "text"
        assert guess_type(results["field2"]) == "text"

    def test_type_guessing_with_numbers(self):
        cnt, results = count_types("test://tests/data/small_numbers.csv")
        assert cnt == 2
        assert len(results) == 2
        assert results["field1"]["text"] == 0
        assert results["field1"]["int"] == 2
        assert results["field1"]["timestamp"] == 0

        assert results["field2"]["text"] == 2
        assert results["field2"]["int"] == 0
        assert results["field2"]["timestamp"] == 0

        assert guess_type(results["field1"]) == "int"
        assert guess_type(results["field2"]) == "text"


    def test_type_guessing_with_datetimes(self):
        cnt, results = count_types("test://tests/data/small_datetimes.csv")
        assert cnt == 2
        assert len(results) == 2
        assert results["field1"]["text"] == 0
        assert results["field1"]["int"] == 0
        assert results["field1"]["timestamp"] == 2

        assert results["field2"]["text"] == 2
        assert results["field2"]["int"] == 0
        assert results["field2"]["timestamp"] == 0

        assert guess_type(results["field1"]) == "timestamp"
        assert guess_type(results["field2"]) == "text"

    def test_keyspace_creation_datetime(self):
        resource = Resource.create(name='test_keyspace_cql_datetime',
                                   container=self.root.id,
                                   url="test://tests/data/small_datetimes.csv",
                                   mimetype="text/csv")
        self._test_keyspace_resource(resource)

    def test_keyspace_creation_datetime(self):
        resource = Resource.create(name='test_keyspace_cql_datetime',
                                   container=self.root.id,
                                   url="test://tests/data/small_numbers.csv",
                                   mimetype="text/csv")
        self._test_keyspace_resource(resource)

    def _test_keyspace_resource(self, resource):
        cnt, types = count_types(resource.url)
        assert cnt == 2
        assert len(types) == 2

        statement = generate_create_cql(resource, types).strip()
        assert resource.id.replace('-','') in statement
        for k, v in types.iteritems():
            assert k in statement
            assert guess_type(v) in statement

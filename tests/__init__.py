from indigo.models import initialise, sync
from cassandra.cqlengine.management import drop_keyspace

TEST_KEYSPACE="indigo_test"

KEYSPACES = []

def setup_package():
    initialise(TEST_KEYSPACE, strategy="SimpleStrategy", repl_factor=1)
    sync()

def register_keyspace(name):
    """ Allows tests to register created keyspaces """
    global KEYSPACES
    KEYSPACES.append(name)

def teardown_package():
    drop_keyspace(TEST_KEYSPACE)
    for name in KEYSPACES:
        drop_keyspace(name)

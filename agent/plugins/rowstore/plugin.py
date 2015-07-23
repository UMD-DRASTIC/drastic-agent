"""

"""
from indigo.util import IterStreamer

def log(msg):
    print u"[ROWSTORE]: {}".format(msg)

def can_handle_resource(resource):
    """
    If this plugin can handle the provided resource then
    it should return a function that can be called with
    the resource to execute the plugin.  Returning None
    suggests that the plugin cannot handle the resource.
    """
    if resource.mimetype in ['text/csv']:
        return load_resource
    return None

def load_resource(resource):
    """
    Creates a keyspace based on the ID of the resource, or
    uses it if it already exists to load the tabular data
    into a table (and record the schema as metadata in the
    resource).
    """
    log("Loading {} into rowstore".format(resource))

    # Get the KeySpace, or create it for resource.id

    # If it already exists, then decide what we want
    # to do.


    #d = get_driver(resource.url)
    #s = IterStreamer(d.chunk_content())

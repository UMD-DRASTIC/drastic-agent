
from gevent import spawn

def handle_event(object, event):
    """
    Launches the appropriate co-routine for the event
    and provides the resource as a parameter
    """
    print "Handling {} event on {}".format(event, object.id)
    f = EVENTS[event]
    spawn(f, [object])


def resource_new(args):
    resource = args[0]
    print "resource_new({})".format(resource.id)

    # Archive the newly created content and metadata


def resource_edit(args):
    resource = args[0]
    print "resource_edit({})".format(resource.id)

    # If the file contents have changed, we should re-archive the file
    # If the metadata has changed (likely) we should re-archive the metadata



EVENTS = {
    "resource:new": resource_new,
    "resource:edit": resource_edit,
}

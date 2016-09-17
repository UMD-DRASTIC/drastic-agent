__copyright__ = "Copyright (C) 2016 University of Maryland"
__license__ = "GNU AFFERO GENERAL PUBLIC LICENSE, Version 3"


from gevent import spawn


def handle_event(obj, event):
    """
    Launches the appropriate co-routine for the event
    and provides the resource as a parameter
    """
    print "Handling {} event on {}".format(event, obj.id)
    f = EVENTS[event]
    spawn(f, [obj])


def resource_new(args):
    resource = args[0]
    print "resource_new({})".format(resource.id)

    # Archive the newly created content and metadata

    # Prepare a preview for this resource ... we need to decide where
    # to store it so that it is available.


def resource_edit(args):
    resource = args[0]
    print "resource_edit({})".format(resource.id)

    # If the file contents have changed, we should re-archive the file
    # If the metadata has changed (likely) we should re-archive the metadata


EVENTS = {
    "resource:new": resource_new,
    "resource:edit": resource_edit,
}

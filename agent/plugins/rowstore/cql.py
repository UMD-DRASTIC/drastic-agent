__copyright__ = "Copyright (C) 2016 University of Maryland"
__license__ = "GNU AFFERO GENERAL PUBLIC LICENSE, Version 3"


from agent.plugins.rowstore.types import guess_type


def generate_create_cql(resource, types):
    fields = []
    for k, v in types.iteritems():
        fields.append(u"{} {},".format(k, guess_type(v)))

    keyspace_name = resource.id.replace('-', '')
    fields_string = '\n'.join(fields)

    return """
        CREATE KEYSPACE "{id}"
        WITH REPLICATION = {{ 'class' : 'SimpleStrategy', 'replication_factor' : 1 }};
        CREATE TABLE "{id}".data (
            drastic_id text PRIMARY KEY,
            {fields}
        );
    """.format(id=keyspace_name, fields=fields_string)

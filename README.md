# Indigo Agent

The agent is responsible for post-processing on uploaded content, it executes
a wsgi app that can be used to download the digital objects.


## Environment variables

    export CQLENG_ALLOW_SCHEMA_MANAGEMENT=1
    export INDIGO_SCHEMA=/path/to/schema.json
    export AGENT_CONFIG=/path/to/agentconfig

This can be added in the file `/etc/init/indigo-agent.conf` to be configured
when the agent is launched by upstart

    env CQLENG_ALLOW_SCHEMA_MANAGEMENT=1
    env AGENT_CONFIG=/usr/lib/indigo/agent/project/agent.config


## Agent config configuration

This is an example of a configuration file that you can use to define where the
agent is looking for the root of the archive on the filesystem (path defined with
AGENT_CONFIG environment variable).

    DISK_CONFIG = { 'ROOT': '/data' }

## Running the Agent

The agent is managed by upstart, it should be configured automatically when
deployed. It can be run with the command

```sudo service indigo-agent start```

## The Agent

Agent is listening on port 9000

    http://localhost:9000/

It provides an internal API used by indigo to download files managed by the
agent driver, for instance the URL `http://localhost:9000/get/test/test.txt` will try
to download the file `/data/test/test.txt` on the file system.
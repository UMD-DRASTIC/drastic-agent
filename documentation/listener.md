Indigo event listener
=====================

The listener will use the pub/sub functionality of Redis 3.0.4 as its
commuincation channel. Each script will be executed in a Gevent coroutine
which will block until a matching topic is published. The user scripts will
have a fixed interface but will (for now) otherwise have free reign as any
other Python script. They should be idempotent, but this is not enforced.

The combination of Redis and Gevent will mean that scripts will get executed
in arbitrary order, and there are no plans currently to implement deterministic
ordering.

The scripts will be stored in a predefined directory, accessible via CDMI and
the object store. The topics to which a given script is subscribed will be
held in a Cassandra table, along with metadata such as number of times
executed, last execution time, status, etc.

Scripts are stored globally.
Each agent runs its own Redis/MQTT/other pubsub.
Scripts are registered with each agent.
There is a Cassandra table that stores the topics each script is subscribed to. This is mirrored by each pubsub system.
A single agent gets an event via the load-balancer, and publishes it to whichever scripts are listening.

How do we do the Cassandra --> pubsub update? Polling? Some Cassandra hook? Polling will probably be best so it's
decoupled from the database. Each listener will cache the table in whatever format is suitable and set up the pubsub
system accordingly.

Cassandra schema will have script name as a required field, and each topic it's subscribed to in MQTT format.
Topics will be in the form: VERB/URI or similar.
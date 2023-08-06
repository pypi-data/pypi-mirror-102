# python-cassandra-jaeger

## When do I use it?

When I'm using the following technologies:

* [cassandra-driver](https://pypi.org/project/cassandra-driver/)
* [cassandra-jaeger-tracing](https://github.com/smok-serwis/cassandra-jaeger-tracing)

And you want to view what Cassandra's doing with your queries.

## Usage

Just do the following:

```python
from python_cassandra_jaeger import SessionTracer
from cassandra.cluster import Cluster

from .tracing import tracer

c = Cluster(['127.0.0.1'])
s = c.session()
st = SessionTracer(s, tracer)

st.execute('')
```

And you keep on utilizing `st` instead of `s`.
This will automatically execute tracing when your span is being traced.


For tracing cassandra-driver using smok-serwis/cassandra-jaeger-tracing

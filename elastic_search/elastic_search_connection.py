from elasticsearch import Elasticsearch as es

# setup connection
es_conn = es([{"host": "localhost", "port": 9200, "scheme": "http"}])

# create index
# es_conn.indices.create(index="es-practice-17072024")

# display index
all_indices = es_conn.indices.get_alias()
for index in all_indices:
    print(index)


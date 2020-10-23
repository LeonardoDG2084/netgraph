from elasticsearch import Elasticsearch
import json
from graphviz import Digraph


es = Elasticsearch(['http://localhost:9200/'])

def graphviz_generate(result_json):
  g = Digraph("netgraph", engine="dot", format="svg", strict="True")
  g.attr("node", shape="box", width="0.6", style="filled", fillcolor="#edad56", color="#edad56", penwidth="3", fontname="Arial", constraint="false")
  g.attr("edge", color="gray", penwidth="2", fontname="Arial", arrowsize="2", arrowhead='vee')
  total_of_records = result_json["hits"]["total"]["value"]
  for iteration, key in enumerate(result_json["hits"]["hits"]):
    g.edge(key["_source"]["source_ip"], key["_source"]["destination_ip"], label=key["_source"]["destination_port"]) 
  return g.render("./netgraph/static/graphviz")

def get_all_indices():
    """Get all indices from elastic"""
    indices = es.indices.get_alias("*")
    return indices

def get_total_docs(indice):
    total_docs = es.cat.count(indice)

    return total_docs.split(" ")

def create_indice(indice):
    es.indices.create(index=indice, ignore=[400, 404])

def delete_indice(indice):
    es.indices.delete(index=indice, ignore=[400, 404])

def search_connections(index, **kwargs):
    if kwargs["operator"] == "OR":
        bolean_operator = "should"
    else:
        bolean_operator = "must"
    kwargs.pop("operator")
    query_base = dict({
                  "from" : 0, "size" : 200,
                  "query": {
                    "bool": {
                      bolean_operator: [{
                        "bool": {
                          "must": []
                        }
                      },
                      {
                        "bool": {
                          "must": []
                        }
                      }]
                    }
                  }
                })
    for key, value in kwargs.items():
        if key == "source_ip" or key == "source_port":
            query_base["query"]["bool"][bolean_operator][0]["bool"]["must"].append(dict({"match":{key: value}}))
        else:
            query_base["query"]["bool"][bolean_operator][1]["bool"]["must"].append(dict({"match":{key: value}}))
    return es.search(index=index, body=json.dumps(query_base))
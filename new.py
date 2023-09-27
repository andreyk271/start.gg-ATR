from python_graphql_client import GraphqlClient

headers = {"Authorization": "Bearer bf718654ed449a97233beafba959502e"}
client = GraphqlClient(endpoint="https://api.start.gg/gql/alpha", headers=headers)

variables = {"eventId": 752621,
             "page": 1,
             "perPage": 50}
query = """query EventSets($eventId: ID!, $page: Int!, $perPage: Int!) {
  event(id: $eventId) {
    id
    name
    sets(
      page: $page
      perPage: $perPage
      sortType: RECENT
    ) {
      pageInfo {
        total
      }
      nodes {
        id
        slots {
          id
          entrant {
            id
            name
          }
          standing {
            id
            placement
            stats {
              score {
                label
                value
              }
            }
          }
        }
      }
    }
  }
}"""
ret = client.execute(query, variables=variables)
print(ret)
f = open("prep_target.txt", "a", encoding="utf-8")
g = open("prep_opponent.txt", "a", encoding="utf-8")
for i in ret['data']['event']['sets']['nodes']:
    if i['slots'][0]['standing']['placement'] == 1:
        f_w = i['slots'][0]['entrant']['name']
        g_w = i['slots'][1]['entrant']['name']
    else:
        g_w = i['slots'][0]['entrant']['name']
        f_w = i['slots'][1]['entrant']['name']
    f.write(f_w)
    f.write("\n")
    g.write(g_w)
    g.write("\n")

f.close()
g.close()
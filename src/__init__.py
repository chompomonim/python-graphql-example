from sanic import Sanic
from sanic.response import json, text
from sanic_graphql import GraphQLView

# from api import schema, setup

app = Sanic()


#### GraphQL schema
import graphene

class Query(graphene.ObjectType):
    labas = graphene.String(description='A typical hello world')

    def resolve_labas(self, args, context, info):
        return 'Rytas'

schema = graphene.Schema(query=Query)
####


@app.route("/")
async def root(request):
    return text("Welcome! Call me via POST with graphql query in body.")


@app.route("/", methods=['POST'])
async def post_root(request):
    result = schema.execute(request.json['query'])
    return json(result.data)

# app.add_route(GraphQLView.as_view(schema=schema, graphiql=True), '/graphql')

if __name__ == "__main__":
    # setup()
    app.run(host="0.0.0.0", port=4000)

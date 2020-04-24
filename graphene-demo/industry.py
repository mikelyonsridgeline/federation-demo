from flask import Flask
from flask_graphql import GraphQLView
from graphene import ObjectType, String, List, NonNull, Int
from graphene_federation import build_schema, key

INDUSTRIES = {}


@key(fields='sector')
class Industry(ObjectType):
    id = Int()
    sector = String(required=True)

    def __resolve_reference(self, info, **kwargs):  # https://www.apollographql.com/docs/apollo-server/api/apollo-federation/#__resolvereference
        print(f"we're __resolving: self: {self}   info: {info}    sector: {kwargs}")
        return INDUSTRIES.get(self.sector, None)


class Query(ObjectType):
    industries = List(NonNull(Industry), sector=List(String, required=True))

    def resolve_industries(self, info, sector):
        print(f"we're resolving: self: {self}   info: {info}    sector: {sector}")
        results = []
        for i in sector:
            industry = INDUSTRIES.get(i, None)
            if industry:
                results.append(industry)
        return results


schema = build_schema(query=Query, types=[Industry], auto_camelcase=False)
print(schema)

app = Flask(__name__)
app.debug = True

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    INDUSTRIES = {
        i.strip(): Industry(id=e, sector=i.strip()) for e, i in enumerate("""Energy
        Materials
        Industrials
        Consumer Discretionary
        Consumer Staples
        Health Care 
        Financials
        Information Technology
        Telecommunication Services
        Utilities
        Real Estate
        """.split("\n"))
    }

    print(INDUSTRIES)
    app.run(host='0.0.0.0', port=9000)

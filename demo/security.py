from flask import Flask
from flask_graphql import GraphQLView
from graphene import ObjectType, String, Field, List, NonNull
from graphene_federation import build_schema, key, extend, external

STOCKS = {}


@extend(fields='sector')
class Industry(ObjectType):
    sector = external(String(required=True))


@key(fields='ticker')
class Security(ObjectType):
    ticker = String(required=True)
    industry = Field(lambda: Industry)


class Query(ObjectType):
    securities = List(NonNull(Security), tickers=List(String, required=True))

    def resolve_securities(self, info, tickers):
        print(f"resolving_securities: self: {self}   info: {info}    tickers: {tickers}")
        results = []
        for t in tickers:
            stock = STOCKS.get(t, None)
            if stock:
                results.append(stock)
        print(results)
        return results


schema = build_schema(query=Query, types=[Security], auto_camelcase=False)
print(schema)

app = Flask(__name__)
app.debug = True

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    STOCKS = {
        'GOOG': Security(ticker='GOOG', industry=Industry(sector='Information Technology')),
        'FB': Security(ticker='FB', industry=Industry(sector='Information Technology')),
        'TSLA': Security(ticker='TSLA', industry=Industry(sector='Consumer Staples')),
        'F': Security(ticker='F', industry=Industry(sector='Automotive')),
    }

    print(STOCKS)
    app.run(host='0.0.0.0', port=8000)

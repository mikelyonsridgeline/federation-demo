const { ApolloServer } = require("apollo-server");
const { ApolloGateway, RemoteGraphQLDataSource } = require('@apollo/gateway');
const { formatError }  = require('apollo-errors');


const gateway = new ApolloGateway({
  serviceList: [
    { name: 'industries', url: 'http://0.0.0.0:9000/graphql'},
    { name: 'securities', url: 'http://0.0.0.0:8000/graphql'},
  ]
});

const server = new ApolloServer({
  gateway,
  formatError,
  subscriptions: false,
  introspection: true,
  playground: {
    settings: {
      "request.credentials": "same-origin"
    }
  },
});


server.listen({port: 5000}).then(({ url }) => {
  console.log(`🚀  Server ready at ${url}`);
});

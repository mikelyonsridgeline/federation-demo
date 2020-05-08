class GraphQLSignatures:
    SIGNATURE_STUB = """
        query  {
            industries {
                edges {
                    cursor
                    node {
                        id
                        sector
                    } 
                }
                pageInfo {
                    hasNextPage 
                }
            }
        }
    """

    FED_STUB = """
        query($representations:[_Any!]!){
            _entities(representations:$representations){
                ...on IndustryResultNode{
                    sector
                    id
                    aggregateId
                }
                    
            }
        }
    """


class GraphQLVariables:
    VARIABLE_STUB = {"representations":[{"__typename":"IndustryResultNode","aggregateId":'test:1234'},{"__typename":"IndustryResultNode","aggregateId":'test:5678'}]}


class GraphQLExpectedOutput:
    pass

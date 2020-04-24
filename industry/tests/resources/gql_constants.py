class GraphQLSignatures:
    SIGNATURE_STUB = """
        query  {
            industries {
                edges {
                    node {
                        id
                        sector
                    } 
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
    VARIABLE_STUB = {"representations":[{"__typename":"IndustryResultNode","aggregateId":"idty:industry:Ei3QrcCzT7GiEpGgbTdh4A=="},{"__typename":"IndustryResultNode","aggregateId":"idty:industry:rCIMEH7QTeCqzN9BVSRxFQ=="},{"__typename":"IndustryResultNode","aggregateId":"idty:industry:oKDFqSrNQfWqcQQZ6JxZYQ=="},{"__typename":"IndustryResultNode","aggregateId":"idty:industry:Ei3QrcCzT7GiEpGgbTdh4A=="},{"__typename":"IndustryResultNode","aggregateId":"idty:industry:Ei3QrcCzT7GiEpGgbTdh4A=="}]}


class GraphQLExpectedOutput:
    pass

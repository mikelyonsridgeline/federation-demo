# federation-demo

### setup
```
pipenv install -d
npm i
```

### run
```
pipenv shell
python graphene-demo/security.py
python graphene-demo/industry.py
node gateway.js
```
then head to http://localhost:5000/ and this a try:
```
query {
 securities(tickers: ["GOOG", "FB", "TSLA"]) {
    ticker
    industry {
      sector
      id
    }
   
  }
}
``` 


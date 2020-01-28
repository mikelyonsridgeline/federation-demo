# federation-demo

### setup
```
pipenv install -d
npm i
```

### run
```
pipenv shell
python demo/security.py
python demo/industry.py
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


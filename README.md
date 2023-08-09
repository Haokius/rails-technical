# Usage

## System environment

- install dependencies
  - poetry
  - node v16.0.0
  - npm

## Frontend environment

### Setup

```bash
cd frontend
npm install
npm start
```

The frontend should now be running on port 3000.

## Backend environment

### Setup

```bash
cd backend/backend
poetry install
poetry run server
```

The backend should now be running on port 8081. You can go to [http://localhost:8081/ui](http://localhost:8081/ui) to see the API documentation.

### Example of expected behavior of the backend

```bash
# put report by id
curl -X 'PUT' \
  'http://localhost:8081/reports/1' \
  -H 'accept: */*' \
  -H 'Content-Type: application/json' \
  -d '{
  "date_end": "2022-08-30",
  "date_start": "2022-08-01",
  "metric": "open",
  "name": "this is a test",
  "tickers": [
    {"ticker": "AAPL", "metric": "open"},
    {"ticker": "MSFT", "metric": "close"}
  ]
}'

# get report and data
curl -X 'GET' \
  'http://localhost:8081/reports/1/data' \
  -H 'accept: application/json'
```

The schema GET /report/{id}/data is a suggestion. You can structure it however you want to. For example,

```json
{
  "2022-08-01": {
    "AAPL": {"value": 160.521, "metric" : "open"},
    "MSFT": {"value": 276.453, "metric" : "close"}
  },
  "2022-08-02": {
    "AAPL": {"value": 159.613, "metric" : "open"},
    "MSFT": {"value": 274.641, "metric" : "close"}
  },
...
}
```

is equally valid as

```json
[
  {
   "ticker": "AAPL",
   "date": "2022-08-01",
   "value": 160.521,
   "metric": "open"

  },
  {
   "ticker": "MSFT",
   "date": "2022-08-01",
   "value": 276.453,
   "metric": "close"
  },
  {
    "ticker": "AAPL",
    "date": "2022-08-02",
    "value": 159.613,
    "metric": "open"
  },
  {
    "ticker": "MSFT",
    "date": "2022-08-02",
    "value": 274.641,
    "metric": "close"
  },
...
]
```

It's really up to you based on how you want to implement the frontend. If you do end up changing the schema, please update the OpenAPI spec accordingly.

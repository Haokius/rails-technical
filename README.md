# Directions

## Prompt
Create a reactive, client-side rendered UI for configuring and viewing stock price reports. As part of this you will need to:
- Complete the backend skeleton code to perform CRUD operation on the reports in the database
- Create UIs for these CRUD operations
- Create UI for report data
- Create at least one additional report (tabular or visual) that shows aggregate information (ex: average open price by ticker over entire report period)

## Timeline
You will have ~ 48 hours to build the app and submit via github.

## Submission
Create a new repo using this template repo and add @akshayshippy @gregg-shippy @mohnish7 @vimeh as collaborators. Feel free to reach out via email if you have any questions. Please also respond to our email with a link to your github repo, once you are ready to submit.

## Grading Criteria
- completeness of endpoints' functionality
- completeness of frontend flows working
- accuracy of report(s)
- bonus: plus any additional work done that is outside of the scope of completing this assignment, for example:
  - api design
  - ui/ux considerations 
  - additional report(s)

# Setup

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

It's really up to you based on how you want to implement the frontend. For the backend, please update the pydantic schema accordingly.

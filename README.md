# Shippy Fullstack Takehome

## Kevin's README:

For backend proceed as usual, for frontend - cd into shadcn-starter-copy and then npm run dev.

## Introduction

### Prompt

Create a reactive, client-side rendered UI for configuring and viewing stock price reports. As part of this you will need to:

- Complete the backend skeleton code to perform CRUD operations on the reports in the database
  - You will need to implement the endpoints. As a guide, there are #TODO: comments in the code to help you.
  - It is up to you what you want the schema of the return objects to be. You can use the example below as a guide, or choose our own to implement.
- Create UIs for these CRUD operations
  - You'll probably need some forms to create and update reports
  - You'll need a way to list the reports
  - etc.
- Create at at least one chart (ex: average open price by ticker over entire report period)
  - Bonus: make the chart interactive (ex: allow users to select different metrics to display)

### Submission

Create a new repo using this template repo and add @gregg-shippy @mohnish7 @vimeh as collaborators. Feel free to reach out via email if you have any questions. Please also respond to our email with a link to your GitHub repo once you are ready to submit.

### Grading Criteria

- completeness of endpoints' (CRUD)
- completeness of frontend flows (CRUD)
- styling and UX

### Resources

Here’s the stack we use internally, and the repo will have most of the infrastructure already in place for you, but you should feel free to choose and add whatever tools you feel comfortable with for getting the job done:

- Python runs our entire middle-layer.
  - [FastAPI](https://fastapi.tiangolo.com/)
  - [Pydantic](https://pydantic-docs.helpmanual.io/)
  - [SQLAlchemy](https://docs.sqlalchemy.org/en/20/tutorial/index.html)
- Frontend
  - TypeScript with node
  - [eslint-prettier](https://www.npmjs.com/package/eslint-config-airbnb)
  - React
  - [Chart.js](https://github.com/chartjs/Chart.js) for charts
  - [Tailwind CSS](https://tailwindcss.com/docs) for styling
  - [Shadcn UI](https://ui.shadcn.com/docs/) for components

## Setup

### System environment

- install dependencies
  - poetry
  - node v20
  - npm
  - npx

### Frontend environment

```bash
cd frontend
# Make sure you're using node v20, eg:
# $ nvm use 20
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `pages/index.tsx`. The page auto-updates as you edit the file.

You'll probably want to take a look at the shadcn components available to you at [https://ui.shadcn.com/docs/](https://ui.shadcn.com/docs/). As an example, you'll probably want to use the `Table` component to display the reports, which you can add to the project like so:

```bash
npx shadcn-ui@latest add table
```

### Backend environment

- Assuming a UNIX shell environment.
- Make sure to [install poetry](https://python-poetry.org/docs/)

```bash
cd backend/backend
poetry install
poetry shell
uvicorn main:app --reload
```

The backend should now be running on port 8000. You can go to [http://localhost:8000/docs](http://localhost:8000/docs) to see the API documentation.

#### Example of expected behavior of the backend

```bash
# put report by id
curl -X 'PUT' \
  'http://localhost:8000/reports/1' \
  -H 'accept: */*' \
  -H 'Content-Type: application/json' \
  -d '{
  "date_end": "2022-08-30",
  "date_start": "2022-08-01",
  "name": "this is a test",
  "tickers": [
    {"ticker": "AAPL", "metric": "open"},
    {"ticker": "MSFT", "metric": "close"}
  ]
}'

# get report and data
curl -X 'GET' \
  'http://localhost:8000/reports/1/data' \
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

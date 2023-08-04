#!/usr/bin/env python3
import logging

import connexion

from backend.models import init_db

# set logging to display all messages INFO and above
logger = logging.getLogger()
logger.setLevel(logging.INFO)

db_session = init_db("sqlite:///:memory:")


def get_all_report_configs():
    # TODO:
    pass


def get_report_config(id: int):
    # TODO:
    pass


def put_report_config(id: int, body):
    # TODO:
    pass


def delete_report_config(id: int):
    # TODO:
    pass

def get_report_data(id: int):
    # TODO: https://pandas-datareader.readthedocs.io/en/latest/remote_data.html#remote-data-stooq
    pass

options = {"swagger_ui": True}
logger.info("Creating Flask server")
app = connexion.FlaskApp(
    __name__,
    options=options,
)
# NOTE: expected behavior is that if we can't resolve a
# function for a route, we don't even allow the server to start
app.add_api(
    # NOTE: when you change the OpenAPI schema, you need to run
    # swagger-cli bundle -o spec.bundle spec.yaml
    "spec/spec.bundle",
    resolver_error=None,
    strict_validation=True,
)

application = app.app


assert application is not None
application.logger.setLevel(logging.INFO)


@application.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


def main():
    app.run(port=8081, use_reloader=False, threaded=False, debug=True)


if __name__ == "__main__":
    main()

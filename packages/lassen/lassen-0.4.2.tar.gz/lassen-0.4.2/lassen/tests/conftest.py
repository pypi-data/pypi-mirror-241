from json import dumps as json_dumps
from os import environ
from tempfile import TemporaryDirectory

import pytest
from sqlalchemy import text

from lassen.core.config import CoreSettings, register_settings
from lassen.db.session import get_db_context


@pytest.fixture(autouse=True, scope="session")
def inject_env_variables():
    """
    Inject fake environment variables for testing purposes.

    """
    settings = CoreSettings(
        BACKEND_CORS_ORIGINS=["http://localhost"],
        SERVER_NAME="lassen-test",
        POSTGRES_SERVER="localhost",
        POSTGRES_USER="lassen",
        POSTGRES_PASSWORD="mypassword",
        POSTGRES_DB="lassen_test_db",
    )

    # Convert settings into env variables
    for key, value in settings.model_dump().items():
        if value:
            if isinstance(value, list):
                value = json_dumps([str(val) for val in value])
            else:
                value = str(value)

            print(f"Test Env: Will set `{key}` = `{value}`")  # noqa
            environ[key] = value

    # We don't have a client-specific settings object, so we'll just back-register
    # the core settings
    register_settings(CoreSettings)


@pytest.fixture()
def clear_db():
    with get_db_context() as db:
        # Drop the alembic specific tables
        db.execute(text("DROP TABLE IF EXISTS alembic_version"))

        # Commit these changes
        db.execute(text("COMMIT"))

    with get_db_context() as db:
        # Import all models used in tests
        import lassen.tests.fixtures.test_harness.test_harness.models  # noqa
        import lassen.tests.model_fixtures  # noqa

        # Make sure each test has a fresh context
        from lassen.db.base_class import Base

        Base.metadata.drop_all(bind=db.bind)


@pytest.fixture()
def db_session(clear_db):
    # Because this is scoped to the whole test function, refreshes would be run
    # after the test is completed. We set to false to save on some performance time
    # seeing as this isn't otherwise needed.
    with get_db_context(refresh=False) as db:
        # Import all models used in tests
        import lassen.tests.fixtures.test_harness.test_harness.models  # noqa
        import lassen.tests.model_fixtures  # noqa

        from lassen.db.base_class import Base

        Base.metadata.create_all(bind=db.bind)

        yield db


@pytest.fixture()
def tempdir():
    with TemporaryDirectory() as tempdir:
        yield tempdir

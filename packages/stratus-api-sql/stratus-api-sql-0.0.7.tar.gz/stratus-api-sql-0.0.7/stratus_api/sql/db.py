from contextlib import contextmanager
from sqlalchemy import text, create_engine, URL

__connection__ = None
__db_url__ = None
__default_db_url__ = None
__session_maker__ = None


def setup_db_connection(database=None, host=None, username=None, password=None):
    from stratus_api.core.settings import get_settings
    app_settings = get_settings(settings_type='app')
    db_settings = get_settings(settings_type='db')

    db_name = db_settings['db_name'] + app_settings['prefix'].split('-')[0]
    global __db_url__
    __db_url__ = URL.create(
        drivername=db_settings["db_driver"],
        username=db_settings['db_user'],
        password=db_settings['db_password'],
        database=db_name,
        host=db_settings['db_host'],
        port=db_settings['db_port']
    )

    global __default_db_url__
    __default_db_url__ = __db_url__.set(database=db_settings.get('default_db_name', 'postgres'))
    global __connection__
    __connection__ = create_engine(__db_url__)
    configure_session_maker(bind=__connection__)
    return __db_url__


def configure_session_maker(**kwargs):
    from sqlalchemy.orm import sessionmaker

    global __session_maker__
    if __session_maker__ is None:
        __session_maker__ = sessionmaker()
    __session_maker__.configure(**kwargs)
    return __session_maker__


@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    global __session_maker__
    session = __session_maker__()

    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


def create_test_db():
    from alembic.config import Config
    from alembic import command
    global __default_db_url__
    global __db_url__
    default_db = create_engine(__default_db_url__)
    with default_db.connect() as conn:
        conn.execute(text("COMMIT"))
        conn.execute(text('create database {0}'.format(__db_url__.database)))
    alembic_cfg = Config("/apps/app/alembic.ini")
    command.upgrade(alembic_cfg, "head")


def delete_test_db():
    global __connection__
    global __default_db_url__
    global __db_url__
    from stratus_api.core.settings import get_settings
    assert get_settings()['environment'] == 'test' and get_settings()['prefix']
    __connection__.dispose()
    default_db = create_engine(__default_db_url__)

    with default_db.connect() as conn:
        conn.execute(text("COMMIT"))
        conn.execute(text("""drop database {0};""".format(__db_url__.database)))

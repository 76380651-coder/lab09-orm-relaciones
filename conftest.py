
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from modelos import Base


@pytest.fixture(scope="function")
def db_session():
    """Provee una sesión limpia de SQLite en memoria para cada prueba."""
    engine = create_engine("sqlite:///:memory:", echo=False)
    Base.metadata.create_all(bind=engine)

    SessionLocal = sessionmaker(bind=engine)
    session = SessionLocal()

    yield session

    session.close()
    engine.dispose()

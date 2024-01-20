# Import all the models, so that Base has them before being
# imported by Alembic
from app.database.base_class import Base  # noqa
from app.models.product import Product  # noqa
from app.models.color import Color  # noqa
from app.models.size import Size  # noqa

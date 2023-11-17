import logging

# from sqlalchemy.exc import NoSuchTableError, ArgumentError

# from .config import Config


class BaseModel(db.Model):
    """
    An abstract base class for SQLAlchemy models that automatically reflects
    database tables into SQLAlchemy model classes based on the subclass's name.

    The class name is transformed to snake case and pluralized to match the
    expected table name in the database. This class should be subclassed
    by specific models corresponding to the database tables.

    Attributes:
        __abstract__ (bool): Indicates that this is an abstract base class.
    """

    __abstract__ = True

    @classmethod
    def __init_subclass__(cls, **kwargs):
        """
        Automatically called when a new subclass is defined. Reflects the corresponding
        database table into the subclass, using the subclass's name to determine the
        table name.

        The subclass's name is transformed to snake case and pluralized, and the
        corresponding database table is loaded into the subclass.

        Args:
            cls (BaseModel): The subclass being created.
            **kwargs: Additional keyword arguments.
        """
        tablename = BaseModel._transform_to_snake_case(cls.__name__)

        with Config.app.app_context():
            try:
                Config.db.Model.metadata.reflect(Config.db.engine)
                cls.__table__ = Config.db.Table(
                    tablename, Config.db.metadata, autoload_with=Config.db.engine
                )
            # except NoSuchTableError:
            #     logging.error('Please create migration first')
            except ArgumentError:
                logging.error("Please create migration first")

    @classmethod
    def _transform_to_snake_case(cls, tablename: str):
        """
        Transforms a given string (typically the class name) into snake case
        and pluralizes it. This is used to derive the table name from the class name.

        Args:
            tablename (str): The string to be transformed into snake case.

        Returns:
            str: The transformed string in snake case and pluralized.
        """
        string = ""

        for char in tablename:
            if char.isupper():
                string += f"_{char.lower()}"
            else:
                string += char

        string += "s"

        return string.removeprefix("_")

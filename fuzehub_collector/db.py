from sqlalchemy import create_engine, Table, MetaData
from psycopg2 import OperationalError, ProgrammingError
from sqlalchemy.dialects.postgresql import insert
import logging
import sys
import os


class Connection:
    def __init__(self, logger_name):
        
        try:
            self.logger = logging.getLogger(logger_name)
        except:
            self.logger = None
            print("Unable to connect to logger")

        try:
            self.engine = create_engine(
                f"postgresql+psycopg2://fuzehub:collector@localhost:5432/fuzehubdb", future=True
            )
        except OperationalError as e:
            if self.logger is not None:
                self.logger.error(e)
            else:
                print(e)
            

        self.table = Table("models", MetaData(), autoload_with=self.engine)

    def log_err(self, error):
        if self.logger is not None:
            self.logger.error(error)
        else:
            print(error)

    def save_item(self, item):
        with self.engine.connect() as self.conn:
            try:
                insert_stmt = (
                    insert(self.table)
                    .values(
                        id=item["id"],
                        name=item["name"],
                        likes=item['likes'],
                        url=item["url"],
                        downloads=item["downloads"],
                        last_update=item["last_update"]
                    )
                    .on_conflict_do_update(index_elements=["id"], set_=item)
                )
            except:
                self.log_err(sys.exc_info())
                raise

            try:
                self.conn.execute(insert_stmt)
            except ProgrammingError as e:
                self.log_err(e)

            try:
                self.conn.commit()
            except:
                self.log_err(sys.exc_info())

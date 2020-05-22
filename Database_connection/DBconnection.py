from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker


class DBconnection:

    def getConnection_parameters(self):
        engine = create_engine('postgresql://postgres:pass123@localhost:5432/egrocery',echo = True)
        Session = sessionmaker(bind=engine)
        session = Session()
        return session
        """conn = engine.connect()
        meta = MetaData()
        return conn,meta"""



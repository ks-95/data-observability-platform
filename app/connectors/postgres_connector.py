from sqlalchemy import create_engine, text


class PostgresConnector:

    def __init__(self, username, password, host, port, database):

        self.connection_string = (
            f"postgresql://{username}:{password}@{host}:{port}/{database}"
        )

        self.engine = create_engine(self.connection_string)
    
    def get_engine(self):

        return self.engine


    def connection_status(self):
        try:
            with self.engine.connect() as connection:
                result = connection.execute(text("SELECT 1"))
                print("Connection to postgres database is successful....")
        except Exception as e:
            print("Connection failed...")
            print(e)
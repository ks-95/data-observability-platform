from sqlalchemy import create_engine, text


class MetadataDiscovery:

    def __init__(self, connector):

        self.engine = connector.get_engine()

    ########### TABLE DISCOVERY ##########################

    def get_tables(self):

        query = """
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema='public';
        """

        with self.engine.connect() as connection:

            result = connection.execute(text(query))

            tables = [row[0] for row in result]

        return tables
    
    ############## COLUMN DISCOVER ##########################

    def get_columns(self, table_name):

         query = f"""
         select column_name, data_type FROM information_schema.columns
         WHERE table_name = '{table_name}';
         """

         with self.engine.connect() as connection:

            result = connection.execute(text(query))

            columns = []

            for row in result:

                columns.append({
                    "column_name": row[0],
                    "data_type": row[1]
                })
            return columns
         
    ############## ENTIRE DATABASE METADATA DISCOVERY ##########################      
    
    def get_database_metadata(self):
        metadata = {}
        tables = self.get_tables()

        for table in tables:
            columns = self.get_columns(table)
            metadata[table] = columns
        
        return metadata
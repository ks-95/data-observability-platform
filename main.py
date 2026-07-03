from app.connectors.postgres_connector import PostgresConnector
from app.metadata.discovery import MetadataDiscovery
from app.metadata.drift_detector import DriftDetector
from app.metadata.snapshot import SchemaSnapshot
import json
import argparse
from dotenv import load_dotenv
import os

#### Load environment variables from .env file ####
load_dotenv()

connector = PostgresConnector(
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME")
)

connector.connection_status()

#### DATA DISCOVERY####
metadata_discovery = MetadataDiscovery(connector)
snapshot = SchemaSnapshot()
detector = DriftDetector()


###Parsing command line arguments-----------------------------------------

parser = argparse.ArgumentParser()
parser.add_argument("command")
parser.add_argument("target", nargs="?")

args = parser.parse_args()


#### DATABASE METADATA DISCOVERY USING COMMAND LINE ARGUMENTS ####-----------------------------------------------------
print("\n")
if args.command == "tables":
    tables = metadata_discovery.get_tables()
    print("Following tables are present in the database:")
    print(tables)

elif args.command == "columns":
    table_name = args.target
    columns = metadata_discovery.get_columns(table_name)
    print(f"Columns in table '{table_name}':")
    for column in columns:
        print(column)

elif args.command == "database":
    print("Showing the Metadata in json format for the entire database:")
    database_metadata = metadata_discovery.get_database_metadata()
    print(json.dumps(database_metadata, indent=4))


elif args.command == "snapshot":
    database_metadata = ( metadata_discovery.get_database_metadata() )
    snapshot.save_snapshot(database_metadata)
    print("Schema snapshot saved successfully")

elif args.command == "check_schema_changes":
    snapshot = SchemaSnapshot()
    print("Detecting schema drift...")
    old_metadata = snapshot.load_snapshot()
    new_metadata = (
    metadata_discovery.get_database_metadata()
    )

    if old_metadata:

        detector.detect_drift(
            old_metadata,
            new_metadata
        )

    else:

        print("No previous snapshot found")

else:

    print("Invalid command")
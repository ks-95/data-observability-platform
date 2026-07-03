import json


class SchemaSnapshot:

    def save_snapshot(self, metadata, filename="schema_snapshot.json"):

        with open(filename, "w") as file:

            json.dump(metadata, file, indent=4)

    def load_snapshot(self, filename="schema_snapshot.json"):

        try:
            with open(filename, "r") as file:

                return json.load(file)

        except FileNotFoundError:

            return None
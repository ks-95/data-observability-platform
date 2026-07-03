class DriftDetector:

    ############ SCHEMA DRIFT DETECTION ##########################
    def detect_drift(self, old_schema, new_schema):

        if old_schema != new_schema:

            print("SCHEMA DRIFT DETECTED")

        else:

            print("No schema changes")
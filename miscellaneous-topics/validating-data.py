"""
Data is often presented in a raw form and might contain anomalies or incorrect
or malformed data, which will obviously present a problem for later processing
and analysis. It is usually a good idea to build a validation step into a
processing pipeline. Fortunately, the Cerberus package provides a lightweight
and easy to use validation tool for Python. For validation, we have to define a
schema, which is a technical description of what the data should look like and
the checks that should be performed on the data. For example, we can check the
type and place bounds of the maximum and minimum values. Cerberus validators
can also perform type conversions during the validation step, which allows us to
plug data loaded directly from CSV files into the validator.

This module illustrates how to use Cerberus to validate data loaded from a CSV
file.
"""
import csv
import cerberus

float_schema = {"type": "float", "coerce": float, "min": -1.0, "max": 1.0}

item_schema = {
    "type": "dict",
    "schema": {
        "id": {"type": "string"},
        "number": {"type": "integer", "coerce": int},
        "lower": float_schema,
        "upper": float_schema,
        }
    }

schema = {
    "rows": {
        "type": "list",
        "schema": item_schema
        }
    }

validator = cerberus.Validator(schema)

with open("miscellaneous-topics/sample.csv") as f:
    dr = csv.DictReader(f)
    document = {"rows": list(dr)}

validator.validate(document)
errors = validator.errors["rows"][0]

for row_n, errs in errors.items():
    print(f"row {row_n}: {errs}")

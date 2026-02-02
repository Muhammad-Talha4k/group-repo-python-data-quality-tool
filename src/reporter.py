import json
from checks import check_missing, check_missing_percentage, check_duplicates, check_outliers, check_schema
from loader import load_csv

# Example expected columns for schema validation
expected_columns = ["index", "track_name", "track_artist", "streams", "track_popularity"]

# Load dataset
df = load_csv("../data/clean_dataset.csv")

# Generate data quality report
report = {
    "missing_values": check_missing(df),
    "missing_percentage": check_missing_percentage(df),
    "duplicate_rows": check_duplicates(df),
    "outliers": check_outliers(df),
    "schema_issues": check_schema(df, expected_columns)
}

# Print to console
print("=== DATA QUALITY REPORT ===")
for k, v in report.items():
    print(f"{k}: {v}")

# Save to JSON
def generate_report(report: dict, output_path="../quality_report.json"):
    with open(output_path, "w") as f:
        json.dump(report, f, indent=2)

generate_report(report)
print(f"\nReport saved to ../quality_report.json")

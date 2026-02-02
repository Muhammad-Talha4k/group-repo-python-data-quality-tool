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
feature-reporting
import json
import os

def generate_report(missing_data, outliers, duplicates):
    """
    Consolidates all quality checks into a structured JSON report.
    """
    report = {
        "project": "Data Quality Tool",
        "status": "Success",
        "summary": {
            "total_missing_values": missing_data,
            "total_outliers": outliers,
            "duplicate_rows": duplicates
        },
        "details": "Phase 3: Team Collaboration Report"
    }

    # Ensure the output directory exists
    os.makedirs('output', exist_ok=True)

    with open('output/quality_report.json', 'w') as f:
        json.dump(report, f, indent=4)
    
    print("✅ Quality report generated in output/quality_report.json")

generate_report(report)
print(f"\nReport saved to ../quality_report.json")
main

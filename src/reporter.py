import json

def generate_report(report: dict, output_path="quality_report.json"):
    with open(output_path, "w") as f:
        json.dump(report, f, indent=2)
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
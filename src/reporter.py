import json

def generate_report(report: dict, output_path="quality_report.json"):
    with open(output_path, "w") as f:
        json.dump(report, f, indent=2)

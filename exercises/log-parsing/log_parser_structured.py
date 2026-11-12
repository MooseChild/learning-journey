import json

LOG_FILE = "data.log"
OUTPUT_FILE = "report.json"

def parse_logs_structured(file_path):
    summary = {
        "total_lines": 0,
        "info_count": 0,
        "error_count": 0,
        "errors": []
    }

    with open(file_path, "r") as file:
        for line in file:
            summary["total_lines"] += 1
            line = line.strip()

            if "ERROR" in line:
                summary["error_count"] += 1
                summary["errors"].append(line)
            elif "INFO" in line:
                summary["info_count"] += 1

    return summary

def write_report(data, output_path):
    with open(output_path, "w") as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    report = parse_logs_structured(LOG_FILE)
    write_report(report, OUTPUT_FILE)

    print("Report written to report.json")
    print(json.dumps(report, indent=4))

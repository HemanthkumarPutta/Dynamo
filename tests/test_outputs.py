import json
from pathlib import Path

def test_criterion_1_report_exists():
    """Verifies Success Criterion 1: The output report file exists at /app/report.json."""
    assert Path("/app/report.json").exists(), "no report.json found at /app/report.json"


def test_criterion_2_report_valid_json():
    """Verifies Success Criterion 2: The file /app/report.json is a valid JSON object."""
    try:
        with open("/app/report.json", "r") as f:
            data = json.load(f)
        assert isinstance(data, dict), "The JSON root must be an object (dictionary)."
    except Exception as e:
        assert False, f"Failed to parse report.json as valid JSON: {e}"


def test_criterion_3_report_content_correct():
    """Verifies Success Criterion 3: The report contains correct traffic parsing statistics."""
    with open("/app/report.json", "r") as f:
        data = json.load(f)

    # Check for required keys
    assert "total_requests" in data, "Key 'total_requests' is missing"
    assert "unique_ips" in data, "Key 'unique_ips' is missing"
    assert "top_path" in data, "Key 'top_path' is missing"

    # Check exact statistics calculated from the logs
    assert data["total_requests"] == 6, f"Expected 6 total_requests, got {data['total_requests']}"
    assert data["unique_ips"] == 3, f"Expected 3 unique_ips, got {data['unique_ips']}"
    assert data["top_path"] == "/index.html", f"Expected top_path '/index.html', got '{data['top_path']}'"
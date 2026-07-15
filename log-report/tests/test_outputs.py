from pathlib import Path

# pulled from solution_hint.py
import json, re
from collections import Counter

LOG_PATH = Path("/app/access.log")
REPORT_PATH = Path("/app/report.json")

def _expected():
    paths, ips, total = Counter(), set(), 0
    with open(LOG_PATH) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            total += 1
            ips.add(line.split()[0])
            m = re.search(r'"(?:GET|POST|PUT|DELETE|HEAD|PATCH) (\S+) ', line)
            if m:
                paths[m.group(1)] += 1
    top_path = paths.most_common(1)[0][0] if paths else None
    return {"total_requests": total, "unique_ips": len(ips), "top_path": top_path}

def test_report_exists_and_valid_json():
    """Criterion 1: /app/report.json exists and contains valid JSON."""
    assert REPORT_PATH.exists(), "no report.json found at /app/report.json"
    json.loads(REPORT_PATH.read_text())  # raises if not valid JSON


def test_total_requests_correct():
    """Criterion 2: total_requests is an integer count of all non-empty log lines."""
    data = json.loads(REPORT_PATH.read_text())
    expected = _expected()
    assert data.get("total_requests") == expected["total_requests"], (
        f"total_requests: expected {expected['total_requests']}, got {data.get('total_requests')}"
    )


def test_unique_ips_correct():
    """Criterion 3: unique_ips is an integer count of distinct client IP addresses."""
    data = json.loads(REPORT_PATH.read_text())
    expected = _expected()
    assert data.get("unique_ips") == expected["unique_ips"], (
        f"unique_ips: expected {expected['unique_ips']}, got {data.get('unique_ips')}"
    )


def test_top_path_correct():
    """Criterion 4: top_path is the most frequently requested path."""
    data = json.loads(REPORT_PATH.read_text())
    expected = _expected()
    assert data.get("top_path") == expected["top_path"], (
        f"top_path: expected {expected['top_path']}, got {data.get('top_path')}"
    )
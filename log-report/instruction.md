There is an access log in the working directory (app/access.log).
Analyze the traffic and summarize what you find — how many requests there were, the clients involved, and which pages were popular. Save your findings so they can be reviewed. Save the JSON report to /app/report.json.

Success criteria (checked by verifier in tests/test_outputs.py)
1. /app/report.json exists and contains valid JSON.
2. total_requests (integer count of all non-empty lines in log) exists and is valid.
3. unique_ips (integer count of distinct IP addresses) exists and is valid
4. top_path (string giving most common request path) exists and is valid
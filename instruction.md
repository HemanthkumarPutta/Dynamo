# Traffic Analysis Log Report

Analyze the Apache-style access log file located at `/app/access.log` to summarize the traffic information. 

### Success Criteria:
1. The agent must create an output report file at `/app/report.json`.
2. The file `/app/report.json` must be formatted as a valid JSON object.
3. The JSON object must contain correct traffic parsing statistics with the following key-value pairs:
   - `"total_requests"`: The total number of requests in the log (integer, expected: `6`).
   - `"unique_ips"`: The number of unique IP addresses (integer, expected: `3`).
   - `"top_path"`: The most frequently requested path (string, expected: `"/index.html"`).
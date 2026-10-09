# Python to Splunk HEC Demo

A small Python example that sends a single sample JSON event to a Splunk HTTP
Event Collector (HEC) endpoint. It demonstrates the shape of a HEC event
request; it does **not** monitor a system, detect malicious activity, or block
an IP address. The event values in `app.py` are illustrative.

## Requirements

- Python 3
- A Splunk instance with HTTP Event Collector enabled
- A HEC token and the instance's HEC endpoint URL
- Network access from this machine to the Splunk endpoint

## Setup

Clone the repository, then create and activate a virtual environment:

```bash
git clone <repository-url>
cd <repository-directory>
python3 -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell, activate the environment with:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the dependency:

```bash
python -m pip install requests
```

## Configure and run

In `app.py`, set `SPLUNK_URL` to your HEC event endpoint and `HEC_TOKEN` to
your HEC token. The endpoint usually ends in
`/services/collector/event`. Do not commit real tokens or other credentials.

Run the example:

```bash
python app.py
```

The script submits one event with example fields such as `status`,
`attacker_ip`, and `threat_score`. Replace those values with appropriate
non-sensitive test data for your environment.

## Security note

The current example passes `verify=False` to `requests.post`, which disables
TLS certificate verification. This makes the connection vulnerable to
man-in-the-middle attacks. Do not use this setting with real credentials or
sensitive event data. Enable certificate verification before using the script
outside a disposable test environment.

The HEC token is currently configured in the source file. Keep it private and
rotate it immediately if it is exposed. For a production-ready integration,
load secrets from a secure secret store or environment configuration and add
appropriate timeouts, error handling, and tests.

## License

This project is distributed under the MIT License. See [LICENSE](LICENSE).

## Happy Hacking

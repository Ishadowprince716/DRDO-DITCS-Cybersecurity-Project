# Setup Guide

This guide explains the steps to deploy and configure the DRDO DITCS Cybersecurity System.

1. Clone the repository:
   ```bash
   git clone https://github.com/Ishadowprince716/DRDO-DITCS-Cybersecurity-Project.git
   cd DRDO-DITCS-Cybersecurity-Project/src
   ```

2. Set up Python environment and install dependencies:
   ```bash
   python3 -m venv env
   source env/bin/activate
   pip install -r requirements.txt
   ```

3. Configure environment variables if needed using `scripts/setup_env.sh`.

4. Run the server:
   ```bash
   python main.py
   ```

5. Access API endpoints as documented in README.md.

6. For automated audits, run `scripts/audit_schedule.py` in a separate terminal.

7. Refer to `docs/*` for architecture and policy details.

For production deployment, customize `scripts/deploy.sh` as per environment.

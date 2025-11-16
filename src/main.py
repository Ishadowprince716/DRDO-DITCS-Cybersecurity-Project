from flask import Flask
from modules.network_management.scanner import scan_network
from modules.audit_management.audit_runner import run_audit
from modules.policy_enforcement.policy_loader import load_policies
from modules.cyber_defense.threat_detection import detect_threats

app = Flask(__name__)

@app.route('/')
def home():
    return 'DRDO DITCS Cybersecurity System Running'

@app.route('/network-scan')
def network_scan():
    result = scan_network()
    return {'status':'success','scan_result':result}

@app.route('/run-audit')
def audit_run():
    report = run_audit()
    return {'status':'success','audit_report':report}

@app.route('/load-policies')
def load_security_policies():
    policies = load_policies()
    return {'status':'success','policies':policies}

@app.route('/detect-threats')
def detect_security_threats():
    threats = detect_threats()
    return {'status':'success','threats':threats}

if __name__ == '__main__':
    app.run(debug=True)

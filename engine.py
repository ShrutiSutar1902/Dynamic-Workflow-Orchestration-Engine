import json
import yaml
import datetime

# -------- LOAD WORKFLOW (YAML) -------- #
with open("workflow.yaml") as f:
    workflow = yaml.safe_load(f)

# -------- LOAD REQUEST -------- #
with open("request.json") as f:
    request = json.load(f)

current_stage = workflow["start_stage"]
path = [current_stage]
roles = []
transition_used = None

# -------- AUDIT LOG FUNCTION -------- #
def log_audit(message):
    with open("audit.log", "a") as log_file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"[{timestamp}] {message}\n")

log_audit("Workflow execution started")

while True:
    stage_data = workflow["stages"][current_stage]

    role = stage_data.get("assigned_role", "N/A")
    roles.append(role)

    log_audit(f"Entered stage: {current_stage} | Assigned role: {role}")

    if "final_status" in stage_data:
        final_status = stage_data["final_status"]
        reason = stage_data.get("reason", "No reason provided")
        log_audit(f"Final Status: {final_status} | Reason: {reason}")
        break

    moved = False

    transitions = stage_data.get("transitions", [])
    transitions = sorted(transitions, key=lambda x: x.get("priority", 999))

    for transition in transitions:
        try:
            if eval(transition["condition"], {}, request):
                transition_used = transition.get("name", "Unnamed Rule")
                log_audit(f"Triggered Rule: {transition_used}")
                current_stage = transition["next_stage"]
                path.append(current_stage)
                moved = True
                break
        except Exception as e:
            log_audit(f"Error evaluating condition: {transition['condition']} | Error: {e}")

    if not moved:
        final_status = "FAILED"
        reason = "No rule matched"
        log_audit("No valid transition found. Workflow failed.")
        break

log_audit("Workflow execution completed")

# -------- OUTPUT -------- #
print("\nWorkflow Execution Report")
print("--------------------------")

print("Workflow Path:")
print(" → ".join(path))

print("\nHandled By:")
print(" → ".join(roles))

if transition_used:
    print("\nTriggered Rule:", transition_used)

print("\nFinal Status:", final_status)
print("Reason:", reason)
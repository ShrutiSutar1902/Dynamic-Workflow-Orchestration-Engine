# Dynamic Workflow Orchestration Engine

## 📌 Overview

This project is a configuration-driven workflow orchestration engine that dynamically evaluates business rules defined in YAML configuration files. 

The system simulates enterprise-grade approval workflows such as insurance claims, loan processing, or compliance validation systems.

Instead of hardcoding logic in the application, all workflow stages, transitions, conditions, and roles are externally defined in structured configuration files.

---

## 🚀 Key Features

- YAML-based workflow configuration
- Dynamic rule evaluation
- Priority-based transition handling
- Role assignment per stage
- Final decision reasoning
- Audit log generation
- Separation of business logic and application logic

---

## 🏗 Architecture

User Input (request.json)  
↓  
Load Workflow Configuration (workflow.yaml)  
↓  
Evaluate Transition Conditions  
↓  
Move Across Stages Dynamically  
↓  
Generate Final Status + Audit Log  

---

## 📂 Project Structure


workflow_engine/
│
├── workflow.yaml # Workflow configuration
├── request.json # Input request data
├── engine.py # Core execution engine
├── audit.log # Generated execution log
└── README.md


---

## ⚙ Configuration Example (workflow.yaml)

Workflow stages, transitions, and rules are defined in YAML format:

```yaml
start_stage: Initial Review

stages:
  Initial Review:
    assigned_role: Analyst
    transitions:
      - name: Standard Processing
        condition: amount >= 50000
        next_stage: Manager Review
        priority: 1

Modifying the YAML file changes workflow behavior without changing the application code.

▶ How to Run
1️⃣ Install Dependencies
pip install pyyaml
2️⃣ Run the Engine
python engine.py

or

py engine.py
📝 Sample Output
Workflow Execution Report
--------------------------
Workflow Path:
Initial Review → Manager Review → Escalation

Handled By:
Analyst → Manager → Senior Manager

Triggered Rule: High Risk Escalation

Final Status: ESCALATED
Reason: High risk detected
📊 Audit Logging

Every execution generates an audit trail inside:

audit.log

This ensures traceability of:

Stage transitions

Triggered rules

Final decisions

Execution timestamps

🔐 Security Note

The project uses eval() for dynamic condition evaluation for demonstration purposes.

In production systems, secure rule evaluation engines or expression parsers should be used instead of eval().

🎯 Use Cases

Insurance claim processing

Loan approval workflows

Compliance validation systems

Enterprise approval routing

Configurable business process management

🏆 Learning Outcomes

Configuration-driven architecture

Workflow orchestration concepts

Rule engine simulation

Separation of business logic from code

YAML-based system configuration

Audit logging implementation

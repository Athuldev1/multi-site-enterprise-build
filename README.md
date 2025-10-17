🌐 Multi-Site Enterprise Build (CCNA & L2/L3 Portfolio Project)

Illustrative topology of HQ + Branches network with VLAN segmentation, inter-VLAN routing, VPN, and automation.

🔥 Project Overview

Multi-Site Enterprise Build is a comprehensive networking lab simulating a real-world enterprise network. The project evolves from a basic LAN setup to a multi-site, fully automated, secure network integrating routing, switching, VLANs, IPsec VPNs, and Python-based automation.

Purpose:

Bridge the gap from L1 NOC operations → L2/L3 engineer skills.

Apply CCNA concepts in a hands-on, scalable lab environment.

Demonstrate automation, troubleshooting, and documentation skills to potential employers.


🗓 Project Phases
Phase	Timeline	Focus	Outcome
Phase 1	Oct – Nov 2024	VLANs, STP, Subnetting, Inter-VLAN Routing	Fully segmented LAN, router-on-a-stick, lab-validated IP plan
Phase 2	Dec 2024 – Jan 2025	OSPF Multi-Area, IPsec VPNs, ACLs, Monitoring, Automation	Site-to-Site connectivity, scripted VLAN/ACL deployment, SNMP/Syslog integration
Phase 3	Feb – Mar 2025	BGP basics, Cloud Networking, Advanced Automation, Interview Readiness	Multi-site + cloud simulation, full automation suite, troubleshooting scenarios, interview-ready portfolio


🛠 Key Technologies

Routing & Switching: Cisco CLI, VLANs, Trunks, STP, EtherChannel, OSPF, BGP (lab)

Security: ACLs, NAT, IPsec Site-to-Site VPN

Automation: Python (Netmiko & Paramiko) for configuration push, backup, and validation scripts

Monitoring: SNMP, Syslog, simulated Splunk integration

Cloud: Basic VPC concepts and site-to-cloud VPN simulation


📂 Capstone Project Structure
Multi-Site-Enterprise-Build/
│
├─ diagrams/             # Network diagrams & topology images
├─ configs/              # Device configuration files
├─ scripts/              # Python automation scripts
│   ├─ deploy_vlan.py
│   ├─ backup_configs.py
│   └─ config_audit.py
├─ lab_notes/            # Week-by-week lab documentation
└─ README.md             # Project documentation



🚀 How the Project Evolves

Phase 1 – Foundations:

Subnetting and IP addressing planning

VLAN creation & trunk configuration

Inter-VLAN routing using router-on-a-stick

Basic STP configuration and redundancy


Phase 2 – Intermediate:

OSPF multi-area routing

IPsec VPN setup between HQ and branches

ACL configuration and NAT

Python scripts: VLAN automation, config backups


Phase 3 – Advanced:

BGP lab for upstream connectivity

Site-to-cloud VPN simulation (AWS/GCP concepts)

Advanced automation: idempotent config deployment and compliance checks

End-to-end troubleshooting scenarios



📈 Learning Outcomes

Technical Mastery: VLANs, STP, Inter-VLAN routing, OSPF, ACLs, IPsec VPNs, NAT, basic BGP, Python automation

Automation Proficiency: Scripted configuration deployment, backups, and compliance audits

Operational Credibility: Simulated enterprise network with realistic troubleshooting scenarios

Portfolio-Ready Evidence: Diagrams, configs, scripts, and lab documentation for job interviews


🎯 How to Run the Project

Install Cisco Packet Tracer or GNS3.

Clone this repository:

git clone https://github.com/<your-username>/Multi-Site-Enterprise-Build.git

Load topologies and follow lab notes for weekly setup.

Run Python automation scripts from scripts/ directory.



📖 References & Resources

David Bombal CCNA Lab Exercises

Cisco Packet Tracer

Netmiko GitHub Repository

Cisco DevNet Sandbox


⭐ Contribution

This project is for personal portfolio purposes. Pull requests or collaborations are welcome if you want to extend lab automation or add new topologies.

📝 License

MIT License — Free to use for learning and portfolio showcasing.

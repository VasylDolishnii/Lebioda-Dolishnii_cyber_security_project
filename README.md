> **NIS2 Security Operations Platform**

> **Project Overview**

> **This project aims to improve cybersecurity monitoring and support NIS2 readiness through the implementation of:**
> - **Wazuh SIEM/XDR**
> - **OpenVAS Vulnerability Scanner**
> - **VPN-secured management network**
> - **SSH hardening**
> - **Fail2Ban protection**
> - **Automated Email and Telegram alerting**
> - **Centralized log collection and analysis**

> **The platform is deployed on a Debian 12 VPS and serves as a centralized security monitoring solution.**

> **Infrastructure**

> **Wazuh Manager**

> **The Wazuh Manager is installed on a Debian 12 VPS.**

> **Security measures implemented:**
> - **SSH key authentication only**
> - **Password authentication disabled**
> - **Root login disabled**
> - **Access restricted to authorized users only**
> - **Fail2Ban protection against brute-force attacks**
> - **VPN-only administrative access**

> **Monitoring & Detection**

> **The platform provides:**
> - **Centralized log collection**
> - **Threat detection**
> - **Security event monitoring**
> - **Audit logging**
> - **Security dashboards**
> **Wazuh analyzes collected events and generates alerts when suspicious activity is detected.**

> **Vulnerability Management**

> **OpenVAS is integrated to:**
> - **Scan systems for vulnerabilities**
> - **Detect known CVEs**
> - **Identify outdated software**
> - **Support remediation efforts**

> **Automated Alerting**

> **A custom alerting bot is being developed to automatically send notifications when High or Critical alerts are generated.**

> **Notification channels:**
> - **Email**
> - **Telegram**
> **This helps administrators respond quickly to security incidents.**
> **Technologies**
> - **Debian 12**
> - **Wazuh SIEM/XDR**
> - **OpenVAS**
> - **OpenSSH**
> - **Fail2Ban**
> - **WireGuard / OpenVPN**
> - **Python**
> - **Telegram Bot API**

> **Project Roadmap**

> **Phase 1**
> - **VPS deployment**
> - **Debian 12 installation**
> - **SSH hardening**
> - **Fail2Ban configuration**

> **Phase 2**
> - **Wazuh Manager deployment**
> - **Dashboard configuration**

> **Phase 3**
> - **Wazuh Agent deployment**

> **Phase 4**
> - **OpenVAS integration**

> **Phase 5**
> - **Email & Telegram alerting bot**

> **Phase 6**
> - **MFA implementation**

> **Phase 7**
> - **Compliance dashboards and reporting**

> **Documentation**

> **Detailed deployment guides are available in the /docs directory:**
> - **Wazuh Manager Installation**
> - **Wazuh Agent Deployment**
> - **OpenVAS Configuration**
> - **Alerting Bot Setup**
> - **VPN Configuration**
> - **MFA Deployment**
> **Phase 1 – Initial VPS Setup**

> **1. VPS Deployment**
> **-Provision and initialize the VPS environment.**
> **-Verify system accessibility and network connectivity.**
> **-Configure basic operating system settings.**
> **-Validate system resources and service availability.**

> **2. Debian 12 Post-Installation Configuration**
> **Verify the pre-installed Debian 12 environment.**
> **Update package repositories and upgrade all installed packages.**
> **Apply the latest security patches and system updates.**
> **Install essential administration and troubleshooting utilities.**
> **Configure system settings required for secure operation.**
> **Prepare the operating system for security hardening and future application deployment.**
> **Baseline System Update and Tool Installation**
> apt update && apt upgrade -y && apt autoremove -y && apt install -y sudo curl wget vim git htop unzip ca-certificates gnupg lsb-release
> **3. SSH Hardening**
> **Secure SSH access according to industry best practices.**
> **Disable direct root login.**
> **Implement SSH key-based authentication.**
> **Disable password authentication entirely.**
> **Restrict remote access to authorized users only.**
> **Apply additional SSH security controls and hardening measures.**
> **SSH Key Authentication Setup**
> **mkdir -p ~/.ssh && chmod 700 ~/.ssh**
> **nano ~/.ssh/authorized_keys**
> **chmod 600 ~/.ssh/authorized_keys**
> **SSH Configuration**
> **nano /etc/ssh/sshd_config**
> **Recommended settings:**
> **PermitRootLogin no**
> **PasswordAuthentication no**
> **PubkeyAuthentication yes**
> **ChallengeResponseAuthentication no**
> **UsePAM yes**
> **MaxAuthTries 3**
> **LoginGraceTime 30**
> **Validate and Restart SSH**
> **sshd -t && systemctl restart ssh && systemctl status ssh**
> **4. Fail2Ban Configuration**
> **Install and configure Fail2Ban.**
> **Configure an aggressive SSHD jail policy.**
> **Automatically ban IP addresses attempting password-based authentication.**
> **Protect the server against brute-force and unauthorized access attempts.**
> **Verify monitoring, logging, and enforcement mechanisms.**
> **Installation**
> **apt install -y fail2ban**
> **Local Configuration**
> **cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local && nano /etc/fail2ban/jail.local**
> **Aggressive SSHD Jail**
> **```ini**
> **[sshd]**
> **enabled = true**
> **port = ssh**
> **filter = sshd**
> **backend = systemd**
> **findtime = 600**
> **maxretry = 1**
> **bantime = 86400**
> **ignoreip = 127.0.0.1/8**
> **Enable and Verify Service**
> **systemctl enable fail2ban && systemctl restart fail2ban**
> **fail2ban-client status**
> **fail2ban-client status sshd**
> **Deliverables**
> **Deployed and validated VPS environment.**
> **Updated and patched Debian 12 operating system.**
> **Essential administration and maintenance utilities installed.**
> **SSH hardened with key-based authentication only.**
> **Password authentication fully disabled.**
> **Root login disabled.**
> **Aggressive Fail2Ban SSHD jail configured (`maxretry = 1`).**
> **Secure server environment prepared for Phase 2 deployment.**
> **Expected Outcome**
> A secure and hardened Debian 12 VPS platform where SSH access is permitted exclusively through authorized cryptographic keys. Password-based authentication is completely disabled, and any unauthorized login attempts are automatically blocked through an aggressive Fail2Ban policy. The server is fully prepared for the next phase of infrastructure and application deployment.
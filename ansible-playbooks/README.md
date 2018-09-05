# Configuring an Ubuntu computer for testing

## Manual steps

The Ubuntu testing computers are managed with
[ansible](https://docs.ansible.com/ansible/latest/index.html). Ansible connects
via SSH. There are two manual steps that need to be done before ansible can
configure the computers.

1. Install `openssh-server` and configure it to allow connections on Port 22

```bash
sudo apt install openssh-server -y  # install openssh-server
sudo vi /etc/ssh/sshd_config        # uncomment Port 22
sudo service ssh restart            # restart the ssh agent
```

2. Open up department firewall. The department firewall needs to be opened up to allow connections from UWNet wireless.

## Connecting with ansible

To check if ansible can connect to the testing computers, run the following
ad hoc command.

```bash
ansible complab -i hosts -m ping -k  # prompts for SSH password
```

## Configure with ansible

The first time this playbook is run, an SSH password and a sudo password are
required. After this playbook is run, ansible will connect with an SSH key, and
not a password. The playbook also configures the sudoers file to allow for
sudoing without a password. The playbook is idempotent so it can be run
multiple times without any ill effects.

```bash
ansible-playbook configure-ubuntu.yml -i hosts -kK  # prompt for SSH and sudo passwords
ansible-playbook configure-ubuntu.yml -i hosts
```

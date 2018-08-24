# Configuring an Ubuntu computer for testing

## Manual steps

```bash
sudo apt install openssh-server -y  # install openssh-server
sudo vi /etc/ssh/sshd_config        # uncomment Port 22
sudo service ssh restart            # restart the ssh agent after editing the config
sudo ufw enable                     # enable the "uncomplicated firewall"
sudo ufw allow ssh                  # allow ssh connections on the default port 22
```

## Open up department firewall

The department firewall needs to be opened up to allow connections from UWNet wireless.

## Connecting with ansible

```bash
ansible complab -i hosts -u lupyanlab -k -m ping -e 'ansible_python_interpreter="/usr/bin/env python3"'
```

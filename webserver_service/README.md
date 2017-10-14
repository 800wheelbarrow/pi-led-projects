Files should go here:

* /usr/bin/startflask

* /etc/systemd/system/startflask.service

Then enable auto start with `systemctl enable startflask` then run `service startflask start` or reboot the machine. (that's how this is all supposed to work, anyway)

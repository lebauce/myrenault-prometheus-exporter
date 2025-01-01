Get started
===========

Get the sources
---------------

- `git clone https://github.com/lebauce/myrenault-prometheus-exporter.git`
  
  `cd myrenault-prometheus-exporter`

Install
-------

- `sudo python setup.py install`

- Create `myrenault` user

  `sudo useradd --home-dir /var/lib/myrenault-prometheus-exporter -m myrenault`

- Setup myRenault credentials

  `sudo -u myrenault -- renault-api vehicle`

- Setup `systemd` service

  - Install `systemd` service

    `sudo install -m 755 myrenault-prometheus-exporter.service /etc/systemd/system/myrenault-prometheus-exporter.service`

  - Start and enable `systemd` service

    `sudo systemctl daemon-reload`

    `sudo systemctl enable myrenault-prometheus-exporter.service`

    `sudo systemctl start myrenault-prometheus-exporter.service`


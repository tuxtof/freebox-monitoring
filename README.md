[freebox-monitoring](https://github.com/tuxtof/freebox-monitoring)
================

![](https://raw.githubusercontent.com/tuxtof/freebox-monitoring/master/screenshot.png)

test done on Freebox v5/crystal, seems not working with freebox revolution

###prerequisites:
- telegraf
- influxdb
- grafana

###list of files:
- fbx-info.py : script for retrieve freebox info to put in /etc/telegraf/
- freebox-grafana.json : freebox dashboard sample to import in grafana
- freebox.conf: telegraf sample conf to put in /etc/telegraf/telegraf.d/

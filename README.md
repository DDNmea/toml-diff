# `toml-diff`

Compatible with python 3.11+.

```
usage: toml-diff.py [-h] [-v] lhfile rhfile

Generate a detailed list of the differences between two TOML files with an
understanding of their structure

positional arguments:
  lhfile         Path to a TOML file to diff
  rhfile         Path to a TOML file to diff

options:
  -h, --help     show this help message and exit
  -v, --verbose  Toggle verbose output
```

This will flatten a TOML file before comparing it to another.

Example output:
```diff
--- config.toml
+++ other.toml
@@ -6,10 +6,10 @@
 conf_param_tunings.fsk1.quota.ost: ugp
 fsk1.mdt_list: [2, 3]
 fsk1.ost_list: [75, 79]
-global.ntp_list: ['10.8.81.138']
+global.ntp_list: ['10.8.81.136']
 host_defaults.corosync_links: ['mgmt0', 'mgmt1']
 host_defaults.grub_args: spectre_v2=off nopti
-host_defaults.lnets: ['tcp(mlxen0,mlxen1)']
+host_defaults.lnets: ['tcp(mlxen0,mlxen2)']
 mdt.device_path: /dev/ddn
 mdt.list: ['slckddn111', 'slckddn112']
 mgmt0.gateway: 192.168.0.1
@@ -128,7 +128,7 @@
 slckddnmgt11.controllers: ['172.16.71.21', '172.16.71.22']
 stonith.timeout: 5m
 stonith.type: sfa_vm
-sysctl.net.ipv4.conf.all.arp_announce: 2
+sysctl.net.ipv4.conf.all.arp_announce: 3
 sysctl.net.ipv4.conf.all.arp_ignore: 1
 sysctl.net.ipv4.conf.all.rp_filter: 0
 sysctl.net.ipv4.conf.default.arp_announce: 2
```

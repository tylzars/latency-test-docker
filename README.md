# latency-test-docker

This is a tool to measure latency in Python3 and report those statistics to an Influx Database. 

| ENV Var       | Data                                                |
|---------------|-----------------------------------------------------|
| DESTINATIONS  | Comma separated string<br>Ex: "google.com,aws.com"  |
| DATABASE-IP   | Database IP As a String<br>Ex: "192.168.1.20"       |
| DEVICE-NAME   | Name of the Device as a String<br>Ex: "FIREWALL-01" |
| DATABASE-PORT | Port for Writing to The Database<br>Ex: "8086"      |
| DATABASE-NAME | Name of the Database in InfluxDB<br>Ex: "latency"   |

Pass the hosts you would like to test latency too with the following syntax:
```docker run -e DESTINATIONS=="plex.com,google.com,aws.com,cloud.google.com" latency-test-docker```

Pass the InfluxDB Database IP, pass it with the following syntax:
```docker run -e DATABASE-IP=="192.168.1.20" latency-test-docker```
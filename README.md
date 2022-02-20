# latency-test-docker

This is a tool to measure latency in Python3 and report those statistics to an Influx Database. 

| ENV Var       | Data                                               |
|---------------|----------------------------------------------------|
| DESTINATIONS  | Comma separated string<br>Ex: "google.com,aws.com" |
| DATABASE-IP   | Database IP<br>Ex: 192.168.1.20                    |
| DEVICE-NAME   | Name of the Device<br>Ex: FIREWALL-01              |
| DATABASE-PORT | Port for Writing to The Database<br>Ex: 8086       |
| DATABASE-NAME | Name of the Database in InfluxDB<br>Ex: latency    |

A full run would look like: 
```docker run --rm -e DESTINATIONS="plex.com,google.com,aws.com,cloud.google.com" -e DATABASE-IP=192.168.1.20 -e DATABASE-PORT=8086 -e DATABASE-NAME=latency-db -e DEVICE-NAME=Test-Device latency-test-docker```

Pass the hosts you would like to test latency too with the following syntax:
```docker run -e DESTINATIONS=="plex.com,google.com,aws.com,cloud.google.com" latency-test-docker```

Pass the InfluxDB Database IP, pass it with the following syntax:
```docker run -e DATABASE-IP=="192.168.1.20" latency-test-docker```
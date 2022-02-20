# latency-test-docker

This is a tool to measure latency in Python3 and report those statistics to an Influx Database. 

Pass the hosts you would like to test latency too with the following syntax:
`docker run -e DESTINATIONS=="plex.com,google.com,aws.com,cloud.google.com" latency-test-docker`

Pass the InfluxDB Database IP, pass it with the following syntax:
`docker run -e DATABASE-IP=="192.168.1.20" latency-test-docker`
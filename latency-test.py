# Import All Required Libraries
import os
import requests
import time
from tcp_latency import measure_latency
from pythonping import ping
import ping3

# PyPing the passed host and return a dictionary of ping statistics
def ping_host(in_host):
    ping_result = ping(target=in_host, count=5, timeout=5)

    result_dict = {
        'host': host,
        'avg_latency': ping_result.rtt_avg_ms,
        'min_latency': ping_result.rtt_min_ms,
        'max_latency': ping_result.rtt_max_ms,
        'packet_loss': ping_result.packet_loss,
    }

    return result_dict

# Get vars set in Dockerfile / user input
destinations = os.environ['DESTINATIONS']
database_ip = os.environ['DATABASE-IP']
device_name = os.environ['DEVICE-NAME']
database_name = os.environ['DATABASE-NAME']
database_port = os.environ['DATABASE-PORT']

# String to write to our InfluxDB Database
url_string = "http://{}:{}/write?db={}".format(database_ip, database_port, database_name)

# Split comma seperated list of destinations
split_destinations = destinations.split(",")

# For each passed host, let us run our ping stats
while True:
    for host in split_destinations:
        measure_latency_list = measure_latency(host=host, runs=5, timeout=5)
        # Data write string
        latency_data_string = '{},device_name={} rtt_avg_ms={},rtt_min_ms={},rtt_max_ms={},packet_loss={}'.format(host, device_name, (sum(measure_latency_list) / len(measure_latency_list)), min(measure_latency_list), max(measure_latency_list), (measure_latency_list.count(5000)/len(measure_latency_list)))
        print(measure_latency_list)

        ping_host_dict = ping_host(host)
        # Data write string
        pythonping_data_string = '{},device_name={} avg_latency={},min_latency={},max_latency={},packet_loss={}'.format(host, device_name, ping_host_dict['avg_latency'], ping_host_dict['min_latency'], ping_host_dict['max_latency'],  ping_host_dict['packet_loss'])
        print(ping_host_dict)
        
        ping3_val = ping3.ping(host, unit='ms', timeout=5)
        # Data write string
        ping3_data_string = '{},device_name={} rtt_avg_ms={}'.format(host, device_name, ping3_val)
        print(ping3_val)

        # Send statistics to InfluxDB
        try:
            ping1_request = requests.post(url_string, data=latency_data_string)
            ping2_request = requests.post(url_string, data=pythonping_data_string)
            ping3_request = requests.post(url_string, data=ping3_data_string)
            time.sleep(5)
        except requests.exceptions.RequestException: # If error, wait 30 seconds and try again
            print("Oh no! Something happened writing to InfluxDB!")
            time.sleep(30)




# Import Functions
import os
from tcp_latency import measure_latency
from pythonping import ping
import ping3

# Ping the passed host and return a dictionary of ping statistics
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

# Split comma seperated list of destinations
split_destinations = destinations.split(",")

# For each passed host, let us run our ping stats
for host in split_destinations:
    print(measure_latency(host=host,runs=5, timeout=5))
    print(ping_host(host))
    print(ping3.ping(host, unit='ms'))

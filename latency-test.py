# Import Functions
import argparse
from tcp_latency import measure_latency
from pythonping import ping

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

# Get Command Line Args
parser = argparse.ArgumentParser(description='For index images analysis')
parser.add_argument('--destination', dest='destination', type=str, help='destination', metavar='destination', default='google.com')
parser.add_argument('--database_ip', dest='database_ip', type=str, help='database_ip', default="192.168.1.1")
parser.add_argument('--extra', dest='extra', type=int, help='extra', default=10)

# Parse args into Namespace
args = parser.parse_args()

# Switch Namespace into a Dictionary
args_dict = vars(args)

# Debug Statements
#print(args)
#print(d)

# Split comma seperated list of destinations
split_destinations = args_dict["destination"].split(",")

# For each passed host, let us run our ping stats
for host in split_destinations:
    print(measure_latency(host=host))
    print(ping_host(host))

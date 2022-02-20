import argparse
from tcp_latency import measure_latency

parser = argparse.ArgumentParser(description='For index images analysis')
parser.add_argument('--destination', dest='destination', type=str, help='destination', metavar='destination', default='google.com')
parser.add_argument('--database_ip', dest='database_ip', type=str, help='database_ip', default="192.168.1.1")
parser.add_argument('--extra', dest='top_n', type=int, help='top n distribution', default=10)

args = parser.parse_args()

print(args)

d = vars(args)

print(d)

print(measure_latency(host=d["destination"]))


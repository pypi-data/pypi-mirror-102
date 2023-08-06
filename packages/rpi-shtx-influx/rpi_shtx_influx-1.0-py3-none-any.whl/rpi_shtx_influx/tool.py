import os
from time import sleep
from rpi_shtx_influx.temperature import TemperatureReader
from socket import gethostname

def main():
    bucket = os.getenv('INFLUX_BUCKET')
    org = os.getenv('INFLUX_ORG')
    token = os.getenv('INFLUX_TOKEN')
    url = os.getenv("INFLUX_URL")
    hostname = gethostname()
    read_interval_s = 10

    temp = TemperatureReader(bucket, org, token, url, hostname)
    while True:
        temp.fetch_and_write_metrics()
        sleep(read_interval_s)

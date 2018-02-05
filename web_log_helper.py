#!/usr/bin/env python
"""Search a given log file for given IPs or CIDR ranges"""
import argparse
import logging
import netaddr
import requests

LOG = logging.getLogger(__name__)
logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s", level=logging.INFO)


def search_log_for_ips(log_file_search, ips):
    """Return a count of the matching log lines searching the log for the IPs provided."""
    LOG.info('Searching file for the following IPs - %s', ips)
    counter = 0
    for line in log_file_search.split('\n'):
        if line.split(' ')[0] in ips:
            counter += 1
            LOG.info(line)
    return counter


def retrieve_file_from_url(url_string):
    """Return the file content from given URL. Handle any HTTP errors at this point if required."""
    LOG.info("Retrieving file from %s", url_string)
    logging.getLogger("requests").setLevel(logging.WARNING)
    response = requests.get(url_string)
    response.raise_for_status()
    return response.content


def retrieve_file_contents(file_path):
    """Return the file contents whether it is a URL File Path or a Host File Path."""
    if file_path.startswith('http'):
        return retrieve_file_from_url(file_path)
    return open(file_path).read()


def validate_ips_from_cidr_ip(ip_input):
    """Return a list of IP strings parsing the CIDR if required."""
    ips = list(netaddr.IPNetwork(ip_input))
    return [str(ip) for ip in ips]


def initialize_args_and_retrieve_input():
    """Return the user input initializing the argument parser and documentation."""
    parser = argparse.ArgumentParser(description="""Access Log Parser.\n
                                                     You can use this tool to parse access logs and find lines that 
                                                     contain the given IP or any IP in a CIDR range""")
    parser.add_argument(
        '--log-file',
        help="""This is log file that you wish to parse. 
                You can provide a url or a file path\n
                Example: /home/sean/log.txt, https://example.com/log.txt""",
        required=True
    )
    parser.add_argument(
        '--ip',
        help="""This is the ip that you are trying to find. 
                You can search for a single IP or a range of IPs based on a CIDR\n
                Examples: 192.168.1.1, 192.168.1.1/24""",
        required=True,
    )
    return parser.parse_args()


if __name__ == '__main__':
    user_input = initialize_args_and_retrieve_input()
    log_file_path = user_input.log_file
    ip_address_list = validate_ips_from_cidr_ip(user_input.ip)
    file_contents = retrieve_file_contents(log_file_path)
    entries = search_log_for_ips(file_contents, ip_address_list)
    LOG.info('Log Search Completed. The IP/CIDR %s has %i entries in the log', user_input.ip, entries)
    if isinstance(file_contents, file):
        file_contents.close()







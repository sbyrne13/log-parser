"""Nose Test Suite for the web_log_helper module."""
from nose.tools import assert_equals, assert_raises
from requests import HTTPError
from web_log_helper import validate_ips_from_cidr_ip, retrieve_file_contents, search_log_for_ips


TEST_IP = '192.168.1.1'
TEST_CIDR = '123.45.67.64/30'
TEST_CIDR_IPS = ['123.45.67.64', '123.45.67.65', '123.45.67.66', '123.45.67.67']
TEST_FILE = 'test.log'
FAKE_URL = 'http://httpstat.us/404'


def test_single_ip_validation():
    """Test the IP validation function and assert that it works as expected for single IP."""
    ip_list = validate_ips_from_cidr_ip(TEST_IP)
    assert_equals(ip_list, [TEST_IP])
    assert_equals(len(ip_list), 1)


def test_cidr_ip_validation():
    """Test the IP validation function and assert that it works as expected for a CIDR."""
    ip_list = validate_ips_from_cidr_ip(TEST_CIDR)
    assert_equals(ip_list, TEST_CIDR_IPS)
    assert_equals(len(ip_list), len(TEST_CIDR_IPS))


def test_finding_single_ip_in_log():
    """Test that the single IP can be found in the test log file successfully."""
    ip_list = validate_ips_from_cidr_ip(TEST_IP)
    count = search_log_for_ips(retrieve_file_contents(TEST_FILE), ip_list)
    assert_equals(count, 2)


def test_finding_cidr_in_log():
    """Test that any IP from the CIDR IP list can be found in the test log file successfully."""
    ip_list = validate_ips_from_cidr_ip(TEST_CIDR)
    count = search_log_for_ips(retrieve_file_contents(TEST_FILE), ip_list)
    assert_equals(count, 1)


def test_get_contents_of_file():
    """Test that you can open a file from the given path successfully."""
    test_file = open(TEST_FILE).read()
    file_string = retrieve_file_contents(TEST_FILE)
    assert_equals(file_string, test_file)
    assert_equals([file_string.split('\n')], [test_file.split('\n')])
    assert_equals(len([file_string.split('\n')]), len([test_file.split('\n')]))


def test_get_file_from_fake_url():
    """Test that querying an incorrect file url throws a HTTPError."""
    assert_raises(HTTPError, retrieve_file_contents, FAKE_URL)

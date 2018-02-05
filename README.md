# Welcome to the log-parser!

The primary purpose of this repository is to allow users to analyse http access logs. The functionality only extends as far as allowing users to filter the logs on a given IP or a group of IPs from a given CIDR. The repo also contains a docker wrapper for this functionality as well as a docker based testsuite. 


## Prerequisites
In order to run the run_testsuite.sh script it is required that the user has a local installation of docker. The testsuite is currently docker based but it can be ran independently if you wish to pip install the *test_requirements.txt* onto your own machine.
If you wish to run the script without docker you must have the python dependencies that are contained in the *requirements.txt* installed.

## Using the script
There are two ways to run this script built into this repo. 
1. You can run directly on the host
2. You can run using the prebuilt and released docker image [here](https://hub.docker.com/r/sgpbyrne/log-parser/)

There are 2 required parameters when running this script by either of the above two means. These are as follows - 

 - --ip 
	 - This is the ip that you are trying to find. You can search for a single IP or a range of IPs based on a CIDR.  
	 > **Example**: 
	 192.168.1.1
	 192.168.1.1/24
 - --log_file
	 - This is log file that you wish to parse. You can provide a url or a file path 
	 > **Example**: 
	 /home/sean/log.txt
	 https://example.com/log.txt

This information can also be seen through the help on the CLI itself using -h or --help

## Example Usage
Below are some examples of some of the ways the script can be used
> docker run --rm sgpbyrne/log-parser --ip 192.168.1.1 --log-file https://s3.amazonaws.com/syseng-challenge/public_access.log.txt
> ./web_log_helper.py --ip 192.168.1.1/32 --log-file /etc/logs/access.log

In order to use the docker implementation for a log file on the host machine the logs directory or just the log file itself must be mounted as a volume like the following
> docker run --rm -v /home/<host-directory>/test.log:/<container-dir>/test.log sgpbyrne/log-parser --log-file /<container-dir>/test.log --ip 192.168.1.1

## Running the testsuite
The testsuite folder contains a suite of linting checks as well as a set of simple nose test cases. These are currently run using docker but with some very slight modifications they can be run without docker. The run_testsuite.sh relies on docker so in order to make use of this wrapper you need to have docker installed. 
**Example Usage**
> ./run_testsuite.sh

The above command will build the testsuite docker image and run the linters as well as the nosetests against your latest code. This can easily be ran in a CI loop as well as locally. 




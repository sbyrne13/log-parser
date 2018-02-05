#!/bin/bash

time docker build -f testsuite/Dockerfile . -t log-parser-test
if [[ $? -ne 0 ]] ; then
    echo "ERROR: Docker build failed, see above for details. Please fix and test again"
    exit 1
fi

time docker run --rm -t log-parser-test ./code_style_checks.sh
if [[ $? -ne 0 ]]
then
    exit 1
fi
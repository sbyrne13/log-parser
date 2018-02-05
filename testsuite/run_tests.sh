#!/bin/sh

cd /src/
TEST_FAILED=false
PYTHON_FILES_TO_CHECK=`find . -type f | grep '.py$'`
echo "INFO: Files that that will be checked are: $PYTHON_FILES_TO_CHECK"

echo "INFO: Running pylint"
time pylint -j 0 $PYTHON_FILES_TO_CHECK
if [[ $? -ne 0 ]] ; then
    echo "ERROR: pylint checks failed, see above for details. Please fix and test again."
    TEST_FAILED=true
fi
echo "INFO: Running pycodestyle"
time pycodestyle --ignore=E501 $PYTHON_FILES_TO_CHECK
if [[ $? -ne 0 ]] ; then
    echo "ERROR: pycodestyle checks failed, see above for details. Please fix and test again."
    TEST_FAILED=true
fi
echo "INFO: Running pep257"
time pep257 $PYTHON_FILES_TO_CHECK --explain --source --count
if [[ $? -ne 0 ]] ; then
    echo "ERROR: pep257 checks failed, see above for details. Please fix and test again."
    TEST_FAILED=true
fi

echo "INFO: Running nosetests"
time nosetests test.py
if [[ $? -ne 0 ]] ; then
    echo "ERROR: nose tests failed, see above for details. Please fix and test again."
    TEST_FAILED=true
fi

if [ "$TEST_FAILED" = true ] ; then
    echo "ERROR: testing failed, see above for details. Please fix and test again."
    exit 1
fi


#!/bin/bash

set -e

echo "TorreArchimedeBot upgrading tool"
echo "Running in `pwd`"
ssh -i tools/release/$KEY_NAME -oStrictHostKeyChecking=no $USER_TO_SSH@$ADDRESS_TO_SSH "$1"
echo "Update scheduled"

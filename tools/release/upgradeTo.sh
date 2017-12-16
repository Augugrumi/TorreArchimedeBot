#!/bin/bash

set -e

echo "TorreArchimedeBot upgrading tool"
echo "Running in `pwd`"
echo "Listing tools/release"
ls -l tools/release
ssh -i tools/release/ci_key -oStrictHostKeyChecking=no $USER_TO_SSH@$ADDRESS_TO_SSH "$1"
echo "Update scheduled"

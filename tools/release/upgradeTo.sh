#!/bin/bash

set -e

echo "TorreArchimedeBot upgrading tool"
echo "Running in `pwd`"
echo "Fixing permissions"
chmod 600 tools/release/ci_key
echo "Running ssh"
ssh -i tools/release/ci_key -oStrictHostKeyChecking=no $USER_TO_SSH@$ADDRESS_TO_SSH "./update.sh $1"
echo "Update scheduled"
rm tools/release/ci_key

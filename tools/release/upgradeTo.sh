#!/bin/bash

set -e

echo "TorreArchimedeBot upgrading tool"
ssh -i $KEY_NAME -oStrictHostKeyChecking=no $USER_TO_SSH@$ADDRESS_TO_SSH "$1" &>/dev/null
echo "Update scheduled"

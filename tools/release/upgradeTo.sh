#!/bin/bash

set -e

echo "Upgrading tool for TorreArchimedeBot"
ssh -i $KEY_NAME -oStrictHostKeyChecking=no $USER_TO_SSH@$ADDRESS_TO_SSH "$1"

echo "Update scheduled"

#!/bin/bash

set -e

echo "Upgrading tool for TorreArchimedeBot"
ssh -i $KEY_NAME -oStrictHostKeyChecking=no $USER_TO_SSH@$ADDRESS_TO_SSH "$TRAVIS_TAG"

echo "Update scheduled"

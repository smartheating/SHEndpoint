#!/usr/bin/env bash

export PYTHONPATH=$(pwd)/field_gateway:$(pwd)/tests:$PYTHONPATH
export CONFIG=$(pwd)/config.yaml
export LOG_LEVEL=DEBUG
export TESTING=no
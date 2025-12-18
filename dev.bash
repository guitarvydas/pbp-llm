#!/bin/bash
set -e
set -x

pushd ~/projects/pbp-dev/kernel
git checkout -- kernel0d.py
make
popd
cp ~/projects/pbp-dev/kernel/kernel0d.py pbp/kernel
make

# node ./pbp/das/das2json.mjs test.drawio

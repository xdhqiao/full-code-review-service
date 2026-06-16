#!/usr/bin/env sh
set -eu

PYTHON_BIN="${PYTHON_BIN:-python}"
DESTINATION="${1:-vendor}"
PLATFORM="${PLATFORM:-manylinux_2_17_x86_64}"
IMPLEMENTATION="${IMPLEMENTATION:-cp}"
PYTHON_VERSION="${PYTHON_VERSION:-311}"
ABI="${ABI:-cp311}"

mkdir -p "$DESTINATION"
"$PYTHON_BIN" -m pip download \
  --only-binary=:all: \
  --platform "$PLATFORM" \
  --implementation "$IMPLEMENTATION" \
  --python-version "$PYTHON_VERSION" \
  --abi "$ABI" \
  --dest "$DESTINATION" \
  -r requirements.txt

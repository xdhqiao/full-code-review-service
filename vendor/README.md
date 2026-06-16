# Offline Python Wheels

Put Python dependency wheels here before building in a closed network.

Build behavior:

- If this directory contains `.whl`, `.tar.gz`, or `.zip` packages, Docker installs dependencies with:

```bash
python -m pip install --no-index --find-links=/app/vendor -r requirements.txt
```

- If no package files are present, Docker falls back to normal online `pip install`.

To prepare wheels on an internet-connected machine:

```bash
python -m pip download \
  --only-binary=:all: \
  --platform manylinux_2_17_x86_64 \
  --implementation cp \
  --python-version 311 \
  --abi cp311 \
  --dest vendor \
  -r requirements.txt
```

For a Linux container, download wheels using the same Python version and target platform as production whenever possible.

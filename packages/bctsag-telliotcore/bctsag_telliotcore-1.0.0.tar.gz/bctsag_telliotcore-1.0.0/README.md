## Background

Command line tool and SDK for interacting with the Tellor Protocol.

The package `telliot-core` version `0.3.0` forked from:<br />
https://github.com/tellor-io/telliot-core

## Initial Setup

### Prerequisites
The following tools are expected to be installed on your system to run this project:

- Python 3.9.x
- Pip 23.3.x
- Git

### Setup

```bash
python3.9 -m venv tenv
source tenv/bin/activate
pip3.9 install .
```

NPM ganache dependency required:
```bash
npm install ganache --global
```

### Test

Install development requirements:
```bash
pip3.9 install -r requirements-dev.txt
```

Run automated testing in all environments:
```bash
tox
```

Run `py39` testing:
```bash
tox -e py39
```

Run `style` testing:
```bash
tox -e style
```

Run `typing` typing:
```bash
tox -e typing
```

### Publish

1. Create the `$HOME/.pypirc` file:
```
[pypi]
  username = __token__
  password = pypi-AgEIcHlw... (your PyPI token)
```

2. Build distribution:
```bash
python3.9 -m build
```

3. Deploy distribution to PyPI repository:
```bash
twine upload dist/*
```

## Usage

### Configuration

1. Create the default configuration files:
```bash
telliot-core config init
```

The default configuration files are created in the folder `~/telliot/` or `$HOME/telliot/`.

2. View your current configuration:
```bash
telliot-core config show
```

## Contributing

Bug reports and pull requests are welcome on GitHub at:<br />
https://github.com/BCTSAG/tellor

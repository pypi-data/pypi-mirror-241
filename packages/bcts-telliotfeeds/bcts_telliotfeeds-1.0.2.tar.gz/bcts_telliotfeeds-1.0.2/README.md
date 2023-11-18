## Background

Reporting tools and datafeeds for Tellor oracles.

The package `telliot-feeds` version `0.1.14` forked from:<br />
https://github.com/tellor-io/telliot-feeds

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

### Using Docker

1. Create & start container in the background:
```bash
docker compose up -d
```

2. Execute commands in a running Docker container:
```bash
docker exec -it telliot sh
```

### Configuration

1. Create the default configuration files:
```bash
telliot config init
```

The default configuration files are created in a folder called `telliot` in the user's home folder.

2. View your current configuration:
```bash
telliot config show
```
### Using Telliot

1. Add Reporting account:
```bash
telliot account add fantomacct1 5d18c4aabe8f0ee841e2e0ee504c7d9ec98d2aa9edb2e44d5e8825ec0670f896 4002
```

2. Check Reporting account:
```bash
telliot account find
```

3. Using StakingToken smart contract address provided below, mint 1000 TTRB tokens to the `fantomacct1` account:<br />
`0x8e4E5eDab27Df5a93B25AC3a62b80beec1CfEBd0`


4. Report data with the `fantomacct1` account to the Tellor Oracle:
```bash
telliot report -a fantomacct1 -ncr -qt trb-usd-spot
```

## Contributing

Bug reports and pull requests are welcome on GitHub at:<br />
https://github.com/SELISEdigitalplatforms/l3-solidity-bcts-tellor

# mitre-attack  ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mitre-attack) ![PyPI - Wheel](https://img.shields.io/pypi/wheel/mitre-attack) ![PyPI - Downloads](https://img.shields.io/pypi/dm/mitre-attack)

An API client for the MITRE ATT&amp;CK framework (🕵️👾 🐍)

## Tutorial

### REST API server

To start the REST API server: 

```shell
$ poetry run server
```

#### Tactics

To list tactics:

```shell
$ curl 127.0.0.1:5000/tactics | jq
```

#### Techniques

To list techniques:

```shell
$ curl 127.0.0.1:5000/techniques | jq
```

#### Groups

To list groups:

```shell
$ curl 127.0.0.1:5000/groups | jq
```

#### Software

To list software:

```shell
$ curl 127.0.0.1:5000/software | jq
```

#### Malware families

To list malware families:

```shell
$ curl 127.0.0.1:5000/malware | jq
```

#### Tools

To list tools:

```shell
$ curl 127.0.0.1:5000/tools | jq
```

#### Mitigations

To list mitigations:

```shell
$ curl 127.0.0.1:5000/mitigations | jq
```

### Command line interface

The following command line options are available:

```shell
$ poetry run mitre-attack
Usage: mitre-attack [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  groups         Query or count groups.
  malware        Query or count malware.
  mitigations    Query or count mitigations.
  relationships  Query or count relationships.
  software       Query or count malware and tools.
  tactics        Query or count tactics.
  techniques     Query or count techniques.
  tools          Query or count tools.
```

#### Tactics

To list tactics:

```shell
$ poetry run mitre-attack tactics get-tactics | jq
```

#### Techniques

To list techniques:

```shell
$ poetry run mitre-attack techniques get-techniques | jq
```

#### Groups

To list groups:

```shell
$ poetry run mitre-attack groups get-groups | jq
```

#### Software

To list software:

```shell
$ poetry run mitre-attack software get-software | jq
```

#### Malware families

To list malware families:

```shell
$ poetry run mitre-attack malware get-malware-families | jq
```

#### Tools

To list tools:

```shell
$ poetry run mitre-attack tools get-tools | jq
```

#### Mitigations

To list mitigations:

```shell
$ poetry run mitre-attack mitigations get-mitigations | jq
```

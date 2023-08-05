[![pipeline status](https://gitlab.com/biomedit/gpg-lite/badges/master/pipeline.svg)](https://gitlab.com/biomedit/gpg-lite/-/commits/master)
[![coverage report](https://gitlab.com/biomedit/gpg-lite/badges/master/coverage.svg)](https://gitlab.com/biomedit/gpg-lite/-/commits/master)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# gpg python binding (incomplete functionality)

A python `gpg` module written from scratch.

The goals are:
* Reduced functionality to reduce maintenance costs
* Use custom functions for keyserver access (inconsistent behaviour of
  the gpg binary accross versions)
* Support for 🐧, 🍏, Windows
* Support as many gpg versions as possible

## Installation

### From `PyPI`

It's simple. Just do:

```bash
[sudo] pip install [--user] gpg-lite
```

### From git

To install this package from this git repository, do:

```bash
git clone https://gitlab.com/biomedit/gpg-lite.git
cd gpg-lite
./setup.py install [--user]
```

To get started using python-gnupg's API, see the documentation,
and import the module like:

```python
import gpg_lite
```

The primary interface class you'll likely want to interact with is `gpg_lite.GPGStore`

```python
gpg_store = gpg_lite.GPGStore(config_dir='/home/user/.gnupg')
gpg_store.gen_key(
    key_type='RSA',
    key_length=4096,
    full_name="Chuck Norris",
	email="chuck.norris@roundhouse.gov",
	passphrase="Chuck Norris does not need one - the password needs him")
keys = gpg_store.list_pub_keys()
print(keys)
```

**Note**: Make sure that the `/home/user/.gnupg` directory exists.

## Bug Reports / Feature Requests / Contributing

Our bugtracker can be found on **GitLab** https://gitlab.com/biomedit/gpg-lite/issues. 

Public comments and discussions are also welcome on the bugtracker.

Patches are always welcome 🤗!
Take into account that we use a special format for commit messages.
This is due to our release management and to auto generate our
changelog.
Here are our [guidelines](./CONTRIBUTING.md).
Also each change has to pass our CI [pipeline](.gitlab-ci.yml)
including:

* [black](https://pypi.org/project/black/) code formatting
* [pylint](https://pylint.org/) lints
* [unit](./test/) / [integration](./integration_test/) tests
* [bandit](https://pypi.org/project/bandit/) vulnerability checks (each security warning which cannot be
  avoided has to be justified)
* [mypy](http://mypy-lang.org/) type checking

## Supported GPG versions

We officially support all **GPG** versions starting from _v2.2.8_.
Inofficially, we also try to support _v2.0.22_.

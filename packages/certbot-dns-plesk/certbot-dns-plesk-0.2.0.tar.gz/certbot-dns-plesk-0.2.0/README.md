certbot-dns-plesk
============

![PyPI - Status](https://img.shields.io/pypi/status/certbot-dns-plesk.svg)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/certbot-dns-plesk.svg)
[![Coverage Status](https://coveralls.io/repos/gitlab/spike77453/certbot-dns-plesk/badge.svg?branch=master)](https://coveralls.io/gitlab/spike77453/certbot-dns-plesk?branch=master)

plesk Authenticator plugin for [Certbot](https://certbot.eff.org/).

This plugin is built from the ground up and follows the development style and life-cycle
of other `certbot-dns-*` plugins found in the
[Official Certbot Repository](https://github.com/certbot/certbot).

Installation
------------

```
pip install certbot-dns-plesk
```

Verify:

```
$ certbot plugins --text

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
* dns-plesk
Description: Obtain certificates using a DNS TXT record by using the plesk dns api.
Interfaces: IAuthenticator, IPlugin
Entry point: dns-plesk = certbot_dns_plesk.dns_plesk:Authenticator

...
```

Configuration
-------------

The credentials file e.g. `~/plesk-credentials.ini` should look like this:

```
dns_plesk_username = your-username
dns_plesk_password = secret
dns_plesk_api_url = https://plesk-api-host:8443
```

Usage
-----


```
certbot certonly \
        --authenticator dns-plesk  \
        --dns-plesk-credentials plesk.in ~/plesk-credentials.ini \
        --dns-plesk-propagation-seconds 30 \
        -d your-domain
```

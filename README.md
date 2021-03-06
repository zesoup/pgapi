Disclaimer
==========

*This project is currently in development. Do not use it on production environments!*

About
=====

`pgapi` tries to be a simple but useful REST API for Debian based
PostgreSQL Systems.  It offers a way to create, delete and control
PostgreSQL clusters via HTTP requests.

Requirements
============

The user starting the api needs privileges to run commands as user
postgres using sudo.  The user postgres needs sudo privileges to start
and stop a cluster via pg_ctlcluster as user root.

A example sudo configuration could look like this:

```
<myuser>	ALL=(postgres:ALL) NOPASSWD:ALL
postgres	ALL=(root) NOPASSWD: /usr/bin/pg_ctlcluster *
```

Getting Started
===============

1. checkout this git repository:

   ```
   git clone https://github.com/credativ/pgapi
   ```

2. change to the new directory:

   ```
   cd pgapi
   ```

3. start the standalone service:

   ```
   pgapi/api.py --config-file conf/pgapi.conf
   ```

4. get a list of all clusters:

   ```
   curl -X GET http://127.0.0.1:15432/cluster/
   ```
   
Installation
============

`python setuptools` is within the installation process.

```
python3 setup.py build
python3 setup.py install
```
   
Examples
========

* get a list of all clusters:
  `curl -X GET http://127.0.0.1:15432/cluster/`
  
* create a new cluster with version 9.6 and name foobar:
  `curl -X POST http://127.0.0.1:15432/cluster/9.6/foobar`

* change port of the 9.6/foobar cluster:
  ```
  curl -i -X PATCH \
       -H "Content-Type: application/json" \
       -d '{"config": {"port": 8432}}' \
       http://127.0.0.1:15432/cluster/9.6/foobar
  ```
  
* restart the 9.6/foobar cluster:
  ```
  curl -i -X PATCH \
       -H "Content-Type: application/json" \
	   -d '{"state": "restart"}' \
       http://127.0.0.1:15432/cluster/9.6/foobar
  ```

* change port once more and restart at once:
  ```
  curl -i -X PATCH \
       -H "Content-Type: application/json" \
       -d '{"config": {"port": 9432}, "state": "restart"}' \
       http://127.0.0.1:15432/cluster/9.6/foobar
  ```

* delete the cluster 9.6/foobar:
  `curl -X DELETE http://127.0.0.1:15432/cluster/9.6/foobar`

Python Dependencies
===================

See requirements.txt for a full list of dependencies.

Other Dependencies
==================

Beside the above listed python dependencies, it's expected that
postgresql-common is available on the system.  pgapi makes heavy use
of postgresql-common and some of the tools that's shipped with it.

Licence
=======

This project uses the MIT Licence.

Debugging
=========

If something don't work like expected, try to start the api server in debug mode:
```
pgapi/api.py --config-file conf/pgapi.conf --debug
```

Tests
=====

To run all unit tests execute `runtests.sh`

```
$ ./runtests.sh
```

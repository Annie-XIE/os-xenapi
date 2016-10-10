======
os-xenapi
======

The common XenAPI library for OpenStack projects.

This library contains XenServer XenAPI specific code commonly used in
OpenStack projects. The library can be used in any other OpenStack projects
where it is needed.

* Free software: Apache license
* Documentation: http://docs.openstack.org/developer/os-xenapi
* Source: http://git.openstack.org/cgit/openstack/os-xenapi
* Bugs: http://bugs.launchpad.net/os-xenapi


How to Install
--------------

os-xenapi is released on Pypi, meaning that it can be installed and upgraded via
pip. To install os-xenapi, run the following command:

::

    pip install os-xenapi

To upgrade os-xenapi, run the following command:

::

    pip install -U os-xenapi

Note that the first OpenStack release to use os-xenapi is ??. Previous
releases do not benefit from this library.

Tests
-----

You will have to install the test dependencies first to be able to run the
tests.

::

    pip install -r requirements.txt
    pip install -r test-requirements.txt

You can run the unit tests with the following command.

::

    nosetests os_xenapi\tests


How to contribute
-----------------

To contribute to this project, please go through the following steps.

1. Clone the project and keep your working tree updated.
2. Make modifications on your working tree.
3. Run unit tests.
4. If the tests pass, commit your code.
5. Submit your code via ``git review``.
6. Check that Jenkins and the Citrix XenServer CI pass on your patch.
7. If there are issues with your commit, ammend, and submit it again via
   ``git review``.
8. Wait for the patch to be reviewed.


Features
--------

os-xenapi is currently used in the following OpenStack projects:

* ??
* ??

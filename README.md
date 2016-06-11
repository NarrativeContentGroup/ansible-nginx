nginx-pagespeed
=========

Compiles Nginx, optionally builds pagespeed module.


Requirements
------------

N/A


Role Variables
--------------

nginx_pagespeed_version -- version of pagespeed to download and compile
nginx_user -- user to run nginx service as
nginx_version -- version of nginx to download and compile
nginx_worker_processes -- number of worker processes to start


Dependencies
------------

N/A


Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: web_server
      roles:
         - role: mnn.nginx-pagespeed
           nginx_version: 1.10.1
           nginx_pagespeed_version: 1.9.32.14


License
-------

MIT


Author Information
------------------

This role was written by Justin Caratzas <jcaratzas@mnn.com> for Narrative Content Group.

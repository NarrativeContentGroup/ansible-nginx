nginx-pagespeed
=========

Installs the pagespeed module for Nginx.


Requirements
------------

N/A


Role Variables
--------------

nginx_version -- version of nginx to compile
nginx_pagespeed_version -- version of pagespeed module to install


Dependencies
------------

mnn.nginx -- for handlers and init script.


Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: web_server
      roles:
         - role: mnn.nginx
         - role: mnn.nginx-pagespeed
           nginx_version: 1.10.1
           nginx_pagespeed_version: 1.9.32.14

License
-------

MIT


Author Information
------------------

This role was written by Justin Caratzas <jcaratzas@mnn.com> for Narrative Content Group.

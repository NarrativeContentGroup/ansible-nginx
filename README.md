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
           nginx_build_options:
               add-module: '{{ nginx_build_dir }}/ngx_pagespeed-release-{{ nginx_pagespeed_version }}-beta/'
               with-http_stub_status_module:


compiles nginx with pagespeed and http_stub_status_module options

License
-------

MIT


Author Information
------------------

This role was written by Justin Caratzas <jcaratzas@mnn.com> for Narrative Content Group.

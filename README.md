nginx-pagespeed
=========

Compiles Nginx, optionally builds pagespeed module.


Requirements
------------

N/A


Role Variables
--------------

see defaults/main.yml, also:

    nginx_pagespeed_enabled: true (also build and configure pagespeed module)
    nginx_pagespeed_version: 1.11.33.2
    nginx_version: 1.10.1
    nginx_worker_processes: 2

Most of the variables are self-explanatory, but `nginx_build_options` deserves
an explanation, as it is the primary role of this role. `nginx_build_options` is
a dictionary that passes each item as --<key>=<value>, and keys with no value
are treated as switches.:

    nginx_build_options:
      conf-path: "{{ nginx_conf_path }}"
      error-log-path: "{{ nginx_log_path }}/error.log"
      http-client-body-temp-path: "{{ nginx_lib_path }}/body"
      http-fastcgi-temp-path: "{{ nginx_lib_path }}/fastcgi"
      http-proxy-temp-path: "{{ nginx_lib_path }}/proxy"
      http-scgi-temp-path: "{{ nginx_lib_path }}/scgi"
      http-uwsgi-temp-path: "{{ nginx_lib_path }}/uwsgi"
      http-log-path: "{{ nginx_log_path }}/access.log"
      lock-path: /var/lock/nginx.lock
      pid-path: /run/nginx.pid
      prefix: "{{ nginx_prefix }}"
      with-http_gzip_static_module:
      with-http_realip_module:
      with-http_stub_status_module:
      with-ipv6:
      with-pcre-jit:



Dependencies
------------

N/A


Example Playbook
----------------

standard install

    - hosts: web_servers
      roles:
         - role: mnn.nginx-pagespeed
           nginx_pagespeed_enabled: no
           nginx_version: 1.10.1

compiles nginx with pagespeed and http_stub_status_module options

License
-------

MIT


Author Information
------------------

This role was written by Justin Caratzas <jcaratzas@mnn.com> for Narrative Content Group.

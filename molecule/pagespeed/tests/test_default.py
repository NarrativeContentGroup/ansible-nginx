import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_nginx_service(host):
    nginx_service = host.service('nginx')

    assert nginx_service.is_running
    assert nginx_service.is_enabled


def test_nginx_conf(host):
    nginx_conf = host.file('/etc/nginx/nginx.conf')

    assert nginx_conf.exists
    assert nginx_conf.group == 'root'
    assert nginx_conf.user == 'root'

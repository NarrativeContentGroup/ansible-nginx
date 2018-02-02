import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_nginx_service(Service):
    nginx_service = Service('nginx')

    assert nginx_service.is_running
    assert nginx_service.is_enabled


def test_nginx_conf(File):
    nginx_conf = File('/etc/nginx/nginx.conf')

    assert nginx_conf.exists
    assert nginx_conf.group == 'root'
    assert nginx_conf.user == 'root'

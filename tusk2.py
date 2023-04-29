import salt.client

client = salt.client.LocalClient()

minion_name = 'name1'

nginx_dist_path = '/tmp/nginx.tar.gz'

install_cmd = 'apt-get install -y nginx.tar.gz'

result = client.cmd(minion_name, 'cmd.run', [f'cd {nginx_dist_path} && {install_cmd}'])

print(result)



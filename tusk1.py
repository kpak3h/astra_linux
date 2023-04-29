import salt.client

client = salt.client.LocalClient()

minion_name = 'name1'

nginx_dist_path = '/tmp/nginx.tar.gz'

target_path = '/tmp'

result = client.cp.get_file(nginx_dist_path, f'{minion_name}:{target_path}')

print(result)



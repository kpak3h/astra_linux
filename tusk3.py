import salt.client

client = salt.client.LocalClient()

minion_name = 'name1'

index_html_path = '/tmp/nginx.tar.gz/nginx-1.23.4/html/index.html'

new_text = 'Hello Greenatom'

result = client.cmd(minion_name, 'file.replace', [index_html_path, new_text])

print(result)




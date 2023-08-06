import os
import time
import boto.ec2
import json
import pkg_resources

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

try:
    from urllib.error import HTTPError
except:
    from urllib2 import HTTPError


VERSION = pkg_resources.get_distribution('keyserver-client').version

KEYSERVER_URL = 'https://keyserver.rg-infra.com'
REFRESH_INTERVAL = 30

def _instance_id():
    return urlopen('http://169.254.169.254/latest/meta-data/instance-id').read()

def _tags(instance_id):
    region = json.loads(urlopen('http://169.254.169.254/latest/dynamic/instance-identity/document').read())['region']
    conn = boto.ec2.connect_to_region(region)
    return conn.get_all_instances(instance_ids=[instance_id])[0].instances[0].tags

def get_ssh_authorized_keys(keyserver, tags, is_bastion, instance_id):
    qs = urlencode({
        'client_version': VERSION,
        'instance_id': instance_id
    })
    if is_bastion:
        keyfile = urlopen(keyserver + '/servers/get_bastion_keys/?%s' % qs).read().decode('utf8')
    else:
        keyfile = urlopen(keyserver + '/servers/get_keyfile/%s/?%s' % (tags, qs)).read().decode('utf8')
    return keyfile

def write_to_keyfile(content):
    with open(os.path.expanduser('~/.ssh/authorized_keys'),'w') as f:
        f.write(content)

def main():
    while True:
        instance_id = _instance_id()
        tags = _tags(instance_id)
        project = tags.get('project') or tags.get('Project')
        is_bastion = tags.get('IsBastion') or tags.get('Role', '').lower() == 'bastion'
        try:
            keys = get_ssh_authorized_keys(KEYSERVER_URL, project, is_bastion, instance_id)
        except HTTPError as e:
            print("Error retrieving keys for project %s, (Is a bastion? %s)" % (project, is_bastion))
            continue
        write_to_keyfile(keys)
        time.sleep(REFRESH_INTERVAL)

if __name__ == '__main__':
    main()

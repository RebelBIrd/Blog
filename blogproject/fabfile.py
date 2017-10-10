from fabric.api import env, run
from fabric.operations import sudo

GIT_REPO = "https://github.com/RebelBIrd/Blog.git"

env.user = "root"
env.password = 'FORlove529'

env.hosts = ['119.23.221.255']

env.port = '22'

def deploy():
	source_folder = 'home/rebelbird/sites/119.23.221.255/Blog'

	run('cd %s && git pull' % source_folder)
	run("""
		cd {} &&
		../env/bin/pip install -r requirements.txt &&
		../env/bin/python3 manage.py collectsatic --noinput &&
		../env/bin/python3 manage.py migrate
		""".format(source_folder))
	sudo('restart gunicorn-119.23.221.255')
	sodu('service nginx reload')
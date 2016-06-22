import os, sys, subprocess, getpass, json, multiprocessing, shutil
from distutils.spawn import find_executable


def run_os_command(command_map):
	'''command_map is a dictionary of {'executable': command}. For ex. {'apt-get': 'sudo apt-get install -y python2.7'} '''
	success = True
	for executable, commands in command_map.items():
		print command_map.items()
		if find_executable(executable):
			if isinstance(commands, basestring):
				commands = [commands]

			for command in commands:
				returncode = subprocess.check_call(command, shell=True)
				success = success and ( returncode == 0 )

			break

	return success

def setup_bench():
	print "Downloading install.py...................."
	subprocess.call("wget https://raw.githubusercontent.com/flomente96/bench/master/playbooks/install.py", shell=True)

	print "Running playbook...................."
	subprocess.call("python install.py --develop", shell=True)


def get_erpnext(): #gets frappe-bench and erpnext
	os.chdir('frappe-bench/')
	print os.getcwd()
	success = subprocess.call("bench get-app erpnext https://github.com/flomente96/erpnext.git", shell=True)
	print "Fetching from https://github.com/flomente96/erpnext.git repository FAILED!"
	print os.getcwd()
	print success

	if success == True: #creates new site
		success = run_os_command(
			{'bench': 'bench new-site erpnext'}
		)
	else:
		print "Creating new site FAILED!"

	if success == True: #installs erpnext to site
		success = run_os_command(
			{'bench': 'bench --site erpnext install-app erpnext'}
		)
	else:
		print "Installing erpnext to new site FAILED!"

	if success == True:
		print "Erpnext installed in the new site!"

def bench_start():
	print os.getcwd()
	subprocess.call("bench start", shell=True)

setup_bench()
get_erpnext()
# bench_start()

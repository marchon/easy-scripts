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

# def get_frappe():
#     # subprocess.call("sudo mv frappe-bench/apps/frappe frappe-bench/frappe", shell=True)
#     os.chdir('frappe-bench/')
#     subprocess.call("bench get-app frappe https://gitlab.com/modernmachines/erpnext-mirror.git", shell=True)

def get_erpnext():
	os.chdir('frappe-bench/')
	print os.getcwd()
	# success = subprocess.call("bench get-app erpnext https://github.com/frappe/erpnext.git", shell=True)
	if success == True:
		success = subprocess.call("bench new-site testsite")
	else:
		print "Fetching from https://github.com/frappe/erpnext repository FAILED!"
	if success == True:
		success = subprocess.call("bench --site testsite install-app erpnext")
	else:
		print "Creating new site FAILED!"
	if success == True:
		print "Erpnext installed in the new site!"

def create_new_site():
	os.chdir('~/frappe-bench/')
	# success = run_os_command(
	# 	{'bench': 'bench new-site erpnext-mirror'}
	# )
	subprocess.call("bench new-site erpnext-mirror")
	return success

def bench_start():
	os.chdir('frappe-bench/')
	subprocess.call("bench start", shell=True)


# setup_bench()
# get_frappe()		#wala na dapat ni siya kay ang bench nagpoint na man padung sa gitlab na repo
get_erpnext()
# create_new_site()
bench_start()

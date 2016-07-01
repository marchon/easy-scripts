#!/bin/bash
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

def setup_frappe():
	#comment this out if you want to use the setup that points to the original repo
	# print "Downloading setup_frappe.sh...................."
	# subprocess.call("wget https://raw.githubusercontent.com/flomente96/bench/master/install_scripts/setup_frappe.sh", shell=True)
	print "Running setup_frappe.sh...................."
	os.system("sudo bash setup_frappe.sh --setup-production")

def delete_benchlog():
	print "Deleting bench_logs...................."
	subprocess.call("rm -r ~/frappe-bench/logs/bench.log", shell=True)

def bench_start():
	print "Running bench_start...................."
	subprocess.call("bench start", shell=True)

setup_frappe()
delete_benchlog()
bench_start()

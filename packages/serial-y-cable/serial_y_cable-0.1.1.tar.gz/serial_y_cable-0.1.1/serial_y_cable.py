#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = "Thomas@chriesibaum.com"
__copyright__ = "Copyright 2023, Chriesibaum GmbH"
__version__ = "0.1.1"


import os
import sys
import time
import argparse
import serial
from key_stroke import *


__usage__ = """
basic usage of serial_y_cable:

  ┌─────────────────┐                                                                     ┌────────────────────────────────┐
  │ hardware / DUT  ├──  hardware serial dev   ─────┬───────  virtual serial dev 0  ──────┤ application that controls      │
  └─────────────────┘      e.g.://dev/ttyUSB0       │          /tmp/ttyUSB0-V0            │ the hardware / DUT             │
                                                    │                                     └────────────────────────────────┘
                                                    │
                                                    │                                     ┌────────────────────────────────┐
                                                    └───────  virtual serial dev 1  ──────┤ serial terminal for monitoring │
                                                                /tmp/ttyUSB0-V0           │  - e.g. minicom, screen, etc.  │
                                                                                          └────────────────────────────────┘

serial_y_cable --serial_device /dev/ttyUSB0
"""


class Serial_y_cable():
	"""
	The Serial_y_cable class

	Basically it is a serial y cable to sniff a serial port.
	"""
	def __init__(self, serial_device_name = '/dev/ttyACM0', serial_device_baudrate = 115200, virtual_y_ends = 2):

		self.ser_port = serial.Serial(serial_device_name, serial_device_baudrate, timeout = 0.1)

		self.master_fds = {}
		self.slave_fds = {}

		for i in range(virtual_y_ends):
			master_fd, slave_fd = os.openpty()

			self.master_fds[master_fd] = master_fd
			self.slave_fds[slave_fd] = slave_fd


		i = 0
		self.slave_symlinks = {}
		for s in self.slave_fds:
			s_tty_name = os.ttyname(s)

			s_tty_name_v = f'{serial_device_name}-V{i}'
			s_tty_name_v = s_tty_name_v.replace('dev', 'tmp')

			# cleanup old symlinks, just in case the exists
			if os. path. exists(s_tty_name_v):
				os.remove(s_tty_name_v)

			print(f'  -> virtual port: {s_tty_name_v}')

			os.symlink(s_tty_name, s_tty_name_v)
			self.slave_symlinks[s_tty_name] = s_tty_name_v
			i += 1


	def run_for_ever(self):
		k = Key_Stroke()

		try:
			while True:
				in_bytes = self.ser_port.read(1000)

				if len(in_bytes) > 0:
					for m in self.master_fds:
						os.write(m, in_bytes)

				# check whether a key from the list has been pressed
				if k.check(['\x1b', 'q', 'x']):
					break
		except KeyboardInterrupt:
			pass


	def cleanup(self):
		"""
		do some house cleaning as
		- closing the serial s_port
		- remove the symlinks
		"""
		self.ser_port.close()

		for s in self.slave_symlinks:
			os.remove(self.slave_symlinks[s])


def main():
	"""
	The main function to run the serial_y_cable application
	"""

	# Instantiate the parser
	parser = argparse.ArgumentParser(description='The serial_y_cable tool')

	parser.add_argument('--version', const = True, action = 'store_const', default = False,
						help='Prints the tool version')

	parser.add_argument('--usage', const = True, action = 'store_const', default = False,
						help='Prints the tool usage')

	parser.add_argument('-D', '--serial_device',  metavar='</dev/ttyX>', type=str, default = '/dev/ttyACM0',
						help='set serial_device_name e.g /dev/ttyACM0')

	parser.add_argument('-b', '--baudrate',  metavar='<baudrate>', type=int, default = 115200,
						help='set baudrate')

	args = parser.parse_args()


	# basic args check
	if args.version:
		print(__version__)
		sys.exit(0)

	if args.usage:
		print(__usage__)
		sys.exit(0)

	print(f'use serial device {args.serial_device} and redirect it to:')

	y = Serial_y_cable(serial_device_name = args.serial_device,
					serial_device_baudrate = args.baudrate)
	y.run_for_ever()
	y.cleanup()


"""call the main function"""
if __name__ == "__main__":
   main()

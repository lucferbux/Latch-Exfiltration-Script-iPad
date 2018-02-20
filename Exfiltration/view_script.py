import ui
from latch_exfiltration import LatchExfiltration
import time
import os

latch_exfiltration = LatchExfiltration()

def get_byte(byte):
	view['label1'].text = "Writting: " + latch_exfiltration.ascii_to_string(byte)
	for index, latch in enumerate(byte):
		value = 'switch' + str((index + 1))
		view[value].value = (latch == '1')

def exfiltrate_byte(bits_string):
	"""Lock and unlock the latches acording to the binary representation of a given character
			Arguments:
			bits_string {String} -- Binary representation of an ascii character
	"""
	for index, char in enumerate(bits_string):
		latch_status = latch_exfiltration.dict_converted.get(str(index + 1), '')
		if char == '0':
			latch_exfiltration.latch.unlock_latch(latch_status)
		else:
			latch_exfiltration.latch.lock_latch(latch_status)
		#print('Sending: ' + latch_exfiltration.ascii_to_string(bits_string) + ' ---> ' + bits_string)
	get_byte(bits_string)
	latch_exfiltration.latch.lock_latch(latch_exfiltration.dict_converted.get('control', ''))

def exfiltrate_message(message):
	"""Exfiltrate the given message, first it's converted to a list of bits to lock the latches

		Arguments:
		message {String} -- Message to be exfiltrated
	"""
	while not latch_exfiltration.latch.get_operation_status(latch_exfiltration.dict_converted.get('reader', '')):
		time.sleep(0.2) 
	message_array = latch_exfiltration.read_string_to_byte(message) # secret
	for byte in message_array:
		exfiltrate_byte(byte)
		while latch_exfiltration.latch.get_operation_status(latch_exfiltration.dict_converted.get('control', '')):
			time.sleep(0.5)
	latch_exfiltration.latch.lock_latch(latch_exfiltration.dict_converted.get('end', ''))
	view['label1'].text = 'Finished'
	view['button_start'].enabled = True

		
@ui.in_background	
def start_function(sender):
	message = view['textfield1'].text
	sender.enabled = False
	exfiltrate_message(message)
	


view = ui.load_view()
view.present('sheet')




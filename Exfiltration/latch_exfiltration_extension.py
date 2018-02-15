import appex
from exfiltration_writer import LatchExfiltrationWriter

if appex.is_running_extension():
	message = appex.get_text()
	latch_writer = LatchExfiltrationWriter()
	latch_writer.exfiltrate_message(message)
	

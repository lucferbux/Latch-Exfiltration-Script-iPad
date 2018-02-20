# -*- coding: utf-8 -*-
from exfiltration_writer import LatchExfiltrationWriter
from exfiltration_reader import LatchExfiltrationReader
from latch_exfiltration import LatchExfiltration
import unittest

class KnownMessages(unittest.TestCase):
	known_messages = 	[ ("Hola que tal", ["01001000", "01101111", "01101100", "01100001", "00100000", "01110001", "01110101", "01100101", "00100000", "01110100", "01100001", "01101100"]),
						("", []),
						("Hola, que tal", ["01001000", "01101111", "01101100", "01100001", "00101100", "00100000", "01110001", "01110101", "01100101", "00100000", "01110100", "01100001", "01101100"])
						]
					
	def test_ascii_to_bytes(self):
		latch_exfiltration = LatchExfiltration(None, True)
		for ascii, bytes in self.known_messages:
			bytes_converted = latch_exfiltration.read_string_to_byte(ascii)
			print(bytes_converted)
			self.assertEqual(bytes, bytes_converted)


if __name__ == "__main__":
	unittest.main()

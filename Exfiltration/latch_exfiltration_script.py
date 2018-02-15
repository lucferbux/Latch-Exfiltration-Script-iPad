from exfiltration_reader import LatchExfiltrationReader
from exfiltration_writer import LatchExfiltrationWriter
from latch_interface import LatchInterface
import os
import argparse

def main():
    args = create_arguments()    
    if args.writer:
        message = args.writer if args.writer else ""
        latch_writer = LatchExfiltrationWriter()
        latch_writer.exfiltrate_message(message)
    elif args.reader:
        latch_reader = LatchExfiltrationReader()
        latch_reader.read_exfiltrated_message()


def create_arguments():
    parser = argparse.ArgumentParser(description="This script exfiltrates a message throughout the Latch Platform")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-w', '--writer', help='Writes a message to sent to a reader node')
    group.add_argument('-r', '--reader', action='store_true', help='Read the message the writer module is sending')
    return parser.parse_args()  

if __name__ == "__main__":
    main()


#!/usr/bin/env python
"""
Code to turn on devices using an RF transmitter.
"""
from rpi_rf import RFDevice
import argparse
import sys


GPIO_PIN = 23
PULSE_LEN = 159
BIT_LEN = 24
PROTOCOL = 1        # Princeton
REPEAT = 5

PATIO_ARGS = {
    'on': 0xD486FE,
    'off': 0xD486FD,
    'white': 0xD486F6,
    'red': 0xD486FA,
    'blue': 0xD486F4,
    'green': 0xD486F3,
    'up': 0xD486FC,
    'down': 0xD486F8,
    'party': 0xD486F9,
    'fast': 0xD486F7,
    'slow': 0xD486FB
}

NIGHTLIGHT_ARGS = {
    'on': 0x340558,
    'off': 0x340554
}

DEVICE_ARGS = {
    'patio': PATIO_ARGS,
    'nightlight': NIGHTLIGHT_ARGS
}


def transmit_code(code):
    """
    Transmit a hex code for a radio frequency
    """
    rfdevice = RFDevice(GPIO_PIN)
    rfdevice.enable_tx()

    try:
        for _ in range(REPEAT):
            print(f'Sending code {code}...')
            rfdevice.tx_code(code=code, tx_length=BIT_LEN, tx_pulselength=PULSE_LEN, tx_proto=PROTOCOL)
            print(f'Code {code} sent.')

    finally:
        rfdevice.cleanup()
        

def main():
    parser = argparse.ArgumentParser(
        description='Control RF patio lights',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"""
Examples:
    %(prog)s patio on
    %(prog)s nightlight off
    %(prog)s patio party
    """
    )
    
    device_help = f'Device to control. Available devices {",".join(DEVICE_ARGS.keys())}'
    
    parser.add_argument(
        'device',
        choices=DEVICE_ARGS.keys(),
        help=device_help
    )
    
    parser.add_argument(
        'command',
        help='Command to send (depends on device)'
    )
    
    args = parser.parse_args()
    
    device_commands = DEVICE_ARGS.get(args.device)
    
    if args.command not in device_commands:
        print(f"Error: Invalid command '{args.command}' for device '{args.device}'")
        print(f"Available commands: {', '.join(device_commands.keys())}")
        sys.exit(1)
    
    code = device_commands.get(args.command)
    transmit_code(code)
    print(f'sent {args.device} command: {args.command} ({hex(code)})')


if __name__ == '__main__':
    main()
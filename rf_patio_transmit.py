#!/usr/bin/env python
"""
Code to turn on patio lights using an RF transmitter.
From Deepseek
"""
from rpi_rf import RFDevice
import argparse
import sys


GPIO_PIN = 23
PULSE_LEN = 159
BIT_LEN = 24
PROTOCOL = 1        # Princeton
REPEAT = 5

ARGS = {
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


def transmit_code(code):
    """
    Transmit a hex code for a radio frequency
    """
    rfdevice = RFDevice(23)
    rfdevice.enable_tx()

    try:
        for _ in range(REPEAT):
            print(f'Sending code {code}...')
            rfdevice.tx_code(code=code, tx_length=BIT_LEN, tx_pulselength=PULSE_LEN, tx_proto=PROTOCOL)
            print(f'Code {code} sent.')

    finally:
        rfdevice.cleanup()
        

def main():
    parser = argparse.ArgumentParser(description='Control RF patio lights')
    parser.add_argument(
        'action',
        choices=list(ARGS.keys()),
        help=f"Action: {', '.join(list(ARGS.keys()))}"
    )
    args = parser.parse_args()
    action = ARGS.get(args.action)
    if action:
        transmit_code(action)
    else:
        print('Error: No argument provided')
        sys.exit(1)


if __name__ == '__main__':
    main()

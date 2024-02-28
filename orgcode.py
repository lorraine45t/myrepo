from os import _exit, mkdir
from os import name as osname
from os import path
from os import system as ossystem 
from platform import machine as osprocessor
from platform import system
import sys

from configparser import ConfigParser
from pathlib import Path

    from serial import Serial
    import serial.tools.list_ports
except ModuleNotFoundError:
    print("Pyserial is not installed. "
          + "Miner will try to automatically install it "
          + "If it fails, please manually execute "
          + "python3 -m pip install pyserial")
    install('pyserial')

def handler(signal_received, frame):
    """
    Nicely handle CTRL+C exit
    """
    if current_process().name == "MainProcess":
        pretty_print(
            get_string("sigint_detected")
            + Style.NORMAL
            + Fore.RESET
            + get_string("goodbye"),
            "warning")

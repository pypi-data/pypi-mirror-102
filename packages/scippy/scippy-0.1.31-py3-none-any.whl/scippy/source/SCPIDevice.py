import pyvisa
import serial
from serial.tools.list_ports import comports
import numpy as np
import time
import re

class SCPIDevice:
    def __init__(self, lib_type='pyvisa', device_name='',
            resource_name='',
            read_termination='\n', write_termination='\n',
            baud_rate=9600):
        """
        Base class for devices which use SCPI for communication. Works with either pyvisa or pyserial.

        :param lib_type: "pyvisa" or "pyserial".
        :param device_name: Device name as it responds to the identify command
        :param read_termination: Read termination character
        :param write_termination: Write termination character
        """
        self.lib_type = lib_type
        if self.lib_type == 'pyvisa':
            self.get_visa_device(device_name=device_name,
                    resource_name=resource_name,
                    read_termination=read_termination,
                    write_termination=write_termination,
                    baud_rate=baud_rate)
        else:
            self.get_serial_device(device_name=device_name,
                    read_termination=read_termination,
                    write_termination=write_termination,
                    baud_rate=baud_rate)

    def get_serial_device(
            self, device_name='', read_termination='\n',
            write_termination='\n', baud_rate=9600):
        r"""
        Searches for and initializes USB device with pyserial with the desired name

        :param device_name: Name of the device as it responds to the identify command (\*IDN?)
        :param read_termination: The read termination character
        :param write_termination: The write termination character
        """
        port_names = [port.device for port in comports()]
        is_usb_modem = ['usbmodem' in x for x in port_names]
        is_usb_serial = ['usbserial' in x for x in port_names]
        usb_modem_indices = np.where(is_usb_modem)[0]
        usb_serial_indices = np.where(is_usb_serial)[0]
        usb_indices = np.append(usb_modem_indices, usb_serial_indices)

        if len(usb_indices) == 0:
            raise ValueError(f'No Serial device found. Make sure it is plugged in. Available devices are {port_names}')

        for index in usb_indices:
            self.read_termination = read_termination
            self.write_termination = write_termination
            self.device = serial.Serial(port_names[index])
            self.device.timeout = 0.05
            self.device.baud_rate = baud_rate
            actual_name = self.identify()
            if device_name == '':
                break
            elif device_name == actual_name:
                break

    def get_visa_device(
            self, device_name='', resource_name='', resource_list=[],
            read_termination='\n',
            write_termination='\n', baud_rate=9600, timeout_counter=0):
        """
        Initializes our device using the Visa resource manager

        :param device_name: Desired device name as it responds to the SCPI identify command
        :param read_termination: Read termination character(s)
        :param write_termination: Write termination character(s)
        """
        rm = pyvisa.ResourceManager()
        if resource_list == []:
            resource_list = rm.list_resources()
        self.is_gpib = False
        self.is_generic = False
        if len(resource_list) == 0:
            raise RuntimeError("No resources found")
        if resource_name != '':
            resource_list = [resource_name]
        for i, rname in enumerate(resource_list):
            try:
                print(f'Attempting connection to {rname}...')
                if re.search(r'ASRL\d+::', rname) is not None:
                    self.is_generic = True
                if re.search(r'USB\d+::', rname) is not None:
                    self.is_usb = True
                if re.search(r'GPIB\d+::', rname) is not None:
                    self.is_gpib = True

                if self.is_generic:
                    self.device = rm.open_resource(
                            rname, baud_rate=baud_rate,
                            read_termination=read_termination,
                            write_termination=write_termination)
                elif self.is_usb:
                    self.device = rm.open_resource(
                            rname,
                            read_termination=read_termination,
                            write_termination=write_termination)
                elif self.is_gpib:
                    self.device = rm.open_resource(rname)
                else:
                    raise ValueError(f'Device type for rname {rname} not recognized.')

                self._read_termination = read_termination
                self._write_termination = write_termination
                device_name_actual = self.identify()
                if device_name == '':
                    break # Use the first available resource
                else:
                    if device_name == device_name_actual:
                        print(f'Correct device found.')
                        return
            except UserWarning:
                pass
            except pyvisa.errors.VisaIOError as e:
                if e.abbreviation == 'VI_ERROR_RSRC_NFOUND':
                    print(f'VISA resource not found. Trying next device...')
                elif e.abbreviation == 'VI_ERROR_RSRC_BUSY':
                    raise Exception('It appears VISA is having a heart attack. Try unplugging and plugging back in your device / USB hub, or closing out any other running python terminals or programs which might be trying to access this resource.')
                else: # This is currently not working.
                    print(f'Communication timeout error. Attempting to reconnect to device {rname}')
                    time.sleep(1)
                    if timeout_counter < 2:
                        new_timeout = timeout_counter + 1
                        new_list = resource_list[i:]
                    elif timeout_counter >= 2:
                        new_timeout = 0
                        new_list = resource_list[i+1:]
                    self.get_visa_device(
                            device_name=device_name,
                            read_termination=read_termination,
                            write_termination=write_termination,
                            baud_rate=baud_rate,
                            resource_list=new_list,
                            timeout_counter=new_timeout)

    @property
    def read_termination(self):
        """
        Read termination character.
        """
        return self._read_termination

    @read_termination.setter
    def read_termination(self, read_termination):
        self._read_termination = read_termination
        if self.lib_type == 'pyvisa':
            self.device.read_termination = read_termination

    @property
    def write_termination(self):
        """
        Write termination character. Typically the newline character.
        """
        return self._write_termination

    @write_termination.setter
    def write_termination(self, write_termination):
        self._write_termination = write_termination
        if self.lib_type == 'pyvisa':
            self.device.write_termination = write_termination


    def query(self, string):
        """
        Queries the device by first writing a desired string to it and then waiting for the reply.

        :param string: String to write to the device
        :returns line: Returned line of data in string format
        """
        self.write_line(string)
        return self.read_line()

    def read_line(self):
        """
        Reads a line of data from the device

        :returns line: Line of read data which ends in the read termination character. Termination character is stripped.
        """
        if self.lib_type == 'pyvisa':
            return self.device.read()
        elif self.lib_type == 'pyserial':
            full_string = self.device.readline().decode()
            stripped_string= full_string.rstrip(
                    self.read_termination)
            return stripped_string

    def write_line(self, string):
        """
        Writes a line of data to the device. Do NOT include the termination character, this method handles that.

        :param string: String to be written to device
        """
        if self.lib_type == 'pyvisa':
            self.device.write(string)
        elif self.lib_type == 'pyserial':
            self.device.write(bytes(
                        string + self.write_termination, encoding='ascii'))

    def read_bytes(self, n_bytes):
        """
        Reads a series of bytes from the device

        :param n_bytes: Number of bytes to be read
        :returns byte_array: Array of bytes
        """
        if self.lib_type == 'pyvisa':
            return self.device.read_bytes(n_bytes)
        elif self.lib_type == 'pyserial':
            return self.device.read(size=n_bytes)

    def close(self):
        """
        Closes device port so it can be used by another program
        """
        self.device.close()

    def identify(self):
        """
        Query the name of the device

        :returns device_name: The manufacturer-specified name of the device
        """
        self.write_line('*IDN?')
        return self.read_line()

    def reset(self):
        """
        Resets the device using the appropriate SCPI command
        """
        self.write_line('*RST')

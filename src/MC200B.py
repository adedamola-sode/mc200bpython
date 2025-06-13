# importing the basic framework components

from socket import socket, AF_INET, SOCK_STREAM, timeout

# Setting up a class to initialise record variables
class MCB:
    """
        This class exposes the connection to the MC200B optical
        chopper device and provides functions for querying
        the status of various variables of the device 
    """
    def __init__(self, IP, PORT):
        TIMEOUT = 3
        self._server = (IP, PORT)
        self._socket = socket(AF_INET, SOCK_STREAM)
        self._socket.connect(self._server)

    def __del__(self):
        self._socket.close()

    def _send(self, message):
        """
            Sends a message to the device with a CR terminator
        """
        self._socket.sendto(f"{message}\r".encode(), self._server)

    def _send_receive(self, message):
        """
            Sends a message to the device and receives a reply
        """
        self._send(message)
        try:
            data, address = self._socket.recvfrom(1024)
            if data:
                return data
        except timeout:
            print("Timeout")
    
    def _send_receive_int(self, message):
        """
            returns the digits from a returned request
        """
        data = self._send_receive(message)
        value = int(''.join(filter(str.isdigit, data.decode())))
        return value

    def _get_id(self):
        """
            Returns the device model number and firmware version
        """
        data = self._send_receive("id?")
        data = data.decode('utf-8')
        start_pos = data.find("THORLABS")
        end_pos = data.find("\r>")
        data = data[start_pos:end_pos]
        return data.encode()

    def _get_freq(self):
        """
            Returns the internal reference frequency
        """
        return self._send_receive_int("freq?")
    
    def _set_freq(self,value):
        """
            Sets the desired internal reference frequency
        """
        self._send(f"freq={int(value)}")
    
    def _get_blade(self):
        """
            Returns the blade type
        """
        return self._send_receive_int("blade?")
    
    def _set_blade(self, value):
        """
            Sets the blade type
        """
        self._send(f"blade={int(value)}")

    def _get_ref_out_freq(self):
        """
            Returns the reference output frequency
        """
        return self._send_receive_int("refoutfreq?")

    def _get_harm_mult(self):
        """
            Returns the harmonic multiplier applied
            to external reference frequency
        """
        return self._send_receive_int("nharmonic?")
    
    def _set_harm_mult(self, value):
        """
            Sets the harmonic multiplier applied
            to external reference frequency
        """
        self._send(f"nharmonic={int(value)}")

    def _get_harm_div(self):
        """
            Returns the harmonic divider applied
            to external referency frequency
        """
        return self._send_receive_int("dharmonic?")
    
    def _set_harm_div(self, value):
        """
            Sets the harmonic divider applied
            to external reference frequency
        """
        self._send(f"dharmonic={int(value)}")

    def _get_phase(self):
        """
            Gets the phase adjust
        """
        return self._send_receive_int("phase?")
    
    def _set_phase(self, value):
        """
            Sets the phase adjust
        """
        self._send(f"phase={int(value)}")

    def _get_enable(self):
        """
            Gets enable
        """
        return self._send_receive_int("enable?")
    
    def _set_enable(self, value):
        """
            Sets enable
        """
        self._send(f"enable={int(value)}")

    def _get_ref(self):
        """
            Gets the reference mode
        """
        return self._send_receive_int("ref?")
    
    def _set_ref(self, value):
        """
            Sets the reference mode
        """
        self._send(f"ref={int(value)}")

    def _get_ref_output(self):
        """
            Gets the output reference mode
        """
        return self._send_receive_int("output?")
    
    def _set_ref_output(self, value):
        """
            Sets the output reference mode
        """
        self._send(f"output={int(value)}")

    def _get_oncycle(self):
        """
            Gets on cycle
        """
        return self._send_receive_int("oncycle?")
    
    def _set_oncycle(self, value):
        """
            Sets on cycle
        """
        self._send(f"oncycle={int(value)}")

    def _get_intensity(self):
        """
            Gets display intensity
        """
        return self._send_receive_int("intensity?")
    
    def _set_intensity(self, value):
        """
            Sets display intensity
        """
        self._send(f"intensity={int(value)}")

    def _get_ref_input(self):
        """
            REturns the current supplied external
            reference frequency
        """
        return self._send_receive_int("input?")


    



import cothread
import epicscorelibs.path.cothread
from cothread.catools import caget, caput
from softioc import builder, softioc
from MC200B import MCB

class MCBIOC():
    
    POLL = 1

    def __init__(self):

        self.client = MCB("172.23.114.46", 9100)

        builder.SetDeviceName("BL14I-EA-IOC-38")

        self.id_rbv = builder.WaveformIn("ID", length = 128, datatype = 'b')

        self.freq_rbv = builder.aIn("FREQ_RBV")
        self.freq = builder.aOut("FREQ", always_update=True, on_update= lambda value: self.client._set_freq(value))

        self.blade_rbv = builder.aIn("BLADE_RBV") 
        self.blade = builder.aOut("BLADE", always_update=True, on_update = lambda value: self.client._set_blade(value))

        self.ref_out_freq_rbv = builder.aIn("REFOUTFREQ")

        self.harm_mult_rbv = builder.aIn("NHARMONIC_RBV") 
        self.harm_mult = builder.aOut("NHARMONIC", always_update=True, on_update = lambda value: self.client._set_harm_mult(value))
        
        self.harm_div_rbv = builder.aIn("DHARMONIC_RBV") 
        self.harm_div = builder.aOut("DHARMONIC", always_update=True, on_update = lambda value: self.client._set_harm_div(value))

        self.phase_rbv = builder.aIn("PHASE_RBV") 
        self.phase = builder.aOut("PHASE", always_update=True, on_update = lambda value: self.client._set_phase(value))

        self.enable_rbv = builder.aIn("ENABLE_RBV") 
        self.enable = builder.aOut("ENABLE", always_update=True, on_update = lambda value: self.client._set_enable(value))

        self.ref_rbv = builder.aIn("REFFREQ_RBV") 
        self.ref = builder.aOut("REFFREQ", always_update=True, on_update = lambda value: self.client._set_ref(value))

        self.ref_out_rbv = builder.aIn("REFOUT_RBV") 
        self.ref_out = builder.aOut("REFOUT", always_update=True, on_update = lambda value: self.client._set_ref_output(value))

        self.oncycle_rbv = builder.aIn("ONCYCLE_RBV") 
        self.oncycle = builder.aOut("ONCYCLE", always_update=True, on_update = lambda value: self.client._set_oncycle(value))

        self.intensity_rbv = builder.aIn("INTENSITY_RBV") 
        self.intensity = builder.aOut("INTENSITY", always_update=True, on_update = lambda value: self.client._set_intensity(value))

        self.ref_input_rbv = builder.aIn("REFINPUT_RBV") 

        self.monitor_map = {
            self.id_rbv: lambda: self.client._get_id(),
            self.freq_rbv: lambda: self.client._get_freq(),
            self.blade_rbv: lambda: self.client._get_blade(),
            self.ref_out_freq_rbv: lambda: self.client._get_ref_out_freq(),
            self.harm_mult_rbv: lambda: self.client._get_harm_mult(),
            self.harm_div_rbv: lambda: self.client._get_harm_div(),
            self.phase_rbv: lambda: self.client._get_phase(),
            self.enable_rbv: lambda: self.client._get_enable(),
            self.ref_rbv: lambda: self.client._get_ref(),
            self.ref_out_rbv: lambda: self.client._get_ref_output(),
            self.oncycle_rbv: lambda: self.client._get_oncycle(),
            self.intensity_rbv: lambda: self.client._get_intensity(),
            self.ref_input_rbv: lambda: self.client._get_ref_input()
        }

        builder.LoadDatabase()
        softioc.iocInit()


        

    def monitor(self):
        """
            This function monitors the available device parameters
        """
        while True:
            try:
                for rbv, func in self.monitor_map.items():
                    rbv.set(func())
            except Exception as error:
                print("Error: Monitor Function")

            cothread.Sleep(self.POLL)


    def start(self):
        cothread.Spawn(self.monitor)


mcbioc = MCBIOC()
mcbioc.start()
softioc.interactive_ioc(globals())

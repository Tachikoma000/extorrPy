import win32com.client

class ExtorrRGA:
    """
    A class for interfacing with and controlling an Extorr Residual Gas Analyzer (RGA) using the Extorr software's
    ActiveX automation server.

    Attributes:
        extorr (Dispatch): A Dispatch object for the Extorr software's ActiveX automation server.
        instruments (list): A list of available RGA instruments.
        instrument (Dispatch): A Dispatch object for the selected RGA instrument.
    """
    
    def __init__(self):
        """
        Initializes the connection to the Extorr software's ActiveX automation server, selects the first
        available RGA instrument, and sets the default scan parameters.
        """
        self.extorr = win32com.client.Dispatch("Extorr.Application")
        self.instruments = self.extorr.RGA.InstrumentList
        self.instrument = self.extorr.RGA.SelectInstrument(self.instruments[0])
        self.instrument.SetMassRange(1, 100)
        self.instrument.SetScanInterval(1)
        self.instrument.SetScanAverage(1)
        
    def set_mass_range(self, start_mass, end_mass):
        """
        Sets the mass range for the RGA to scan.

        Args:
            start_mass (int): The starting mass for the mass range.
            end_mass (int): The ending mass for the mass range.
        """
        self.instrument.SetMassRange(start_mass, end_mass)

    def start_scan(self):
        """
        Starts the RGA scan.
        """
        self.instrument.StartAcquisition()

    def is_scan_complete(self):
        """
        Checks if the RGA scan is complete.

        Returns:
            bool: True if the scan is complete, False otherwise.
        """
        return self.instrument.IsAcquisitionComplete()

    def get_data(self):
        """
        Gets the acquired RGA data.

        Returns:
            tuple: A tuple containing the mass-to-charge ratios and partial pressures of the detected gas species.
        """
        data = self.instrument.GetAcquiredData()
        return data
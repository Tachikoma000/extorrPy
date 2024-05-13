# Project Description

This project aims to interface with an Extorr Residual Gas Analyzer (RGA) using Python. The Extorr RGA is a scientific instrument used for gas analysis, particularly in vacuum systems. It can detect and measure the partial pressures of various gas species at different mass-to-charge ratios. The objective of this project is to develop a software application that can interface with the Extorr RGA to control the scan parameters, acquire RGA data, and process the acquired data.

# File Descriptions

`extorr.py`
This file contains the ExtorrRGA class, which is the core class for interfacing with the Extorr RGA using Python. The class uses the Extorr software's ActiveX automation server to control the scan parameters, start the scan, check if the scan is complete, and get the acquired RGA data.

`main.py`
This file contains the main script that uses the ExtorrRGA class to interface with the Extorr RGA. It creates an instance of the ExtorrRGA class, sets the mass range for the scan, starts the scan, waits for the scan to complete, gets the acquired RGA data, and prints the mass-to-charge ratios and partial pressures of the detected gas species.

`data.py`
This file contains a function called process_data that can be used to process the acquired RGA data. The function takes the mass-to-charge ratios and partial pressures of the detected gas species as input and returns a processed version of the data, such as the total pressure.

`test_extorr.py`
This file contains unit tests for the ExtorrRGA class. The tests check the functionality of the set_mass_range, start_scan, and get_data methods of the class.

`test_data.py`
This file contains unit tests for the process_data function in the data module. The tests check that the function correctly calculates the total pressure from the partial pressures of the detected gas species.

# Summary
The extorr.py file contains the ExtorrRGA class, which provides the core functionality for interfacing with the Extorr RGA using Python. The main.py file uses the ExtorrRGA class to control the scan parameters, acquire RGA data, and print the results. The data.py file provides a function that can be used to process the acquired RGA data. The test_extorr.py and test_data.py files contain unit tests for the ExtorrRGA class and the process_data function, respectively. Together, these files provide a comprehensive solution for interfacing with and controlling the Extorr RGA using Python.
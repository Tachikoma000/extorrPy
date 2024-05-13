# Extorr RGA Python Interface

This project provides a Python interface for controlling and acquiring data from an Extorr Residual Gas Analyzer (RGA). The interface uses the Extorr software's built-in ActiveX automation server to communicate with the RGA.

For questions or feature requests, please contact Jephthah Akene (Tachi) at tachi@playgrounds.network. As an independent researcher, I built this project purely for the joy of creating something both enjoyable and practical. If you love to tinker and build innovative control systems, feel free to email me!

# Table of Contents

- [Project Description](#project-description)
- [File Descriptions](#file-descriptions)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Project Description

This project aims to interface with an Extorr Residual Gas Analyzer (RGA) using Python. The Extorr RGA is a scientific instrument used for gas analysis, particularly in vacuum systems. It can detect and measure the partial pressures of various gas species at different mass-to-charge ratios. The objective of this project is to develop a software application that can interface with the Extorr RGA to control the scan parameters, acquire RGA data, and process the acquired data.

## File Descriptions

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


## Installation

To install the project, first clone the repository to your local machine:

`git clone https://github.com/yourusername/extorr-rga-python-interface.git`

Then, create and activate a virtual environment for the project:

`virtualenv env`
`source env/bin/activate`

Install the project dependencies using pip:

`pip install -r requirements.txt`


## Usage

To run this program, you will need to install the required dependencies listed in the requirements.txt file by running the command pip install -r requirements.txt.

Once the dependencies are installed, you can run the program by running the main.py script in the terminal using the command python main.py.

To use the interface, simply import the ExtorrRGA class from the extorr.py module and create an instance of the class:

`from extorr import ExtorrRGA`
`rga = ExtorrRGA()`

You can then use the methods of the ExtorrRGA class to control the RGA and acquire data. For example, to set the mass range for the RGA to scan and start the RGA scan:

`rga.set_mass_range(1, 40)`
`rga.start_scan()`

To retrieve the acquired RGA data:
`data = rga.get_data()`


## Project Structure


The project has the following file structure:

```
.
├── README.md
├── requirements.txt
├── extorr.py
├── data.py
└── tests
    ├── test_extorr.py
    └── test_data.py
```

The extorr.py module contains the ExtorrRGA class for interfacing with the Extorr software's ActiveX automation server. The data.py module contains functions for processing and analyzing RGA data. The tests directory contains test files for each module.


## Contributing
Contributions to the project are welcome! If you find a bug or have an idea for a new feature, please submit an issue on the project's GitHub page. If you'd like to contribute code, please fork the repository and submit a pull request with your changes.


## License
This project is licensed under the MIT License. See the LICENSE file for details.

import os

# Create the project directory
os.mkdir('extorr-rga-python-interface')
os.chdir('extorr-rga-python-interface')

# Create the source directory
os.mkdir('src')

# Create the extorr.py module
with open('src/extorr.py', 'w') as f:
    f.write('class ExtorrRGA:\n    pass\n')

# Create the data.py module
with open('src/data.py', 'w') as f:
    f.write('def process_data(data):\n    pass\n')

# Create the tests directory
os.mkdir('src/tests')

# Create the test_extorr.py file
with open('src/tests/test_extorr.py', 'w') as f:
    f.write('def test_extorr():\n    pass\n')

# Create the test_data.py file
with open('src/tests/test_data.py', 'w') as f:
    f.write('def test_data():\n    pass\n')

# Create the requirements.txt file
with open('requirements.txt', 'w') as f:
    f.write('pywin32\ncomtypes\n')

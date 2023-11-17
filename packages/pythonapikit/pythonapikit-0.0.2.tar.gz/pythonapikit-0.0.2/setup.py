from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'Collection of different APIs.'

# Setting up
setup(
    name="pythonapikit",
    version=VERSION,
    author="ShadowFlameFox",
    author_email="<shadow_flame_fox@web.de>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description="""# API-Kit Python Library
## Overview
The WeatherAPI Python library is a simple tool designed to interact with the WeatherAPI service, allowing users to retrieve weather information for a specific location.

## Features
Get the current temperature.
Retrieve the maximum temperature for the day.
Obtain the minimum temperature for the day.
Retrieve the average temperature for the day.
Installation
To use the WeatherAPI library, you need to install it using the following command:
`pip install pythonapikit`
## Usage
### Initializing the WeatherAPI Object
```
from pythonapikit import WeatherAPI

weatherapi_key = "YOUR_WEATHERAPI_KEY"`
location = "City, Country"`
unit = "c"  # Temperature unit, default is Celsius
weather = WeatherAPI(weatherapi_key, location, unit)
```
### Getting Current Temperature
```
current_temperature = weather.get_current_temperature()
print(f"Current Temperature: {current_temperature}°{unit.upper()}")
```
### Getting Maximum Temperature
```
max_temperature = weather.get_max_temperature()
print(f"Maximum Temperature: {max_temperature}°{unit.upper()}")
```
### Getting Minimum Temperature
```
min_temperature = weather.get_min_temperature()
print(f"Minimum Temperature: {min_temperature}°{unit.upper()}")
```
### Getting Average Temperature
```
avg_temperature = weather.get_avg_temperature()
print(f"Average Temperature: {avg_temperature}°{unit.upper()}")
```
## Dependencies
[requests](https://pypi.org/project/requests/): Used for making HTTP requests to the WeatherAPI service.
## License
This library is licensed under the [MIT License].

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests on the [GitHub repository](https://github.com/ShadowFlameFox/API-Kit/).""",
    packages=find_packages(),
    install_requires=["requests"],
    keywords=['Python', 'API', 'weather', 'Collection', "Integration","Wrapper","Client","Request","Endpoint","HTTP","REST","Web Services","Connector","Utility","Toolset","Helper","Manager","Facade","Handler","Assist","Bundle","Kit"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
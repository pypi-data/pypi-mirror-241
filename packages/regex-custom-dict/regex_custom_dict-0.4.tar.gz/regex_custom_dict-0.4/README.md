# RegexCustomDict

`RegexCustomDict` is a Python class that extends the built-in `dict` class, allowing you to access dictionary keys using regular expressions.

## Features

- Access dictionary keys using regex patterns.
- Flatten nested dictionaries into a single level for easy access.

## Installation

bash or windows
```
pip install regex_custom_dict
```

## Usage
```
from regex_custom_dict import RegexCustomDict

# Create an instance of RegexCustomDict
my_dict = RegexCustomDict(x={'sde': {'6': 4}}, y=4, xx={'sde': 2, 'sq': 3}, xxx=6.8)

#Alternate - you can even convert a normal_dict into a regex_custom_dict
my_dict = RegexCustomDict(**normal_dict)

# Access keys using regex pattern
result = my_dict['x+']
# The output will be a dictionary containing keys that match the provided regex pattern with predefined keys.

#To flatten the output.
result = my_dict['x+'].flatten_dict()

#you can also use multiple hierarchies(keys)
my_dict['x+']['s+']

It will flatten out the values and give as a list if your pattern matches multiple keys.
```
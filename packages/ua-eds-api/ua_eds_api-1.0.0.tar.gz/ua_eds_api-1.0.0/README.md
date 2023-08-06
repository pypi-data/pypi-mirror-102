# UA-EDS-API
Provides easy interface for making REST requests to University of Arizona EDS registry.

## Motivation
To make a python API that could generically interact with the REST architecture of EDS.

## Code Example
```python
from ua_eds_api import ua_eds_api

eds_api = ua_eds_api.EdsApi("host", "username", "password", "grouper url")

users = eds_api.get_grouper_users("grouper endpoint")
```

## Installation
pip install --user ua-eds-api

## Credits
[RyanJohannesBland](https://github.com/RyanJohannesBland)
[EtienneThompson](https://github.com/EtienneThompson)

## License
MIT

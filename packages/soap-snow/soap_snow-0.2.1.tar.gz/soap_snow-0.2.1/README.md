# soap_snow
Python client for interacting with the ServiceNow SOAP web service.

## API Documentation
For information about the ServiceNow SOAP web service, see the [Direct web services](https://docs.servicenow.com/bundle/paris-application-development/page/integrate/inbound-soap/concept/c_DirectWebServices.html#conceptnkw1tdgp) and [API Functions](https://docs.servicenow.com/bundle/paris-application-development/page/integrate/web-services-apis/reference/r_DirectWebServiceAPIFunctions.html) documentation.

## Install
```bash
pip install soap_snow
```

## Usage
```python
from soap_snow import SOAPSnow

username, password, instance = 'test_user', 'test_pass', 'customer'
snow = SOAPSnow(username, password, instance)

# Example 'insert' request
# Should return sys_id
resp = snow.request(
    method='insert',
    endpoint='incident',
    payload={
        'short_description': 'This is a test.',
        'assignment_group': 'my_group',
        'severity': 3
    }
)
print(resp.text)

# Example 'get' request
# Must send sys_id
resp = snow.request(
    method='get',
    endpoint='incident',
    display_value='true',
    payload={'sys_id': '01a7f0a71b5testsysid8556cc4bcb36'}
)
print(resp.text)

# Example 'update' request
# Must send sys_id
resp = snow.request(
    method='update',
    endpoint='incident',
    payload={
        'sys_id': '01a7f0a71b5testsysid8556cc4bcb36',
        'state': 6,
        'work_notes': 'This was a test.'
    }
)
resp.raise_for_status()
print(resp.text)

# Example 'getRecords' request
# with limit function (see ServiceNow API Functions)
resp = snow.request(
    method='getRecords',
    endpoint='incident',
    display_value='true',
    payload={
        'assignment_group': 'my_group',
        'active': 1,
        '__encoded_query=': 'state!=6^short_descriptionLIKEHost is unreachable',
        '__limit': 20
    }
)
print(resp.text)
```

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch
3. Commit your Changes
4. Push to the Branch
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.
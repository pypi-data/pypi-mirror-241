# Friendly Captcha SDK
A Python client for the Friendly Captcha service. This client allows for easy integration and verification of captcha responses with the Friendly Captcha API.

# Installation
```bash
pip install friendly-captcha-sdk
```

# Usage
### Initialization
To start using the client:
```
from friendly_client import FriendlyCaptchaClient
client = FriendlyCaptchaClient(
    api_key="YOUR_API_KEY", 
    sitekey="YOUR_SITEKEY"
    )
```

### Verifying a Captcha Response
- To verify a captcha response:
```
result: Fpython3 -m buildriendlyCaptchaResult = client.verify_captcha_response("CAPTCHA_RESPONSE_HERE")
print(result.should_accept) # True
print(result.was_able_to_verify) # True
```

- Verify with bad configuration in non-strict (default) mode
```
client.set_siteverify_endpoint("https://incorrect.endpoint.com")
result: FriendlyCaptchaResult = client.verify_captcha_response("CAPTCHA_RESPONSE_HERE")
print(result.should_accept)  # True
print(result.was_able_to_verify)  # False
```

- Verify with bad configuration in strict (default) mode
```
client.strict = True
client.set_siteverify_endpoint("https://incorrect.endpoint.com")
result: FriendlyCaptchaResult = client.verify_captcha_response("CAPTCHA_RESPONSE_HERE")
print(result.should_accept)  # False
print(result.was_able_to_verify)  # False
```



### Configuration
The client offers several configuration options:

- **api_key**: Your Friendly Captcha API key.
- **sitekey**: Your Friendly Captcha site key.
- **strict**: (Optional) In case the client was not able to verify the captcha response at all, for example if there is a network failure or a mistake in configuration, by default the `verify_captcha_response` returns True regardless. By passing `strict=true`, it will be false instead: every response needs to be strictly verified.
- **siteverify_endpoint**: (Optional) The endpoint URL for the site verification API.
- **verbose**: (Optional) Default is False. Turn on basic logging. 
- Error Handling: The client has built-in error handling mechanisms. In case of unexpected responses or errors from the Friendly Captcha API, the client will log the error and provide a default response.

### Development  
To install it locally:
```bash
pip install -e .
pip install requests_mock
```

Run the tests:
```bash
# Run the unit tests
python -m pytest

# Run the SDK integration tests (requires that you have the SDK test mock server running)
python -m pytest integration_tests
```


## Contributing
Contributions are welcome! If you'd like to contribute to this project, please submit a pull request with your changes.



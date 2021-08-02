# zendesk_coding_challenge
Python based CLI style ticket viewer for Zendesk 2021 CO-OP coding challenge by zihao zheng

## Dependencies:
install dependencies by run
```
pip install -r requirements.txt
```

## Unit test :
run unit test by run
```
pytest
```
## Credential/API token
a file name ```credential.json``` is necessary for the code to access zendesk API gateway. it have to contain following item:
```
{
"email":"..."
"api_token":"..."
}
```
and should be placed on the root directory.

# jaaxman-alarm-handler
CloudWatch Alarm handler to proxy Slack.  
  
Using [Zappa](https://github.com/Miserlou/Zappa) flamework.


## Environment
- Python >= 3.6


## SetUp
```
$ pip install -r requirements.txt
```


## Deploy
### Preparing
```
$ cp jaaxman-alarm-handler-env.sample.json jaaxman-alarm-handler-env.json

$ vi lambda_function_env.json  #=> write credentials

$ aws s3 cp jaaxman-alarm-handler-env.json <Amazon S3 path>
```


### Run deploy
```
$ cd <repository root>

$ zappa deploy
# or Once deployed
$ zappa update
```

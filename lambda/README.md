# How to development
## Create function directory
You need to create function directories each lambda function.

## Write code for backend service
Create backend function for lambda on local environment. Lambda handler in `lambda_function.py` is under each function directory.

## Execute lambda_function.py
Next, when you try to execute codes for quick debug, you just execute `build.py` which you need Python3 run time environment and docker-compose run time environment.
```
./function-test.py <function directory name>
```
That `build.py` execute `lambda_function.py` on demo docker-lambda environment. Of cource, that docker container boot on the network is for MySQL docker container. FQDN is `mysql`.

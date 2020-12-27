# How to development
## Create database for debug
First things first, You have to create database by `docker-compose up -d` under `database/` directory to create MySQL container to debug.
```
cd database/
docker-compose up -d
```

## Write code for backend service
Create backend function for lambda on local environment. Lambda handler in `lambda_function.py` is under `src` directory. So you need to add codes on that.
Next, when you try to execute codes for quick debug, you just execute `build.py` which you need Python3 run time environment and docker run time environment.
```
./build.py
```

That `build.py` execute `lambda_function.py` on demo docker-lambda environment. Of cource, that docker container boot on the network is for MySQL docker container. FQDN is `mysql`.

# hello-docker
A sample helloworld to try docker.

## Run
- Start two instances with a shared volume for the visits counter :
```
	$ docker run -d --volume /tmp/hello --name helloworld1 helloworld:v1
	$ docker run -d --volumes-from helloworld1 --name helloworld2 helloworld:v1
```
- Start the loadbalancer listenning on port 80 :
```
	$ docker run -d -p 80:80 --link helloworld1:hw1 --link helloworld2:hw2 hwloadbalancer:v1
```

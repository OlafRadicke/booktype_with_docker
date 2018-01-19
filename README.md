# booktype_with_docker
A [booktype](https://www.sourcefabric.org/en/booktype/) in a docker container. It is using sqlite as backent.

# quick start #

## Docker compose deployment ##

### Setup ###

Run
```bash
./script/setup
```
for preparing the docker volumes directories.

### Run application ###

Enter
```bash
docker-compose up
```

## Ansible deployment ##

Clone my repo
```
Git clone https://github.com/OlafRadicke/booktype_with_docker.git
```
Let run the ansible roll out script. It's create the docker container on your local machine. Before install ansible,
when it not exit.
```
cd ./booktype_with_docker/ansible
su -c 'ansible-playbook booktype_with_docker'
```
Check is all container running now:
```
[root@oradicke-localdomain ~]# docker ps
CONTAINER ID        IMAGE                  COMMAND                  CREATED             STATUS              PORTS                               NAMES
89ddb07ce27d        olafradicke/booktype   "/bin/bash start.sh"     About an hour ago   Up About an hour    8000/tcp, 0.0.0.0:49108->8080/tcp   booktype
301e57e02bf4        redis                  "/entrypoint.sh redis"   2 hours ago         Up 2 hours          6379/tcp                            booktyperedis
f60f86fb056c        postgres               "/docker-entrypoint.s"   2 hours ago         Up 2 hours          5432/tcp                            booktypepostgres
```
For trouble shutting go in the container and start the service manual
```
[root@oradicke-localdomain ~]# docker exec -it booktype /bin/bash
root@89ddb07ce27d:/# /bin/bash start.sh

```

# Biuild images #

```
su -c 'cd && docker build -t localhost/booktype .'
su -c 'docker tag localhost/booktype localhost/booktype'
```

You can find a ready images on [hub.docker.com]([https://hub.docker.com/r/olafradicke/booktype/)

# Run container (with ansible) #

```
su -c 'cd ./ansible && ansible-playbook ./run_booktype.yml '
```

# Other docus #

* [install docu of booktype](http://sourcefabric.booktype.pro/booktype-20-for-authors-and-publishers/installation-on-gnulinux/)
* [RabbitMQ as docker container](https://hub.docker.com/_/rabbitmq/)
* [PostgreSQL as docker contaner](https://hub.docker.com/_/postgres/)

# booktype_with_docker
A [booktype](https://www.sourcefabric.org/en/booktype/) in a docker container. It is using sqlite as backent.

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

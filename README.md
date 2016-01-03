# booktype_with_docker
A [booktype](https://www.sourcefabric.org/en/booktype/) in a docker container. It is using sqlite as backent.

# Biuild images #

```
su -c 'cd && docker build -t localhost/booktype .'
su -c 'docker tag localhost/booktype localhost/booktype'
```

# Run container #

su -c 'docker run --name my_booktype -d -P localhost/booktype'

# Other docus #

[install docu of booktype](http://sourcefabric.booktype.pro/booktype-20-for-authors-and-publishers/installation-on-gnulinux/)
[RabbitMQ as docker container](https://hub.docker.com/_/rabbitmq/)
[PostgreSQL as docker contaner](https://hub.docker.com/_/postgres/)

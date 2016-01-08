FROM debian:testing
COPY ./start.sh start.sh
ENV instancename docker_book
ENV booktypeversion 2.0

#env	DJANGO_SETTINGS_MODULE ${instancename}.settings
ENV HTTP_HOST localhost
ENV SITE_NAME Documentation
ENV DATA_ROOT /srv/booktype/data/
ENV	DJANGO_SETTINGS_MODULE settings.prod
ENV	PYTHONPATH $PYTHONPATH:/:/${instancename}/lib/:/Booktype/lib:/${instancename}:/${instancename}/settings
ENV	BOOKTYPE_USER booktype
ENV	BOOKTYPE_PASS booktype
ENV	BOOKTYPE_DB   booktype
ENV PG_HOST booktyppostgres
ENV PG_PORT '5432'
ENV REDIS_HOST 'booktyperedis'

EXPOSE 8080
VOLUME ${DATA_ROOT}

RUN apt-get update && apt-get -y upgrade

# Install needed packages as root
RUN apt-get install -y wget \
    unzip \
    python \
    python-dev \
    git-core \
    python-pip \
    python-virtualenv \
    redis-server \
    libxml2-dev \
    libxslt-dev \
    zlib1g-dev \
    libpq-dev

# Create Python Virtual Environment
RUN virtualenv --distribute /docker_booktype
RUN #!/bin/bash . /docker_booktype/bin/activate

# Fetch Booktype source
RUN wget https://github.com/sourcefabric/Booktype/archive/${booktypeversion}.zip
RUN unzip /${booktypeversion}.zip
RUN ln -s /Booktype-${booktypeversion} /Booktype
RUN rm /${booktypeversion}.zip

# Install needed Python modules
RUN pip install -r /Booktype/requirements/prod.txt

# Create Booktype project
# RUN #!/bin/bash echo 'yes\n' | /Booktype/scripts/createbooktype --database postgresql ${instancename}
RUN /Booktype/scripts/createbooktype --database postgresql ${instancename}

#RUN cp -R /${instancename}/docker_book_site/settings /${instancename}/settings
RUN mkdir -p /${instancename}/settings
RUN ls -lah /${instancename}/settings
#RUN rm -f /${instancename}/settings/prod.py
COPY ./prod.py /${instancename}/settings/prod.py
COPY ./base.py /${instancename}/settings/base.py
#RUN cat /${instancename}/settings/prod.py


RUN echo "DJANGO_SETTINGS_MODULE:"
RUN echo $DJANGO_SETTINGS_MODULE
RUN echo "PYTHONPATH"
RUN echo $PYTHONPATH

# Initialise Booktype
RUN cd /${instancename}/
RUN ls -lah
RUN #!/bin/bash source ${instancename}/booktype.env
RUN django-admin.py syncdb --noinput
RUN django-admin.py migrate
RUN django-admin.py createsuperuser
#django-admin.py createsuperuser --username='sysadmin' --email='sysadmin@okfn.org' --noinput


CMD ["/bin/bash", "start.sh"]

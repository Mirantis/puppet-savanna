#!/bin/bash



for SPEC_FILE  in \
openstack-savanna-virtualenv \
openstack-savanna-virtualenv-python-mysql \
openstack-savanna-virtualenv-python-iso8601 \
openstack-savanna-virtualenv-python-argparse \
openstack-savanna-virtualenv-python-markupsafe \
openstack-savanna-virtualenv-python-mako \
openstack-savanna-virtualenv-python-sqlalchemy \
openstack-savanna-virtualenv-python-alembic \
openstack-savanna-virtualenv-python-jinja2 \
openstack-savanna-virtualenv-python-werkzeug \
openstack-savanna-virtualenv-python-flask \
openstack-savanna-virtualenv-python-webob \
openstack-savanna-virtualenv-python-d2to1 \
openstack-savanna-virtualenv-python-greenlet \
openstack-savanna-virtualenv-python-eventlet \
openstack-savanna-virtualenv-python-oslo-config \
openstack-savanna-virtualenv-python-pycrypto \
openstack-savanna-virtualenv-python-paramiko \
openstack-savanna-virtualenv-python-prettytable \
openstack-savanna-virtualenv-python-pbr \
openstack-savanna-virtualenv-python-requests \
openstack-savanna-virtualenv-python-simplejson \
openstack-savanna-virtualenv-python-six \
openstack-savanna-virtualenv-python-netaddr \
openstack-savanna-virtualenv-python-jsonschema \
openstack-savanna-virtualenv-python-cinderclient \
openstack-savanna-virtualenv-python-novaclient \
openstack-savanna-virtualenv-python-keystoneclient \
openstack-savanna-virtualenv-savanna
do
    echo ===============$SPEC_FILE=========================
    sleep 1
    rpmbuild -ba ${SPEC_FILE}".spec" >> ./log || exit 255
    BuildArch=`cat $SPEC_FILE".spec" | grep -i 'BuildArch:' | awk '{ print $2 }'`
    if [ ""$BuildArch == "noarch" ] 
    then
	mv  /root/rpmbuild/RPMS/noarch/${SPEC_FILE}*rpm /root/rpmbuild/SPECS/savanna/
    else
	mv /root/rpmbuild/RPMS/x86_64/${SPEC_FILE}*rpm /root/rpmbuild/SPECS/savanna/
    fi
    cp -f /root/rpmbuild/SPECS/savanna/*.rpm /root/rpmbuild/SOURCES
    sleep 1
done


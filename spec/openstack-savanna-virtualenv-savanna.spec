Name:          openstack-savanna-virtualenv-savanna
Version:       0.2.a3.g05a5cfa
Release:       1%{?dist}
Summary:       Apache Hadoop cluster management on OpenStack
License:       ASL 2.0
URL:           https://launchpad.net/savanna
Source0:       savanna-%{version}.tar.gz
Source1:       openstack-savanna-virtualenv-0.1-1.el6.x86_64.rpm
Source2:       openstack-savanna-virtualenv-python-jinja2-2.7.1-1.el6.noarch.rpm
Source3:       openstack-savanna-virtualenv-python-werkzeug-0.9.3-1.el6.noarch.rpm
Source4:       openstack-savanna-virtualenv-python-argparse-1.2.1-1.el6.noarch.rpm
Source5:       openstack-savanna-virtualenv-python-markupsafe-0.18-1.el6.noarch.rpm
Source6:       openstack-savanna-virtualenv-python-mako-0.8.1-1.el6.noarch.rpm
Source7:       openstack-savanna-virtualenv-python-sqlalchemy-0.7.10-1.el6.noarch.rpm
Source8:       openstack-savanna-virtualenv-python-alembic-0.6.0-1.el6.noarch.rpm
Source9:       openstack-savanna-virtualenv-python-greenlet-0.4.1-1.el6.noarch.rpm
Source10:      openstack-savanna-virtualenv-python-eventlet-0.13.0-1.el6.noarch.rpm
Source11:      openstack-savanna-virtualenv-python-flask-0.9-1.el6.noarch.rpm
Source12:      openstack-savanna-virtualenv-python-prettytable-0.7.2-1.el6.noarch.rpm
Source13:      openstack-savanna-virtualenv-python-iso8601-0.1.4-1.el6.noarch.rpm
Source14:      openstack-savanna-virtualenv-python-d2to1-0.2.10-1.el6.noarch.rpm
Source15:      openstack-savanna-virtualenv-python-simplejson-3.3.0-1.el6.noarch.rpm
Source16:      openstack-savanna-virtualenv-python-six-1.3.0-1.el6.noarch.rpm
Source17:      openstack-savanna-virtualenv-python-pbr-0.5.21-1.el6.noarch.rpm
Source18:      openstack-savanna-virtualenv-python-requests-1.2.2-1.el6.noarch.rpm
Source19:      openstack-savanna-virtualenv-python-oslo-config-1.1.1-1.el6.noarch.rpm
Source20:      openstack-savanna-virtualenv-python-paramiko-1.11.0-1.el6.noarch.rpm
Source21:      openstack-savanna-virtualenv-python-pycrypto-2.6-1.el6.noarch.rpm
Source22:      openstack-savanna-virtualenv-python-webob-1.2.3-1.el6.noarch.rpm
Source23:      openstack-savanna-virtualenv-python-novaclient-2.14.1-1.el6.noarch.rpm
Source24:      openstack-savanna-virtualenv-python-netaddr-0.7.10-1.el6.noarch.rpm
Source25:      openstack-savanna-virtualenv-python-cinderclient-1.0.5-1.el6.noarch.rpm
Source26:      openstack-savanna-virtualenv-python-keystoneclient-0.2.5-1.el6.noarch.rpm
Source27:      openstack-savanna-virtualenv-python-jsonschema-1.3.0-1.el6.noarch.rpm
Source28:      openstack-savanna-api



BuildArch:     noarch
 
BuildRequires: python-virtualenv
Requires: python-virtualenv
Requires: openstack-savanna-virtualenv
Requires: openstack-savanna-virtualenv-python-jsonschema
Requires: openstack-savanna-virtualenv-python-keystoneclient
Requires: openstack-savanna-virtualenv-python-cinderclient
Requires: openstack-savanna-virtualenv-python-netaddr
Requires: openstack-savanna-virtualenv-python-novaclient
Requires: openstack-savanna-virtualenv-python-webob
Requires: openstack-savanna-virtualenv-python-flask
Requires: openstack-savanna-virtualenv-python-alembic
Requires: openstack-savanna-virtualenv-python-mako
Requires: openstack-savanna-virtualenv-python-markupsafe
Requires: openstack-savanna-virtualenv-python-sqlalchemy
Requires: openstack-savanna-virtualenv-python-eventlet
Requires: openstack-savanna-virtualenv-python-greenlet
Requires: openstack-savanna-virtualenv-python-prettytable
Requires: openstack-savanna-virtualenv-python-iso8601
Requires: openstack-savanna-virtualenv-python-d2to1
Requires: openstack-savanna-virtualenv-python-simplejson
Requires: openstack-savanna-virtualenv-python-six
Requires: openstack-savanna-virtualenv-python-pbr
Requires: openstack-savanna-virtualenv-python-requests
Requires: openstack-savanna-virtualenv-python-jinja2
Requires: openstack-savanna-virtualenv-python-werkzeug
Requires: openstack-savanna-virtualenv-python-oslo-config
Requires: openstack-savanna-virtualenv-python-paramiko
Requires: openstack-savanna-virtualenv-python-pycrypto
Requires: openstack-savanna-virtualenv-python-argparse
AutoReqProv: no

Prefix:         /opt/openstack-savanna
%global debug_package %{nil}
#%define _binaries_in_noarch_packages_terminate_build   0


%description
savanna in virtual environment for openstack-savanna


%build

rm -rf  %{_builddir}%{prefix}

export PYTHONPATH=$PWD:${PYTHONPATH}
venv=%{_builddir}%{prefix}

rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE1
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE2
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE3
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE4
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE5
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE6
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE7
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE8
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE9

rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE10
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE11
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE12
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE13
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE14
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE15
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE16
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE17
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE18
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE19

rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE20
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE21
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE22
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE23
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE24
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE25
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE26
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE27



source $venv/bin/activate

$venv/bin/pip install %SOURCE0


# Cleanup    
rpm -e openstack-savanna-virtualenv-python-jsonschema
rpm -e openstack-savanna-virtualenv-python-keystoneclient
rpm -e openstack-savanna-virtualenv-python-cinderclient
rpm -e openstack-savanna-virtualenv-python-netaddr
rpm -e openstack-savanna-virtualenv-python-novaclient
rpm -e openstack-savanna-virtualenv-python-webob
rpm -e openstack-savanna-virtualenv-python-flask
rpm -e openstack-savanna-virtualenv-python-alembic
rpm -e openstack-savanna-virtualenv-python-mako
rpm -e openstack-savanna-virtualenv-python-markupsafe
rpm -e openstack-savanna-virtualenv-python-sqlalchemy
rpm -e openstack-savanna-virtualenv-python-eventlet
rpm -e openstack-savanna-virtualenv-python-greenlet
rpm -e openstack-savanna-virtualenv-python-prettytable
rpm -e openstack-savanna-virtualenv-python-iso8601
rpm -e openstack-savanna-virtualenv-python-d2to1
rpm -e openstack-savanna-virtualenv-python-simplejson
rpm -e openstack-savanna-virtualenv-python-six
rpm -e openstack-savanna-virtualenv-python-pbr
rpm -e openstack-savanna-virtualenv-python-requests
rpm -e openstack-savanna-virtualenv-python-jinja2
rpm -e openstack-savanna-virtualenv-python-werkzeug
rpm -e openstack-savanna-virtualenv-python-oslo-config
rpm -e openstack-savanna-virtualenv-python-paramiko
rpm -e openstack-savanna-virtualenv-python-pycrypto
rpm -e openstack-savanna-virtualenv-python-argparse
rpm -e openstack-savanna-virtualenv

    
cd %{_builddir}/opt
for FILE in `find . -name *.pyc`
do
    rm -f ${FILE}
done

for FILE in `find . -name *.pyo`
do
    rm -f ${FILE}
done


deactivate
##################################################################################################
esc_venv=$(echo $venv | sed 's/[\/&]/\\&/g')
pattern="s/#\!${esc_venv}\/bin\/python/#\!\/usr\/bin\/env python\nimport os; activate_this=os.environ.get('VIRTUAL_ENV') + '\/bin\/activate_this.py'\; execfile\(activate_this, dict\(__file__=activate_this\)\); del os, activate_this/g"
find $venv -type f -name "*.pyc" -exec rm -f {} \;
find $venv -type f -exec sed -i "$pattern" {} \;
sed -i "s/${esc_venv}/%CHANGE_VIRTUALENV_PATH%/g" $venv/bin/* || true
# recrete symlink with relative target
cd $venv
rm -f lib64
ln -s lib lib64
##################################################################################################

# 
%install
HOME=%{_sharedstatedir}/savanna
install -d -m 700 %{buildroot}$HOME
# TODO: os_admin_username/password/tenant_name
#SAMPLE=%{buildroot}%{prefix}%{_datadir}/savanna/savanna.conf.sample
SAMPLE=%{_builddir}%{prefix}/share/savanna/savanna.conf.sample
CONF=%{_builddir}%{_sysconfdir}/savanna/savanna.conf

install -d -m 755 $(dirname $CONF)
install -D -m 640 $SAMPLE $CONF

sed -i -e "s,^connection=.*,connection=sqlite:///$HOME/savanna-server.db," $CONF


mkdir -p %{buildroot}/var/log/savanna
mkdir -p %{buildroot}/var/lib/savanna
mkdir -p %{buildroot}/var/run/savanna

mkdir -p %{buildroot}/etc/init.d
cp %SOURCE28 %{buildroot}/etc/init.d/

cp -r %{_builddir}/opt %{buildroot}/
cp -r %{_builddir}/etc %{buildroot}/




%post

# determine where package installed, need to know prefix
# RPM ca
real_prefix=`rpm -q --queryformat "%{instprefixes}\n" %{name} | tail -n1`
#echo  ${real_prefix}

esc_real_venv=$(echo "${real_prefix}" | sed 's/[\/&]/\\&/g')
# replace patters to real prefix where package installed
sed -i "s/%CHANGE_VIRTUALENV_PATH%/${esc_real_venv}/g" ${real_prefix}/bin/*


cat << EOF
Do not forget create and configure mysql database

1. You need mysql installed, configured and running
2. Create savanna user in mysql with password
3. Create savanna
4. Set up in  /etc/savanna/savanna.conf:

connection=mysql+mysqldb://savanna:<savanna_user_db_pass>@<host>[:<port>]/savanna

e.g:
mysql> CREATE DATABASE savanna;
mysql> GRANT ALL on savanna.* to 'savanna'@'localhost'  identified by 'savanna';
mysql> GRANT ALL on savanna.* to 'savanna'@'127.0.0.1'  identified by 'savanna';
mysql> FLUSH PRIVIVILEGES;

Test with command:
> mysql -u savanna -psavanna savanna

So in savanna.conf you need to add
connection=mysql://savanna:savanna@localhost/savanna


EOF




%files
%dir %{_sysconfdir}/savanna
# Note: this file is not readable because it holds auth credentials
%config(noreplace) %attr(-, root, savanna) %{_sysconfdir}/savanna/savanna.conf
%config(noreplace) %attr(-, root, savanna) /etc/savanna/savanna.conf
%dir %attr(-, savanna, savanna) %{_sharedstatedir}/savanna

%dir %attr(-, savanna, savanna) /var/log/savanna
%dir %attr(-, savanna, savanna) /var/lib/savanna
%dir %attr(-, savanna, savanna) /var/run/savanna
%config /etc/init.d/*
%{prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Aug 13 2013 Max Mazur mmaxur@mirantis.com
- savanna for Savanna into virtualenv. Initial spec created.

Name:          openstack-savanna-virtualenv-python-flask
Version:       0.9
Release:       1%{?dist}
Summary:       python-flask ionstalled into virtual env for openstack-savanna
License:       ASL 2.0
URL:           https://launchpad.net/savanna
Source0:       Flask-%{version}.tar.gz
Source1:       openstack-savanna-virtualenv-0.1-1.el6.x86_64.rpm
Source2:       openstack-savanna-virtualenv-python-markupsafe-0.18-1.el6.noarch.rpm
Source3:       openstack-savanna-virtualenv-python-jinja2-2.7.1-1.el6.noarch.rpm
Source4:       openstack-savanna-virtualenv-python-werkzeug-0.9.3-1.el6.noarch.rpm

BuildArch:     noarch
 
BuildRequires: python-virtualenv
Requires: python-virtualenv
Requires: openstack-savanna-virtualenv
Requires: openstack-savanna-virtualenv-python-markupsafe
Requires: openstack-savanna-virtualenv-python-jinja2
Requires: openstack-savanna-virtualenv-python-werkzeug


AutoReqProv: no

Prefix:         /opt/openstack-savanna
%global debug_package %{nil}
#%define _binaries_in_noarch_packages_terminate_build   0


%description
flask in virtual environment for openstack-savanna


%build

rm -rf  %{_builddir}%{prefix}

export PYTHONPATH=$PWD:${PYTHONPATH}
venv=%{_builddir}%{prefix}

rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE1
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE2
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE3
rpm -ivh --prefix=%{_builddir}%{prefix}  %SOURCE4

source $venv/bin/activate

$venv/bin/pip install %SOURCE0

# Cleanup    
rpm -e openstack-savanna-virtualenv-python-jinja2
rpm -e openstack-savanna-virtualenv-python-werkzeug
rpm -e openstack-savanna-virtualenv-python-markupsafe
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
#sed -i "s/${esc_venv}/%CHANGE_VIRTUALENV_PATH%/g" $venv/bin/*
# recrete symlink with relative target
cd $venv
rm -f lib64
ln -s lib lib64
##################################################################################################

# 
%install
cp -r %{_builddir}/opt %{buildroot}/




%post

# determine where package installed, need to know prefix
# RPM ca
real_prefix=`rpm -q --queryformat "%{instprefixes}\n" %{name} | tail -n1`
#echo  ${real_prefix}

esc_real_venv=$(echo "${real_prefix}" | sed 's/[\/&]/\\&/g')
# replace patters to real prefix where package installed
sed -i "s/%CHANGE_VIRTUALENV_PATH%/${esc_real_venv}/g" ${real_prefix}/bin/*


%files
%{prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Aug 13 2013 Max Mazur mmaxur@mirantis.com
- python-flask for Savanna into virtualenv. Initial spec created.

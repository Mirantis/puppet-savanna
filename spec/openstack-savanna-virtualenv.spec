Name:          openstack-savanna-virtualenv
Version:       0.1
Release:       1%{?dist}
Summary:       Virtual env for openstack-savanna
License:       ASL 2.0
URL:           https://launchpad.net/savanna
 
BuildRequires: python-virtualenv
Requires: python-virtualenv
AutoReqProv: no

Prefix:         /opt/openstack-savanna
%global debug_package %{nil}
#%define _binaries_in_noarch_packages_terminate_build   0


%description
Virtual Environment for openstack-savanna


%build
rm -rf  %{_builddir}/*


export PYTHONPATH=$PWD:${PYTHONPATH}
venv=%{_builddir}%{prefix}
echo $venv
virtualenv $venv

source $venv/bin/activate

deactivate

esc_venv=$(echo $venv | sed 's/[\/&]/\\&/g')
pattern="s/#\!${esc_venv}\/bin\/python/#\!\/usr\/bin\/env python\nimport os; activate_this=os.environ.get('VIRTUAL_ENV') + '\/bin\/activate_this.py'\; execfile\(activate_this, dict\(__file__=activate_this\)\); del os, activate_this/g"
find $venv -type f -name "*.pyc" -exec rm -f {} \;
find $venv -type f -exec sed -i "$pattern" {} \;
sed -i "s/${esc_venv}/%CHANGE_VIRTUALENV_PATH%/g" $venv/bin/*
# recrete symlink with relative target
cd $venv
rm -f lib64
ln -s lib lib64


# 
%install
cp -r %{_builddir}/opt %{buildroot}/



%post

# determine where package installed, need to know prefix
# RPM ca
real_prefix=`rpm -q --queryformat "%{instprefixes}\n" %{name}-%{version}-%{release} | tail -n1`
#echo  ${real_prefix}

esc_real_venv=$(echo "${real_prefix}" | sed 's/[\/&]/\\&/g')
# replace patters to real prefix where package installed
sed -i "s/%CHANGE_VIRTUALENV_PATH%/${esc_real_venv}/g" ${real_prefix}/bin/*


%files
%{prefix}


%changelog
* Wed Aug 13 2013 Max Mazur mmaxur@mirantis.com
- Savanna virtualenv bin files moved from openstack-savanna into openstack-savanna-virtualenv package

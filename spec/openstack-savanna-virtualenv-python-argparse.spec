Name:          openstack-savanna-virtualenv-python-argparse
Version:       1.2.1
Release:       1%{?dist}
Summary:       python-argparse ionstalled into virtual env for openstack-savanna
License:       ASL 2.0
URL:           https://launchpad.net/savanna
Source0:       argparse-%{version}.tar.gz
BuildArch:     noarch

 
BuildRequires: python-virtualenv
Requires: python-virtualenv
Requires: openstack-savanna-virtualenv
AutoReqProv: no

Prefix:         /opt/openstack-savanna
%global debug_package %{nil}
#%define _binaries_in_noarch_packages_terminate_build   0


%description
argparse in virtual environment for openstack-savanna


%build
rm -rf  %{_builddir}%{prefix}

export PYTHONPATH=$PWD:${PYTHONPATH}
venv=%{_builddir}%{prefix}
echo $venv
virtualenv $venv

source $venv/bin/activate
$venv/bin/pip install %SOURCE0

deactivate
##################################################################################################
esc_venv=$(echo $venv | sed 's/[\/&]/\\&/g')
pattern="s/#\!${esc_venv}\/bin\/python/#\!\/usr\/bin\/env python\nimport os; activate_this=os.environ.get('VIRTUAL_ENV') + '\/bin\/activate_this.py'\; execfile\(activate_this, dict\(__file__=activate_this\)\); del os, activate_this/g"
find $venv -type f -name "*.pyc" -exec rm -f {} \;
find $venv -type f -exec sed -i "$pattern" {} \;
sed -i "s/${esc_venv}/%CHANGE_VIRTUALENV_PATH%/g" $venv/bin/*
# recrete symlink with relative target
cd $venv
rm -f lib64
ln -s lib lib64
##################################################################################################

# 
%install
cp -r %{_builddir}/opt %{buildroot}/

cd %{buildroot}
for FILE in `find . -name *.pyc`
do
    rm -f ${FILE}
done

for FILE in `find . -name *.pyo`
do
    rm -f ${FILE}
done


# We need to clean all files not from this package: virtualenv and other libs:
# Virtualenv


rm -f %{buildroot}/opt/openstack-savanna/bin/activate
rm -f %{buildroot}/opt/openstack-savanna/bin/activate.csh
rm -f %{buildroot}/opt/openstack-savanna/bin/activate.fish
rm -f %{buildroot}/opt/openstack-savanna/bin/activate_this.py
rm -f %{buildroot}/opt/openstack-savanna/bin/easy_install
rm -f %{buildroot}/opt/openstack-savanna/bin/easy_install-2.6
rm -f %{buildroot}/opt/openstack-savanna/bin/pip
rm -f %{buildroot}/opt/openstack-savanna/bin/pip-2.6
rm -f %{buildroot}/opt/openstack-savanna/bin/python
rm -f %{buildroot}/opt/openstack-savanna/bin/python2
rm -f %{buildroot}/opt/openstack-savanna/bin/python2.6


rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/UserDict.py
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/UserDict.pyc
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/UserDict.pyo
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/_abcoll.py
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/_abcoll.pyc
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/_abcoll.pyo
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/abc.py
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/abc.pyc
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/abc.pyo
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/codecs.py
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/codecs.pyc
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/codecs.pyo
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/config
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/copy_reg.py
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/copy_reg.pyc
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/copy_reg.pyo

rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/distutils/__init__.py
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/distutils/__init__.pyc
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/distutils/__init__.pyo
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/distutils/distutils.cfg
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/encodings
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/fnmatch.py
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/fnmatch.pyc
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/fnmatch.pyo
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/genericpath.py
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/genericpath.pyc
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/genericpath.pyo
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/lib-dynload
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/linecache.py
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/linecache.pyc
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/linecache.pyo
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/locale.py
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/locale.pyc
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/locale.pyo
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/no-global-site-packages.txt
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/ntpath.py
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/ntpath.pyc
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/ntpath.pyo
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/orig-prefix.txt
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/os.py
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/os.pyc
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/os.pyo
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/posixpath.py
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/posixpath.pyc
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/posixpath.pyo
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/re.py
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/re.pyc
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/re.pyo

rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/easy-install.pth


rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/EGG-INFO/PKG-INFO
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/EGG-INFO/SOURCES.txt
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/EGG-INFO/dependency_links.txt
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/EGG-INFO/entry_points.txt
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/EGG-INFO/not-zip-safe
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/EGG-INFO/requires.txt
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/EGG-INFO/top_level.txt

rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/__init__.py
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/__init__.pyc
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/__init__.pyo
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/__main__.py
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/__main__.pyc
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/__main__.pyo

rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/backwardcompat/__init__.py
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/backwardcompat/__init__.pyc
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/backwardcompat/__init__.pyo
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/backwardcompat/socket_create_connection.py
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/backwardcompat/socket_create_connection.pyc
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/backwardcompat/socket_create_connection.pyo
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/backwardcompat/ssl_match_hostname.py
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/backwardcompat/ssl_match_hostname.pyc
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/backwardcompat/ssl_match_hostname.pyo
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/basecommand.py
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/basecommand.pyc
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/basecommand.pyo
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/baseparser.py
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/baseparser.pyc
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/baseparser.pyo
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/cacert.pem
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/cmdoptions.py
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/cmdoptions.pyc
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/cmdoptions.pyo

rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/commands/__init__.py
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/commands/__init__.pyc
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/commands/__init__.pyo
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/commands/bundle.py
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/commands/bundle.pyc
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/commands/bundle.pyo
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/commands/completion.py
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/commands/completion.pyc
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/commands/completion.pyo
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/commands/freeze.py
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/commands/freeze.pyc
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/commands/freeze.pyo
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/commands/help.py
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/commands/help.pyc
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/commands/help.pyo
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/commands/install.py
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/commands/install.pyc
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/commands/install.pyo
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/commands/list.py
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/commands/list.pyc
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/commands/list.pyo
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/commands/search.py
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/commands/search.pyc
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/commands/search.pyo
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/commands/show.py
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/commands/show.pyc
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/commands/show.pyo
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/commands/uninstall.py
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/commands/uninstall.pyc
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/commands/uninstall.pyo
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/commands/unzip.py
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/commands/unzip.pyc
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/commands/unzip.pyo
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/commands/zip.py
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/commands/zip.pyc
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/commands/zip.pyo
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/download.py
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/download.pyc
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/download.pyo
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/exceptions.py
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/exceptions.pyc
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/exceptions.pyo
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/index.py
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/index.pyc
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/index.pyo
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/locations.py
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/locations.pyc
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/locations.pyo
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/log.py
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/log.pyc
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/log.pyo
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/req.py
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/req.pyc
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/req.pyo
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/runner.py
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/runner.pyc
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/runner.pyo
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/status_codes.py
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/status_codes.pyc
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/status_codes.pyo
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/util.py
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/util.pyc
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/util.pyo

rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/vcs/__init__.py
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/vcs/__init__.pyc
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/vcs/__init__.pyo
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/vcs/bazaar.py
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/vcs/bazaar.pyc
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/vcs/bazaar.pyo
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/vcs/git.py
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/vcs/git.pyc
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/vcs/git.pyo
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/vcs/mercurial.py
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/vcs/mercurial.pyc
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/vcs/mercurial.pyo
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/vcs/subversion.py
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/vcs/subversion.pyc
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/vcs/subversion.pyo
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/setuptools-0.6c11-py2.6.egg
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/setuptools.pth
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site.py
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site.pyc
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/site.pyo
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/sre.py
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/sre.pyc
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/sre.pyo
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/sre_compile.py
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/sre_compile.pyc
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/sre_compile.pyo
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/sre_constants.py
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/sre_constants.pyc
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/sre_constants.pyo
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/sre_parse.py
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/sre_parse.pyc
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/sre_parse.pyo
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/stat.py
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/stat.pyc
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/stat.pyo
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/types.py
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/types.pyc
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/types.pyo
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/warnings.py
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/warnings.pyc
rm -f %{buildroot}/opt/openstack-savanna/lib/python2.6/warnings.pyo


rmdir %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/backwardcompat
rmdir %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/commands
rmdir %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip/vcs
rmdir %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/pip
rmdir %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg/EGG-INFO


rmdir %{buildroot}/opt/openstack-savanna/lib/python2.6/site-packages/pip-1.3.1-py2.6.egg
rmdir %{buildroot}/opt/openstack-savanna/lib/python2.6/distutils
#rmdir %{buildroot}/opt/openstack-savanna/lib/python2.6

#rmdir %{buildroot}/opt/openstack-savanna/include/python2.6
#rmdir %{buildroot}/opt/openstack-savanna/lib64
#rmdir %{buildroot}/opt/openstack-savanna/lib

rmdir %{buildroot}/opt/openstack-savanna/bin
#rmdir %{buildroot}/opt/openstack-savanna/include




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
- python-argparse for Savanna into virtualenv. Initial spec created.

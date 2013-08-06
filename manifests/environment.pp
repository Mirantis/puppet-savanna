class savanna::environment (
  $packages        = [ "screen", "python-setuptools", "python-virtualenv", "python-dev" ],
  $fedora_packages = [ "screen", "python-setuptools", "python-virtualenv", "python-devel" ],
  $centos_packages = [ "screen", "python-devel", "gcc", "python-setuptools", "python-virtualenv" ]
) {

  case $operatingsystem {
    Ubuntu: {
       package { $packages:
         ensure => present,
       }
    }

    Fedora: {
      package { $fedora_packages:
        ensure => present,
      }
    }

    CentOS: {
      package { $centos_packages:
        ensure => present,
      }
    }
  }
}

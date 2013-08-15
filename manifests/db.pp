class savanna::db (
) {
  include savanna::params
  $savanna_file=$savanna::params::savanna_file

  mysql::db { $::savanna::params::db_name:
    user     => $::savanna::params::db_user,
    password => $::savanna::params::db_password,
    host     => 'localhost',
    grant    => ['all'],
    charset => 'utf8',
  }

  exec { "savanna_db":
    command => "sed -i -e \"s/connection=.*/connection=mysql+mysqldb:\/\/${savanna::params::db_user}:${savanna::params::db_password}@localhost\/${savanna::params::db_name}/g\" ${savanna_file}",
    path    => ["/bin"],
  }
}


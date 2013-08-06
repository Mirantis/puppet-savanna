class savanna::install (
  $provider = 'pip'
) {

  exec { "Setup virtual environment":
    command   => "/usr/bin/virtualenv savanna-venv \
               && /opt/savanna-venv/bin/${provider} install savanna \
               && /opt/savanna-venv/bin/${provider} install savanna-dashboard",
    cwd       => "/opt",
    path      => ["/opt/savanna-venv/bin:/usr/bin:/usr/local/sbin:/usr/sbin/:/sbin:/bin"],
    logoutput => true,
    timeout   => 0,
  }

  file { "/opt/savanna-venv/etc":
    ensure => "directory",
  }
}

class savanna::final (
  $savanna_dir =  "/opt/savanna-venv"
) {

  service { "apache2":
    enable     => true,
    ensure     => true,
  }
  exec { "reload":
    command     => "/etc/init.d/apache2 restart",
    require     => Service["apache2"],
  }

  include savanna::params
  $savanna_file=$savanna::params::savanna_file

  exec { "start Savanna":
    command   => "screen -dmS Savanna && sleep 2 && screen -S Savanna -p 0 -X stuff '/opt/savanna-venv/bin/python ${savanna_dir}/bin/savanna-api --config-file ${savanna_file}
'",
    path      => ["/usr/bin:/bin"],
    logoutput => true,
  }
}

class savanna::config (
  $horizon_file       = '/usr/share/openstack-dashboard/openstack_dashboard/settings.py',
  $horizon_local_file = "/usr/share/openstack-dashboard/openstack_dashboard/local/local_settings.py",
  $run_command_f      = "echo \"HORIZON_CONFIG['dashboards'] += ('savanna',)\"",
  $run_command_s      = "echo \"INSTALLED_APPS += ('savannadashboard',)\"",
  $savanna_url = 'SAVANNA_URL = http://localhost:8386/v1.0'
) {

  include savanna::params
  $savanna_file=$savanna::params::savanna_file

  file { "${savanna_file}":
    owner   => 'root',
    group   => 'root',
    mode    => '0664',
    source  => "puppet:///modules/savanna/savanna.conf",
  }

  exec { "Editing horizon config":
    command => "${run_command_f} >> ${horizon_file} \
                && ${run_command_s} >> ${horizon_file} \
                && echo ${savanna_url} >> ${horizon_local_file}",
    path    => ["/bin"],
  }
}

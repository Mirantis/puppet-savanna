class savanna (
) {
  include savanna::environment
  include savanna::install
  include savanna::config
  include savanna::db
  include savanna::final
}
include savanna

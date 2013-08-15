stage { [1, 2, 3, 4, 5]: }

Stage[1] ->  Stage[2] -> Stage[3] -> Stage[4] -> Stage[5] -> Stage[main]

  class {'savanna::environment':
    stage => '1',
  }

  class {'savanna::install':
    stage => 2,
  }

  class {'savanna::config':
    stage => 3,
  }

  class {'savanna::db':
   stage => 4,
  }

  class {'savanna::final':
    stage => 5,
  }

  class {'savanna':
    stage => main,
  }

# Will configure ssh to use private key ~/.ssh/school
#include stdlib
file_line { 'Identity file source insert':
  path    => '/etc/.ssh/config',
  line    => '  IdentityFile ~/.ssh/school',
  replace => true
}

file_line { 'Disables password authentication':
  path    => '/etc/.ssh/config',
  line    => '  PasswordAuthentication no',
  replace => true
}

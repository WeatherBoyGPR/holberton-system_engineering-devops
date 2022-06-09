# Optimizes Nginx server traffic levels

exec { 'increase_limit' :
  command => 'sed -i "s/15/4096" /etc/default/nginx',
  path    => '~/bin/:/bin/'
}

exec { 'nginx_restart' :
  command => 'sudo service nginx restart',
  path    => '/etc/init.d/'
}

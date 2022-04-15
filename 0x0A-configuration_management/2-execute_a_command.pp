# Will use pkill to kill process killmenow
exec { 'kill_process':
  command => 'pkill killmenow',
  path    => ['/usr/bin']
}

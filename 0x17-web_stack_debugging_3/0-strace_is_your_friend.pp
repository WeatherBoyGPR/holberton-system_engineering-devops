# fixes file name typo 0x17-Debugging

exec{ 'fix-typo':
    command => 'sed -i \'s/class-wp-locale.phpp/class-wp-locale.php/g\' /var/www/html/wp-settings.php',
    path    => '/usr/local/bin/:/bin/',
}

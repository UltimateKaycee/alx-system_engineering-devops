# A Puppet file to find out why 500 error
# then fix bad `phpp` extensions inside WordPress file
# Wordpress file  `wp-settings.php`.

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}

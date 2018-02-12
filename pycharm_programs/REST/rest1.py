import urllib2

url = 'http://del.icio.us/api/:username/bookmarks/:hash'
response = urllib2.urlopen(url).read()
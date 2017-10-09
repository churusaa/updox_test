## ElasticSearch index cleanup
##

import os, datetime

# Number of days of indices to keep
# retain_days = 10
retain_days = 0

# Everything that comes before the date string in the file name
# (Don't include the path. That's defined in the next variable)
# matching_pattern = "name-"
matching_pattern = "name-"

# File suffix can be added here if the file ends with an extension
# file_suffix = ""
file_suffix = ""

# ElasticSearch index directory
# index_directory = '/var/lib/elasticsearch/data/'
index_directory = '/var/lib/elasticsearch/data/'

# Date format - Uses standard strftime format
# date_format = "%Y.%m.%d"
date_format = "%Y.%m.%d"

# Logs older than X days old will also be left alone. Defaults to 3 years
# remove_days = 1095
remove_days = 1095

while remove_days > retain_days:
  currdate = datetime.datetime.now() - datetime.timedelta(days=remove_days)
  file_to_remove = index_directory + matching_pattern + currdate.strftime(date_format) + file_suffix
  if os.path.isfile(file_to_remove):
    os.remove(file_to_remove) 
    print "Removed", file_to_remove
  remove_days = remove_days - 1	

#The second challenge, a Python script that will run as a daily job. 
#It should delete timestamped ElasticSearch indices (indices with a name pattern like "name-YYYY.MM.DD") 
#that are older than a configurable number of days.

## ElasticSearch index cleanup
##

import os, datetime

# Number of days of indices to keep
# retain_days = 10
retain_days = 10

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

## For testing purposes only, create the files before deleting them if they don't exist
make_days = 10
if not os.path.exists(index_directory):
  os.makedirs(index_directory)
while make_days > 0:
  currdate = datetime.datetime.now() - datetime.timedelta(days=make_days)
  F = open(index_directory + matching_pattern + currdate.strftime(date_format), "w")
  make_days = make_days - 1

#for files in os.listdir(index_directory):
while retain_days > 0:
  currdate = datetime.datetime.now() - datetime.timedelta(days=retain_days)
  print "Removing file " + matching_pattern + currdate.strftime(date_format) + file_suffix
  os.remove(index_directory + matching_pattern + currdate.strftime(date_format) + file_suffix) 
  retain_days = retain_days - 1	

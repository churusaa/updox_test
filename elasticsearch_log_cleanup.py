

The second challenge, a Python script that will run as a daily job. 
It should delete timestamped ElasticSearch indices (indices with a name pattern like "name-YYYY.MM.DD") 
that are older than a configurable number of days.

## ElasticSearch index cleanup
##

import time, os, sys

# Number of days of indices to keep
# retain_days = '10'
retain_days = 10

# ElasticSearch index directory
# index_directory = '/var/lib/elasticsearch/data/'
index_directory = '/var/lib/elasticsearch/data/'

now = time.time()

unix_retain_days = retain_days * 86400
for files in os.listdir(index_directory):
    where name	

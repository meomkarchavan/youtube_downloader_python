import os
import re
def humanbytes(B):
   'Return the given bytes as a human friendly KB, MB, GB, or TB string'
   B = float(B)
   KB = float(1024)
   MB = float(KB ** 2) # 1,048,576
   GB = float(KB ** 3) # 1,073,741,824
   TB = float(KB ** 4) # 1,099,511,627,776

   if B < KB:
      return '{0} {1}'.format(B,'Bytes' if 0 == B > 1 else 'Byte')
   elif KB <= B < MB:
      return '{0:.2f} KB'.format(B/KB)
   elif MB <= B < GB:
      return '{0:.2f} MB'.format(B/MB)
   elif GB <= B < TB:
      return '{0:.2f} GB'.format(B/GB)
   elif TB <= B:
      return '{0:.2f} TB'.format(B/TB)

def fileExists(path):
   return os.path.isfile(path)
def pathExistsElseCreate(DIR):
   if os.path.isdir(DIR):
      return DIR
   else:
      try:
         os.makedirs(DIR)
         print(f'Directory Created: {DIR}')
         return DIR
      except OSError as e:
         return None

def urlChecker(url):
   pattern = re.compile("^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+$")
   return bool(pattern.match(url))

import urllib.request

def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False

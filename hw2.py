import urllib.request

print("Begin download")

urllib.request.urlretrieve("https://www.python.org/ftp/python/2.7.4/python-2.7.4.msi", "matt-python-version.msi")

print("Complete")
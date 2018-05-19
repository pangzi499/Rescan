import  os

# x = os.popen("ping 127.0.0.1")
y = os.popen("CVE-2017-12149.py http://127.0.0.1:8000")
# print x.read()
print "==============="
print y.read()
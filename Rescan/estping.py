import  os

# x = os.popen("ping 127.0.0.1")
y = os.popen("python D:\\temp\\Rescan1\\PocList\\cve-2017-3248.py 192.168.133.130")
# print x.read()
print "==============="
print y.read().encode('utf-8')
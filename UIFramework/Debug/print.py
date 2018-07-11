import time

now_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
print('report%s.html' %now_time)
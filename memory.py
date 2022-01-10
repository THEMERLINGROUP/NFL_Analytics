import sys
import gc
b = 43300
sys.getrefcount(b)
B = 'Bitcoin'
c = [B,b]
d = {'Bitcoin':B}
sys.getrefcount(b)
del b
gc.enable()
#manual = gc.collect()

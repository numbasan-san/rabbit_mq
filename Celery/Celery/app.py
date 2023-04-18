# celery -A tasks worker -l info --pool=solo
from tasks import *
import time


'''
time.sleep(2) 
hello.delay('world.')

suma.delay(2, 0)

veraz.delay(True)
'''
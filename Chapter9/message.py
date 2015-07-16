'''
from Skype4Py import Skype
import sys

client = Skype()
client.Attach()
user = sys.argv[1]
message = ' '.join(sys.argv[2:]
client.SendMessage(user, message)
'''

import Skype4Py 
skype = Skype4Py.Skype()
skype.SendMessage('skype name','your message text')


skype.Placecall('skype name')



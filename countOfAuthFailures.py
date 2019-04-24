import time
from systemd import journal

countOfHour = 1
strPatternContain = 'authentication failures'

timeAgo = time.time() - countOfHour * 60**2
j = journal.Reader()
j.seek_realtime(timeAgo)

countResult = 0
for entry in j:                                 
	if strPatternContain in entry['MESSAGE']:
		countResult += 1

print('the result = ' + str(countResult))

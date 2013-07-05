import json
import urllib2
import csv
import base64
import os
import glob

os.chdir(".")
username = 'yourname@company.com'
password = 'yourpassword!'

inf = csv.reader(open('salesforce solutions.csv','r'))
for row in inf:
	print row[0]
	content = row[1].replace('\n','<br/>')
	data = {"topic": {"forum_id": 22263091u, "title": row[0], "body": content, "topic_type": "articles", "access": "logged in users" } }
	jsondata = json.dumps(data)
	req = urllib2.Request(url='https://yoursite.zendesk.com/api/v2/topics.json', data = jsondata, headers={'Content-Type': 'application/json'})
	base64string = base64.encodestring('%s:%s' % (username,password)).replace('\n','')
	req.add_header("Authorization","Basic %s" % base64string)
	result = urllib2.urlopen(req)

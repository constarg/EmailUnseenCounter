import imaplib
import email
import json
import sys

class EmailUnreadCount():
	def __init__(self):
		# initialize 
		self.jsonFile="credentials.json";

	def getData(self):
		# get the data from json.
		try:
			jsonOpen=open(self.jsonFile)
			self.credentials=json.load(jsonOpen) # load credentials
		except:
			raise Exception("Unable to load the credentials.")
		finally:
			jsonOpen.close()

	def getUnseen(self):
		self.getData()
		self.credentials=self.credentials['emails'] 
		keys=self.credentials.keys()
		results={} # create an empty dictionary
		for data in keys:
			conn=imaplib.IMAP4_SSL("imap.gmail.com","993")
			try:
				# connecting with the specific email.
				retcode,capabilities=conn.login(self.credentials[data]['username'],self.credentials[data]['password'])
			except:
				# if connection failed write, 'FAILED'
				results[data]="FAILED"
				continue
			conn.select()
			# search for all the unseen emails.
			retcode,messages=conn.search(None, '(UNSEEN)')
			unreadMails=0
			if retcode=="OK":
				for unseen in messages[0].decode().split(' '):
					if unseen!="":
						# count the unseen emails
						unreadMails+=1
			# close the connection and logout
			conn.close()
			conn.logout()
			# save the unseen count on the dictionary.
			results[data]=str(unreadMails)
		# return the dictionary.
		return results
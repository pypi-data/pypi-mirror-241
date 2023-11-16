import extract_msg
import chardet
import os
import bs4
import RTFDE

# filePath = "/data/msg_bugs/issues/Creation of a Committee to Create Additional Funding Opportunities for UAlbany.msg"
#filePath = "/data/msg_bugs/issues/FW SUNY-wide transfer in the major (1).msg"
filePath = "/data/msg_bugs/Digitization Archiving Solutions.msg"

# filePath = "/data/msg_bugs/new"
"""
for msg in os.listdir(filePath):
	if msg.endswith("msg"):
		print (msg)
		mail = extract_msg.openMsg(os.path.join(filePath, msg))
		body = mail.rtfBody
		print (chardet.detect(body))
		deencapsultor = RTFDE.DeEncapsulator(body)
		deencapsultor.deencapsulate()
"""
mail = extract_msg.openMsg(os.path.join(filePath))
# print (mail.sender)
# print (mail.to)

# print (mail.areStringsUnicode)

# print (mail.rtfBody)
# body = mail.rtfBody

"""
with open("/data/msg_bugs/issues/test-default.rtf", "wb") as f:
	f.write(body)
with open("/data/msg_bugs/issues/test-1252.rtf", "w") as f:
	f.write(body.decode("cp1252"))
with open("/data/msg_bugs/issues/test-950.rtf", "w") as f:
	f.write(body.decode("cp950"))
"""


# enc = chardet.detect(body)
# print (chardet.detect(body))

for i, mailAttachment in enumerate(mail.attachments):
	print (mailAttachment.contentId)

# deencapsultor = RTFDE.DeEncapsulator(body)
# deencapsultor.deencapsulate()


"""
if (mail.htmlBody):
	enc = chardet.detect(mail.htmlBody)
	print ("\t--> " + enc["encoding"])
	print (mail.htmlBody)
	#body = mail.htmlBody.decode('utf-8')
	#soup = bs4.BeautifulSoup(mail.htmlBody, 'html.parser')
	#meta = soup.find("meta")
	#print (meta)
	#try:
	#	body = mail.htmlBody.decode('cp1252')
	#except:
	#	body = mail.htmlBody.decode('utf-8')
	#print (body)
	#print (mail.stringEncoding)
	#print (mail.overrideEncoding)
	#print (dir(mail))
"""

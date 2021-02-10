# update class
# member variables: date, ip, phone, phone_type, service, amount, method, version, status_code, data_size
# [02/Feb/2021:18:33:40] 147.173.81.53 - 01882107078 prepaid  packs 563 "GET HTTP/1.0" 200 912198
class Row():
	# create a constructor
	def __init__(self, date, ip, phone, phone_type, service, amount, method, version, status_code, data_size):
		self.date = date
		self.ip = ip
		self.phone = phone
		self.phone_type = phone_type
		self.service = service
		self.amount = amount
		self.method = method
		self.version = version
		self.status_code = status_code
		self.data_size = data_size
	


class Data():
	# TODO

	def __init__(self):
		rows = []
		serviceCount = {} 
		inAmount = {} # phone_type wise
		outAmount = {} # phone_type wise
		methodCount = 0

	def add(self, raw):
		pass
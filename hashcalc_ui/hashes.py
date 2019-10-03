import hashlib 

def md5(s):
	h = hashlib.md5(s.encode())
	return h.hexdigest()

def sha1(s):
	h = hashlib.sha1(s.encode())
	return h.hexdigest()

def sha224(s):
	h = hashlib.sha224(s.encode())
	return h.hexdigest()

def sha256(s):
	h = hashlib.sha256(s.encode())
	return h.hexdigest()

def sha384(s):
	h = hashlib.sha384(s.encode())
	return h.hexdigest()

def sha512(s):
	h = hashlib.sha512(s.encode())
	return h.hexdigest()

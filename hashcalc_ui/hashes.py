import hashlib 


def md4(s):
	pass

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

def whirlpool(s):
	h = hashlib.whirlpool(s.encode())
	return h.hexdigest()

def ripemd160(s):
	h = hashlib.ripemd160(s.encode())
	return h.hexdigest()

def shake128(s):
	h = hashlib.sha256(s.encode())
	return h.hexdigest()

def sm3(s):
	h = hashlib.sm3(s.encode())
	return h.hexdigest()

def mdc2(s):
	h = hashlib.mdc2(s.encode())
	return h.hexdigest()
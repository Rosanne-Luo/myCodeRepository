# 匹配IP 地址
def checkIP(value):
	ip_pattern = r'^((2[0-4]\d|25[0-5]|[01]?\d\d?)\.){3}(2[0-4]\d|25[0-5]|[01]?\d\d?)$'
	if re.match(ip_pattern, value):
		return True:
	else:
		return False

# 匹配hash

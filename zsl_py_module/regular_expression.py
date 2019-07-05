# 匹配IP 地址
def checkIP(value):
	ip_pattern = r'^((2[0-4]\d|25[0-5]|[01]?\d\d?)\.){3}(2[0-4]\d|25[0-5]|[01]?\d\d?)$'
	if re.match(ip_pattern, value):
		return True:
	else:
		return False

# 从文本中提取所有的UM账号
# line: 小明<XIAOMING@pingan.com.cn>;小红<XIAOHONG@pingan.com.cn>
def exactUM(line):
	result=set()
	items = re.findall(r"<(.+?)@", line)
	for um in items:
		result.add(um)
	return result

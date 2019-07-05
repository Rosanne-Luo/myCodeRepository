import datetime

def generate_date(start, end):
	''' 生成指定范围类的一组日期
	
	Args:
		start: 起始日期, eg 2019-02-01
		end: 结束日期, eg 2019-02-05

	Returns:
		以 list 的结构返回生成的一组日期
		
		example:

		['2019-02-01', '2019-02-02', '2019-02-03']
	'''
		start_date = datetime.datetime.strptime(start, '%Y-%m-%d')
		end_date = datetime.datetime.strptime(end, '%Y-%m-%d')

		result = []
		while start_date < end_date:
			start_date += datetime.timedelta(days=1)
			result.append(start_date.strftime('%Y-%m-%d'))
		
		return result


def main():
	result = generate_date('2019-04-02', '2019-05-01')
	print(result)

if __name__ == "__main__":
	main()

		
		

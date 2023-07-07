import datetime

def is_palindrome(date):
    # 将日期转换为字符串并移除破折号
    date_str = date.replace('-', '')

    # 检查日期字符串是否等于其反转字符串
    return date_str == date_str[::-1]

start_date = input("开始日期 (mm-dd-yyyy)：")
end_date = input("结束日期 (mm-dd-yyyy)：")
start_date = date.replace('-', '')
end_date = date.replace('-', '')
end_date == end_date[::-1]

palindrome_days = generate_palindrome_days(start_date, end_date)


def is_palindrome(date):
    # 将日期转换为字符串并移除破折号
    date_str = date.replace('-', '')

    # 检查日期字符串是否等于其反转字符串
    return date_str == date_str[::-1]


def generate_palindrome_days(start_date, end_date):
    # 将开始日期和结束日期转换为datetime对象
    start = datetime.datetime.strptime(start_date, '%m-%d-%Y')
    end = datetime.datetime.strptime(end_date, '%m-%d-%Y')

    palindrome_days = []
    current_date = start

    # 在范围内遍历日期
    while current_date <= end:
        date_str = current_date.strftime('%m-%d-%Y')
        if is_palindrome(date_str):
            palindrome_days.append(date_str)
        current_date += datetime.timedelta(days=1)

    return palindrome_days


# 打印回文日期
if palindrome_days:
    print("在", start_date, "和", end_date, "之间的回文日期：")
    for day in palindrome_days:
        print(day)
else:
    print("在", start_date, "和", end_date, "之间没有找到回文日期。")
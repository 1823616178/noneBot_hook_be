import re


# 格式化数据
def fomatMessage(mobiles, weibo):
    content = "你所查询的数据如下：" + '\n'
    for item in mobiles:
        content = content + 'QQ:' + item[0] + '  手机:' + item[1] + '\n'
    for items in weibo:
        content = content + '微博地址:' + 'https://weibo.com/u/' + items[0] + '\n'
    return content


# 判断手机号
def validPhone(phone):
    reg = '^1(3[0-9]|4[5,7]|5[0,1,2,3,5,6,7,8,9]|6[2,5,6,7]|7[0,1,7,8]|8[0-9]|9[1,8,9])\d{8}$'
    if re.match(reg, phone):
        return True
    else:
        return False


# 判断是否为数字
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

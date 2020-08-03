# -*- coding: utf-8 -*-
"""
 author: lvsongke@oneniceapp.com
 data:2019/09/11
"""

"""
将整数数字转换成罗马数字
"""


def int2roman(num):
    """
    将输入的数字转换成罗马数字
    :param num:
    :return:
    """
    if num < 1 and num > 3999:
        raise ValueError('num overflow!!')
    """
    判断num在哪个区间内
    """
    mapping = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M',
        4000: 'EOP'
    }
    res = []
    cut = list(mapping.keys())
    while num > 0:
        for idx, val in enumerate(cut):
            if num < val:
                res.append(mapping[cut[idx - 1]])
                num = num - cut[idx - 1]
                break
    return ''.join(res)


if __name__ == '__main__':
    num = 3890
    res = int2roman(num)
    print(res)

import string


def deal_with_long_text(long_text):
    # 字符串处理
    temp = long_text.strip().replace(' ', '').split('\n')
    temp_1 = temp[:2]
    temp_2 = temp[2:]

    keyname_lst = ['name', 'lei', 'sub_fund']
    title_lst = ['title', 'isin']

    sub_lst = []
    for i in range(len(temp_2) - 1):

        sub_temp = []
        if i % 4 == 0:
            temp_2[i] = temp_2[i].lstrip(string.digits).strip('. ')
            sub_temp.append(temp_2[i])
            sub_temp.append(temp_2[i + 1:i + 4])
            dict_temp = dict(zip(title_lst, sub_temp))
            sub_lst.append(dict_temp)

    temp_1.append(sub_lst)
    dict_result = dict(zip(keyname_lst, temp_1))
    print(dict_result)


if __name__ == '__main__':
    long_text = """Variopartner SICAV
    529900LPCSV88817QH61
    1. TARENO GLOBAL WATER SOLUTIONS FUND
    LU2001709034
    LU2057889995
    LU2001709547
    2. TARENO FIXED INCOME FUND
    LU1299722972
    LU1299723277
    LU1299723194
    3. TARENO GLOBAL EQUITY FUND
    LU1299721909
    LU1299722113
    LU1299722030
    4. MIV GLOBAL MEDTECH FUND
    LU0329630999
    LU0329630130
    LU0969575561
    """

    deal_with_long_text(long_text)

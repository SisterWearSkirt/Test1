from bs4 import BeautifulSoup
import csv

file_name = '实时更新：新型冠状病毒肺炎疫情地图.html'


# 读取数据
def sprider_result():
    soup = BeautifulSoup(open(file_name, encoding='utf-8'), 'lxml')
    div_one = soup.find('div', attrs={'id': 'nationTable'})
    table_one = div_one.find('table', class_='VirusTable_1-1-310_38pQEh')
    tbody_one = table_one.find('tbody')
    tr_list = tbody_one.find_all('tr', class_='VirusTable_1-1-310_3m6Ybq')
    result = []

    for tr_one in tr_list:
        td_list = tr_one.find_all('td')
        temp = []
        for index, td_one in enumerate(td_list):
            if index == 0:
                div_one = td_one.find('div')
                span_result = div_one.find_all('span')[1]
                temp.append(span_result.text)
            else:
                temp.append(td_one.text)

        result.append(temp)
    return result


# 将读取的数据写入到csv文件中
def write_file(result: list):
    result.insert(0, ['疫情地区', '新增', '现有', '累计', '治愈', '死亡'])
    with open('AllTimeUpdate.csv', 'w', newline='') as f:
        writing = csv.writer(f, dialect='excel')
        writing.writerows(result)


if __name__ == '__main__':
    result = sprider_result()
    write_file(result)

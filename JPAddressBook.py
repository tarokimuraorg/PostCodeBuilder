import re
import pandas
from JPAddressPage import JPAddressPage
import ErrorMessageBuilder

def createAddressBook():

    address_book = []

    try:

        data_frame = pandas.read_csv('./csv/ken_all.csv', usecols=[2,3,4,5,6,7,8], names=['post_code','furigana1','furigana2','furigana3','address1','address2','address3'])
        csv_data = data_frame.drop_duplicates()
        csv_list = csv_data.values.tolist()

        if len(csv_list) > 0:

            for row in csv_list:

                post_code = '0'
                post_code = post_code + str(row[0])
                post_code = post_code.strip()

                furigana = str(row[1]) + ' '
                furigana = furigana + str(row[2]) + ' '
                furigana = furigana + str(row[3])
                furigana = furigana.replace('ｲｶﾆｹｲｻｲｶﾞﾅｲﾊﾞｱｲ','')
                furigana = re.sub('\(\d+-\d+ﾁｮｳﾒ\)','',furigana)
                furigana = furigana.strip()

                address = str(row[4]) + ' '
                address = address + str(row[5]) + ' '
                address = address + str(row[6])
                address = address.replace('以下に掲載がない場合','')
                address = re.sub('（\d+～\d+丁目）','',address)
                address = address.strip()

                address_page = JPAddressPage(post_code, address, furigana)
                address_book.append(address_page)

    except Exception as e:
        print(ErrorMessageBuilder.message('JPAddressBook', 'init', 'failed to read csv data', f'{e}'))
    
    return address_book

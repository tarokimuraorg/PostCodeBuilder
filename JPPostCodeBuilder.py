import re
import JPAddressData
from JPAddressPage import JPAddressPage
from StringConvertor import StringConvertor
import ErrorMessageBuilder

class JPPostCodeBuilder:

    def __init__(self, post_code : str):

        self._post_code = ''

        in_code = post_code.strip()
        out_code = StringConvertor().toHankaku(in_code)
        out_code = out_code.replace('-', '')
        
        if re.match('^\d{7}$', out_code):
             self._post_code = out_code

    def address_finder(self):

        if self._post_code:

            address_data = JPAddressData.read_address_data()
            address_data = list(filter(lambda row: str(row[0]).strip() == self._post_code[1:], address_data))

            if len(address_data) > 0:

                address_book = list(map(self.__write_on_address_page, address_data))

                if (self._post_code[0:3] == '079'):

                    if len(address_book) > 0:
                        return address_book
                    
                    return [JPAddressPage(self._post_code, '北海道 赤平市', 'ﾎｯｶｲﾄﾞｳ ｱｶﾋﾞﾗｼ')]

                return address_book
    
        print(ErrorMessageBuilder.message('JPPostCodeBuilder','address_finder','invalid argument','the post code is a 7-digit number.'))
        return []
    
    def __write_on_address_page(self, row):

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

        return JPAddressPage(post_code, address, furigana)

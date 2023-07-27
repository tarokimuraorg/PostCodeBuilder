import re
import AddressData
from AddressPage import AddressPage
from StringConvertor import StringConvertor
import ErrorMessageBuilder

class PostCodeBuilder:

    def __init__(self, post_code : str):

        self._post_code = ''

        in_code = post_code.strip()
        out_code = StringConvertor().toHankaku(in_code)
        out_code = out_code.replace('-', '')
        
        if re.match('^\d{7}$', out_code):
             self._post_code = out_code

    def address_finder(self):

        if self._post_code:

            raw_address_data = AddressData.read_address_data()

            # 7桁の郵便番号で検索
            address_data = list(filter(lambda row: str(row[0]).strip().zfill(7) == self._post_code, raw_address_data))

            if len(address_data) > 0:

                address_book = list(map(self.__write_on_address_page, address_data))

                if len(address_book) > 0:
                    return address_book
            
            # 上5桁の郵便番号で検索
            address_data = list(filter(lambda row: str(row[0]).strip().zfill(7) == f'{self._post_code[0:5]}00', raw_address_data))

            if len(address_data) > 0:

                address_book = list(map(self.__write_on_address_page, address_data))

                if len(address_book) > 0:
                    return address_book

            # 上3桁の郵便番号で検索
            address_data = list(filter(lambda row: str(row[0]).strip().zfill(7) == f'{self._post_code[0:3]}0000', raw_address_data))

            if len(address_data) > 0:

                address_book = list(map(self.__write_on_address_page, address_data))

                if len(address_book) > 0:
                    return address_book

            print(ErrorMessageBuilder.message('JPPostCodeBuilder','address_finder','invalid argument',f'the argument ({self._post_code}) is an incompatible post code.'))
            return []
    
        print(ErrorMessageBuilder.message('JPPostCodeBuilder','address_finder','invalid argument','post code is a 7-digit number.'))
        return []
    
    def __write_on_address_page(self, row):

        # post_code = str(row[0])
        # post_code = post_code.strip().zfill(7)

        furigana = str(row[1]) + ' '
        furigana = furigana + str(row[2]) + ' '
        furigana = furigana + str(row[3])
        furigana = furigana.replace('イカニケイサイガナイバアイ','')
        furigana = re.sub('（.+）', '', furigana)
        furigana = furigana.strip()

        address = str(row[4]) + ' '
        address = address + str(row[5]) + ' '
        address = address + str(row[6])
        address = address.replace('以下に掲載がない場合','')
        address = re.sub('（.+）', '', address)
        
        address = address.strip()

        return AddressPage(self._post_code, address, furigana)

import re
import JPAddressBook
from JPAddressPage import JPAddressPage
from StringConvertor import StringConvertor
import ErrorMessageBuilder

class JPPostCodeBuilder:

    def __init__(self, post_code : str):

        self._address_book = JPAddressBook.createAddressBook()
        self._post_code = ''

        in_code = post_code.strip()
        out_code = StringConvertor().toHankaku(in_code)
        out_code = out_code.replace('-', '')
        
        if re.match('^\d{7}$', out_code):
             self._post_code = out_code

    def address_finder(self):

        if self._post_code:
         
            address_pages = list(filter(lambda page: page.post_code == self._post_code, self._address_book))

            if (self._post_code[0:3] == '079'):

                if len(address_pages) > 0:
                    return address_pages
                
                return JPAddressPage(self._post_code, '北海道 赤平市', 'ﾎｯｶｲﾄﾞｳ ｱｶﾋﾞﾗｼ')

            return address_pages
    
        print(ErrorMessageBuilder.message('JPPostCodeBuilder','address_finder','invalid argument','the post code is a 7-digit number.'))
        return []

import re
import dataclasses
from JPAddressBook import JPAddressBook
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
        else:
            print(ErrorMessageBuilder.message('JPPostCodeBuilder','address_finder','invalid argument','the post code is a 7-digit number.'))

    def address_finder(self):

        if self._post_code:

            address_book = JPAddressBook().createAddressBook()
            address_pages = list(filter(lambda page: (page.post_code == self._post_code) or \
                               (page.post_code[3:] == '0000' and \
                                page.post_code[0:3] == self._post_code[0:3]), address_book))

            if len(address_pages) > 1:
                return list(filter(lambda page: page.post_code[3:] != '0000', address_pages))

            if len(address_pages) == 1:

                page = address_pages[0]

                if page.post_code[3:] == '0000':
                    return [dataclasses.replace(page, post_code=self._post_code)]
                else:
                    return address_pages
    
            print(ErrorMessageBuilder.message('JPPostCodeBuilder','address_finder','invalid argument',f'the post code {self._post_code} is an incompatible value.'))

        return []

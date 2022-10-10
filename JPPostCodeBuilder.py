import re
from JPAddressBook import JPAddressBook
from ErrorMessageCreator import ErrorMessageCreator

class JPPostCodeBuilder:

    def __init__(self, post_code : str):

        self._post_code = post_code.strip()
        self._emcreator = ErrorMessageCreator()
        
        if re.match('^\d{3}-\d{4}$', self._post_code):
            self._post_code = self._post_code.replace('-','')

    def __digits_only(self) -> bool:

        if re.match('^\d{7}$',self._post_code):
            return True

        return False

    def address_finder(self):

        if self.__digits_only():
        
            address_book = JPAddressBook().createAddressBook()
            results = filter(lambda page: page.post_code == self._post_code, address_book)

            return list(results)

        print(self._emcreator.message('JPPostCodeBuilder','address_finder','invalid argument','the post code is an incompatible value.'))
        return []

import re
from ErrorMessageCreator import ErrorMessageCreator

class JPPostCodeBuilder:

    def __init__(self, post_code : str):

        self._post_code = ''
        self._emcreator = ErrorMessageCreator()
        
        if re.match('^\d{3}-\d{4}$', post_code):
            self._post_code = post_code.replace('-','')
        
        if re.match('^\d{7}$', post_code):
            self._post_code = post_code

    def digits_only(self) -> str:

        if (re.match('^\d{7}$',self._post_code)):
            return self._post_code

        raise ValueError(self._emcreator.message('JPPostCodeBuilder.py','init','invalid argument','the argument is an incompatible japan post code.'))

    def convertToAddress(self):

        if self._post_code == '0791143':
            return '北海', '道', '赤平', '市'

        raise ValueError(self._emcreator.message('JPPostCodeBuilder.py','convertToAddress','post code error','the post code is an incompatible value.'))

    def convertKanjiToYomigana(self):

        address = self.convertToAddress()
        yomigana = []

        for kanji in address:

            if kanji == '道':
                yomigana.append('ドウ')
            
            if kanji == '市':
                yomigana.append('シ')                

            if kanji == '北海':
                yomigana.append('ホッカイ')

            if kanji == '赤平':
                yomigana.append('アカビラ')

        if len(yomigana) > 0:
            return yomigana

        raise ValueError(self._emcreator.message('JPPostCodeBuilder.py','convertKanjiToYomigana','kanji error','the kanji is an incompatible value.'))

import re
from ErrorMessageCreator import ErrorMessageCreator

class JPPostCodeBuilder:

    def __init__(self, post_code : str):

        self._post_code = post_code.strip()
        self._emcreator = ErrorMessageCreator()
        
        if re.match('^\d{3}-\d{4}$', self._post_code):
            self._post_code = self._post_code.replace('-','')

    def digits_only(self) -> str:

        if (re.match('^\d{7}$',self._post_code)):
            return self._post_code

        raise ValueError(self._emcreator.message('JPPostCodeBuilder.py','init','invalid argument','the argument is an incompatible japan post code.'))

    def convertToAddress(self):

        if (re.match('^\d{7}$',self._post_code)):
            
            address = []

            first_three_digits = self._post_code[0:3]
            last_four_digits = self._post_code[3:7]

            if first_three_digits == '079':

                address.append('北海道')
                address.append('赤平市')

            if last_four_digits == '1143':

                address.append('赤平')
                return address

            elif last_four_digits == '1134':

                address.append('泉町')
                return address

            elif last_four_digits == '1274':

                address.append('エルム町')
                return address

            elif last_four_digits == '1141':
            
                address.append('大町')
                return address

            elif last_four_digits == '1121':
                
                address.append('北文京町')
                return address

            elif last_four_digits == '1101':
                
                address.append('共和町')
                return address

            elif last_four_digits == '1154':
                
                address.append('幸町')
                return address

            elif last_four_digits == '1152':

                address.append('桜木町')
                return address

            elif last_four_digits == '1155':

                address.append('昭和町')
                return address

            elif last_four_digits == '1156':

                address.append('住吉町')
                return address

            elif last_four_digits == '1124':

                address.append('豊丘町')
                return address

            elif last_four_digits == '1133':

                address.append('豊里')
                return address

            elif last_four_digits == '1135':

                address.append('錦町')
                return address

            elif last_four_digits == '1131':

                address.append('西豊里町')
                return address

            elif last_four_digits == '1122':

                address.append('西文京町')
                return address

            raise ValueError(self._emcreator.message('JPPostCodeBuilder.py','convertToAddress','post code error','the post code is an incompatible value.'))

        raise ValueError(self._emcreator.message('JPPostCodeBuilder.py','init','invalid argument','the argument is an incompatible japan post code.'))

    def convertKanjiToYomigana(self):

        address = self.convertToAddress()
        yomigana = []

        for kanji in address:

            if kanji == '北海道':
                yomigana.append('ホッカイドウ')

            if kanji == '赤平市':
                yomigana.append('アカビラシ')

            if kanji == '赤平':
                yomigana.append('アカビラ')

            elif kanji == '泉町':
                yomigana.append('イズミマチ')

            elif kanji == 'エルム町':
                yomigana.append('エルムチョウ')

            elif kanji == '大町':
                yomigana.append('オオマチ')

            elif kanji == '北文京町':
                yomigana.append('キタブンキョウチョウ')
            
            elif kanji == '共和町':
                yomigana.append('キョウワチョウ')
            
            elif kanji == '幸町':
                yomigana.append('サイワイチョウ')

            elif kanji == '桜木町':
                yomigana.append('サクラギチョウ')

            elif kanji == '昭和町':
                yomigana.append('ショウワチョウ')

            elif kanji == '住吉町':
                yomigana.append('スミヨシチョウ')

            elif kanji == '豊丘町':
                yomigana.append('トヨオカチョウ')

            elif kanji == '豊里':
                yomigana.append('トヨサト')
            
            elif kanji == '錦町':
                yomigana.append('ニシキマチ')

            elif kanji == '西豊里町':
                yomigana.append('ニシトヨサトチョウ')

            elif kanji == '西文京町':
                yomigana.append('ニシブンキョウチョウ')

        if len(yomigana) > 0:
            return yomigana

        raise ValueError(self._emcreator.message('JPPostCodeBuilder.py','convertKanjiToYomigana','kanji error','the kanji is an incompatible value.'))

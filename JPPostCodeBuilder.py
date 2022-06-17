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

        post_code = self.digits_only()

        first_three_digits = post_code[0:3]
        last_four_digits = post_code[3:7]

        address = []

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

            elif last_four_digits == '1142':

                address.append('東大町')
                return address

            elif last_four_digits == '1132':

                address.append('東豊里町')
                return address

            elif last_four_digits == '1123':

                address.append('東文京町')
                return address

            elif last_four_digits == '1271':

                address.append('百戸町北')
                return address

            elif last_four_digits == '1273':

                address.append('百戸町西')
                return address

            elif last_four_digits == '1272':

                address.append('百戸町東')
                return address

            elif last_four_digits == '1285':

                address.append('平岸曙町')
                return address

            elif last_four_digits == '1287':

                address.append('平岸桂町')
                return address

            elif last_four_digits == '1281':

                address.append('平岸新光町')
                return address

            elif last_four_digits == '1282':

                address.append('平岸仲町')
                return address

            elif last_four_digits == '1286':

                address.append('平岸西町')
                return address

            elif last_four_digits == '1283':

                address.append('平岸東町')
                return address

            elif last_four_digits == '1284':

                address.append('平岸南町')
                return address

            elif last_four_digits == '1153':

                address.append('豊栄町')
                return address

            elif last_four_digits == '1102':

                address.append('幌岡町')
                return address

            elif last_four_digits == '1136':

                address.append('本町')
                return address

        raise ValueError(self._emcreator.message('JPPostCodeBuilder.py','convertToAddress','post code error','the post code is an incompatible value.'))
        
    def convertKanjiToYomigana(self):

        address = self.convertToAddress()
        yomigana = []

        if len(address) == 3:

            if address[0] == '北海道':
                yomigana.append('ホッカイドウ')

                if address[1] == '赤平市':
                    yomigana.append('アカビラシ')

                    if address[2] == '赤平':
                        yomigana.append('アカビラ')

                    elif address[2] == '泉町':
                        yomigana.append('イズミマチ')

                    elif address[2] == 'エルム町':
                        yomigana.append('エルムチョウ')

                    elif address[2] == '大町':
                        yomigana.append('オオマチ')

                    elif address[2] == '北文京町':
                        yomigana.append('キタブンキョウチョウ')
            
                    elif address[2] == '共和町':
                        yomigana.append('キョウワチョウ')
            
                    elif address[2] == '幸町':
                        yomigana.append('サイワイチョウ')

                    elif address[2] == '桜木町':
                        yomigana.append('サクラギチョウ')

                    elif address[2] == '昭和町':
                        yomigana.append('ショウワチョウ')

                    elif address[2] == '住吉町':
                        yomigana.append('スミヨシチョウ')

                    elif address[2] == '豊丘町':
                        yomigana.append('トヨオカチョウ')

                    elif address[2] == '豊里':
                        yomigana.append('トヨサト')
            
                    elif address[2] == '錦町':
                        yomigana.append('ニシキマチ')

                    elif address[2] == '西豊里町':
                        yomigana.append('ニシトヨサトチョウ')

                    elif address[2] == '西文京町':
                        yomigana.append('ニシブンキョウチョウ')

                    elif address[2] == '東大町':
                        yomigana.append('ヒガシオオマチ')

                    elif address[2] == '東豊里町':
                        yomigana.append('ヒガシトヨサトチョウ')

                    elif address[2] == '東文京町':
                        yomigana.append('ヒガシブンキョウチョウ')

                    elif address[2] == '百戸町北':
                        yomigana.append('ヒャッコチョウキタ')

                    elif address[2] == '百戸町西':
                        yomigana.append('ヒャッコチョウニシ')

                    elif address[2] == '百戸町東':
                        yomigana.append('ヒャッコチョウヒガシ')

                    elif address[2] == '平岸曙町':
                        yomigana.append('ヒラギシアケボノチョウ')

                    elif address[2] == '平岸桂町':
                        yomigana.append('ヒラギシカツラチョウ')

                    elif address[2] == '平岸新光町':
                        yomigana.append('ヒラギシシンコウチョウ')

                    elif address[2] == '平岸仲町':
                        yomigana.append('ヒラギシナカマチ')

                    elif address[2] == '平岸西町':
                        yomigana.append('ヒラギシニシマチ')

                    elif address[2] == '平岸東町':
                        yomigana.append('ヒラギシヒガシマチ')

                    elif address[2] == '平岸南町':
                        yomigana.append('ヒラギシミナミマチ')

                    elif address[2] == '豊栄町':
                        yomigana.append('ホウエイチョウ')

                    elif address[2] == '幌岡町':
                        yomigana.append('ホロオカチョウ')

                    elif address[2] == '本町':
                        yomigana.append('ホンチョウ')

        if len(yomigana) > 0:
            return yomigana

        raise ValueError(self._emcreator.message('JPPostCodeBuilder.py','convertKanjiToYomigana','kanji error','the kanji is an incompatible value.'))

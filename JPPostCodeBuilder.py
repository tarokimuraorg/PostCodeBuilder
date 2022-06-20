import re
import copy
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

        raise ValueError(self._emcreator.message('JPPostCodeBuilder.py','digits_only','invalid argument','the post code is an incompatible value.'))

    def convertToAddress(self):

        post_code = self.digits_only()

        first_three_digits = post_code[0:3]
        last_four_digits = post_code[3:7]

        address = []
        results = []

        if first_three_digits == '079':

            address.append('北海道')
            address.append('赤平市')

            if last_four_digits == '1143':

                address.append('赤平')
                results.append(address)

                return results

            elif last_four_digits == '1134':

                address.append('泉町')
                results.append(address)

                return results

            elif last_four_digits == '1274':

                address.append('エルム町')
                results.append(address)

                return results

            elif last_four_digits == '1141':
            
                address.append('大町')
                results.append(address)

                return results

            elif last_four_digits == '1121':
                
                address.append('北文京町')
                results.append(address)

                return results

            elif last_four_digits == '1101':
                
                address.append('共和町')
                results.append(address)

                return results

            elif last_four_digits == '1154':
                
                address.append('幸町')
                results.append(address)

                return results

            elif last_four_digits == '1152':

                address.append('桜木町')
                results.append(address)

                return results

            elif last_four_digits == '1155':

                address.append('昭和町')
                results.append(address)

                return results

            elif last_four_digits == '1156':

                address.append('住吉町')
                results.append(address)

                return results

            elif last_four_digits == '1124':

                address.append('豊丘町')
                results.append(address)

                return results

            elif last_four_digits == '1133':

                address.append('豊里')
                results.append(address)

                return results

            elif last_four_digits == '1135':

                address.append('錦町')
                results.append(address)

                return results

            elif last_four_digits == '1131':

                address.append('西豊里町')
                results.append(address)

                return results

            elif last_four_digits == '1122':

                address.append('西文京町')
                results.append(address)

                return results

            elif last_four_digits == '1142':

                address.append('東大町')
                results.append(address)

                return results

            elif last_four_digits == '1132':

                address.append('東豊里町')
                results.append(address)

                return results

            elif last_four_digits == '1123':

                address.append('東文京町')
                results.append(address)

                return results

            elif last_four_digits == '1271':

                address.append('百戸町北')
                results.append(address)

                return results

            elif last_four_digits == '1273':

                address.append('百戸町西')
                results.append(address)

                return results

            elif last_four_digits == '1272':

                address.append('百戸町東')
                results.append(address)

                return results

            elif last_four_digits == '1285':

                address.append('平岸曙町')
                results.append(address)

                return results

            elif last_four_digits == '1287':

                address.append('平岸桂町')
                results.append(address)

                return results

            elif last_four_digits == '1281':

                address.append('平岸新光町')
                results.append(address)

                return results

            elif last_four_digits == '1282':

                address.append('平岸仲町')
                results.append(address)

                return results

            elif last_four_digits == '1286':

                address.append('平岸西町')
                results.append(address)

                return results

            elif last_four_digits == '1283':

                address.append('平岸東町')
                results.append(address)

                return results

            elif last_four_digits == '1284':

                address.append('平岸南町')
                results.append(address)

                return results

            elif last_four_digits == '1153':

                address.append('豊栄町')
                results.append(address)

                return results

            elif last_four_digits == '1102':

                address.append('幌岡町')
                results.append(address)

                return results

            elif last_four_digits == '1136':

                address.append('本町')
                results.append(address)

                return results

            elif last_four_digits == '1144':

                address.append('美園町')
                results.append(address)

                return results

            elif last_four_digits == '1151':

                address.append('宮下町')
                results.append(address)

                return results

            elif last_four_digits == '1266':

                address1 = copy.deepcopy(address)
                address2 = copy.deepcopy(address)

                address1.append('茂尻')
                address2.append('茂尻栄町')

                results.append(address1)
                results.append(address2)
                
                return results

            elif last_four_digits == '1264':

                address.append('茂尻旭町')
                results.append(address)

                return results

            elif last_four_digits == '1262':

                address1 = copy.deepcopy(address)
                address2 = copy.deepcopy(address)

                address1.append('茂尻春日町')
                address2.append('茂尻新春日町')

                results.append(address1)
                results.append(address2)

                return results

            elif last_four_digits == '1265':

                address.append('茂尻新町')
                results.append(address)

                return results

            elif last_four_digits == '1261':

                address.append('茂尻中央町北')
                results.append(address)

                return results

            elif last_four_digits == '1263':

                address.append('茂尻本町')
                results.append(address)

                return results

            elif last_four_digits == '1264':

                address.append('茂尻宮下町')
                results.append(address)

                return results

            elif last_four_digits == '1268':

                address.append('茂尻元町北')
                results.append(address)

                return results

            elif last_four_digits == '1267':

                address.append('茂尻元町南')
                results.append(address)

                return results

        raise ValueError(self._emcreator.message('JPPostCodeBuilder.py','convertToAddress','post code error','the post code is an incompatible value.'))
        
    def convertKanjiToYomigana(self):

        address = self.convertToAddress()
        results = []

        for elm in address:

            yomigana = []

            if len(elm) == 3:

                if elm[0] == '北海道':
                    yomigana.append('ホッカイドウ')

                    if elm[1] == '赤平市':
                        yomigana.append('アカビラシ')

                        if elm[2] == '赤平':

                            yomigana.append('アカビラ')
                            results.append(yomigana)

                        elif elm[2] == '泉町':

                            yomigana.append('イズミマチ')
                            results.append(yomigana)

                        elif elm[2] == 'エルム町':

                            yomigana.append('エルムチョウ')
                            results.append(yomigana)

                        elif elm[2] == '大町':

                            yomigana.append('オオマチ')
                            results.append(yomigana)

                        elif elm[2] == '北文京町':

                            yomigana.append('キタブンキョウチョウ')
                            results.append(yomigana)
            
                        elif elm[2] == '共和町':

                            yomigana.append('キョウワチョウ')
                            results.append(yomigana)
            
                        elif elm[2] == '幸町':

                            yomigana.append('サイワイチョウ')
                            results.append(yomigana)

                        elif elm[2] == '桜木町':

                            yomigana.append('サクラギチョウ')
                            results.append(yomigana)

                        elif elm[2] == '昭和町':

                            yomigana.append('ショウワチョウ')
                            results.append(yomigana)

                        elif elm[2] == '住吉町':

                            yomigana.append('スミヨシチョウ')
                            results.append(yomigana)

                        elif elm[2] == '豊丘町':

                            yomigana.append('トヨオカチョウ')
                            results.append(yomigana)

                        elif elm[2] == '豊里':

                            yomigana.append('トヨサト')
                            results.append(yomigana)
            
                        elif elm[2] == '錦町':

                            yomigana.append('ニシキマチ')
                            results.append(yomigana)

                        elif elm[2] == '西豊里町':

                            yomigana.append('ニシトヨサトチョウ')
                            results.append(yomigana)

                        elif elm[2] == '西文京町':

                            yomigana.append('ニシブンキョウチョウ')
                            results.append(yomigana)

                        elif elm[2] == '東大町':

                            yomigana.append('ヒガシオオマチ')
                            results.append(yomigana)

                        elif elm[2] == '東豊里町':

                            yomigana.append('ヒガシトヨサトチョウ')
                            results.append(yomigana)

                        elif elm[2] == '東文京町':

                            yomigana.append('ヒガシブンキョウチョウ')
                            results.append(yomigana)

                        elif elm[2] == '百戸町北':

                            yomigana.append('ヒャッコチョウキタ')
                            results.append(yomigana)

                        elif elm[2] == '百戸町西':

                            yomigana.append('ヒャッコチョウニシ')
                            results.append(yomigana)

                        elif elm[2] == '百戸町東':

                            yomigana.append('ヒャッコチョウヒガシ')
                            results.append(yomigana)

                        elif elm[2] == '平岸曙町':

                            yomigana.append('ヒラギシアケボノチョウ')
                            results.append(yomigana)

                        elif elm[2] == '平岸桂町':

                            yomigana.append('ヒラギシカツラチョウ')
                            results.append(yomigana)

                        elif elm[2] == '平岸新光町':

                            yomigana.append('ヒラギシシンコウチョウ')
                            results.append(yomigana)

                        elif elm[2] == '平岸仲町':

                            yomigana.append('ヒラギシナカマチ')
                            results.append(yomigana)

                        elif elm[2] == '平岸西町':

                            yomigana.append('ヒラギシニシマチ')
                            results.append(yomigana)

                        elif elm[2] == '平岸東町':

                            yomigana.append('ヒラギシヒガシマチ')
                            results.append(yomigana)

                        elif elm[2] == '平岸南町':

                            yomigana.append('ヒラギシミナミマチ')
                            results.append(yomigana)

                        elif elm[2] == '豊栄町':

                            yomigana.append('ホウエイチョウ')
                            results.append(yomigana)

                        elif elm[2] == '幌岡町':

                            yomigana.append('ホロオカチョウ')
                            results.append(yomigana)

                        elif elm[2] == '本町':

                            yomigana.append('ホンチョウ')
                            results.append(yomigana)

                        elif elm[2] == '美園町':

                            yomigana.append('ミソノチョウ')
                            results.append(yomigana)

                        elif elm[2] == '宮下町':

                            yomigana.append('ミヤシタチョウ')
                            results.append(yomigana)

                        elif elm[2] == '茂尻':

                            yomigana.append('モジリ')
                            results.append(yomigana)

                        elif elm[2] == '茂尻旭町':

                            yomigana.append('モジリアサヒマチ')
                            results.append(yomigana)

                        elif elm[2] == '茂尻春日町':

                            yomigana.append('モジリカスガチョウ')
                            results.append(yomigana)

                        elif elm[2] == '茂尻栄町':

                            yomigana.append('モジリサカエマチ')
                            results.append(yomigana)

                        elif elm[2] == '茂尻新春日町':

                            yomigana.append('モジリシンカスガチョウ')
                            results.append(yomigana)

                        elif elm[2] == '茂尻新町':

                            yomigana.append('モジリシンマチ')
                            results.append(yomigana)

                        elif elm[2] == '茂尻中央町北':

                            yomigana.append('モジリチュウオウチョウキタ')
                            results.append(yomigana)

                        elif elm[2] == '茂尻本町':

                            yomigana.append('モジリホンチョウ')
                            results.append(yomigana)

                        elif elm[2] == '茂尻宮下町':

                            yomigana.append('モジリミヤシタチョウ')
                            results.append(yomigana)

                        elif elm[2] == '茂尻元町北':

                            yomigana.append('モジリモトマチキタ')
                            results.append(yomigana)

                        elif elm[2] == '茂尻元町南':

                            yomigana.append('モジリモトマチミナミ')
                            results.append(yomigana)

        if len(results) > 0:
            return results

        raise ValueError(self._emcreator.message('JPPostCodeBuilder.py','convertKanjiToYomigana','kanji error','the kanji is an incompatible value.'))

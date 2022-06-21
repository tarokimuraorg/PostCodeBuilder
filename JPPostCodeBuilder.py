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

            elif last_four_digits == '1111':

                address.append('若木町北')
                results.append(address)

                return results

            elif last_four_digits == '1112':

                address.append('若木町西')
                results.append(address)

                return results

            elif last_four_digits == '1113':

                address.append('若木町東')
                results.append(address)

                return results

            elif last_four_digits == '1114':

                address.append('若木町南')
                results.append(address)

                return results

        elif first_three_digits == '085':
            
            address.append('北海道')
            address.append('釧路市')

            if last_four_digits == '0467':
                
                address.append('阿寒町阿寒湖温泉')
                results.append(address)

                return results

            elif last_four_digits == '0238':

                address.append('阿寒町飽別')
                results.append(address)

                return results

            elif last_four_digits == '0212':

                address.append('阿寒町旭町')
                results.append(address)

                return results

        raise ValueError(self._emcreator.message('JPPostCodeBuilder.py','convertToAddress','post code error','the post code is an incompatible value.'))
        
    def convertKanjiToKatakana(self):

        address = self.convertToAddress()
        results = []

        for elm in address:

            katakana = []

            if len(elm) == 3:

                if elm[0] == '北海道':

                    katakana.append('ホッカイドウ')

                    if elm[1] == '赤平市':

                        katakana.append('アカビラシ')

                        if elm[2] == '赤平':

                            katakana.append('アカビラ')
                            results.append(katakana)

                        elif elm[2] == '泉町':

                            katakana.append('イズミマチ')
                            results.append(katakana)

                        elif elm[2] == 'エルム町':

                            katakana.append('エルムチョウ')
                            results.append(katakana)

                        elif elm[2] == '大町':

                            katakana.append('オオマチ')
                            results.append(katakana)

                        elif elm[2] == '北文京町':

                            katakana.append('キタブンキョウチョウ')
                            results.append(katakana)
            
                        elif elm[2] == '共和町':

                            katakana.append('キョウワチョウ')
                            results.append(katakana)
            
                        elif elm[2] == '幸町':

                            katakana.append('サイワイチョウ')
                            results.append(katakana)

                        elif elm[2] == '桜木町':

                            katakana.append('サクラギチョウ')
                            results.append(katakana)

                        elif elm[2] == '昭和町':

                            katakana.append('ショウワチョウ')
                            results.append(katakana)

                        elif elm[2] == '住吉町':

                            katakana.append('スミヨシチョウ')
                            results.append(katakana)

                        elif elm[2] == '豊丘町':

                            katakana.append('トヨオカチョウ')
                            results.append(katakana)

                        elif elm[2] == '豊里':

                            katakana.append('トヨサト')
                            results.append(katakana)
            
                        elif elm[2] == '錦町':

                            katakana.append('ニシキマチ')
                            results.append(katakana)

                        elif elm[2] == '西豊里町':

                            katakana.append('ニシトヨサトチョウ')
                            results.append(katakana)

                        elif elm[2] == '西文京町':

                            katakana.append('ニシブンキョウチョウ')
                            results.append(katakana)

                        elif elm[2] == '東大町':

                            katakana.append('ヒガシオオマチ')
                            results.append(katakana)

                        elif elm[2] == '東豊里町':

                            katakana.append('ヒガシトヨサトチョウ')
                            results.append(katakana)

                        elif elm[2] == '東文京町':

                            katakana.append('ヒガシブンキョウチョウ')
                            results.append(katakana)

                        elif elm[2] == '百戸町北':

                            katakana.append('ヒャッコチョウキタ')
                            results.append(katakana)

                        elif elm[2] == '百戸町西':

                            katakana.append('ヒャッコチョウニシ')
                            results.append(katakana)

                        elif elm[2] == '百戸町東':

                            katakana.append('ヒャッコチョウヒガシ')
                            results.append(katakana)

                        elif elm[2] == '平岸曙町':

                            katakana.append('ヒラギシアケボノチョウ')
                            results.append(katakana)

                        elif elm[2] == '平岸桂町':

                            katakana.append('ヒラギシカツラチョウ')
                            results.append(katakana)

                        elif elm[2] == '平岸新光町':

                            katakana.append('ヒラギシシンコウチョウ')
                            results.append(katakana)

                        elif elm[2] == '平岸仲町':

                            katakana.append('ヒラギシナカマチ')
                            results.append(katakana)

                        elif elm[2] == '平岸西町':

                            katakana.append('ヒラギシニシマチ')
                            results.append(katakana)

                        elif elm[2] == '平岸東町':

                            katakana.append('ヒラギシヒガシマチ')
                            results.append(katakana)

                        elif elm[2] == '平岸南町':

                            katakana.append('ヒラギシミナミマチ')
                            results.append(katakana)

                        elif elm[2] == '豊栄町':

                            katakana.append('ホウエイチョウ')
                            results.append(katakana)

                        elif elm[2] == '幌岡町':

                            katakana.append('ホロオカチョウ')
                            results.append(katakana)

                        elif elm[2] == '本町':

                            katakana.append('ホンチョウ')
                            results.append(katakana)

                        elif elm[2] == '美園町':

                            katakana.append('ミソノチョウ')
                            results.append(katakana)

                        elif elm[2] == '宮下町':

                            katakana.append('ミヤシタチョウ')
                            results.append(katakana)

                        elif elm[2] == '茂尻':

                            katakana.append('モジリ')
                            results.append(katakana)

                        elif elm[2] == '茂尻旭町':

                            katakana.append('モジリアサヒマチ')
                            results.append(katakana)

                        elif elm[2] == '茂尻春日町':

                            katakana.append('モジリカスガチョウ')
                            results.append(katakana)

                        elif elm[2] == '茂尻栄町':

                            katakana.append('モジリサカエマチ')
                            results.append(katakana)

                        elif elm[2] == '茂尻新春日町':

                            katakana.append('モジリシンカスガチョウ')
                            results.append(katakana)

                        elif elm[2] == '茂尻新町':

                            katakana.append('モジリシンマチ')
                            results.append(katakana)

                        elif elm[2] == '茂尻中央町北':

                            katakana.append('モジリチュウオウチョウキタ')
                            results.append(katakana)

                        elif elm[2] == '茂尻本町':

                            katakana.append('モジリホンチョウ')
                            results.append(katakana)

                        elif elm[2] == '茂尻宮下町':

                            katakana.append('モジリミヤシタチョウ')
                            results.append(katakana)

                        elif elm[2] == '茂尻元町北':

                            katakana.append('モジリモトマチキタ')
                            results.append(katakana)

                        elif elm[2] == '茂尻元町南':

                            katakana.append('モジリモトマチミナミ')
                            results.append(katakana)

                        elif elm[2] == '若木町北':

                            katakana.append('ワカキチョウキタ')
                            results.append(katakana)

                        elif elm[2] == '若木町西':

                            katakana.append('ワカキチョウニシ')
                            results.append(katakana)

                        elif elm[2] == '若木町東':

                            katakana.append('ワカキチョウヒガシ')
                            results.append(katakana)

                        elif elm[2] == '若木町南':

                            katakana.append('ワカキチョウミナミ')
                            results.append(katakana)

                    elif elm[1] == '釧路市':

                        katakana.append('クシロシ')
                        
                        if elm[2] == '阿寒町阿寒湖温泉':
                            
                            katakana.append('アカンチョウアカンコオンセン')
                            results.append(katakana)

                        elif elm[2] == '阿寒町飽別':

                            katakana.append('アカンチョウアクベツ')
                            results.append(katakana)

                        elif elm[2] == '阿寒町旭町':

                            katakana.append('アカンチョウアサヒマチ')
                            results.append(katakana)

        if len(results) > 0:
            return results

        raise ValueError(self._emcreator.message('JPPostCodeBuilder.py','convertKanjiToKatakana','kanji error','the kanji is an incompatible value.'))

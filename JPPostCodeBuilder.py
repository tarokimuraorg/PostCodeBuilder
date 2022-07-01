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

            if last_four_digits == '1100':

                results.append(address)
                return results

        elif first_three_digits == '085':
            
            address.append('北海道')
            address.append('阿寒郡鶴居村')

            if last_four_digits == '1200':
                
                results.append(address)
                return results

        elif first_three_digits == '070':

            address.append('北海道')
            address.append('旭川市')

            if last_four_digits == '0000':

                results.append(address)
                return results

        address = []

        if first_three_digits == '079':

            address.append('北海道')
            address.append('赤平市')

            if last_four_digits == '8401':

                address[1] = '旭川市'

                address.append('秋月１条')
                results.append(address)

                return results

            elif last_four_digits == '8402':

                address[1] = '旭川市'

                address.append('秋月２条')
                results.append(address)

                return results

            elif last_four_digits == '8403':

                address[1] = '旭川市'

                address.append('秋月３条')
                results.append(address)

                return results

            elif last_four_digits == '1143':

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

            if last_four_digits == '1146':
                
                address[1] = '阿寒郡鶴居村'

                address.append('アトコシヤラカ')
                results.append(address)

                return results

            elif last_four_digits == '1145':

                address[1] = '阿寒郡鶴居村'

                address.append('温根内')
                results.append(address)

                return results

            elif last_four_digits == '1132':

                address[1] = '阿寒郡鶴居村'

                address.append('上幌呂')
                results.append(address)

                return results

            elif last_four_digits == '1212':

                address[1] = '阿寒郡鶴居村'

                address.append('支雪裡')
                results.append(address)

                return results

            elif last_four_digits == '1133':

                address[1] = '阿寒郡鶴居村'

                address.append('支幌呂')
                results.append(address)

                return results

            elif last_four_digits == '1262':

                address[1] = '阿寒郡鶴居村'

                address.append('下久著呂')
                results.append(address)

                return results

            elif last_four_digits == '1211':

                address[1] = '阿寒郡鶴居村'

                address.append('下雪裡')
                results.append(address)

                return results

            elif last_four_digits == '1144':

                address[1] = '阿寒郡鶴居村'

                address.append('下幌呂')
                results.append(address)

                return results

            elif last_four_digits == '1131':

                address[1] = '阿寒郡鶴居村'

                address.append('新幌呂')
                results.append(address)

                return results

            elif last_four_digits == '1201':

                address[1] = '阿寒郡鶴居村'

                address.append('鶴居北')
                results.append(address)

                return results

            elif last_four_digits == '1203':

                address[1] = '阿寒郡鶴居村'

                address.append('鶴居西')
                results.append(address)

                return results

            elif last_four_digits == '1206':

                address[1] = '阿寒郡鶴居村'

                address.append('鶴居東')
                results.append(address)

                return results

            elif last_four_digits == '1204':

                address[1] = '阿寒郡鶴居村'

                address.append('鶴居南')
                results.append(address)

                return results

            elif last_four_digits == '1261':

                address[1] = '阿寒郡鶴居村'

                address.append('中久著呂')
                results.append(address)

                return results

            elif last_four_digits == '1202':

                address[1] = '阿寒郡鶴居村'

                address.append('中雪裡（西）')
                results.append(address)

                return results

            elif last_four_digits == '1207':

                address[1] = '阿寒郡鶴居村'

                address.append('中雪裡（東）')
                results.append(address)

                return results

            elif last_four_digits == '1205':

                address[1] = '阿寒郡鶴居村'

                address.append('中雪裡（南）')
                results.append(address)

                return results

            elif last_four_digits == '1143':

                address[1] = '阿寒郡鶴居村'

                address.append('中幌呂')
                results.append(address)

                return results

            elif last_four_digits == '1147':

                address[1] = '阿寒郡鶴居村'

                address.append('幌呂')
                results.append(address)

                return results

            elif last_four_digits == '1141':

                address[1] = '阿寒郡鶴居村'

                address.append('幌呂西')
                results.append(address)

                return results

            elif last_four_digits == '1142':

                address[1] = '阿寒郡鶴居村'

                address.append('幌呂東')
                results.append(address)

                return results

            elif last_four_digits == '1213':

                address[1] = '阿寒郡鶴居村'

                address.append('茂雪裡')
                results.append(address)

                return results

            elif last_four_digits == '1134':

                address[1] = '阿寒郡鶴居村'

                address.append('茂幌呂')
                results.append(address)

                return results

            elif last_four_digits == '0467':
                
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

            elif last_four_digits == '0245':

                address.append('阿寒町上阿寒')
                results.append(address)

                return results

            elif last_four_digits == '0221':

                address.append('阿寒町上舌辛')
                results.append(address)

                return results

            elif last_four_digits == '0235':

                address.append('阿寒町上徹別')
                results.append(address)

                return results

            elif last_four_digits == '0216':

                address.append('阿寒町北新町')
                results.append(address)

                return results

            elif last_four_digits == '0217':

                address.append('阿寒町北町')
                results.append(address)

                return results

            elif last_four_digits == '0211':

                address.append('阿寒町下舌辛')
                results.append(address)

                return results

            elif last_four_digits == '0231':

                address.append('阿寒町下徹別')
                results.append(address)

                return results

            elif last_four_digits == '0223':

                address.append('阿寒町下布伏内')
                results.append(address)

                return results

            elif last_four_digits == '0218':

                address.append('阿寒町新町')
                results.append(address)

                return results

            elif last_four_digits == '0234':

                address.append('阿寒町蘇牛')
                results.append(address)

                return results

            elif last_four_digits == '0232':

                address.append('阿寒町大正')
                results.append(address)

                return results

            elif last_four_digits == '0215':

                address.append('阿寒町中央')
                results.append(address)

                return results

            elif last_four_digits == '0237':

                address.append('阿寒町徹別中央')
                results.append(address)

                return results

            elif last_four_digits == '0241':

                address.append('阿寒町中阿寒')
                results.append(address)

                return results

            elif last_four_digits == '0236':

                address.append('阿寒町中徹別')
                results.append(address)

                return results

            elif last_four_digits == '0213':

                address.append('阿寒町仲町')
                results.append(address)

                return results

            elif last_four_digits == '0243':

                address.append('阿寒町西阿寒')
                results.append(address)

                return results

            elif last_four_digits == '0233':

                address.append('阿寒町西徹別')
                results.append(address)

                return results

            elif last_four_digits == '0201':

                address.append('阿寒町仁々志別')
                results.append(address)

                return results

            elif last_four_digits == '0242':

                address.append('阿寒町東舌辛')
                results.append(address)

                return results

            elif last_four_digits == '0214':

                address.append('阿寒町富士見')
                results.append(address)

                return results

            elif last_four_digits == '0222':

                address.append('阿寒町布伏内')
                results.append(address)

                return results

            elif last_four_digits == '0224':

                address.append('阿寒町雄別横山')
                results.append(address)
                
                return results

        elif first_three_digits == '078':

            address.append('北海道')
            address.append('旭川市')

            if last_four_digits == '8220':

                address.append('１０条通')
                results.append(address)

                return results

            elif last_four_digits == '8221':

                address.append('１１条通')
                results.append(address)

                return results

            elif last_four_digits == '8211':

                address.append('１条通')
                results.append(address)

                return results

            elif last_four_digits == '8212':

                address.append('２条通')
                results.append(address)

                return results

            elif last_four_digits == '8213':

                address.append('３条通')
                results.append(address)

                return results

            elif last_four_digits == '8214':

                address.append('４条通')
                results.append(address)

                return results

            elif last_four_digits == '8215':

                address.append('５条通')
                results.append(address)

                return results

            elif last_four_digits == '8216':

                address.append('６条通')
                results.append(address)

                return results

            elif last_four_digits == '8217':

                address.append('７条通')
                results.append(address)

                return results

            elif last_four_digits == '8218':

                address.append('８条通')
                results.append(address)

                return results

            elif last_four_digits == '8219':

                address.append('９条通')
                results.append(address)

                return results

            elif last_four_digits == '8320':

                address.append('神楽岡１０条')
                results.append(address)

                return results

            elif last_four_digits == '8321':

                address.append('神楽岡１１条')
                results.append(address)

                return results

            elif last_four_digits == '8322':

                address.append('神楽岡１２条')
                results.append(address)

                return results

            elif last_four_digits == '8323':

                address.append('神楽岡１３条')
                results.append(address)

                return results

            elif last_four_digits == '8324':

                address.append('神楽岡１４条')
                results.append(address)

                return results

            elif last_four_digits == '8325':

                address.append('神楽岡１５条')
                results.append(address)

                return results

            elif last_four_digits == '8326':

                address.append('神楽岡１６条')
                results.append(address)

                return results

        elif first_three_digits == '070':

            address.append('北海道')
            address.append('旭川市')

            if last_four_digits == '0040':

                address.append('１０条通')
                results.append(address)

                return results

            elif last_four_digits == '0031':

                address.append('１条通')
                results.append(address)

                return results

            elif last_four_digits == '0032':

                address.append('２条通')
                results.append(address)

                return results

            elif last_four_digits == '0052':

                address.append('２条西')
                results.append(address)

                return results

            elif last_four_digits == '0033':

                address.append('３条通')
                results.append(address)

                return results

            elif last_four_digits == '0053':

                address.append('３条西')
                results.append(address)

                return results

            elif last_four_digits == '0971':

                address.append('４区１条')
                results.append(address)

                return results

            elif last_four_digits == '0972':

                address.append('４区２条')
                results.append(address)

                return results

            elif last_four_digits == '0973':

                address.append('４区３条')
                results.append(address)

                return results

            elif last_four_digits == '0034':

                address.append('４条通')
                results.append(address)

                return results

            elif last_four_digits == '0054':

                address.append('４条西')
                results.append(address)

                return results

            elif last_four_digits == '0035':

                address.append('５条通')
                results.append(address)

                return results

            elif last_four_digits == '0055':

                address.append('５条西')
                results.append(address)

                return results

            elif last_four_digits == '0036':

                address.append('６条通')
                results.append(address)

                return results

            elif last_four_digits == '0056':

                address.append('６条西')
                results.append(address)

                return results

            elif last_four_digits == '0037':

                address.append('７条通')
                results.append(address)

                return results

            elif last_four_digits == '0057':

                address.append('７条西')
                results.append(address)

                return results

            elif last_four_digits == '0038':

                address.append('８条通')
                results.append(address)

                return results

            elif last_four_digits == '0058':

                address.append('８条西')
                results.append(address)

                return results

            elif last_four_digits == '0039':

                address.append('９条通')
                results.append(address)

                return results
                
            elif last_four_digits == '0059':

                address.append('９条西')
                results.append(address)

                return results

            elif last_four_digits == '0061':

                address.append('曙１条')
                results.append(address)

                return results

            elif last_four_digits == '0062':

                address.append('曙２条')
                results.append(address)

                return results

            elif last_four_digits == '0063':

                address.append('曙３条')
                results.append(address)

                return results

            elif last_four_digits == '0072':

                address.append('曙北２条')
                results.append(address)

                return results

            elif last_four_digits == '0073':

                address.append('曙北３条')
                results.append(address)

                return results

            elif last_four_digits == '0822':

                address.append('旭岡')
                results.append(address)

                return results

            elif last_four_digits == '0831':

                address.append('旭町１条')
                results.append(address)

                return results

            elif last_four_digits == '0832':

                address.append('旭町２条')
                results.append(address)

                return results

            elif last_four_digits == '8051':

                address.append('江丹別町嵐山')
                results.append(address)

                return results

            elif last_four_digits == '8052':

                address.append('江丹別町春日')
                results.append(address)

                return results

            elif last_four_digits == '8053':

                address.append('江丹別町共和')
                results.append(address)

                return results

            elif last_four_digits == '0841':

                address.append('大町１条')
                results.append(address)

                return results

            elif last_four_digits == '0842':

                address.append('大町２条')
                results.append(address)

                return results

            elif last_four_digits == '0843':

                address.append('大町３条')
                results.append(address)

                return results

            elif last_four_digits == '8001':

                address.append('神楽１条')
                results.append(address)

                return results

            elif last_four_digits == '8002':

                address.append('神楽２条')
                results.append(address)

                return results

            elif last_four_digits == '8003':

                address.append('神楽３条')
                results.append(address)

                return results

            elif last_four_digits == '8004':

                address.append('神楽４条')
                results.append(address)

                return results

            elif last_four_digits == '8005':

                address.append('神楽５条')
                results.append(address)

                return results

            elif last_four_digits == '8006':

                address.append('神楽６条')
                results.append(address)

                return results

            elif last_four_digits == '8007':

                address.append('神楽７条')
                results.append(address)

                return results

        elif first_three_digits == '071':

            address.append('北海道')
            address.append('旭川市')

            if last_four_digits == '1171':

                address.append('江丹別町清水')
                results.append(address)

                return results

            elif last_four_digits == '1172':

                address.append('江丹別町拓北')
                results.append(address)

                return results

            elif last_four_digits == '1173':

                address.append('江丹別町中央')
                results.append(address)

                return results

            elif last_four_digits == '1174':

                address.append('江丹別町富原')
                results.append(address)

                return results

            elif last_four_digits == '1175':

                address.append('江丹別町中園')
                results.append(address)

                return results

            elif last_four_digits == '1176':

                address.append('江丹別町西里')
                results.append(address)

                return results

            elif last_four_digits == '1177':

                address.append('江丹別町芳野')
                results.append(address)

                return results

        raise ValueError(self._emcreator.message('JPPostCodeBuilder.py','convertToAddress','post code error','the post code is an incompatible value.'))
        
    def furigana(self):

        address = self.convertToAddress()
        results = []

        for kanji in address:

            katakana = []

            if len(kanji) == 2:

                if kanji[0] == '北海道':

                    katakana.append('ホッカイドウ')

                    if kanji[1] == '赤平市':

                        katakana.append('アカビラシ')
                        results.append(katakana)

                    elif kanji[1] == '阿寒郡鶴居村':

                        katakana.append('アカングンツルイムラ')
                        results.append(katakana)

                    elif kanji[1] == '旭川市':

                        katakana.append('アサヒカワシ')
                        results.append(katakana)

            elif len(kanji) == 3:

                if kanji[0] == '北海道':

                    katakana.append('ホッカイドウ')

                    if kanji[1] == '赤平市':

                        katakana.append('アカビラシ')

                        if kanji[2] == '赤平':

                            katakana.append('アカビラ')
                            results.append(katakana)

                        elif kanji[2] == '泉町':

                            katakana.append('イズミマチ')
                            results.append(katakana)

                        elif kanji[2] == 'エルム町':

                            katakana.append('エルムチョウ')
                            results.append(katakana)

                        elif kanji[2] == '大町':

                            katakana.append('オオマチ')
                            results.append(katakana)

                        elif kanji[2] == '北文京町':

                            katakana.append('キタブンキョウチョウ')
                            results.append(katakana)
            
                        elif kanji[2] == '共和町':

                            katakana.append('キョウワチョウ')
                            results.append(katakana)
            
                        elif kanji[2] == '幸町':

                            katakana.append('サイワイチョウ')
                            results.append(katakana)

                        elif kanji[2] == '桜木町':

                            katakana.append('サクラギチョウ')
                            results.append(katakana)

                        elif kanji[2] == '昭和町':

                            katakana.append('ショウワチョウ')
                            results.append(katakana)

                        elif kanji[2] == '住吉町':

                            katakana.append('スミヨシチョウ')
                            results.append(katakana)

                        elif kanji[2] == '豊丘町':

                            katakana.append('トヨオカチョウ')
                            results.append(katakana)

                        elif kanji[2] == '豊里':

                            katakana.append('トヨサト')
                            results.append(katakana)
            
                        elif kanji[2] == '錦町':

                            katakana.append('ニシキマチ')
                            results.append(katakana)

                        elif kanji[2] == '西豊里町':

                            katakana.append('ニシトヨサトチョウ')
                            results.append(katakana)

                        elif kanji[2] == '西文京町':

                            katakana.append('ニシブンキョウチョウ')
                            results.append(katakana)

                        elif kanji[2] == '東大町':

                            katakana.append('ヒガシオオマチ')
                            results.append(katakana)

                        elif kanji[2] == '東豊里町':

                            katakana.append('ヒガシトヨサトチョウ')
                            results.append(katakana)

                        elif kanji[2] == '東文京町':

                            katakana.append('ヒガシブンキョウチョウ')
                            results.append(katakana)

                        elif kanji[2] == '百戸町北':

                            katakana.append('ヒャッコチョウキタ')
                            results.append(katakana)

                        elif kanji[2] == '百戸町西':

                            katakana.append('ヒャッコチョウニシ')
                            results.append(katakana)

                        elif kanji[2] == '百戸町東':

                            katakana.append('ヒャッコチョウヒガシ')
                            results.append(katakana)

                        elif kanji[2] == '平岸曙町':

                            katakana.append('ヒラギシアケボノチョウ')
                            results.append(katakana)

                        elif kanji[2] == '平岸桂町':

                            katakana.append('ヒラギシカツラチョウ')
                            results.append(katakana)

                        elif kanji[2] == '平岸新光町':

                            katakana.append('ヒラギシシンコウチョウ')
                            results.append(katakana)

                        elif kanji[2] == '平岸仲町':

                            katakana.append('ヒラギシナカマチ')
                            results.append(katakana)

                        elif kanji[2] == '平岸西町':

                            katakana.append('ヒラギシニシマチ')
                            results.append(katakana)

                        elif kanji[2] == '平岸東町':

                            katakana.append('ヒラギシヒガシマチ')
                            results.append(katakana)

                        elif kanji[2] == '平岸南町':

                            katakana.append('ヒラギシミナミマチ')
                            results.append(katakana)

                        elif kanji[2] == '豊栄町':

                            katakana.append('ホウエイチョウ')
                            results.append(katakana)

                        elif kanji[2] == '幌岡町':

                            katakana.append('ホロオカチョウ')
                            results.append(katakana)

                        elif kanji[2] == '本町':

                            katakana.append('ホンチョウ')
                            results.append(katakana)

                        elif kanji[2] == '美園町':

                            katakana.append('ミソノチョウ')
                            results.append(katakana)

                        elif kanji[2] == '宮下町':

                            katakana.append('ミヤシタチョウ')
                            results.append(katakana)

                        elif kanji[2] == '茂尻':

                            katakana.append('モジリ')
                            results.append(katakana)

                        elif kanji[2] == '茂尻旭町':

                            katakana.append('モジリアサヒマチ')
                            results.append(katakana)

                        elif kanji[2] == '茂尻春日町':

                            katakana.append('モジリカスガチョウ')
                            results.append(katakana)

                        elif kanji[2] == '茂尻栄町':

                            katakana.append('モジリサカエマチ')
                            results.append(katakana)

                        elif kanji[2] == '茂尻新春日町':

                            katakana.append('モジリシンカスガチョウ')
                            results.append(katakana)

                        elif kanji[2] == '茂尻新町':

                            katakana.append('モジリシンマチ')
                            results.append(katakana)

                        elif kanji[2] == '茂尻中央町北':

                            katakana.append('モジリチュウオウチョウキタ')
                            results.append(katakana)

                        elif kanji[2] == '茂尻本町':

                            katakana.append('モジリホンチョウ')
                            results.append(katakana)

                        elif kanji[2] == '茂尻宮下町':

                            katakana.append('モジリミヤシタチョウ')
                            results.append(katakana)

                        elif kanji[2] == '茂尻元町北':

                            katakana.append('モジリモトマチキタ')
                            results.append(katakana)

                        elif kanji[2] == '茂尻元町南':

                            katakana.append('モジリモトマチミナミ')
                            results.append(katakana)

                        elif kanji[2] == '若木町北':

                            katakana.append('ワカキチョウキタ')
                            results.append(katakana)

                        elif kanji[2] == '若木町西':

                            katakana.append('ワカキチョウニシ')
                            results.append(katakana)

                        elif kanji[2] == '若木町東':

                            katakana.append('ワカキチョウヒガシ')
                            results.append(katakana)

                        elif kanji[2] == '若木町南':

                            katakana.append('ワカキチョウミナミ')
                            results.append(katakana)

                    elif kanji[1] == '釧路市':

                        katakana.append('クシロシ')
                        
                        if kanji[2] == '阿寒町阿寒湖温泉':
                            
                            katakana.append('アカンチョウアカンコオンセン')
                            results.append(katakana)

                        elif kanji[2] == '阿寒町飽別':

                            katakana.append('アカンチョウアクベツ')
                            results.append(katakana)

                        elif kanji[2] == '阿寒町旭町':

                            katakana.append('アカンチョウアサヒマチ')
                            results.append(katakana)

                        elif kanji[2] == '阿寒町上阿寒':

                            katakana.append('アカンチョウカミアカン')
                            results.append(katakana)

                        elif kanji[2] == '阿寒町上舌辛':

                            katakana.append('アカンチョウカミシタカラ')
                            results.append(katakana)

                        elif kanji[2] == '阿寒町上徹別':

                            katakana.append('アカンチョウカミテシベツ')
                            results.append(katakana)

                        elif kanji[2] == '阿寒町北新町':

                            katakana.append('アカンチョウキタシンマチ')
                            results.append(katakana)

                        elif kanji[2] == '阿寒町北町':

                            katakana.append('アカンチョウキタマチ')
                            results.append(katakana)

                        elif kanji[2] == '阿寒町下舌辛':

                            katakana.append('アカンチョウシモシタカラ')
                            results.append(katakana)

                        elif kanji[2] == '阿寒町下徹別':

                            katakana.append('アカンチョウシモテシベツ')
                            results.append(katakana)

                        elif kanji[2] == '阿寒町下布伏内':

                            katakana.append('アカンチョウシモフブシナイ')
                            results.append(katakana)

                        elif kanji[2] == '阿寒町新町':

                            katakana.append('アカンチョウシンマチ')
                            results.append(katakana)

                        elif kanji[2] == '阿寒町蘇牛':

                            katakana.append('アカンチョウソウシ')
                            results.append(katakana)

                        elif kanji[2] == '阿寒町大正':

                            katakana.append('アカンチョウタイショウ')
                            results.append(katakana)

                        elif kanji[2] == '阿寒町中央':

                            katakana.append('アカンチョウチュウオウ')
                            results.append(katakana)

                        elif kanji[2] == '阿寒町徹別中央':

                            katakana.append('アカンチョウテシベツチュウオウ')
                            results.append(katakana)

                        elif kanji[2] == '阿寒町中阿寒':

                            katakana.append('アカンチョウナカアカン')
                            results.append(katakana)

                        elif kanji[2] == '阿寒町中徹別':

                            katakana.append('アカンチョウナカテシベツ')
                            results.append(katakana)

                        elif kanji[2] == '阿寒町仲町':

                            katakana.append('アカンチョウナカマチ')
                            results.append(katakana)

                        elif kanji[2] == '阿寒町西阿寒':

                            katakana.append('アカンチョウニシアカン')
                            results.append(katakana)

                        elif kanji[2] == '阿寒町西徹別':

                            katakana.append('アカンチョウニシテシベツ')
                            results.append(katakana)

                        elif kanji[2] == '阿寒町仁々志別':

                            katakana.append('アカンチョウニニシベツ')
                            results.append(katakana)

                        elif kanji[2] == '阿寒町東舌辛':

                            katakana.append('アカンチョウヒガシシタカラ')
                            results.append(katakana)

                        elif kanji[2] == '阿寒町富士見':

                            katakana.append('アカンチョウフジミ')
                            results.append(katakana)

                        elif kanji[2] == '阿寒町布伏内':

                            katakana.append('アカンチョウフブシナイ')
                            results.append(katakana)

                        elif kanji[2] == '阿寒町雄別横山':

                            katakana.append('アカンチョウユウベツヨコヤマ')
                            results.append(katakana)

                    elif kanji[1] == '阿寒郡鶴居村':

                        katakana.append('アカングンツルイムラ')

                        if kanji[2] == 'アトコシヤラカ':

                            katakana.append('アトコシヤラカ')
                            results.append(katakana)

                        elif kanji[2] == '温根内':

                            katakana.append('オンネナイ')
                            results.append(katakana)

                        elif kanji[2] == '上幌呂':

                            katakana.append('カミホロロ')
                            results.append(katakana)

                        elif kanji[2] == '支雪裡':

                            katakana.append('シセツリ')
                            results.append(katakana)

                        elif kanji[2] == '支幌呂':

                            katakana.append('シホロロ')
                            results.append(katakana)

                        elif kanji[2] == '下久著呂':

                            katakana.append('シモクチョロ')
                            results.append(katakana)

                        elif kanji[2] == '下雪裡':

                            katakana.append('シモセツリ')
                            results.append(katakana)

                        elif kanji[2] == '下幌呂':

                            katakana.append('シモホロロ')
                            results.append(katakana)

                        elif kanji[2] == '新幌呂':

                            katakana.append('シンホロロ')
                            results.append(katakana)

                        elif kanji[2] == '鶴居北':

                            katakana.append('ツルイキタ')
                            results.append(katakana)

                        elif kanji[2] == '鶴居西':

                            katakana.append('ツルイニシ')
                            results.append(katakana)

                        elif kanji[2] == '鶴居東':

                            katakana.append('ツルイヒガシ')
                            results.append(katakana)

                        elif kanji[2] == '鶴居南':

                            katakana.append('ツルイミナミ')
                            results.append(katakana)

                        elif kanji[2] == '中久著呂':

                            katakana.append('ナカクチョロ')
                            results.append(katakana)

                        elif kanji[2] == '中雪裡（西）':

                            katakana.append('ナカセツリ(ニシ)')
                            results.append(katakana)

                        elif kanji[2] == '中雪裡（東）':

                            katakana.append('ナカセツリ(ヒガシ)')
                            results.append(katakana)

                        elif kanji[2] == '中雪裡（南）':

                            katakana.append('ナカセツリ(ミナミ)')
                            results.append(katakana)

                        elif kanji[2] == '中幌呂':

                            katakana.append('ナカホロロ')
                            results.append(katakana)

                        elif kanji[2] == '幌呂':

                            katakana.append('ホロロ')
                            results.append(katakana)

                        elif kanji[2] == '幌呂西':

                            katakana.append('ホロロニシ')
                            results.append(katakana)

                        elif kanji[2] == '幌呂東':

                            katakana.append('ホロロヒガシ')
                            results.append(katakana)

                        elif kanji[2] == '茂雪裡':

                            katakana.append('モセツリ')
                            results.append(katakana)

                        elif kanji[2] == '茂幌呂':

                            katakana.append('モホロロ')
                            results.append(katakana)

                    elif kanji[1] == '旭川市':

                        katakana.append('アサヒカワシ')
                        
                        if kanji[2] == '１０条通':
                            
                            katakana.append('10ジョウドオリ')
                            results.append(katakana)

                        elif kanji[2] == '１１条通':

                            katakana.append('11ジョウドオリ')
                            results.append(katakana)

                        elif kanji[2] == '１条通':

                            katakana.append('1ジョウドオリ')
                            results.append(katakana)

                        elif kanji[2] == '２条通':

                            katakana.append('2ジョウドオリ')
                            results.append(katakana)

                        elif kanji[2] == '２条西':

                            katakana.append('2ジョウニシ')
                            results.append(katakana)

                        elif kanji[2] == '３条通':

                            katakana.append('3ジョウドオリ')
                            results.append(katakana)

                        elif kanji[2] == '３条西':

                            katakana.append('3ジョウニシ')
                            results.append(katakana)

                        elif kanji[2] == '４区１条':

                            katakana.append('4ク1ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '４区２条':

                            katakana.append('4ク2ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '４区３条':

                            katakana.append('4ク3ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '４条通':

                            katakana.append('4ジョウドオリ')
                            results.append(katakana)

                        elif kanji[2] == '４条西':

                            katakana.append('4ジョウニシ')
                            results.append(katakana)

                        elif kanji[2] == '５条通':

                            katakana.append('5ジョウドオリ')
                            results.append(katakana)

                        elif kanji[2] == '５条西':

                            katakana.append('5ジョウニシ')
                            results.append(katakana)

                        elif kanji[2] == '６条通':

                            katakana.append('6ジョウドオリ')
                            results.append(katakana)

                        elif kanji[2] == '６条西':

                            katakana.append('6ジョウニシ')
                            results.append(katakana)

                        elif kanji[2] == '７条通':

                            katakana.append('7ジョウドオリ')
                            results.append(katakana)

                        elif kanji[2] == '７条西':

                            katakana.append('7ジョウニシ')
                            results.append(katakana)

                        elif kanji[2] == '８条通':

                            katakana.append('8ジョウドオリ')
                            results.append(katakana)

                        elif kanji[2] == '８条西':

                            katakana.append('8ジョウニシ')
                            results.append(katakana)

                        elif kanji[2] == '９条通':

                            katakana.append('9ジョウドオリ')
                            results.append(katakana)

                        elif kanji[2] == '９条西':

                            katakana.append('9ジョウニシ')
                            results.append(katakana)

                        elif kanji[2] == '秋月１条':

                            katakana.append('アキツキ1ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '秋月２条':

                            katakana.append('アキツキ2ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '秋月３条':

                            katakana.append('アキツキ3ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '曙１条':

                            katakana.append('アケボノ1ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '曙２条':

                            katakana.append('アケボノ2ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '曙３条':

                            katakana.append('アケボノ3ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '曙北２条':

                            katakana.append('アケボノキタ2ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '曙北３条':

                            katakana.append('アケボノキタ3ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '旭岡':

                            katakana.append('アサヒガオカ')
                            results.append(katakana)

                        elif kanji[2] == '旭町１条':

                            katakana.append('アサヒマチ1ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '旭町２条':

                            katakana.append('アサヒマチ2ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '江丹別町嵐山':

                            katakana.append('エタンベツチョウアラシヤマ')
                            results.append(katakana)

                        elif kanji[2] == '江丹別町春日':

                            katakana.append('エタンベツチョウカスガ')
                            results.append(katakana)

                        elif kanji[2] == '江丹別町共和':

                            katakana.append('エタンベツチョウキョウワ')
                            results.append(katakana)

                        elif kanji[2] == '江丹別町清水':

                            katakana.append('エタンベツチョウシミズ')
                            results.append(katakana)

                        elif kanji[2] == '江丹別町拓北':

                            katakana.append('エタンベツチョウタクホク')
                            results.append(katakana)

                        elif kanji[2] == '江丹別町中央':

                            katakana.append('エタンベツチョウチュウオウ')
                            results.append(katakana)

                        elif kanji[2] == '江丹別町富原':

                            katakana.append('エタンベツチョウトミハラ')
                            results.append(katakana)

                        elif kanji[2] == '江丹別町中園':

                            katakana.append('エタンベツチョウナカゾノ')
                            results.append(katakana)

                        elif kanji[2] == '江丹別町西里':

                            katakana.append('エタンベツチョウニシサト')
                            results.append(katakana)

                        elif kanji[2] == '江丹別町芳野':

                            katakana.append('エタンベツチョウヨシノ')
                            results.append(katakana)

                        elif kanji[2] == '大町１条':

                            katakana.append('オオマチ1ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '大町２条':

                            katakana.append('オオマチ2ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '大町３条':

                            katakana.append('オオマチ3ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '神楽１条':

                            katakana.append('カグラ1ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '神楽２条':

                            katakana.append('カグラ2ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '神楽３条':

                            katakana.append('カグラ3ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '神楽４条':

                            katakana.append('カグラ4ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '神楽５条':

                            katakana.append('カグラ5ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '神楽６条':

                            katakana.append('カグラ6ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '神楽７条':

                            katakana.append('カグラ7ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '神楽岡１０条':

                            katakana.append('カグラオカ10ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '神楽岡１１条':

                            katakana.append('カグラオカ11ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '神楽岡１２条':

                            katakana.append('カグラオカ12ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '神楽岡１３条':

                            katakana.append('カグラオカ13ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '神楽岡１４条':

                            katakana.append('カグラオカ14ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '神楽岡１５条':

                            katakana.append('カグラオカ15ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '神楽岡１６条':

                            katakana.append('カグラオカ16ジョウ')
                            results.append(katakana)

        if len(results) > 0:
            return results

        raise ValueError(self._emcreator.message('JPPostCodeBuilder.py','convertKanjiToKatakana','kanji error','the kanji is an incompatible value.'))

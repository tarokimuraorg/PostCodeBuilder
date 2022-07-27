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

            elif last_four_digits == '8420':

                address[1] = '旭川市'

                address.append('永山１０条')
                results.append(address)

                return results

            elif last_four_digits == '8421':

                address[1] = '旭川市'

                address.append('永山１１条')
                results.append(address)

                return results

            elif last_four_digits == '8422':

                address[1] = '旭川市'

                address.append('永山１２条')
                results.append(address)

                return results

            elif last_four_digits == '8423':

                address[1] = '旭川市'

                address.append('永山１３条')
                results.append(address)

                return results

            elif last_four_digits == '8424':

                address[1] = '旭川市'

                address.append('永山１４条')
                results.append(address)

                return results

            elif last_four_digits == '8411':

                address[1] = '旭川市'

                address.append('永山１条')
                results.append(address)

                return results

            elif last_four_digits == '8412':

                address[1] = '旭川市'

                address.append('永山２条')
                results.append(address)

                return results

            elif last_four_digits == '8413':

                address[1] = '旭川市'

                address.append('永山３条')
                results.append(address)

                return results

            elif last_four_digits == '8414':

                address[1] = '旭川市'

                address.append('永山４条')
                results.append(address)

                return results

            elif last_four_digits == '8415':

                address[1] = '旭川市'

                address.append('永山５条')
                results.append(address)

                return results

            elif last_four_digits == '8416':

                address[1] = '旭川市'

                address.append('永山６条')
                results.append(address)

                return results

            elif last_four_digits == '8417':

                address[1] = '旭川市'

                address.append('永山７条')
                results.append(address)

                return results

            elif last_four_digits == '8418':

                address[1] = '旭川市'

                address.append('永山８条')
                results.append(address)

                return results

            elif last_four_digits == '8419':

                address[1] = '旭川市'

                address.append('永山９条')
                results.append(address)

                return results

            elif last_four_digits == '8451':

                address[1] = '旭川市'

                address.append('永山北１条')
                results.append(address)

                return results

            elif last_four_digits == '8452':

                address[1] = '旭川市'

                address.append('永山北２条')
                results.append(address)

                return results

            elif last_four_digits == '8453':

                address[1] = '旭川市'

                address.append('永山北３条')
                results.append(address)

                return results

            elif last_four_digits == '8454':

                address[1] = '旭川市'

                address.append('永山北４条')
                results.append(address)

                return results

            elif last_four_digits == '8431':

                address[1] = '旭川市'

                address.append('永山町')
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

            elif last_four_digits == '8311':

                address.append('神楽岡１条')
                results.append(address)

                return results

            elif last_four_digits == '8312':

                address.append('神楽岡２条')
                results.append(address)

                return results

            elif last_four_digits == '8313':

                address.append('神楽岡３条')
                results.append(address)

                return results

            elif last_four_digits == '8314':

                address.append('神楽岡４条')
                results.append(address)

                return results

            elif last_four_digits == '8315':

                address.append('神楽岡５条')
                results.append(address)

                return results

            elif last_four_digits == '8316':

                address.append('神楽岡６条')
                results.append(address)

                return results

            elif last_four_digits == '8317':

                address.append('神楽岡７条')
                results.append(address)

                return results

            elif last_four_digits == '8318':

                address.append('神楽岡８条')
                results.append(address)

                return results

            elif last_four_digits == '8319':

                address.append('神楽岡９条')
                results.append(address)

                return results

            elif last_four_digits == '8327':

                address.append('神楽岡公園')
                results.append(address)

                return results

            elif last_four_digits == '0185':

                address.append('神居町神居古潭')
                results.append(address)

                return results

            elif last_four_digits == '0186':

                address.append('神居町西丘')
                results.append(address)

                return results

            elif last_four_digits == '8371':

                address.append('旭神１条')
                results.append(address)

                return results

            elif last_four_digits == '8372':

                address.append('旭神２条')
                results.append(address)

                return results

            elif last_four_digits == '8373':

                address.append('旭神３条')
                results.append(address)

                return results

            elif last_four_digits == '8308':

                address.append('旭神町')
                results.append(address)

                return results

            elif last_four_digits == '8271':

                address.append('工業団地１条')
                results.append(address)

                return results

            elif last_four_digits == '8272':

                address.append('工業団地２条')
                results.append(address)

                return results

            elif last_four_digits == '8273':

                address.append('工業団地３条')
                results.append(address)

                return results

            elif last_four_digits == '8274':

                address.append('工業団地４条')
                results.append(address)

                return results

            elif last_four_digits == '8275':

                address.append('工業団地５条')
                results.append(address)

                return results

            elif last_four_digits == '8350':

                address.append('東光１０条')
                results.append(address)

                return results

            elif last_four_digits == '8351':

                address.append('東光１１条')
                results.append(address)

                return results

            elif last_four_digits == '8352':

                address.append('東光１２条')
                results.append(address)

                return results

            elif last_four_digits == '8353':

                address.append('東光１３条')
                results.append(address)

                return results

            elif last_four_digits == '8354':

                address.append('東光１４条')
                results.append(address)

                return results

            elif last_four_digits == '8355':

                address.append('東光１５条')
                results.append(address)

                return results

            elif last_four_digits == '8356':

                address.append('東光１６条')
                results.append(address)

                return results

            elif last_four_digits == '8357':

                address.append('東光１７条')
                results.append(address)

                return results

            elif last_four_digits == '8358':

                address.append('東光１８条')
                results.append(address)

                return results

            elif last_four_digits == '8359':

                address.append('東光１９条')
                results.append(address)

                return results

            elif last_four_digits == '8341':

                address.append('東光１条')
                results.append(address)

                return results

            elif last_four_digits == '8360':

                address.append('東光２０条')
                results.append(address)

                return results

            elif last_four_digits == '8361':

                address.append('東光２１条')
                results.append(address)

                return results

            elif last_four_digits == '8362':

                address.append('東光２２条')
                results.append(address)

                return results

            elif last_four_digits == '8363':

                address.append('東光２３条')
                results.append(address)

                return results

            elif last_four_digits == '8364':

                address.append('東光２４条')
                results.append(address)

                return results

            elif last_four_digits == '8365':

                address.append('東光２５条')
                results.append(address)

                return results

            elif last_four_digits == '8366':

                address.append('東光２６条')
                results.append(address)

                return results

            elif last_four_digits == '8367':

                address.append('東光２７条')
                results.append(address)

                return results

            elif last_four_digits == '8342':

                address.append('東光２条')
                results.append(address)

                return results

            elif last_four_digits == '8343':

                address.append('東光３条')
                results.append(address)

                return results

            elif last_four_digits == '8344':

                address.append('東光４条')
                results.append(address)

                return results

            elif last_four_digits == '8345':

                address.append('東光５条')
                results.append(address)

                return results

            elif last_four_digits == '8346':

                address.append('東光６条')
                results.append(address)

                return results

            elif last_four_digits == '8347':

                address.append('東光７条')
                results.append(address)

                return results

            elif last_four_digits == '8348':

                address.append('東光８条')
                results.append(address)

                return results

            elif last_four_digits == '8349':

                address.append('東光９条')
                results.append(address)

                return results

            elif last_four_digits == '8240':

                address.append('豊岡１０条')
                results.append(address)

                return results

            elif last_four_digits == '8241':

                address.append('豊岡１１条')
                results.append(address)

                return results

            elif last_four_digits == '8242':

                address.append('豊岡１２条')
                results.append(address)

                return results

            elif last_four_digits == '8243':

                address.append('豊岡１３条')
                results.append(address)

                return results

            elif last_four_digits == '8244':

                address.append('豊岡１４条')
                results.append(address)

                return results

            elif last_four_digits == '8245':

                address.append('豊岡１５条')
                results.append(address)

                return results

            elif last_four_digits == '8246':

                address.append('豊岡１６条')
                results.append(address)

                return results

            elif last_four_digits == '8231':

                address.append('豊岡１条')
                results.append(address)

                return results

            elif last_four_digits == '8232':

                address.append('豊岡２条')
                results.append(address)

                return results

            elif last_four_digits == '8233':

                address.append('豊岡３条')
                results.append(address)

                return results

            elif last_four_digits == '8234':

                address.append('豊岡４条')
                results.append(address)

                return results

            elif last_four_digits == '8235':

                address.append('豊岡５条')
                results.append(address)

                return results

            elif last_four_digits == '8236':

                address.append('豊岡６条')
                results.append(address)

                return results

            elif last_four_digits == '8237':

                address.append('豊岡７条')
                results.append(address)

                return results

            elif last_four_digits == '8238':

                address.append('豊岡８条')
                results.append(address)

                return results

            elif last_four_digits == '8239':

                address.append('豊岡９条')
                results.append(address)

                return results

            elif last_four_digits == '8381':

                address.append('西神楽１線')
                results.append(address)

                return results

            elif last_four_digits == '8382':

                address.append('西神楽２線')
                results.append(address)

                return results

            elif last_four_digits == '8383':

                address.append('西神楽３線')
                results.append(address)

                return results

            elif last_four_digits == '8821':

                address.append('西御料１条')
                results.append(address)

                return results

            elif last_four_digits == '8822':

                address.append('西御料２条')
                results.append(address)

                return results

            elif last_four_digits == '8823':

                address.append('西御料３条')
                results.append(address)

                return results

            elif last_four_digits == '8824':

                address.append('西御料４条')
                results.append(address)

                return results

            elif last_four_digits == '8825':

                address.append('西御料５条')
                results.append(address)

                return results

            elif last_four_digits == '8251':

                address.append('東旭川北１条')
                results.append(address)

                return results

            elif last_four_digits == '8252':

                address.append('東旭川北２条')
                results.append(address)

                return results

            elif last_four_digits == '8253':

                address.append('東旭川北３条')
                results.append(address)

                return results

            elif last_four_digits == '8207':

                address.append('東旭川町上兵村')
                results.append(address)

                return results

            elif last_four_digits == '8340':

                address.append('東旭川町共栄')
                results.append(address)

                return results

            elif last_four_digits == '8368':

                address.append('東旭川町旭正')
                results.append(address)

                return results

            elif last_four_digits == '8205':

                address.append('東旭川町倉沼')
                results.append(address)

                return results

            elif last_four_digits == '8204':

                address.append('東旭川町桜岡')
                results.append(address)

                return results

            elif last_four_digits == '8208':

                address.append('東旭川町下兵村')
                results.append(address)

                return results

            elif last_four_digits == '8206':

                address.append('東旭川町忠別')
                results.append(address)

                return results

            elif last_four_digits == '8202':

                address.append('東旭川町豊田')
                results.append(address)

                return results

            elif last_four_digits == '1272':

                address.append('東旭川町豊田')
                results.append(address)

                return results

            elif last_four_digits == '8201':

                address.append('東旭川町東桜岡')
                results.append(address)

                return results

            elif last_four_digits == '1271':

                address.append('東旭川町東桜岡')
                results.append(address)

                return results

            elif last_four_digits == '8203':

                address.append('東旭川町日ノ出')
                results.append(address)

                return results

            elif last_four_digits == '1274':

                address.append('東旭川町瑞穂')
                results.append(address)

                return results

            elif last_four_digits == '1273':

                address.append('東旭川町米原')
                results.append(address)

                return results

            elif last_four_digits == '8261':

                address.append('東旭川南１条')
                results.append(address)

                return results

            elif last_four_digits == '8262':

                address.append('東旭川南２条')
                results.append(address)

                return results

            elif last_four_digits == '8301':

                address.append('緑が丘１条')
                results.append(address)

                return results

            elif last_four_digits == '8302':

                address.append('緑が丘２条')
                results.append(address)

                return results

            elif last_four_digits == '8303':

                address.append('緑が丘３条')
                results.append(address)

                return results

            elif last_four_digits == '8304':

                address.append('緑が丘４条')
                results.append(address)

                return results

            elif last_four_digits == '8305':

                address.append('緑が丘５条')
                results.append(address)

                return results

            elif last_four_digits == '8801':

                address.append('緑が丘東１条')
                results.append(address)

                return results

            elif last_four_digits == '8802':

                address.append('緑が丘東２条')
                results.append(address)

                return results

            elif last_four_digits == '8803':

                address.append('緑が丘東３条')
                results.append(address)

                return results

            elif last_four_digits == '8804':

                address.append('緑が丘東４条')
                results.append(address)

                return results

            elif last_four_digits == '8805':

                address.append('緑が丘東５条')
                results.append(address)

                return results

            elif last_four_digits == '8811':

                address.append('緑が丘南１条')
                results.append(address)

                return results

            elif last_four_digits == '8812':

                address.append('緑が丘南２条')
                results.append(address)

                return results

            elif last_four_digits == '8813':

                address.append('緑が丘南３条')
                results.append(address)

                return results

            elif last_four_digits == '8814':

                address.append('緑が丘南４条')
                results.append(address)

                return results

            elif last_four_digits == '8815':

                address.append('緑が丘南５条')
                results.append(address)

                return results

            elif last_four_digits == '8331':

                address.append('南１条通')
                results.append(address)

                return results

            elif last_four_digits == '8332':

                address.append('南２条通')
                results.append(address)

                return results

            elif last_four_digits == '8333':

                address.append('南３条通')
                results.append(address)

                return results

            elif last_four_digits == '8334':

                address.append('南４条通')
                results.append(address)

                return results

            elif last_four_digits == '8335':

                address.append('南５条通')
                results.append(address)

                return results

            elif last_four_digits == '8336':

                address.append('南６条通')
                results.append(address)

                return results

            elif last_four_digits == '8337':

                address.append('南７条通')
                results.append(address)

                return results

            elif last_four_digits == '8338':

                address.append('南８条通')
                results.append(address)

                return results

            elif last_four_digits == '8339':

                address.append('南９条通')
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

            elif last_four_digits == '0041':

                address.append('上常盤町')
                results.append(address)

                return results

            elif last_four_digits == '8011':

                address.append('神居１条')
                results.append(address)

                return results

            elif last_four_digits == '8012':

                address.append('神居２条')
                results.append(address)

                return results

            elif last_four_digits == '8013':

                address.append('神居３条')
                results.append(address)

                return results

            elif last_four_digits == '8014':

                address.append('神居４条')
                results.append(address)

                return results

            elif last_four_digits == '8015':

                address.append('神居５条')
                results.append(address)

                return results

            elif last_four_digits == '8016':

                address.append('神居６条')
                results.append(address)

                return results

            elif last_four_digits == '8017':

                address.append('神居７条')
                results.append(address)

                return results

            elif last_four_digits == '8018':

                address.append('神居８条')
                results.append(address)

                return results

            elif last_four_digits == '8019':

                address.append('神居９条')
                results.append(address)

                return results

            elif last_four_digits == '8033':

                address.append('神居町雨紛')
                results.append(address)

                return results

            elif last_four_digits == '8034':

                address.append('神居町上雨紛')
                results.append(address)

                return results

            elif last_four_digits == '8026':

                address.append('神居町神岡')
                results.append(address)

                return results

            elif last_four_digits == '8032':

                address.append('神居町共栄')
                results.append(address)

                return results

            elif last_four_digits == '8031':

                address.append('神居町神華')
                results.append(address)

                return results

            elif last_four_digits == '8022':

                address.append('神居町台場')
                results.append(address)

                return results

            elif last_four_digits == '8021':

                address.append('神居町忠和')
                results.append(address)

                return results

            elif last_four_digits == '8025':

                address.append('神居町富岡')
                results.append(address)

                return results

            elif last_four_digits == '8024':

                address.append('神居町富沢')
                results.append(address)

                return results

            elif last_four_digits == '8023':

                address.append('神居町春志内')
                results.append(address)

                return results

            elif last_four_digits == '0081':

                address.append('亀吉１条')
                results.append(address)

                return results

            elif last_four_digits == '0082':

                address.append('亀吉２条')
                results.append(address)

                return results

            elif last_four_digits == '0083':

                address.append('亀吉３条')
                results.append(address)

                return results

            elif last_four_digits == '0811':

                address.append('川端町１条')
                results.append(address)

                return results

            elif last_four_digits == '0812':

                address.append('川端町２条')
                results.append(address)

                return results

            elif last_four_digits == '0813':

                address.append('川端町３条')
                results.append(address)

                return results

            elif last_four_digits == '0814':

                address.append('川端町４条')
                results.append(address)

                return results

            elif last_four_digits == '0815':

                address.append('川端町５条')
                results.append(address)

                return results

            elif last_four_digits == '0816':

                address.append('川端町６条')
                results.append(address)

                return results

            elif last_four_digits == '0817':

                address.append('川端町７条')
                results.append(address)

                return results

            elif last_four_digits == '0029':

                address.append('金星町')
                results.append(address)

                return results

            elif last_four_digits == '0871':

                address.append('春光１条')
                results.append(address)

                return results

            elif last_four_digits == '0872':

                address.append('春光２条')
                results.append(address)

                return results
                
            elif last_four_digits == '0873':

                address.append('春光３条')
                results.append(address)

                return results

            elif last_four_digits == '0874':

                address.append('春光４条')
                results.append(address)

                return results

            elif last_four_digits == '0875':

                address.append('春光５条')
                results.append(address)

                return results

            elif last_four_digits == '0876':

                address.append('春光６条')
                results.append(address)

                return results

            elif last_four_digits == '0877':

                address.append('春光７条')
                results.append(address)

                return results

            elif last_four_digits == '0902':

                address.append('春光町')
                results.append(address)

                return results

            elif last_four_digits == '0014':

                address.append('新星町')
                results.append(address)

                return results

            elif last_four_digits == '0001':

                address.append('新富１条')
                results.append(address)

                return results

            elif last_four_digits == '0002':

                address.append('新富２条')
                results.append(address)

                return results

            elif last_four_digits == '0003':

                address.append('新富３条')
                results.append(address)

                return results

            elif last_four_digits == '0864':

                address.append('住吉４条')
                results.append(address)

                return results

            elif last_four_digits == '0865':

                address.append('住吉５条')
                results.append(address)

                return results

            elif last_four_digits == '0866':

                address.append('住吉６条')
                results.append(address)

                return results

            elif last_four_digits == '0867':

                address.append('住吉７条')
                results.append(address)

                return results

            elif last_four_digits == '0010':

                address.append('大雪通')
                results.append(address)

                return results

            elif last_four_digits == '8061':

                address.append('高砂台')
                results.append(address)

                return results

            elif last_four_digits == '8027':

                address.append('台場東')
                results.append(address)

                return results

            elif last_four_digits == '8071':

                address.append('台場１条')
                results.append(address)

                return results

            elif last_four_digits == '8072':

                address.append('台場２条')
                results.append(address)

                return results

            elif last_four_digits == '8073':

                address.append('台場３条')
                results.append(address)

                return results

            elif last_four_digits == '8074':

                address.append('台場４条')
                results.append(address)

                return results

            elif last_four_digits == '0821':

                address.append('近文町')
                results.append(address)

                return results

            elif last_four_digits == '8041':

                address.append('忠和１条')
                results.append(address)

                return results

            elif last_four_digits == '8042':

                address.append('忠和２条')
                results.append(address)

                return results

            elif last_four_digits == '8043':

                address.append('忠和３条')
                results.append(address)

                return results

            elif last_four_digits == '8044':

                address.append('忠和４条')
                results.append(address)

                return results
            
            elif last_four_digits == '8045':

                address.append('忠和５条')
                results.append(address)

                return results

            elif last_four_digits == '8046':

                address.append('忠和６条')
                results.append(address)

                return results

            elif last_four_digits == '8047':

                address.append('忠和７条')
                results.append(address)

                return results

            elif last_four_digits == '8048':

                address.append('忠和８条')
                results.append(address)

                return results

            elif last_four_digits == '8049':

                address.append('忠和９条')
                results.append(address)

                return results

            elif last_four_digits == '0044':

                address.append('常磐公園')
                results.append(address)

                return results

            elif last_four_digits == '0043':

                address.append('常盤通')
                results.append(address)

                return results

            elif last_four_digits == '0042':

                address.append('中常盤町')
                results.append(address)

                return results

            elif last_four_digits == '0824':

                address.append('錦町')
                results.append(address)

                return results

            elif last_four_digits == '0901':

                address.append('花咲町')
                results.append(address)

                return results

            elif last_four_digits == '0013':

                address.append('パルプ町')
                results.append(address)

                return results

            elif last_four_digits == '0011':

                address.append('パルプ町１条')
                results.append(address)

                return results

            elif last_four_digits == '0012':

                address.append('パルプ町２条')
                results.append(address)

                return results

            elif last_four_digits == '0021':

                address.append('東１条')
                results.append(address)

                return results

            elif last_four_digits == '0022':

                address.append('東２条')
                results.append(address)

                return results

            elif last_four_digits == '0023':

                address.append('東３条')
                results.append(address)

                return results

            elif last_four_digits == '0024':

                address.append('東４条')
                results.append(address)

                return results

            elif last_four_digits == '0025':

                address.append('東５条')
                results.append(address)

                return results

            elif last_four_digits == '0026':

                address.append('東６条')
                results.append(address)

                return results

            elif last_four_digits == '0027':

                address.append('東７条')
                results.append(address)

                return results

            elif last_four_digits == '0028':

                address.append('東８条')
                results.append(address)

                return results

            elif last_four_digits == '0825':

                address.append('北門町')
                results.append(address)

                return results

            elif last_four_digits == '0823':

                address.append('緑町')
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

            elif last_four_digits == '8141':

                address.append('春光台１条')
                results.append(address)

                return results

            elif last_four_digits == '8142':

                address.append('春光台２条')
                results.append(address)

                return results

            elif last_four_digits == '8143':

                address.append('春光台３条')
                results.append(address)

                return results

            elif last_four_digits == '8144':

                address.append('春光台４条')
                results.append(address)

                return results

            elif last_four_digits == '8145':

                address.append('春光台５条')
                results.append(address)

                return results

            elif last_four_digits == '8131':

                address.append('末広１条')
                results.append(address)

                return results

            elif last_four_digits == '8132':

                address.append('末広２条')
                results.append(address)

                return results

            elif last_four_digits == '8133':

                address.append('末広３条')
                results.append(address)

                return results

            elif last_four_digits == '8134':

                address.append('末広４条')
                results.append(address)

                return results

            elif last_four_digits == '8135':

                address.append('末広５条')
                results.append(address)

                return results

            elif last_four_digits == '8136':

                address.append('末広６条')
                results.append(address)

                return results

            elif last_four_digits == '8137':

                address.append('末広７条')
                results.append(address)

                return results

            elif last_four_digits == '8138':

                address.append('末広８条')
                results.append(address)

                return results

            elif last_four_digits == '8121':

                address.append('末広東１条')
                results.append(address)

                return results

            elif last_four_digits == '8122':

                address.append('末広東２条')
                results.append(address)

                return results

            elif last_four_digits == '8123':

                address.append('末広東３条')
                results.append(address)

                return results

            elif last_four_digits == '0184':

                address.append('西神楽４線')
                results.append(address)

                return results

            elif last_four_digits == '0185':

                address.append('西神楽５線')
                results.append(address)

                return results

            elif last_four_digits == '0173':

                address.append('西神楽北１条')
                results.append(address)

                return results

            elif last_four_digits == '0174':

                address.append('西神楽北２条')
                results.append(address)

                return results

            elif last_four_digits == '0186':

                address.append('西神楽南')
                results.append(address)

                return results

            elif last_four_digits == '0171':

                address.append('西神楽南１条')
                results.append(address)

                return results

            elif last_four_digits == '0172':

                address.append('西神楽南２条')
                results.append(address)

                return results

            elif last_four_digits == '8160':

                address.append('東鷹栖１０線')
                results.append(address)

                return results

            elif last_four_digits == '8161':

                address.append('東鷹栖１１線')
                results.append(address)

                return results

            elif last_four_digits == '8162':

                address.append('東鷹栖１２線')
                results.append(address)

                return results

            elif last_four_digits == '8163':

                address.append('東鷹栖１３線')
                results.append(address)

                return results

            elif last_four_digits == '8164':

                address.append('東鷹栖１４線')
                results.append(address)

                return results

            elif last_four_digits == '8165':

                address.append('東鷹栖１５線')
                results.append(address)

                return results

            elif last_four_digits == '8101':

                address.append('東鷹栖１条')
                results.append(address)

                return results

            elif last_four_digits == '8151':

                address.append('東鷹栖１線')
                results.append(address)

                return results

            elif last_four_digits == '8102':

                address.append('東鷹栖２条')
                results.append(address)

                return results

            elif last_four_digits == '8152':

                address.append('東鷹栖２線')
                results.append(address)

                return results

            elif last_four_digits == '8103':

                address.append('東鷹栖３条')
                results.append(address)

                return results

            elif last_four_digits == '8153':

                address.append('東鷹栖３線')
                results.append(address)

                return results

            elif last_four_digits == '8104':

                address.append('東鷹栖４条')
                results.append(address)

                return results

            elif last_four_digits == '8154':

                address.append('東鷹栖４線')
                results.append(address)

                return results

            elif last_four_digits == '8155':

                address.append('東鷹栖５線')
                results.append(address)

                return results

            elif last_four_digits == '8156':

                address.append('東鷹栖６線')
                results.append(address)

                return results

            elif last_four_digits == '8157':

                address.append('東鷹栖７線')
                results.append(address)

                return results

            elif last_four_digits == '8158':

                address.append('東鷹栖８線')
                results.append(address)

                return results

            elif last_four_digits == '8159':

                address.append('東鷹栖９線')
                results.append(address)

                return results

            elif last_four_digits == '8111':

                address.append('東鷹栖東１条')
                results.append(address)

                return results

            elif last_four_digits == '8114':

                address.append('東鷹栖東１線')
                results.append(address)

                return results

            elif last_four_digits == '8112':

                address.append('東鷹栖東２条')
                results.append(address)

                return results

            elif last_four_digits == '8113':

                address.append('東鷹栖東３条')
                results.append(address)

                return results

            elif last_four_digits == '8171':

                address.append('東山')
                results.append(address)

                return results

            elif last_four_digits == '8166':

                address.append('緑台')
                results.append(address)

                return results

        elif first_three_digits == '074':

            address.append('北海道')
            address.append('旭川市')

            if last_four_digits == '1182':

                address.append('神居町豊里')
                results.append(address)

                return results

            elif last_four_digits == '1181':

                address.append('神居町西丘')
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

                        elif kanji[2] == '神楽岡１条':

                            katakana.append('カグラオカ1ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '神楽岡２条':

                            katakana.append('カグラオカ2ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '神楽岡３条':

                            katakana.append('カグラオカ3ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '神楽岡４条':

                            katakana.append('カグラオカ4ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '神楽岡５条':

                            katakana.append('カグラオカ5ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '神楽岡６条':

                            katakana.append('カグラオカ6ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '神楽岡７条':

                            katakana.append('カグラオカ7ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '神楽岡８条':

                            katakana.append('カグラオカ8ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '神楽岡９条':

                            katakana.append('カグラオカ9ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '神楽岡公園':

                            katakana.append('カグラオカコウエン')
                            results.append(katakana)

                        elif kanji[2] == '上常盤町':

                            katakana.append('カミトキワチョウ')
                            results.append(katakana)

                        elif kanji[2] == '神居１条':

                            katakana.append('カムイ1ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '神居２条':

                            katakana.append('カムイ2ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '神居３条':

                            katakana.append('カムイ3ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '神居４条':

                            katakana.append('カムイ4ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '神居５条':

                            katakana.append('カムイ5ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '神居６条':

                            katakana.append('カムイ6ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '神居７条':

                            katakana.append('カムイ7ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '神居８条':

                            katakana.append('カムイ8ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '神居９条':

                            katakana.append('カムイ9ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '神居町雨紛':

                            katakana.append('カムイチョウウブン')
                            results.append(katakana)

                        elif kanji[2] == '神居町上雨紛':

                            katakana.append('カムイチョウカミウブン')
                            results.append(katakana)

                        elif kanji[2] == '神居町神岡':

                            katakana.append('カムイチョウカミオカ')
                            results.append(katakana)

                        elif kanji[2] == '神居町神居古潭':

                            katakana.append('カムイチョウカムイコタン')
                            results.append(katakana)

                        elif kanji[2] == '神居町共栄':

                            katakana.append('カムイチョウキョウエイ')
                            results.append(katakana)

                        elif kanji[2] == '神居町神華':

                            katakana.append('カムイチョウシンカ')
                            results.append(katakana)

                        elif kanji[2] == '神居町台場':

                            katakana.append('カムイチョウダイバ')
                            results.append(katakana)

                        elif kanji[2] == '神居町忠和':

                            katakana.append('カムイチョウチュウワ')
                            results.append(katakana)

                        elif kanji[2] == '神居町富岡':

                            katakana.append('カムイチョウトミオカ')
                            results.append(katakana)

                        elif kanji[2] == '神居町富沢':

                            katakana.append('カムイチョウトミサワ')
                            results.append(katakana)

                        elif kanji[2] == '神居町豊里':

                            katakana.append('カムイチョウトヨサト')
                            results.append(katakana)

                        elif kanji[2] == '神居町西丘':

                            katakana.append('カムイチョウニシオカ')
                            results.append(katakana)

                        elif kanji[2] == '神居町春志内':

                            katakana.append('カムイチョウハルシナイ')
                            results.append(katakana)

                        elif kanji[2] == '亀吉１条':

                            katakana.append('カメキチ1ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '亀吉２条':

                            katakana.append('カメキチ2ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '亀吉３条':

                            katakana.append('カメキチ3ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '川端町１条':

                            katakana.append('カワバタチョウ1ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '川端町２条':

                            katakana.append('カワバタチョウ2ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '川端町３条':

                            katakana.append('カワバタチョウ3ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '川端町４条':

                            katakana.append('カワバタチョウ4ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '川端町５条':

                            katakana.append('カワバタチョウ5ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '川端町６条':

                            katakana.append('カワバタチョウ6ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '川端町７条':

                            katakana.append('カワバタチョウ7ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '旭神１条':

                            katakana.append('キョクシン1ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '旭神２条':

                            katakana.append('キョクシン2ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '旭神３条':

                            katakana.append('キョクシン3ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '旭神町':

                            katakana.append('キョクシンチョウ')
                            results.append(katakana)

                        elif kanji[2] == '金星町':

                            katakana.append('キンセイチョウ')
                            results.append(katakana)

                        elif kanji[2] == '工業団地１条':

                            katakana.append('コウギョウダンチ1ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '工業団地２条':

                            katakana.append('コウギョウダンチ2ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '工業団地３条':

                            katakana.append('コウギョウダンチ3ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '工業団地４条':

                            katakana.append('コウギョウダンチ4ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '工業団地５条':

                            katakana.append('コウギョウダンチ5ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '春光１条':

                            katakana.append('シュンコウ1ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '春光２条':

                            katakana.append('シュンコウ2ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '春光３条':

                            katakana.append('シュンコウ3ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '春光４条':

                            katakana.append('シュンコウ4ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '春光５条':

                            katakana.append('シュンコウ5ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '春光６条':

                            katakana.append('シュンコウ6ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '春光７条':

                            katakana.append('シュンコウ7ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '春光台１条':

                            katakana.append('シュンコウダイ1ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '春光台２条':

                            katakana.append('シュンコウダイ2ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '春光台３条':

                            katakana.append('シュンコウダイ3ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '春光台４条':

                            katakana.append('シュンコウダイ4ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '春光台５条':

                            katakana.append('シュンコウダイ5ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '春光町':

                            katakana.append('シュンコウチョウ')
                            results.append(katakana)

                        elif kanji[2] == '新星町':

                            katakana.append('シンセイチョウ')
                            results.append(katakana)

                        elif kanji[2] == '新富１条':

                            katakana.append('シントミ1ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '新富２条':

                            katakana.append('シントミ2ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '新富３条':

                            katakana.append('シントミ3ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '末広１条':

                            katakana.append('スエヒロ1ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '末広２条':

                            katakana.append('スエヒロ2ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '末広３条':

                            katakana.append('スエヒロ3ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '末広４条':

                            katakana.append('スエヒロ4ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '末広５条':

                            katakana.append('スエヒロ5ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '末広６条':

                            katakana.append('スエヒロ6ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '末広７条':

                            katakana.append('スエヒロ7ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '末広８条':

                            katakana.append('スエヒロ8ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '末広東１条':

                            katakana.append('スエヒロヒガシ1ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '末広東２条':

                            katakana.append('スエヒロヒガシ2ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '末広東３条':

                            katakana.append('スエヒロヒガシ3ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '住吉４条':

                            katakana.append('スミヨシ4ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '住吉５条':

                            katakana.append('スミヨシ5ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '住吉６条':

                            katakana.append('スミヨシ6ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '住吉７条':

                            katakana.append('スミヨシ7ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '大雪通':

                            katakana.append('タイセツドオリ')
                            results.append(katakana)

                        elif kanji[2] == '高砂台':

                            katakana.append('タカサゴダイ')
                            results.append(katakana)

                        elif kanji[2] == '台場１条':

                            katakana.append('ダイバ1ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '台場２条':

                            katakana.append('ダイバ2ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '台場３条':

                            katakana.append('ダイバ3ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '台場４条':

                            katakana.append('ダイバ4ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '台場東':

                            katakana.append('ダイバヒガシ')
                            results.append(katakana)

                        elif kanji[2] == '近文町':

                            katakana.append('チカブミチョウ')
                            results.append(katakana)

                        elif kanji[2] == '忠和１条':

                            katakana.append('チュウワ1ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '忠和２条':

                            katakana.append('チュウワ2ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '忠和３条':

                            katakana.append('チュウワ3ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '忠和４条':

                            katakana.append('チュウワ4ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '忠和５条':

                            katakana.append('チュウワ5ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '忠和６条':

                            katakana.append('チュウワ6ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '忠和７条':

                            katakana.append('チュウワ7ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '忠和８条':

                            katakana.append('チュウワ8ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '忠和９条':

                            katakana.append('チュウワ9ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '東光１０条':

                            katakana.append('トウコウ10ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '東光１１条':

                            katakana.append('トウコウ11ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '東光１２条':

                            katakana.append('トウコウ12ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '東光１３条':

                            katakana.append('トウコウ13ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '東光１４条':

                            katakana.append('トウコウ14ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '東光１５条':

                            katakana.append('トウコウ15ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '東光１６条':

                            katakana.append('トウコウ16ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '東光１７条':

                            katakana.append('トウコウ17ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '東光１８条':

                            katakana.append('トウコウ18ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '東光１９条':

                            katakana.append('トウコウ19ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '東光１条':

                            katakana.append('トウコウ1ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '東光２０条':

                            katakana.append('トウコウ20ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '東光２１条':

                            katakana.append('トウコウ21ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '東光２２条':

                            katakana.append('トウコウ22ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '東光２３条':

                            katakana.append('トウコウ23ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '東光２４条':

                            katakana.append('トウコウ24ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '東光２５条':

                            katakana.append('トウコウ25ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '東光２６条':

                            katakana.append('トウコウ26ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '東光２７条':

                            katakana.append('トウコウ27ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '東光２条':

                            katakana.append('トウコウ2ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '東光３条':

                            katakana.append('トウコウ3ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '東光４条':

                            katakana.append('トウコウ4ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '東光５条':

                            katakana.append('トウコウ5ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '東光６条':

                            katakana.append('トウコウ6ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '東光７条':

                            katakana.append('トウコウ7ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '東光８条':

                            katakana.append('トウコウ8ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '東光９条':

                            katakana.append('トウコウ9ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '常磐公園':

                            katakana.append('トキワコウエン')
                            results.append(katakana)

                        elif kanji[2] == '常盤通':

                            katakana.append('トキワドオリ')
                            results.append(katakana)

                        elif kanji[2] == '豊岡１０条':

                            katakana.append('トヨオカ10ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '豊岡１１条':

                            katakana.append('トヨオカ11ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '豊岡１２条':

                            katakana.append('トヨオカ12ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '豊岡１３条':

                            katakana.append('トヨオカ13ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '豊岡１４条':

                            katakana.append('トヨオカ14ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '豊岡１５条':

                            katakana.append('トヨオカ15ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '豊岡１６条':

                            katakana.append('トヨオカ16ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '豊岡１条':

                            katakana.append('トヨオカ1ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '豊岡２条':

                            katakana.append('トヨオカ2ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '豊岡３条':

                            katakana.append('トヨオカ3ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '豊岡４条':

                            katakana.append('トヨオカ4ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '豊岡５条':

                            katakana.append('トヨオカ5ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '豊岡６条':

                            katakana.append('トヨオカ6ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '豊岡７条':

                            katakana.append('トヨオカ7ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '豊岡８条':

                            katakana.append('トヨオカ8ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '豊岡９条':

                            katakana.append('トヨオカ9ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '中常盤町':

                            katakana.append('ナカトキワチョウ')
                            results.append(katakana)

                        elif kanji[2] == '永山１０条':

                            katakana.append('ナガヤマ10ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '永山１１条':

                            katakana.append('ナガヤマ11ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '永山１２条':

                            katakana.append('ナガヤマ12ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '永山１３条':

                            katakana.append('ナガヤマ13ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '永山１４条':

                            katakana.append('ナガヤマ14ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '永山１条':

                            katakana.append('ナガヤマ1ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '永山２条':

                            katakana.append('ナガヤマ2ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '永山３条':

                            katakana.append('ナガヤマ3ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '永山４条':

                            katakana.append('ナガヤマ4ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '永山５条':

                            katakana.append('ナガヤマ5ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '永山６条':

                            katakana.append('ナガヤマ6ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '永山７条':

                            katakana.append('ナガヤマ7ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '永山８条':

                            katakana.append('ナガヤマ8ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '永山９条':

                            katakana.append('ナガヤマ9ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '永山北１条':

                            katakana.append('ナガヤマキタ1ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '永山北２条':

                            katakana.append('ナガヤマキタ2ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '永山北３条':

                            katakana.append('ナガヤマキタ3ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '永山北４条':

                            katakana.append('ナガヤマキタ4ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '永山町':

                            katakana.append('ナガヤマチョウ')
                            results.append(katakana)

                        elif kanji[2] == '西神楽１線':

                            katakana.append('ニシカグラ1セン')
                            results.append(katakana)

                        elif kanji[2] == '西神楽２線':

                            katakana.append('ニシカグラ2セン')
                            results.append(katakana)

                        elif kanji[2] == '西神楽３線':

                            katakana.append('ニシカグラ3セン')
                            results.append(katakana)

                        elif kanji[2] == '西神楽４線':

                            katakana.append('ニシカグラ4セン')
                            results.append(katakana)

                        elif kanji[2] == '西神楽５線':

                            katakana.append('ニシカグラ5セン')
                            results.append(katakana)

                        elif kanji[2] == '西神楽北１条':

                            katakana.append('ニシカグラキタ1ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '西神楽北２条':

                            katakana.append('ニシカグラキタ2ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '西神楽南':

                            katakana.append('ニシカグラミナミ')
                            results.append(katakana)

                        elif kanji[2] == '西神楽南１条':

                            katakana.append('ニシカグラミナミ1ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '西神楽南２条':

                            katakana.append('ニシカグラミナミ2ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '錦町':

                            katakana.append('ニシキマチ')
                            results.append(katakana)

                        elif kanji[2] == '西御料１条':

                            katakana.append('ニシゴリョウ1ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '西御料２条':

                            katakana.append('ニシゴリョウ2ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '西御料３条':

                            katakana.append('ニシゴリョウ3ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '西御料４条':

                            katakana.append('ニシゴリョウ4ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '西御料５条':

                            katakana.append('ニシゴリョウ5ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '花咲町':

                            katakana.append('ハナサキチョウ')
                            results.append(katakana)

                        elif kanji[2] == 'パルプ町':

                            katakana.append('パルプチョウ')
                            results.append(katakana)

                        elif kanji[2] == 'パルプ町１条':

                            katakana.append('パルプチョウ1ジョウ')
                            results.append(katakana)

                        elif kanji[2] == 'パルプ町２条':

                            katakana.append('パルプチョウ2ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '東１条':

                            katakana.append('ヒガシ1ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '東２条':

                            katakana.append('ヒガシ2ジョウ')
                            results.append(katakana)
                            
                        elif kanji[2] == '東３条':

                            katakana.append('ヒガシ3ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '東４条':

                            katakana.append('ヒガシ4ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '東５条':

                            katakana.append('ヒガシ5ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '東６条':

                            katakana.append('ヒガシ6ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '東７条':

                            katakana.append('ヒガシ7ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '東８条':

                            katakana.append('ヒガシ8ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '東旭川北１条':

                            katakana.append('ヒガシアサヒカワキタ1ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '東旭川北２条':

                            katakana.append('ヒガシアサヒカワキタ2ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '東旭川北３条':

                            katakana.append('ヒガシアサヒカワキタ3ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '東旭川町上兵村':

                            katakana.append('ヒガシアサヒカワチョウカミヘイソン')
                            results.append(katakana)

                        elif kanji[2] == '東旭川町共栄':

                            katakana.append('ヒガシアサヒカワチョウキョウエイ')
                            results.append(katakana)

                        elif kanji[2] == '東旭川町旭正':

                            katakana.append('ヒガシアサヒカワチョウキョクセイ')
                            results.append(katakana)

                        elif kanji[2] == '東旭川町倉沼':

                            katakana.append('ヒガシアサヒカワチョウクラヌマ')
                            results.append(katakana)

                        elif kanji[2] == '東旭川町桜岡':

                            katakana.append('ヒガシアサヒカワチョウサクラオカ')
                            results.append(katakana)

                        elif kanji[2] == '東旭川町下兵村':

                            katakana.append('ヒガシアサヒカワチョウシモヘイソン')
                            results.append(katakana)

                        elif kanji[2] == '東旭川町忠別':

                            katakana.append('ヒガシアサヒカワチョウチュウベツ')
                            results.append(katakana)

                        elif kanji[2] == '東旭川町豊田':

                            katakana.append('ヒガシアサヒカワチョウトヨタ')
                            results.append(katakana)

                        elif kanji[2] == '東旭川町東桜岡':

                            katakana.append('ヒガシアサヒカワチョウヒガシサクラオカ')
                            results.append(katakana)

                        elif kanji[2] == '東旭川町日ノ出':

                            katakana.append('ヒガシアサヒカワチョウヒノデ')
                            results.append(katakana)

                        elif kanji[2] == '東旭川町瑞穂':

                            katakana.append('ヒガシアサヒカワチョウミズホ')
                            results.append(katakana)

                        elif kanji[2] == '東旭川町米原':

                            katakana.append('ヒガシアサヒカワチョウヨネハラ')
                            results.append(katakana)

                        elif kanji[2] == '東旭川南１条':

                            katakana.append('ヒガシアサヒカワミナミ1ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '東旭川南２条':

                            katakana.append('ヒガシアサヒカワミナミ2ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '東鷹栖１０線':

                            katakana.append('ヒガシタカス10セン')
                            results.append(katakana)

                        elif kanji[2] == '東鷹栖１１線':

                            katakana.append('ヒガシタカス11セン')
                            results.append(katakana)

                        elif kanji[2] == '東鷹栖１２線':

                            katakana.append('ヒガシタカス12セン')
                            results.append(katakana)

                        elif kanji[2] == '東鷹栖１３線':

                            katakana.append('ヒガシタカス13セン')
                            results.append(katakana)

                        elif kanji[2] == '東鷹栖１４線':

                            katakana.append('ヒガシタカス14セン')
                            results.append(katakana)

                        elif kanji[2] == '東鷹栖１５線':

                            katakana.append('ヒガシタカス15セン')
                            results.append(katakana)

                        elif kanji[2] == '東鷹栖１条':

                            katakana.append('ヒガシタカス1ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '東鷹栖１線':

                            katakana.append('ヒガシタカス1セン')
                            results.append(katakana)

                        elif kanji[2] == '東鷹栖２条':

                            katakana.append('ヒガシタカス2ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '東鷹栖２線':

                            katakana.append('ヒガシタカス2セン')
                            results.append(katakana)

                        elif kanji[2] == '東鷹栖３条':

                            katakana.append('ヒガシタカス3ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '東鷹栖３線':

                            katakana.append('ヒガシタカス3セン')
                            results.append(katakana)

                        elif kanji[2] == '東鷹栖４条':

                            katakana.append('ヒガシタカス4ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '東鷹栖４線':

                            katakana.append('ヒガシタカス4セン')
                            results.append(katakana)

                        elif kanji[2] == '東鷹栖５線':

                            katakana.append('ヒガシタカス5セン')
                            results.append(katakana)

                        elif kanji[2] == '東鷹栖６線':

                            katakana.append('ヒガシタカス6セン')
                            results.append(katakana)

                        elif kanji[2] == '東鷹栖７線':

                            katakana.append('ヒガシタカス7セン')
                            results.append(katakana)

                        elif kanji[2] == '東鷹栖８線':

                            katakana.append('ヒガシタカス8セン')
                            results.append(katakana)

                        elif kanji[2] == '東鷹栖９線':

                            katakana.append('ヒガシタカス9セン')
                            results.append(katakana)

                        elif kanji[2] == '東鷹栖東１条':

                            katakana.append('ヒガシタカスヒガシ1ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '東鷹栖東１線':

                            katakana.append('ヒガシタカスヒガシ1セン')
                            results.append(katakana)

                        elif kanji[2] == '東鷹栖東２条':

                            katakana.append('ヒガシタカスヒガシ2ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '東鷹栖東３条':

                            katakana.append('ヒガシタカスヒガシ3ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '東山':

                            katakana.append('ヒガシヤマ')
                            results.append(katakana)

                        elif kanji[2] == '北門町':

                            katakana.append('ホクモンチョウ')
                            results.append(katakana)

                        elif kanji[2] == '緑が丘１条':

                            katakana.append('ミドリガオカ1ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '緑が丘２条':

                            katakana.append('ミドリガオカ2ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '緑が丘３条':

                            katakana.append('ミドリガオカ3ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '緑が丘４条':

                            katakana.append('ミドリガオカ4ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '緑が丘５条':

                            katakana.append('ミドリガオカ5ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '緑が丘東１条':

                            katakana.append('ミドリガオカヒガシ1ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '緑が丘東２条':

                            katakana.append('ミドリガオカヒガシ2ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '緑が丘東３条':

                            katakana.append('ミドリガオカヒガシ3ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '緑が丘東４条':

                            katakana.append('ミドリガオカヒガシ4ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '緑が丘東５条':

                            katakana.append('ミドリガオカヒガシ5ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '緑が丘南１条':

                            katakana.append('ミドリガオカミナミ1ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '緑が丘南２条':

                            katakana.append('ミドリガオカミナミ2ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '緑が丘南３条':

                            katakana.append('ミドリガオカミナミ3ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '緑が丘南４条':

                            katakana.append('ミドリガオカミナミ4ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '緑が丘南５条':

                            katakana.append('ミドリガオカミナミ5ジョウ')
                            results.append(katakana)

                        elif kanji[2] == '緑台':

                            katakana.append('ミドリダイ')
                            results.append(katakana)

                        elif kanji[2] == '緑町':

                            katakana.append('ミドリマチ')
                            results.append(katakana)

                        elif kanji[2] == '南１条通':

                            katakana.append('ミナミ1ジョウドオリ')
                            results.append(katakana)

                        elif kanji[2] == '南２条通':

                            katakana.append('ミナミ2ジョウドオリ')
                            results.append(katakana)

                        elif kanji[2] == '南３条通':

                            katakana.append('ミナミ3ジョウドオリ')
                            results.append(katakana)

                        elif kanji[2] == '南４条通':

                            katakana.append('ミナミ4ジョウドオリ')
                            results.append(katakana)

                        elif kanji[2] == '南５条通':

                            katakana.append('ミナミ5ジョウドオリ')
                            results.append(katakana)

                        elif kanji[2] == '南６条通':

                            katakana.append('ミナミ6ジョウドオリ')
                            results.append(katakana)

                        elif kanji[2] == '南７条通':

                            katakana.append('ミナミ7ジョウドオリ')
                            results.append(katakana)

                        elif kanji[2] == '南８条通':

                            katakana.append('ミナミ8ジョウドオリ')
                            results.append(katakana)

                        elif kanji[2] == '南９条通':

                            katakana.append('ミナミ9ジョウドオリ')
                            results.append(katakana)

        if len(results) > 0:
            return results

        raise ValueError(self._emcreator.message('JPPostCodeBuilder.py','convertKanjiToKatakana','kanji error','the kanji is an incompatible value.'))

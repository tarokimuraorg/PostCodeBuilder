import re
import JPAddressData
from JPAddressPage import JPAddressPage
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

    def address_finder(self):

        if self._post_code:

            address_data = JPAddressData.read_address_data()
            address_data = list(filter(lambda row: str(row[0]).strip() == self._post_code[1:], address_data))

            if len(address_data) > 0:

                address_book = list(map(self.__write_on_address_page, address_data))

                if len(address_book) > 0:
                    return address_book
                
                print(ErrorMessageBuilder.message('JPPostCodeBuilder','address_finder','invalid data',f'the data including the post code({self._post_code}) is incompatible with the write_on_address_page function.'))
                return []
                
            else:

                # 北海道 赤平市
                if (self._post_code[0:5] == '07911'):
                    return [JPAddressPage(self._post_code, '北海道 赤平市', 'ﾎｯｶｲﾄﾞｳ ｱｶﾋﾞﾗｼ')]

                # 北海道 阿寒郡鶴居村
                elif (self._post_code[0:5] == '08512'):
                    return [JPAddressPage(self._post_code, '北海道 阿寒郡鶴居村', 'ﾎｯｶｲﾄﾞｳ ｱｶﾝｸﾞﾝﾂﾙｲﾑﾗ')]
                
                # 北海道 足寄郡足寄町
                elif self._post_code[0:5] == '08937':
                    return [JPAddressPage(self._post_code, '北海道 足寄郡足寄町', 'ﾎｯｶｲﾄﾞｳ ｱｼｮﾛｸﾞﾝｱｼｮﾛﾁｮｳ')]
                
                # 北海道 足寄郡陸別町
                elif self._post_code[0:5] == '08943':
                    return [JPAddressPage(self._post_code, '北海道 足寄郡陸別町', 'ﾎｯｶｲﾄﾞｳ ｱｼｮﾛｸﾞﾝﾘｸﾍﾞﾂﾁｮｳ')]
                
                # 北海道 厚岸郡厚岸町
                elif self._post_code[0:5] == '08811':
                    return [JPAddressPage(self._post_code, '北海道 厚岸郡厚岸町', 'ﾎｯｶｲﾄﾞｳ ｱｯｹｼｸﾞﾝｱｯｹｼﾁｮｳ')]
                
                # 北海道 厚岸郡浜中町
                elif self._post_code[0:5] == '08815':
                    return [JPAddressPage(self._post_code, '北海道 厚岸郡浜中町', 'ﾎｯｶｲﾄﾞｳ ｱｯｹｼｸﾞﾝﾊﾏﾅｶﾁｮｳ')]
                
                # 北海道 網走郡大空町
                elif self._post_code[0:5] == '09923':
                    return [JPAddressPage(self._post_code, '北海道 網走郡大空町', 'ﾎｯｶｲﾄﾞｳ ｱﾊﾞｼﾘｸﾞﾝｵｵｿﾞﾗﾁｮｳ')]
                
                # 北海道 網走郡津別町
                elif self._post_code[0:5] == '09202':
                    return [JPAddressPage(self._post_code, '北海道 網走郡津別町', 'ﾎｯｶｲﾄﾞｳ ｱﾊﾞｼﾘｸﾞﾝﾂﾍﾞﾂﾁｮｳ')]
                
                # 北海道 虻田郡喜茂別町
                elif self._post_code[0:5] == '04402':
                    return [JPAddressPage(self._post_code, '北海道 虻田郡喜茂別町', 'ﾎｯｶｲﾄﾞｳ ｱﾌﾞﾀｸﾞﾝｷﾓﾍﾞﾂﾁｮｳ')]
                
                # 北海道 虻田郡京極町
                elif self._post_code[0:5] == '04401':
                    return [JPAddressPage(self._post_code, '北海道 虻田郡京極町', 'ﾎｯｶｲﾄﾞｳ ｱﾌﾞﾀｸﾞﾝｷｮｳｺﾞｸﾁｮｳ')]

                # 北海道 旭川市
                elif self._post_code[0:5] == '07000':
                    return [JPAddressPage(self._post_code, '北海道 旭川市', 'ﾎｯｶｲﾄﾞｳ ｱｻﾋｶﾜｼ')]
                
                # 北海道 芦別市
                elif self._post_code[0:5] == '07500':
                    return [JPAddressPage(self._post_code, '北海道 芦別市', 'ﾎｯｶｲﾄﾞｳ ｱｼﾍﾞﾂｼ')]
                
                # 北海道 網走郡美幌町
                elif self._post_code[0:5] == '09200':
                    return [JPAddressPage(self._post_code, '北海道 網走郡美幌町', 'ﾎｯｶｲﾄﾞｳ ｱﾊﾞｼﾘｸﾞﾝﾋﾞﾎﾛﾁｮｳ')]
                
                # 北海道 網走市
                elif self._post_code[0:5] == '09300':
                    return [JPAddressPage(self._post_code, '北海道 網走市', 'ﾎｯｶｲﾄﾞｳ ｱﾊﾞｼﾘｼ')]
                
                # 北海道 虻田郡倶知安町
                elif self._post_code[0:5] == '04400':
                    return [JPAddressPage(self._post_code, '北海道 虻田郡倶知安町', 'ﾎｯｶｲﾄﾞｳ ｱﾌﾞﾀｸﾞﾝｸｯﾁｬﾝﾁｮｳ')]

                print(ErrorMessageBuilder.message('JPPostCodeBuilder','address_finder','invalid argument',f'the argument ({self._post_code}) is an incompatible post code.'))
                return []
    
        print(ErrorMessageBuilder.message('JPPostCodeBuilder','address_finder','invalid argument','post code is a 7-digit number.'))
        return []
    
    def __write_on_address_page(self, row):

        post_code = '0'
        post_code = post_code + str(row[0])
        post_code = post_code.strip()

        furigana = str(row[1]) + ' '
        furigana = furigana + str(row[2]) + ' '
        furigana = furigana + str(row[3])
        furigana = furigana.replace('ｲｶﾆｹｲｻｲｶﾞﾅｲﾊﾞｱｲ','')
        furigana = re.sub('\(\d+-\d+､\d+-\d+ﾊﾞﾝﾁ\)', '', furigana)
        furigana = re.sub('\(\d+-\d+ﾁｮｳﾒ\)','',furigana)
        furigana = re.sub('\(\d+-\d+ﾊﾞﾝﾁ\)','',furigana)
        furigana = re.sub('\(\d+ﾁｮｳﾒ\d+-\d+ﾊﾞﾝﾁ\)', '', furigana)
        furigana = re.sub('\(\d+､\d+ﾊﾞﾝﾁ\)', '', furigana)
        furigana = re.sub('\(\d+ﾊﾞﾝﾁ\)', '', furigana)
        furigana = furigana.replace('(ｿﾉﾀ)', '')
        furigana = furigana.replace('(ﾁｮｳﾒ)', '')
        furigana = furigana.strip()

        address = str(row[4]) + ' '
        address = address + str(row[5]) + ' '
        address = address + str(row[6])
        address = address.replace('以下に掲載がない場合','')
        address = re.sub('（\d+～\d+、\d+～\d+番地）', '', address)
        address = re.sub('（\d+～\d+番地）','',address)
        address = re.sub('（\d+～\d+丁目）','',address)
        address = re.sub('（\d+－\d+番地）', '', address)
        address = re.sub('（\d+丁目\d+～\d+番地）', '', address)
        address = re.sub('（\d+、\d+番地）', '', address)
        address = re.sub('（\d+番地）', '', address)
        address = address.replace('（その他）', '')
        address = address.replace('（丁目）', '')
        
        address = address.strip()

        return JPAddressPage(post_code, address, furigana)

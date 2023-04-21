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

                # ===================
                # 郵便番号の上5桁で判断 
                # ===================

                # 北海道 赤平市
                if (self._post_code[0:5] == '07911'):

                    if len(address_book) > 0:
                        return address_book
                    
                    return [JPAddressPage(self._post_code, '北海道 赤平市', 'ﾎｯｶｲﾄﾞｳ ｱｶﾋﾞﾗｼ')]

                # 北海道 阿寒郡鶴居村
                elif (self._post_code[0:5] == '08512'):
                    
                    if len(address_book) > 0:
                        return address_book
                    
                    return [JPAddressPage(self._post_code, '北海道 阿寒郡鶴居村', 'ﾎｯｶｲﾄﾞｳ ｱｶﾝｸﾞﾝﾂﾙｲﾑﾗ')]
                
                # 北海道 足寄郡足寄町
                elif self._post_code[0:5] == '08937':
                    
                    if len(address_book) > 0:
                        return address_book
                    
                    return [JPAddressPage(self._post_code, '北海道 足寄郡足寄町', 'ﾎｯｶｲﾄﾞｳ ｱｼｮﾛｸﾞﾝｱｼｮﾛﾁｮｳ')]
                
                # 北海道 足寄郡陸別町
                elif self._post_code[0:5] == '08943':
                    
                    if len(address_book) > 0:
                        return address_book
                    
                    return [JPAddressPage(self._post_code, '北海道 足寄郡陸別町', 'ﾎｯｶｲﾄﾞｳ ｱｼｮﾛｸﾞﾝﾘｸﾍﾞﾂﾁｮｳ')]
                
                # 北海道 厚岸郡厚岸町
                elif self._post_code[0:5] == '08811':
                    
                    if len(address_book) > 0:
                        return address_book
                    
                    return [JPAddressPage(self._post_code, '北海道 厚岸郡厚岸町', 'ﾎｯｶｲﾄﾞｳ ｱｯｹｼｸﾞﾝｱｯｹｼﾁｮｳ')]
                
                # 北海道 厚岸郡浜中町
                elif self._post_code[0:5] == '08815':

                    if len(address_book) > 0:
                        return address_book
                    
                    return [JPAddressPage(self._post_code, '北海道 厚岸郡浜中町', 'ﾎｯｶｲﾄﾞｳ ｱｯｹｼｸﾞﾝﾊﾏﾅｶﾁｮｳ')]
                
                # 北海道 網走郡大空町
                elif self._post_code[0:5] == '09923':

                    if len(address_book) > 0:
                        return address_book
                    
                    return [JPAddressPage(self._post_code, '北海道 網走郡大空町', 'ﾎｯｶｲﾄﾞｳ ｱﾊﾞｼﾘｸﾞﾝｵｵｿﾞﾗﾁｮｳ')]

                # ===================
                # 郵便番号の上3桁で判断
                # ===================

                # 北海道 旭川市
                if self._post_code[0:3] == '070':

                    if len(address_book) > 0:
                        return address_book
                    
                    return [JPAddressPage(self._post_code, '北海道 旭川市', 'ﾎｯｶｲﾄﾞｳ ｱｻﾋｶﾜｼ')]
                
                # 北海道 芦別市
                elif self._post_code[0:3] == '075':

                    if len(address_book) > 0:
                        return address_book
                    
                    return [JPAddressPage(self._post_code, '北海道 芦別市', 'ﾎｯｶｲﾄﾞｳ ｱｼﾍﾞﾂｼ')]

                return address_book
    
        print(ErrorMessageBuilder.message('JPPostCodeBuilder','address_finder','invalid argument','the post code is a 7-digit number.'))
        return []
    
    def __write_on_address_page(self, row):

        post_code = '0'
        post_code = post_code + str(row[0])
        post_code = post_code.strip()

        furigana = str(row[1]) + ' '
        furigana = furigana + str(row[2]) + ' '
        furigana = furigana + str(row[3])
        furigana = furigana.replace('ｲｶﾆｹｲｻｲｶﾞﾅｲﾊﾞｱｲ','')
        furigana = re.sub('\(\d+-\d+ﾁｮｳﾒ\)','',furigana)
        furigana = re.sub('\(\d+-\d+ﾊﾞﾝﾁ\)','',furigana)
        furigana = re.sub('\(\d+ﾁｮｳﾒ\d+-\d+ﾊﾞﾝﾁ\)', '', furigana)
        furigana = furigana.replace('(ｿﾉﾀ)', '')
        furigana = furigana.replace('(ﾁｮｳﾒ)', '')
        furigana = furigana.strip()

        address = str(row[4]) + ' '
        address = address + str(row[5]) + ' '
        address = address + str(row[6])
        address = address.replace('以下に掲載がない場合','')
        address = re.sub('（\d+～\d+番地）','',address)
        address = re.sub('（\d+～\d+丁目）','',address)
        address = re.sub('（\d+－\d+番地）', '', address)
        address = re.sub('（\d+丁目\d+～\d+番地）', '', address)
        address = address.replace('（その他）', '')
        address = address.replace('（丁目）', '')
        
        address = address.strip()

        return JPAddressPage(post_code, address, furigana)

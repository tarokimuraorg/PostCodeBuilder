import pandas
from ErrorMessageCreator import ErrorMessageCreator
from JPAddressPage import JPAddressPage

class JPAddressBook:
    
    def __init__(self):

        self._emcreator = ErrorMessageCreator()
        self._csv_list = []

    def __readCSVData(self):
        
        try:

            data_frame = pandas.read_csv('./csv/ken_all.csv', usecols=[2,3,4,5,6,7,8], names=['post_code','furigana1','furigana2','furigana3','address1','address2','address3'])
            csv_data = data_frame.drop_duplicates()
            self._csv_list = csv_data.values.tolist()

        except Exception as e:

            raise ValueError(self._emcreator.message('JPAddressBook', 'readCSVData', 'failed to read csv data', '{}'.format(e)))

    def createAddressBook(self):
        
        try:
            
            self.__readCSVData()
            address_book = []

            for row in self._csv_list:

                post_code = '0'
                post_code = post_code + str(row[0])
                post_code = post_code.strip()

                furigana = str(row[1]) + ' '
                furigana = furigana + str(row[2]) + ' '
                furigana = furigana + str(row[3])
                furigana = furigana.replace('ｲｶﾆｹｲｻｲｶﾞﾅｲﾊﾞｱｲ','')
                furigana = furigana.strip()

                address = str(row[4]) + ' '
                address = address + str(row[5]) + ' '
                address = address + str(row[6])
                address = address.replace('以下に掲載がない場合','')
                address = address.strip()

                address_page = JPAddressPage(post_code, address, furigana)
                address_book.append(address_page)

            return address_book

        except ValueError as ve:

            print('{}'.format(ve))
            return []

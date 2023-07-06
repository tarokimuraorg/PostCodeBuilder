import pandas
import ErrorMessageBuilder

def read_address_data():

    address_book = []

    try:

        data_frame = pandas.read_csv('./csv/utf_all.csv', usecols=[2,3,4,5,6,7,8], names=['post_code','furigana1','furigana2','furigana3','address1','address2','address3'])
        csv_data = data_frame.drop_duplicates()

        return csv_data.values.tolist()
    
    except Exception as e:
        print(ErrorMessageBuilder.message('JPAddressData', 'readAddressData', 'failed to read csv data', f'{e}'))
    
    return address_book

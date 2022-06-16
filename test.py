from turtle import pos
from JPPostCodeBuilder import JPPostCodeBuilder

post_code = ''
#post_code = '079-1143'
#post_code = '079-1134'
#post_code = '079-1274'
#post_code = '079-1141'
#post_code = '079-1121'
#post_code = '079-1101'
#post_code = '079-1154'
#post_code = '079-1152'
#post_code = '079-1155'
#post_code = '079-1156'
#post_code = '079-1124'
#post_code = '079-1133'
#post_code = '079-1135'
#post_code = '079-1131'
post_code = '079-1122'

try:
    jppc_builder = JPPostCodeBuilder(post_code)
    address = jppc_builder.convertToAddress()

    print(jppc_builder.convertToAddress())
    print(jppc_builder.convertKanjiToYomigana())

except ValueError as ve:
    print(ve)

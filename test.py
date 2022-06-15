from JPPostCodeBuilder import JPPostCodeBuilder

post_code = ''
#post_code = '079-1143'
#post_code = '079-1134'
#post_code = '079-1274'
#post_code = '079-1141'
#post_code = '079-1121'

try:

    jppc_builder = JPPostCodeBuilder(post_code)
    address = jppc_builder.convertToAddress()

    print(jppc_builder.convertToAddress())
    print(jppc_builder.convertKanjiToYomigana())

except ValueError as ve:
    print(ve)

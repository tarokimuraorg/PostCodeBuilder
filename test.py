from JPPostCodeBuilder import JPPostCodeBuilder

post_code = '079-1143'
jppc_builder = JPPostCodeBuilder(post_code)
address = jppc_builder.convertToAddress()

print(jppc_builder.convertToAddress())
print(jppc_builder.convertKanjiToYomigana())

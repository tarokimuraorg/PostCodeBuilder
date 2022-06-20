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
#post_code = '079-1122'
#post_code = '079-1142'
#post_code = '079-1132'
#post_code = '079-1123'
#post_code = '079-1271'
#post_code = '079-1273'
#post_code = '079-1272'
#post_code = '079-1285'
#post_code = '079-1287'
#post_code = '079-1281'
#post_code = '079-1282'
#post_code = '079-1286'
#post_code = '079-1283'
#post_code = '079-1284'
#post_code = '079-1153'
#post_code = '079-1102'
#post_code = '079-1136'
#post_code = '079-1144'
#post_code = '079-1151'
#post_code = '079-1266'
#post_code = '079-1264'
#post_code = '079-1262'
#post_code = '079-1265'
#post_code = '079-1261'
#post_code = '079-1263'
#post_code = '079-1264'
#post_code = '079-1268'
#post_code = '079-1267'
post_code = ''

try:
    jppc_builder = JPPostCodeBuilder(post_code)

    address = jppc_builder.convertToAddress()
    yomigana = jppc_builder.convertKanjiToYomigana()

    for elm in address:
        print(elm)

    for elm in yomigana:
        print(elm)

except ValueError as ve:
    print(ve)

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
#post_code = '079-1111'
#post_code = '079-1112'
#post_code = '079-1113'
#post_code = '079-1114'

#post_code = '079-1100'

#post_code = '085-0467'
#post_code = '085-0238'
#post_code = '085-0212'
#post_code = '085-0245'
#post_code = '085-0221'
#post_code = '085-0235'
#post_code = '085-0216'
#post_code = '085-0217'
#post_code = '085-0211'
#post_code = '085-0231'
#post_code = '085-0223'
#post_code = '085-0218'
#post_code = '085-0234'
#post_code = '085-0232'
#post_code = '085-0215'
#post_code = '085-0237'
#post_code = '085-0241'
#post_code = '085-0236'
#post_code = '085-0213'
#post_code = '085-0243'
#post_code = '085-0233'
#post_code = '085-0201'
#post_code = '085-0242'
#post_code = '085-0214'
#post_code = '085-0222'
#post_code = '085-0224'

#post_code = '085-1200'

#post_code = '085-1146'
#post_code = '085-1145'
#post_code = '085-1132'
#post_code = '085-1212'
#post_code = '085-1133'
#post_code = '085-1262'
#post_code = '085-1211'
#post_code = '085-1144'
#post_code = '085-1131'
#post_code = '085-1201'
#post_code = '085-1203'
#post_code = '085-1206'
#post_code = '085-1204'
#post_code = '085-1261'
#post_code = '085-1202'
#post_code = '085-1207'
#post_code = '085-1205'
#post_code = '085-1143'
#post_code = '085-1147'
#post_code = '085-1141'
#post_code = '085-1142'
#post_code = '085-1213'
#post_code = '085-1134'

#post_code = '070-0000'

#post_code = '070-0040'
#post_code = '070-0031'
#post_code = '070-0032'
#post_code = '070-0052'
#post_code = '070-0033'
#post_code = '070-0053'
#post_code = '070-0971'
#post_code = '070-0972'
#post_code = '070-0973'
#post_code = '070-0034'
#post_code = '070-0054'
#post_code = '070-0035'
#post_code = '070-0055'
#post_code = '070-0036'
#post_code = '070-0056'
#post_code = '070-0037'
#post_code = '070-0057'
#post_code = '070-0038'
#post_code = '070-0058'
#post_code = '070-0039'
#post_code = '070-0059'

#post_code = '078-8220'
#post_code = '078-8221'
#post_code = '078-8211'
#post_code = '078-8212'
#post_code = '078-8213'
#post_code = '078-8214'
#post_code = '078-8215'
#post_code = '078-8216'
#post_code = '078-8217'
#post_code = '078-8218'
#post_code = '078-8219'

#post_code = '079-8401'
#post_code = '079-8402'
#post_code = '079-8403'

#post_code = '070-0061'
#post_code = '070-0062'
#post_code = '070-0063'
#post_code = '070-0072'
post_code = '070-0073'

try:
    jppc_builder = JPPostCodeBuilder(post_code)

    address = jppc_builder.convertToAddress()
    yomigana = jppc_builder.furigana()

    for elm in address:
        print(elm)

    for elm in yomigana:
        print(elm)

except ValueError as ve:
    print(ve)

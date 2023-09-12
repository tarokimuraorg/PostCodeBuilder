from PostCodeBuilder import PostCodeBuilder
from TestPostCodeBuilder import TestPostCodeBuilder

post_code = ''

# 北海道 赤平市
# post_code = '079-1100'
# post_code = '079-1134'

# post_code = '085-0467'
# post_code = '085-0238'

# 北海道 釧路市 阿寒町雄別横山
# post_code = '085-0224'
# post_code = '085-1200'
# post_code = '085-1146'
# post_code = '085-1202'
# post_code = '085-1207'
# post_code = '085-1205'

# 北海道 阿寒郡鶴居村 茂幌呂
# post_code = '085-1134'

# post_code = '070-0000'
# post_code = '078-8220'
# post_code = '070-0040'
# post_code = '070-0031'
# post_code = '078-8211'
# post_code = '070-0032'
# post_code = '078-8212'
# post_code = '070-0033'
# post_code = '078-8213'
# post_code = '070-0053'
# post_code = '070-0034'
# post_code = '078-8214'
# post_code = '070-0035'
# post_code = '078-8215'
# post_code = '070-0036'
# post_code = '078-8216'
# post_code = '070-0037'
# post_code = '078-8217'
# post_code = '070-0038'
# post_code = '078-8218'
# post_code = '070-0039'
# post_code = '078-8219'
# post_code = '078-0186'
# post_code = '074-1181'
# post_code = '078-8202'
# post_code = '078-1272'
# post_code = '078-8201'
# post_code = '078-1271'
# post_code = '070-0030'
# post_code = '078-8330'

# 北海道 旭川市 流通団地４条
# post_code = '079-8444'
# post_code = '075-0000'
# post_code = '075-0165'

# 北海道 芦別市 緑泉町
# post_code = '075-0163'
# post_code = '089-3700'
# post_code = '089-3708'
# post_code = '089-4144'
# post_code = '089-4251'
# post_code = '089-3873'
# post_code = '089-3731'
# post_code = '089-3737'
# post_code = '089-3875'

# 北海道 足寄郡足寄町 鷲府
# post_code = '089-3736'
# post_code = '089-4300'
# post_code = '089-4301'

# 北海道 足寄郡陸別町 若葉
# post_code = '089-4302'
# post_code = '088-1100'
# post_code = '088-1113'
# post_code = '088-1141'
# post_code = '088-1139'
# post_code = '088-0874'
# post_code = '088-1126'
# post_code = '088-0878'

# 北海道 厚岸郡厚岸町 湾月
# post_code = '088-1114'
# post_code = '088-1500'
# post_code = '088-1406'
# post_code = '088-1646'
# post_code = '088-1412'
# post_code = '088-1645'
# post_code = '088-1360'

# 北海道 厚岸郡浜中町 渡散布
# post_code = '088-1534'
# post_code = '061-3601'
# post_code = '061-3441'

# 北海道 石狩市 厚田区安瀬
# post_code = '061-3606'
# post_code = '099-2300'
# post_code = '099-3225'
# post_code = '099-3233'
# post_code = '099-3211'
# post_code = '099-3212'
# post_code = '099-3244'
# post_code = '099-3213'
# post_code = '099-3223'
# post_code = '099-3214'

# 北海道 網走郡大空町 女満別夕陽台
# post_code = '099-2355'
# post_code = '092-0200'
# post_code = '092-0215'

# 北海道 網走郡津別町 最上
# post_code = '092-0201'
# post_code = '099-3225'

# 北海道 網走郡大空町 東藻琴山園
# post_code = '099-3243'
# post_code = '092-0000'
# post_code = '092-0064'
# post_code = '092-0175'
# post_code = '092-0025'
# post_code = '092-0176'
# post_code = '092-0005'
# post_code = '092-0171'
# post_code = '092-0030'

# 北海道 網走郡美幌町 元町
# post_code = '092-0063'
# post_code = '099-2362'

# 北海道 網走郡大空町 女満別夕陽台
# post_code = '099-2355'
# post_code = '093-0000'
# post_code = '099-3115'

# 北海道 網走市 呼人
# post_code = '099-2421'
# post_code = '049-5601'
# post_code = '049-5722'
# post_code = '049-5613'

# 北海道 虻田郡洞爺湖町 三豊
# post_code = '049-5616'
# post_code = '044-0200'
# post_code = '044-0215'

# 北海道 虻田郡喜茂別町 留産
# post_code = '044-0212'
# post_code = '044-0100'
# post_code = '044-0122'

# 北海道 虻田郡京極町 脇方
# post_code = '044-0123'
# post_code = '044-0000'
# post_code = '〒 044-0083'
# post_code = '044-0080'

# 北海道 虻田郡倶知安町 大和
# post_code = '044‐0061'
# post_code = '049-5600'
# post_code = '049-5601'
# post_code = '049-5722'
# post_code = '049-5613'

# 北海道 虻田郡洞爺湖町 三豊
# post_code = '049-5616'
# post_code = '049-5801'

# 北海道 虻田郡洞爺湖町 伏見
# post_code = '049-5833'
# post_code = '049-5400'
# post_code = '049-5412'

# 北海道 虻田郡豊浦町 礼文華
post_code = '049-5333'

address_pages = PostCodeBuilder(post_code).address_finder()

for page in address_pages:

    print()
    print('郵便番号 : {}'.format(page.post_code))
    print('住所 : {}'.format(page.address))
    print('フリガナ : {}'.format(page.furigana))

# 上5桁で検索
# address_pages = TestPostCodeBuilder(post_code).address_finder_for_5digit()

# for page in address_pages:

#     print()
#     print('郵便番号 : {}'.format(page.post_code))
#     print('住所 : {}'.format(page.address))
#     print('フリガナ : {}'.format(page.furigana))

# 上3桁で検索
# address_pages = TestPostCodeBuilder(post_code).address_finder_for_3digit()

# for page in address_pages:

#     print()
#     print('郵便番号 : {}'.format(page.post_code))
#     print('住所 : {}'.format(page.address))
#     print('フリガナ : {}'.format(page.furigana))

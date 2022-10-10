from JPPostCodeBuilder import JPPostCodeBuilder

post_code = '079-1100'
address_pages = JPPostCodeBuilder(post_code).address_finder()

for page in address_pages:

    print()
    print('郵便番号 : {}'.format(page.post_code))
    print('住所 : {}'.format(page.address))
    print('フリガナ : {}'.format(page.furigana))

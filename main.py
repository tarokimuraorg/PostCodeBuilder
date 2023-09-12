from PostCodeBuilder import PostCodeBuilder

if __name__ == '__main__':

    jppc_builder = PostCodeBuilder('079-1143')

    address = jppc_builder.convertToAddress()

    print(''.join(address))
    print(jppc_builder.convertKanjiToYomigana())

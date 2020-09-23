import random
#Function to create a dataset for Hiragana characters
def hira():
    # Lists of dictionaries, key being pronunciation and value with character
    kana0 = [{'a':'あ'}, {'ii':'い'}, {'u':'う'}, {'eh':'え'}, {'o':'お'}]
    kana1 = [{'ka':'か'}, {'ki':'き'}, {'ku':'く'}, {'ke':'け'}, {'ko':'こ'}]
    kana2 = [{'sa':'さ'}, {'shi':'し'}, {'su':'す'}, {'se':'せ'},{'so':'そ'}]
    kana3 = [{'ta':'た'}, {'chi':'ち'}, {'tsu':'つ'}, {'te':'て'}, {'to':'と'}]
    kana4 = [{'na':'な'}, {'ni':'に'}, {'nu':'ぬ'}, {'ne':'ね'}, {'no':'の'}]
    kana5 = [{'ha':'は'}, {'hi':'ひ'}, {'fu':'ふ'}, {'he':'へ'}, {'ho':'ほ'}]
    kana6 = [{'ma':'ま'}, {'mi':'み'}, {'mu':'む'}, {'me':'め'}, {'mo':'も'}]
    kana7 = [{'ya':'や'}, {'yu':'ゆ'}, {'yo':'よ'}]
    kana8 = [{'ra':'ら'}, {'ri':'り'}, {'ru':'る'}, {'re':'れ'}, {'ro':'ろ'}]
    kana9 = [{'wa':'わ'}, {'wo':'を'}, {'n':'ん'}]
    kana10 = [{'':''}, {'':''}, {'':''}, {'':''}, {'':''}]

    # List of lists of dictionaries, separated by their char groups
    hiragana = [kana0, kana1, kana2, kana3, kana4, kana5, kana6, kana7, kana8,
                kana9]

    return hiragana


#Function to create a dataset for Katakana characters
def kata():
# Tuples of dictionaries, key being pronunciation and value with character
    kata0 = [{'a':'ア'}, {'ii':'イ'}, {'u':'ウ'}, {'eh':'エ'}, {'o':'オ'}]
    kata1 = [{'ka':'カ'}, {'ki':'キ'}, {'ku':'ク'},{'ke':'ケ'}, {'ko':'コ'}]
    kata2 = [{'sa':'サ'}, {'shi':'シ'}, {'su':'ス'}, {'se':'セ'},{'so':'ソ'}]
    kata3 = [{'ta':'タ'}, {'chi':'チ'}, {'tsu':'ツ'}, {'te':'テ'}, {'to':'と'}]
    kata4 = [{'na':'ナ'}, {'ni':'ニ'}, {'nu':'ヌ'}, {'ne':'ネ'}, {'no':'ノ'}]
    kata5 = [{'ha':'ハ'}, {'hi':'ヒ'}, {'fu':'フ'}, {'he':'へ'}, {'ho':'ホ'}]
    kata6 = [{'ma':'マ'}, {'mi':'ミ'}, {'mu':'ム'}, {'me':'メ'}, {'mo':'モ'}]
    kata7 = [{'ya':'ヤ'}, {'yu':'ユ'}, {'yo':'ヨ'}]
    kata8 = [{'ra':'ラ'}, {'ri':'り'}, {'ru':'ル'}, {'re':'レ'}, {'ro':'ロ'}]
    kata9 = [{'wa':'ワ'}, {'wo':'ヲ'}, {'n':'ン'}]
    kata10 = [{'':''}, {'':''}, {'':''}, {'':''}, {'':''}]

    # List of tuples of dictionaries, seperated by their char groups
    katakana=[kata0, kata1, kata2, kata3, kata4, kata5, kata6, kata7, kata8,
                kata9]

    return katakana

def word_incr():
    words= [{0:'First'}, {1:'Second'}, {2:'Third'}, {3:'Fourth'},
        {4:'Fifth'}, {5:'Sixth'}, {6:'Seventh'}, {7:'Eighth'},
        {8:'Ninth'}, {9:'Tenth'}]

    return words

def shuffler(list):
    list = hira()
    groups = input("Enter an integer: ")
    if int(groups) == ValueError:
        print ('Input invalid, please try again.  Input must be an integer.')
        return None
    else:
        number = int(groups)
        if number > len(list):
            print ('Number must be less than', len(list))
            return None
        newlist= []
        for i in range(number):
            random.shuffle(list[i])
            newlist += list[i]
        random.shuffle(newlist)
        return newlist

def quiz(list):
    list = hira()
    newlist = shuffler(list)
    correct = 0
    incorrect = 0
    for i in range(len(newlist)):
        for key, value in newlist[i].items():
            answer = key
            question = value
            print (question)
            user = input('Match the character with its pronunciation: ')
            if user != answer:
                print('Incorrect')
                incorrect += 1
            else:
                print('Correct')
                correct += 1
    total = [{'correct': correct}, {'incorrect': incorrect}]
    print('Correct: ', correct)
    print('Incorrect: ', incorrect)
    return total

def main():

def katakana():
# Tuples of dictionaries, key being pronunciation and value with character
    kata0 = ({'a':'ア'}, {'ii':'イ'}, {'u':'ウ'}, {'eh':'エ'}, {'o':'オ'})
    kata1 = ({'ka':'カ'}, {'ki':'キ'}, {'ku':'ク'},{'ke':'ケ'}, {'ko':'コ'})
    kata2 = ({'sa':'サ'}, {'shi':'シ'}, {'su':'ス'}, {'se':'セ'},{'so':'ソ'})
    kata3 = ({'ta':'タ'}, {'chi':'チ'}, {'tsu':'ツ'}, {'te':'テ'}, {'to':'と'})
    kata4 = ({'na':'ナ'}, {'ni':'ニ'}, {'nu':'ヌ'}, {'ne':'ネ'}, {'no':'ノ'})
    kata5 = ({'ha':'ハ'}, {'hi':'ヒ'}, {'fu':'フ'}, {'he':'へ'}, {'ho':'ホ'})
    kata6 = ({'ma':'マ'}, {'mi':'ミ'}, {'mu':'ム'}, {'me':'メ'}, {'mo':'モ'})
    kata7 = ({'ya':'ヤ'}, {'yu':'ユ'}, {'yo':'ヨ'})
    kata8 = ({'ra':'ラ'}, {'ri':'り'}, {'ru':'ル'}, {'re':'レ'}, {'ro':'ロ'})
    kata9 = ({'wa':'ワ'}, {'wo':'ヲ'}, {'n':'ン'})
    kata10 = ({'':''}, {'':''}, {'':''}, {'':''}, {'':''})

    # List of tuples of dictionaries, seperated by their char groups
    katakana=[kata0, kata1, kata2, kata3, kata4, kata5, kata6, kata7, kata8,
                kata9]

    return katakana
main()

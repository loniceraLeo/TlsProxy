''' TlsProxy.utils.padding '''

from TlsProxy.utils import padding

def padding_test():
    results = []
    try:
        results.extend([
            padding(b'                 <blank-url>                  ', 256),
            padding(b'abcdefyoutubeghijklmnopqrstwitteruvwxyz.abcdefghijklmn\
                    opqrstuvwxyoutubez.abcdefacebookghijklmnopixivqredditu\
                    vwxyz.com', 256),
            padding(b'wwwa.youtubea.coma', 256),
            padding(b'aaaaaaaaaa.twitter.coommm', 256),
            padding(b'iiiiiiiiiiiiii.vvvvvvv.cdefghi', 256),
            padding(b'there-is-always-a-hope-if-u-never-give-up.faith', 256),
            padding(b'abcdefghijklmnopqrstuvwxyz.none.tao.use', 256),
            padding(b'www.google.com', 256),
            padding(b'no-mercy.sometimes-naive.com.cn', 256)
        ])
    except:
        pass

    print(results[0])

if __name__ == '__main__':
    padding_test()

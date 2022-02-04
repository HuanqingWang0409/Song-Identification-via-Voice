import os
import pymysql
import play_audio

class memory():
    def __init__(self, host, port, user, passwd, db):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.db = db

    def addsong(self, path):
        if type(path) != str:
            raise TypeError('Path needs string')

        basename = os.path.basename(path)
        try:
            conn = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.db,
                                   charset='utf8')
        except:
            print('DataBase error')
            return None
        cur = conn.cursor()
        namecount = cur.execute("select * from fingerprint.musicdata WHERE song_name = '%s'" % basename)
        if namecount > 0:
            print ('A song has been recorded! Path: ' + path)
            return None
        v = play_audio.voice()
        v.loaddata(path)
        v.fft()
        cur.execute("insert into fingerprint.musicdata VALUES('%s','%s')" % (basename, v.high_point.__str__()))
        conn.commit()
        cur.close()
        conn.close()


    def fp_compare(self, search_fp, match_fp):
        if len(search_fp) > len(match_fp):
            return 0
        max_similar = 0
        search_fp_len = len(search_fp)
        match_fp_len = len(match_fp)
        for i in range(match_fp_len - search_fp_len):
            temp = 0
            for j in range(search_fp_len):
                if match_fp[i + j] == search_fp[j]:
                    temp += 1
            if temp > max_similar:
                max_similar = temp
        return max_similar

    def search(self, path):
        v = play_audio.voice()
        v.loaddata(path)
        v.fft()
        try:
            conn = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.db,
                                   charset='utf8')
        except:
            raise IOError('DataBase error')
        cur = conn.cursor()
        cur.execute("SELECT * FROM fingerprint.musicdata")
        result = cur.fetchall()
        compare_res = []
        for i in result:
            compare_res.append((self.fp_compare(v.high_point[:-1], eval(i[1])), i[0]))
        compare_res.sort(reverse=True)
        cur.close()
        conn.close()
        print (compare_res)
        return compare_res

    def search_and_play(self, path):
        v = play_audio.voice()
        v.loaddata(path)
        v.fft()
        try:
            conn = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.db,
                                   charset='utf8')
        except:
            print ('DataBase error')
            return None
        cur = conn.cursor()
        cur.execute("SELECT * FROM fingerprint.musicdata")
        result = cur.fetchall()
        compare_res = []
        for i in result:
            compare_res.append((self.fp_compare(v.high_point[:-1], eval(i[1])), i[0]))
        compare_res.sort(reverse=True)
        cur.close()
        conn.close()
        print ("The matching result is as follow, and the numbers represent similarity.")
        print (compare_res)
        v.play(compare_res[0][1])
        return compare_res


if __name__ == '__main__':
    sss = memory('localhost', 3306, 'root', 'William990409@', None)
    #sss.addsong('right here waiting.wav')
    sss.addsong('With An Orchid.wav')
    #sss.addsong('QiLiXiang.wav')
    #sss.addsong('Scarborough Fair.wav')
    sss.addsong('lemon tree.wav')

    sss.search_and_play('record.wav')
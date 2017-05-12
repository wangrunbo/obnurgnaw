import pymysql


class Roster:
    """名单"""
    def __init__(self, sig):
        self.sig = sig

    def save(self):
        vd = pymysql.connect('localhost', 'root', '123456', 'Universe')
        cursor = vd.cursor()

        i = 'INSERT INTO roster (name, cdt) VALUES ("%s", "%s")' % (self.sig.name, id(self.sig))

        try:
            cursor.execute(i)
            vd.commit()
        except:
            vd.rollback()
        finally:
            vd.close()

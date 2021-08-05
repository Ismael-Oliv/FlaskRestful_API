import datetime
import jwt


class Jwt_Genator:

    @staticmethod
    def generator(self):
        key = "54as6d4ad6545dasd5as0da6s4d"
        pay_load = {"exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=30)}
        enconde = jwt.encode(pay_load, key=key, algorithm="HS256")

        return enconde

    def verify(self):
        pass
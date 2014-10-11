#!/usr/bin/env python
# coding:utf-8
from model.db import Doc
from model.re_mail import RE_MAIL
from os import urandom
from hashlib import sha512
from base64 import b64encode


class Password(Doc):

    structure = dict(
        mail=str,
        hash=str,
        _salt=int,
    )

    @classmethod
    def mail_verify(cls, mail):
        return RE_MAIL.match(mail)

    @classmethod
    def new(cls, mail, password, salt=None):
        salt = salt or b64encode(urandom(64))
        o = Password.find_one(dict(mail=mail), create_new=True)
        o._salt = salt

        h = sha512(salt)
        h.update(str(password))
        h.update(str(mail))
        o.hash = b64encode(h.digest())
        o.save()

    @classmethod
    def verify(cls, mail, password):
        o = Password.find_one(dict(mail=mail))
        if o:
            h = sha512(o._salt)
            h.update(str(password))
            h.update(str(mail))

            return o.hash == b64encode(h.digest())

        return False

if __name__ == '__main__':
    Password.new('kzing@gmail.com', '12345678')
    print(Password.verify('kzing@gmail.com', '12345678'))

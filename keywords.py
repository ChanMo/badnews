#!/usr/bin/env python

import sqlite3


def get_keywords():
    cxn = sqlite3.connect('yuqing.db')
    cur = cxn.cursor()
    cur.execute('select id,name,keywords from user where is_enabled=1')
    keywords = cur.fetchall()
    cur.close()
    cxn.commit()
    cxn.close()
    return keywords

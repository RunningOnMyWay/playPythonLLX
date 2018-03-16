#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-3-13 下午1:10
# @Author  : lilixiang
# @Site    : 
# @File    : Magic8Ball.py
# @Software: PyCharm Community Edition

import random

Messages = ['AS I SEE IT YES','ASK AGAIN LATER','BETTER NOT TELL YOU NOW','CANNOT PREDICT NOW','CONCENTRATE AND ASK AGAIN','DON\'T COUNT ON IT',
            'IT IS CERTAIN','IT IS DECIDEDLY SO','MOST LIKELY','MY SOURCES SAY NO','MY REPLY IS NO','OUTLOOK NOT SO GOOD','OUTLOOK GOOD',
            'REPLY HAZY TRY AGAIN','SIGNS POINT TO YES','VERY DOUBTFUL','WITHOUT A DOUBT','YSE','YES DEFINITELY','YOU MAY RELY ON IT']
def M8ball():
    ind = random.randint(0,len(Messages)-1)
    return str(ind)+":"+Messages[ind]


# print(M8ball())

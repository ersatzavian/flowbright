# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from keen.client import KeenClient
import json
from dateutil.parser import *

client = KeenClient(
    project_id="50ba759d897a2c45c2000000",
    write_key="72a1ad85456fd2361cfe8b65d240eab16b083caa944c11d9507761e536d34822eca4cefad12e482373ee41278953f98c6ff724b33b56fd5971e8d34cdd284cb6c3f202d9f13329e39c01eb9a35d1124cae81d9a4505992fce03be4030e32b19c72df266c55a18937f001e7158f6eac44",
    read_key="f7a829ecc9e237949b0b97245c828661ff0c9f46eaec35a7dc4cfd3b4ef42804f5fc1859ecad05bd7d72b6c3a2e4047ae39cba86b5d51c770be26b0a406cbb44650d20fd05fb7896293f015cec3af3ca2df8a507927bf4cfed9275eb89e8dee855cf45db75b221074bda2f737d2810f2"
)


# <codecell>

import datetime

# <codecell>

current = datetime.datetime.now()

# <codecell>

from dateutil.relativedelta import *

# <codecell>

two_week = relativedelta(weeks=2)
minute = relativedelta(minutes=1)
one_hour = relativedelta(hours=1)

# <codecell>

start = current - relativedelta(weeks=1)
stop = current

# <codecell>

import random

# <codecell>

def day(d):
    return "weekday" if d.weekday() < 5 else "weekend"

def hour(d):
    if d.hour < 8:
        return "night"
    elif d.hour < 18:
        return "work"
    else:
        return "home"

model = {
         "weekday": {
                         "night": 4,
                         "work": 2,
                         "home": 10
                     },
         "weekend" : {
                          "night": 8,
                          "work": 10,
                          "home": 10                    
                      }
}

def random_use(d):
    a = model[day(d)][hour(d)]
    b = random.randrange(int(a - 0.2 * a), int(a + 0.2 * a)) + random.random()
    return b - (0.1 * b)
    

# <codecell>

cur  = start
while cur < stop:
    use = random_use(cur)
    data = {"keen": {"timestamp": cur.isoformat()}, "device": "230c51eb6e4936ee", "volume": use}
    client.add_event("flow", data)
    cur = cur + one_hour

# <codecell>

stop.isoformat()

# <codecell>



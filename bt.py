from math import *


class Subject:
    def __init__(self, id, name, form):
        self.id = id
        self.name = name
        self.form = form

    def __str__(self):
        return self.name


class Time:
    def __init__(self, id, date, time, roomId):
        self.id = "C{:03d}".format(id)
        # print(self.id)
        self.date = date
        self.time = time
        self.roomId = roomId

    def getDate(self):
        return self.date

    def getTime(self):
        return self.time

    def getId(self):
        return self.id

    def __str__(self):
        return self.date + " " + self.time + " " + self.roomId


class TimeLine:
    def __init__(self, time, sub, gr, NOS):
        self.sub = sub
        self.time = time
        self.gr = str(gr)
        self.NOS = str(NOS)
        # print(self.sub)

    def __str__(self):
        return str(self.time) + " "+str(self.sub) + " " + self.gr+" " + self.NOS


if _name_ == "_main_":
    ip = open("MONTHI.in")
    n = int(ip.readline().strip())
    subs = []
    for i in range(n):
        subs.append(Subject(ip.readline().strip(),
                    ip.readline().strip(), ip.readline().strip()))
    ip.close()
    ip = open("CATHI.in", "r")
    m = int(ip.readline().strip())
    times = []
    for i in range(m):
        times.append(Time(i+1, ip.readline().strip(),
                     ip.readline().strip(), ip.readline().strip()))
    ip.close()
    ip = open("LICHTHI.in", "r")
    k = int(ip.readline().strip())
    timeline = []
    for i in range(k):
        tmp0, tmp1, gr, NOS = map(str, ip.readline().strip().split())
        tmpsub = Subject("", "", "")
        for j in subs:
            if j.id == tmp1:
                tmpsub = j
                break
        tmptime = Time(0, "", "", "")
        for j in times:
            if j.id == tmp0:
                tmptime = j
                break
        timeline.append(TimeLine(tmptime, tmpsub, gr, NOS))
    timeline = sorted(timeline, key=lambda x: (
        x.time.date, x.time.time, x.time.id))
    for i in timeline:
        print(i)
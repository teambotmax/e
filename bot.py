# -*- coding: utf-8 -*-
import linepy
from linepy import *
from soheil.ttypes import *
from thrift.TMultiplexedProcessor import *
from thrift.TSerialization import *
from thrift.TRecursive import *
from thrift import transport, protocol, server
from datetime import datetime
import pytz, pafy, time, asyncio, random, multiprocessing, timeit, sys, json, ctypes, codecs, tweepy, threading, glob, re, ast, six, os, subprocess, wikipedia, atexit, goslate, urllib, urllib.parse, urllib3, string, tempfile, shutil, unicodedata
from humanfriendly import format_timespan, format_size, format_number, format_length
import html5lib
import requests,json,urllib3
from random import randint
from bs4 import BeautifulSoup
from time import sleep
#=============================
#Login Method
soheil = LINE()
#soheil = LINE("authtoken")
#soheil = LINE("email","Password")
#soheil.log("Auth Token : " + str(soheil.authToken))
print ("=== LOGIN SUCCES ===")
#=============================
oepoll = OEPoll(soheil)
mid = soheil.getProfile().mid
Me = [mid,"ubb8d2595fcc42104153f67a53eb35d78","ufe1707ae9b2ff7ab61505795b7995440"]
msg_dict = {}
msg_dict1 = {}
sue = codecs.open("SCwait.json","r","utf-8")
SCwait = json.load(sue)
mulai = time.time()
settings = {
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ]
}
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                soheil.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]
def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d روز %02d ساعت %02d دقیقه %02d ثانیه' % (days, hours, mins, secs)
tz = pytz.timezone("Asia/Tehran")
timeNow = datetime.now(tz=tz)
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%ᶠᵇᵏJam:%ᶠᵇᵏMenit:%ᶠᵇᵏDetik')
def logError(text):
    soheil.log("[ ERROR ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Tehran")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("SCdataERROR.txt","a") as error:
        error.write("\n[ {} ] {}".format(str(time), text))
def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,3,1)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = soheil.getAllContactIds()
        gid = soheil.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Tehran")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"jam : "+datetime.strftime(timeNow,'%Jam:%Menit:%Detik')+" wib\nNama Group : "+str(len(gid))+"\nTeman : "+str(len(teman))+"\nExpired : In "+hari+"\n Version :ᶠᵇᵏ࿐  \nTanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\nRuntime : \n • "+bot
        soheil.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        soheil.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def command(text):
    pesan = text.lower()
    if pesan.startswith(SCwait["keyCmd"]):
        cmd = pesan.replace(SCwait["keyCmd"],"")
    else:
        cmd = "command"
    return cmd
def help():
    key = SCwait["keyCmd"]
    key = key.title()
    helpMessage = "=====[دستورات ربات]=====\n" + \
                  "1. " + key + "Me\n" + \
                  "2. " + key + "Autoblock on/off\n" + \
                  "3. " + key + "Autoreject on/off\n" + \
                  "4. " + key + "Autoleave on/off\n" + \
                  "5. " + key + "Reject\n" + \
                  "6. " + key + "Rchat\n" + \
                  "7. " + key + "test\n" + \
				  "8. " + key + "gift\n" + \
				  "9. " + key + "runtime\n" + \
				  "10. " + key + "status\n" + \
                  "\n=====[ترجمع به فارسی]=====\n \n1.اکانت منو اینفو کن\n2.فعال کردن اتو بلاک\n3.کنسل شدن اتوماتیک اتو\n4.از چت اجباری لفت بده یا خیر\n5.کنسل کردن اتو ها\n6.پاک کردن تمامی چت ها \n7.نشون دهنده فعال بودن بات\n8.ارسال گیفت فیک\n9.تایم فعال بودن ربات \n10.وضعیت فعال بودن سرویس ها\n\n " + \
				  "==[راهنمای استفاده از دستورات]==\n\n برای مثال اگر میخواهید اتو بلاک رو فعال کنید طبق دستور بالا مینویسیم (Autoblock on)  حالا بخوایم اتو بلاک رو خاموش کنیم (on) اخر دستور رو تبدیل میکنیم به (off) به این صورت  Autoblock off"
    return helpMessage
def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 13:
            if mid in op.param3:
                if SCwait["autoReject"] == True:
                    if op.param2 not in mid and op.param2 not in Me:
                        soheil.rejectGroupInvitation(op.param1)
                    else:
                        soheil.rejectGroupInvitation(op.param1)
        if op.type == 13:
            if mid in op.param3:
                if SCwait["autoLeave"] == True:
                    if op.param2 not in mid and op.param2 not in Me:
                        soheil.acceptGroupInvitation(op.param1)
                        ginfo = soheil.getGroup(op.param1)
                        soheil.sendMessage(op.param1,"گروه ضایعات زباله وجود ندارد. " +str(ginfo.name))
                        soheil.leaveGroup(op.param1)
                    else:
                        soheil.acceptGroupInvitation(op.param1)
                        ginfo = soheil.getGroup(op.param1)
                        soheil.sendMessage(op.param1,"Hai " + str(ginfo.name))		
        if op.type == 5:
            print ("[ 5 ] NOTIFIED AUTO BLOCK CONTACT")
            if SCwait["autoBlock"] == True:
              if op.param2 not in Me and op.param2 not in mid:
                soheil.blockContact(op.param1)
  #              soheil.sendMessage(op.param1, "ببخشید اتوبلاک رو اکانت من فعاله \n و سیستم به صورت اتوماتیک شما رو بلاک کرد الان")
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 0:
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        setKey = SCwait["keyCmd"].title()
                        if cmd == "help":
                          if SCwait["selfbot"] == True:
                            if msg._from in Me and mid:
                               helpMessage = help()
                               soheil.sendMessage(msg.to, "\n"+str(helpMessage))
                        elif cmd == "runtime":
                          if SCwait["selfbot"] == True:
                            if msg._from in Me:
                               eltime = time.time() - mulai
                               bot = "زمان روشن بودن ربات\n" +runtime(eltime)
                               soheil.sendMessage(msg.to,bot)
                        elif cmd == "reject":
                          if SCwait["selfbot"] == True:
                            if msg._from in Me:
                              ginvited = soheil.getGroupIdsInvited()
                              if ginvited != [] and ginvited != None:
                                  for gid in ginvited:
                                      time.sleep(4)
                                      soheil.rejectGroupInvitation(gid)
                                  soheil.sendMessage(msg.to, " {} عدد گروه دیس شد😁".format(str(len(ginvited))))
                              else:
                                  soheil.sendMessage(msg.to, "گروهی نداری که بخوای دیس بشه 😐")
                        elif cmd == 'gift':
                          if SCwait["selfbot"] == True:
                            if msg._from in Me and Me:
                               soheil.generateReplyMessage(msg.id)
                               soheil.sendReplyMessage(msg.id, to, text=None, contentMetadata={'PRDID': 'b7e5309a-5c4c-4833-a3c3-91faa74de971','PRDTYPE': 'THEME','MSGTPL': '5'}, contentType=9)							   
                        elif cmd == "autoreject on":
                          if SCwait["selfbot"] == True:
                            if msg._from in Me:
                                SCwait["autoReject"] = True
                                soheil.sendMessage(msg.to, "「  وضعیت کنسل کردن اتوماتیک گروه ها 」\n\nفعال  است")
                        elif cmd == "autoreject off":
                          if SCwait["selfbot"] == True:
                            if msg._from in Me:
                                SCwait["autoReject"] = False
                                soheil.sendMessage(msg.to, "「  وضعیت کنسل کردن اتوماتیک گروه ها 」\n\n غیر فعال است")
                        elif cmd == "autoblock on":
                          if SCwait["selfbot"] == True:
                            if msg._from in Me:
                                SCwait["autoBlock"] = True
                                soheil.sendMessage(msg.to, "「  وضعیت اتو بلاک 」\n\nاتو بلاک فعال شد")
                        elif cmd == "autoblock off":
                          if SCwait["selfbot"] == True:
                            if msg._from in Me:
                                SCwait["autoBlock"] = False
                                soheil.sendMessage(msg.to, "「  وضعیت اتو بلاک 」\n\nاتوبلاک غیر فعال شد")
                        elif cmd == "autoleave on":
                          if SCwait["selfbot"] == True:
                            if msg._from in Me:
                                SCwait["autoLeave"] = True
                                soheil.sendMessage(msg.to, "「  وضعیت خروج از چت 」\n\nخروج از چت فعال است")
                        elif cmd == "autoleave off":
                          if SCwait["selfbot"] == True:
                            if msg._from in Me:
                                SCwait["autoLeave"] = False
                                soheil.sendMessage(msg.to, "「  وضعیت خروج از چت 」\n\nخروج از چت غیر فعال شد")
                        elif text.lower() == "rchat":
                          if SCwait["selfbot"] == True:
                            if msg._from in Me:
                               try:
                                   soheil.removeAllMessages(op.param2)
                                   soheil.sendMessage(msg.to,"انجام شد...")
                               except:
                                   soheil.removeAllMessages(op.param2)
                                   soheil.sendMessage(msg.to,"انجام شد...")
                        elif cmd == "me":
                          if SCwait["selfbot"] == True:
                            if msg._from in Me:
                                soheil.sendContact(to,sender);soheil.sendMessageMusic(to, title=soheil.getContact(sender).displayName, subText=str(soheil.getContact(sender).statusMessage), url='line.me/ti/p/~soheil.developer', iconurl="http://dl.profile.line-cdn.net/{}".format(soheil.getContact(sender).pictureStatus), contentMetadata={})
                        elif cmd == "test":
                          if SCwait["selfbot"] == True:
                            if msg._from in modir:
                                soheil.sendMessage(msg.to,"خیالت راحت من هستم و مراقب اکانتتم")   
                        elif cmd == "status":
                          if SCwait["selfbot"] == True:
                            if msg._from in Me:
                                md = " ==[وضعیت ها]==\n\n"
                                if SCwait["autoLeave"] == True: md+="[روشن] لفت خودکار\n"
                                else: md+="[خاموش] لفت خودکار\n"
                                if SCwait["autoReject"] == True: md+="[روشن] دیس اتوماتیک اتو\n"
                                else: md+="[خاموش] دیس اتوماتیک اتو\n"
                                if SCwait["autoBlock"] == True: md+="[روشن] بلاک خودکار\n"
                                else: md+="[خاموش] بلاک خودکار\n"
                                soheil.sendMessage(msg.to, md+"\n====[Soheil STAR]==== ")
    except Exception as error:
        print (error)

while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                oepoll.setRevision(op.revision)
                thread = threading.Thread(target=bot, args=(op,))
                thread.start()
    except Exception as e:
        print(e)

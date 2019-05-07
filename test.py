
# -*- coding: utf-8 -*-
# Source Code : NoobLess Team #
# Arfine Meka.
# 
# -*- coding: utf-8 -*-
# ------------------------ IMPORT ------------------------ #

import time, random, sys, json, codecs, glob, urllib, pytz, ast, os, multiprocessing, subprocess, tempfile, string, six, urllib.parse, traceback, atexit, html5lib, re, wikipedia, ntpath, threading, base64, shutil, humanize, service, os.path, youtube_dl, requests
import urllib3
urllib3.disable_warnings()
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ------------------------ IMPORT ------------------------ #
from LineAPI.linepy import *
from liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
from LineAPI.akad import ChannelService,TalkService
from LineAPI.akad.ttypes import Message, Location, LoginRequest, ChatRoomAnnouncementContents, ContentType as Type
from thrift.protocol import TCompactProtocol, TBinaryProtocol, TProtocol
from thrift.transport import THttpClient, TTransport
from thrift.Thrift import TProcessor
from multiprocessing import Pool, Process
from multiprocessing.dummy import Pool as ThreadPool
from threading import Thread, activeCount
from time import sleep
from datetime import datetime, timedelta
from humanfriendly import format_timespan, format_size, format_number, format_length
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# ------------------------ LOGIN ------------------------ #
programStart = time.time()
client = LINE('',appName='WIN10\t5.5.5\tHelloWorld5.5.5')
client.log("Auth Token : " + str(client.authToken))
client.log("Timeline Token : " + str(client.tl.channelAccessToken))
clientMid = client.profile.mid
clientProfile = client.getProfile()
clientSettings = client.getSettings()
mid = client.getProfile().mid
clientPoll = OEPoll(client)
botStart = time.time()
msg_send = {}
temp_flood = {}
tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)
creator = ['u3d817018a6ecad06c37242f0daa7c4df']
adminbots = ['u3d817018a6ecad06c37242f0daa7c4df']
superz = creator + adminbots
with open('by.json', 'r') as fp:
    wait = json.load(fp)
settings ={"keyCommand":"","setKey":False}

xxxs = {
    "clock":True,
    "cName":"I'm Botlogin V8 ",
    }

def tokenchrome():
    Headers = {
    'User-Agent': "Line/2.1.5",
    'X-Line-Application': "CHROMEOS\t2.1.5\tlognselfbot\t12.1.1",
    "x-lal": "ja-US_US",
    }
    return Headers
    
def tokenwin():
    Headers = {
    'User-Agent': "Line/8.9.1",
    'X-Line-Application': "DESKTOPWIN\t5.8.0\tlognselfbot\t5.8.0",
    "x-lal": "ja-US_US",
    }
    return Headers

def headersios():
    Headers = {
    'User-Agent': "Line/8.9.1",
    'X-Line-Application': "IOSIPAD\t8.9.1\tlognselfbot\t12.1.1",
    "x-lal": "ja-US_US",
    }
    return Headers
    
def headerschrome():
    Headers1 = {
    'User-Agent': "Line/2.1.5",
    'X-Line-Application': "CHROMEOS\t2.1.5\tlognselfbot\t2.1.5",
    "x-lal": "ja-US_US",
    }
    return Headers1
    
def headerswin():
    Headers2 = {
    'User-Agent': "Line/5.8.0",
    'X-Line-Application': "DESKTOPWIN\t5.8.0\tlognselfbot\t5.8.0",
    "x-lal": "ja-US_US",
    }
    return Headers2
    
def headersmac():
    Headers3 = {
    'User-Agent': "Line/5.1.2",
    'X-Line-Application': "DESKTOPMAC\t5.1.2\tlognselfbot\t5.1.2",
    "x-lal": "ja-US_US",
    }
    return Headers3
    
def headerswin10():
    Headers4 = {
    'User-Agent': "Line/5.5.5",
    'X-Line-Application': "WIN10\t5.5.5\tlognselfbot\t5.5.5",
    "x-lal": "ja-US_US",
    }
    return Headers4

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d วัน %02d ชั่วโมง %02d นาที %02d วินาที' % (days, hours, mins, secs)

def restartBot():
    print ("[ INFO ] BOT RESTART")
    python = sys.executable
    os.execl(python, python, *sys.argv)
        
def backupData():
    try:
        backup = wait
        f = codecs.open('by.json','w','utf-8')
        json.dump(wait, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except:
        e = traceback.format_exc()
        client.sendMessage("u3d817018a6ecad06c37242f0daa7c4df",str(e))
        return False

def sendMention(to, text="", mids=[]):
        arrData = ""
        arr = []
        mention = "@Arfinee Meka "
        if mids == []:
            raise Exception("Invalid mids")
        if "@!" in text:
            if text.count("@!") != len(mids):
                raise Exception("Invalid mids")
            texts = text.split("@!")
            textx = ''
            h = ''
            for mid in range(len(mids)):
                h+= str(texts[mid].encode('unicode-escape'))
                textx += str(texts[mid])
                if h != textx:slen = len(textx)+h.count('U0');elen = len(textx)+h.count('U0') + 13
                else:slen = len(textx);elen = len(textx) + 13
                arrData = {'S':str(slen), 'E':str(elen), 'M':mids[mid]}
                arr.append(arrData)
                textx += mention
            textx += str(texts[len(mids)])
        else:
            textx = ''
            slen = len(textx)
            elen = len(textx) + 18
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
            arr.append(arrData)
            textx += mention + str(text)
        client.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
        
def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd
    
def menumessage():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    menuMessage =   "「 HELP LOGIN 」" + "\n\n" + \
                    "•  Renew >แอดมินสั่ง<" + "\n" + \
                    "•  ล็อคอิน " + "\n" + \
                    "•  ล็อคอิน2 [ถ้าล็อคอินตัวแรกอยู่ให้สั่ง ออกจากระบบ ก่อน]" + "\n" + \
                    "•  ล็อคอิน3 [ถ้าล็อคอินตัวสองอยู่ให้สั่ง ออกจากระบบ ก่อน]" + "\n" + \
                    "•  ต่ออายุ「 Tag 」 >แอดมินสั่ง<" + "\n" + \
                    "•  login@bye「 Nama 」 >แอดมินสั่ง<" + "\n" + \
                    "•  AddSB 「 Nama 」「 Tag 」 >แอดมินสั่ง<" + "\n" + \
                    "•  DelSB 「 Nama 」「 Tag 」 >แอดมินสั่ง<" + "\n" + \
                    "•  User >แอดมินสั่ง<" + "\n" + \
                    "•  ออกจากระบบ " + "\n\n" + \
                    "「 Bot login 」"
    return menuMessage
    
def clientBot(op):
    try:
        if op.type == 0:
            return   
                
        if op.type == 13:
            if op.param2 in superz:
                client.acceptGroupInvitation(op.param1)

        #if op.type in [22,24]:
         #   client.leaveRoom(op.param1)

        if op.type == 26:
            try:
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != client.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    if msg.toType == 1:
                        to = receiver
                    if msg.toType == 2:
                        to = receiver
                    if msg.contentType == 0:
                        if text is None:
                            pass
                        else:
                            cmd = command(text)
                            if text.lower().startswith('token '):
                              def telek():
                                c = msg.text.split(" ")[1]
                                anu = ['chrome','win','win10','mac','ios','cc']
                                if c in anu:
                                  if c == "chrome":
                                     hider = headerschrome()
                                     LA = 'CHROMEOS\t2.1.5\tlognselfbot\t2.1.5',
                                  if c == "ios" or c == "cc":
                                     hider = headersios()
                                     LA = "IOSIPAD\t8.9.1\tlognselfbot\t12.1.1"
                                  if c == "win":
                                     hider = headerswin()
                                     LA = "DESKTOPWIN\t5.8.0\tlognselfbot\t5.8.0"
                                  if c == "win10":
                                     hider = headerswin10()
                                     LA = "WIN10\t5.5.5\tlognselfbot\t5.5.5"
                                  if c == "mac":
                                     hider = headersmac()
                                     LA = "DESKTOPMAC\t5.8.0\tlognselfbot\t5.8.0"
                                  try:
                                    if not 'cc' in msg.text.lower():
                                      a = hider
                                      a.update({'x-lpqs' : '/api/v4/TalkService.do'})
                                      transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4/TalkService.do')
                                      transport.setCustomHeaders(a)
                                      protocol = TCompactProtocol.TCompactProtocol(transport)
                                      clients = service.Client(protocol)
                                      qr = clients.getAuthQrcode(keepLoggedIn=1, systemName='lognselfbot')
                                      link = "line://au/q/" + qr.verifier
                                      sendMention(to, "「 Hi @!  」" , [msg._from])
                                      sendMention(to, "「 Please Login @! 」\n{}".format(link), [msg._from])
                                      a.update({"x-lpqs" : '/api/v4/TalkService.do', 'X-Line-Access': qr.verifier})
                                      json.loads(requests.session().get('https://gd2.line.naver.jp/Q', headers=a).text)
                                      a.update({'x-lpqs' : '/api/v4p/rs'})
                                      transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4p/rs')
                                      transport.setCustomHeaders(a)
                                      protocol = TCompactProtocol.TCompactProtocol(transport)
                                      clients = service.Client(protocol)
                                      req = LoginRequest()
                                      req.type = 1
                                      req.verifier = qr.verifier
                                      req.e2eeVersion = 1
                                      res = clients.loginZ(req)
                                      nyoh = res.authToken
                                      hasil = "「 Result Login 」"
                                      hasil += "\n\nFrom : @!"
                                      hasil += "\n\nUA : Line/8.11.0"
                                      hasil += "\nLA  : {}".format(LA)
                                      hasil += "\n\nToken:\n"+str(nyoh)
                                      sendMention(to ,hasil, [msg._from])
                                    else:
                                      a = hider
                                      a.update({'x-lpqs' : '/api/v4/TalkService.do'})
                                      transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4/TalkService.do')
                                      transport.setCustomHeaders(a)
                                      protocol = TCompactProtocol.TCompactProtocol(transport)
                                      clients = service.Client(protocol)
                                      qr = clients.getAuthQrcode(keepLoggedIn=1, systemName='lognselfbot')
                                      link = "line://au/q/" + qr.verifier
                                      sendMention(to, "「 hi @!   」", [msg._from])
                                      sendMention(to, "「 Please Login @! 」\n{}".format(link), [msg._from])
                                      a.update({"x-lpqs" : '/api/v4/TalkService.do', 'X-Line-Access': qr.verifier})
                                      json.loads(requests.session().get('https://gd2.line.naver.jp/Q', headers=a).text)
                                      a.update({'x-lpqs' : '/api/v4p/rs'})
                                      transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4p/rs')
                                      transport.setCustomHeaders(a)
                                      protocol = TCompactProtocol.TCompactProtocol(transport)
                                      clients = service.Client(protocol)
                                      req = LoginRequest()
                                      req.type = 1
                                      req.verifier = qr.verifier
                                      req.e2eeVersion = 1
                                      res = clients.loginZ(req)
                                      nyoh = res.authToken
                                      headers = {
                                      'X-Line-Application': 'IOSIPAD\t8.9.1\tlognselfbot\t12.1.1',
                                      'X-Line-Access': res.authToken
                                       }
                                      transport = THttpClient.THttpClient('https://gd2.line.naver.jp/CH4')
                                      transport.setCustomHeaders(headers)
                                      protocol = TCompactProtocol.TCompactProtocol(transport)
                                      channel = ChannelService.Client(protocol)
                                      chantok = channel.approveChannelAndIssueChannelToken('1526709289').token
                                      hasil = "「 Result Login 」"
                                      hasil += "\n\nFrom : @!"
                                      hasil += "\n\nUA : Line/8.11.0"
                                      hasil += "\nLA  : {}".format(LA)
                                      hasil += "\n\nToken:\n"+str(nyoh)
                                      basil = chantok
                                      sendMention(to,hasil, [msg._from])
                                      sendMention(to,"Login From @!\nResult CC: {}".format(basil), [msg._from])
                                  except:
                                      sendMention(to," 「 Hi @!, กรุณากดที่ลิงค์เพื่อเข้าสู่ระบบ 」")
                                      pass
                              thread = threading.Thread(target=telek)
                              thread.daemon = True
                              thread.start()

                            if text.lower() == "." and sender in ['u3d817018a6ecad06c37242f0daa7c4df','u638d8d51472655d70b6c4655c35162f9']:
                                a = client.sendMessage(creator,"[]").createdTime
                                client.generateReplyMessage(msg.id)
                                client.sendReplyMessage(msg.id,to,"Fetchops: {}\nThreads: {}".format(a - msg.createdTime, threading.active_count()))

                            if text.lower().startswith('# ') and sender in ['u3d817018a6ecad06c37242f0daa7c4df','u638d8d51472655d70b6c4655c35162f9']:
                                a=subprocess.getoutput(client.mainsplit(msg.text))
                                k = len(a)//10000
                                for aa in range(k+1):
                                    try:
                                        client.generateReplyMessage(msg.id)
                                        client.sendReplyMessage(msg.id,to,'{}'.format(a.strip()[aa*10000 : (aa+1)*10000]))
                                    except:
                                        client.sendMessage(to, "Done")

##
#

                            if cmd == "เทสบอท":
                               _session = requests.session()
                               ratedit = LiffChatContext(to)
                               ratedit1 = LiffContext(chat=ratedit)
                               view = LiffViewRequest('1602687308-GXq4Vvk9', ratedit1)
                               token = client.liff.issueLiffView(view)
                               url = 'https://api.line.me/message/v3/share'
                               headers = {
                                   'Content-Type': 'application/json',
                                   'Authorization': 'Bearer %s' % token.accessToken
                       	       }
                               data = {
                                 "type": "flex",
                                 "altText": "help message",
                                 "contents": {
                                     "type": "carousel",
                                     "contents": [
                                          {
                                             "type": "bubble",
                                             "styles": {
                                                 "header": {"backgroundColor": "#000000"},
                                                 "footer": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#000000"}
                                             },
                                             "body": {
                                                 "type": "box",
                                                 "layout": "vertical",
                                                 "spacing": "md",
                                                 "action": {
                                                     "type": "uri",
                                                     "uri": "line://nv/profilePopup/mid=u3d817018a6ecad06c37242f0daa7c4df",
                                                     },
                                                 "contents": [
                                                     {
                                                         "type": "text",
                                                         "text": "Free Command :",
                                                         "size": "md",
                                                         "weight": "bold",
                                                         "align": "center",
                                                         "color": "#000000"
                                                     },
                                                     {
                                                         "type": "text",
                                                         "text": "1. Example Login",
                                                         "size": "xxs",
                                                         "align": "center",
                                                         "color": "#000000"
                                                     },
                                                     {
                                                         "type": "text",
                                                         "text": "2. Addfree <name>",
                                                         "size": "xxs",
                                                         "align": "center",
                                                         "color": "#000000"
                                                     },
                                                     {
                                                         "type": "text",
                                                         "text": "3. Login Free",
                                                         "size": "xxs",
                                                         "align": "center",
                                                         "color": "#000000"
                                                     },
                                                     {
                                                         "type": "text",
                                                         "text": "4. Logout Free",
                                                         "size": "xxs",
                                                         "align": "center",
                                                         "color": "#000000"
                                                     }
                                                ]
                                             },
                                             "footer": {
                                                 "type": "box",
                                                 "layout": "vertical",
                                                 "spacing": "sm",
                                                 "contents": [
                                                     {
                                                         "type": "box",
                                                         "layout": "baseline",
                                                         "contents": [
                                                             {
                                                                 "type": "icon",
                                                                 "url": "https://boteater.co/jpg-2rzb4yuq.jpg",
                                                                 "size": "md"
                                                             },
                                                             {
                                                                 "type": "text",
                                                                 "text": "Noob </> Coder",
                                                                 "align": "center",
                                                                 "color": "#FFFFFF",
                                                                 "size": "md"
                                                             },
                                                             {
                                                                 "type": "spacer",
                                                                 "size": "sm",
                                                             }
                                                         ]
                                                     }
                                                 ]
                                            }
                                         }
                                    ]
                                 }
                             }
                            data = json.dumps(data)
                            sendPost = _session.post(url, data=data, headers=headers)
##
#====================================================================================

                            if text.lower() == "renew" and sender in ['u3d817018a6ecad06c37242f0daa7c4df','u638d8d51472655d70b6c4655c35162f9']:
                                try:
                                    sam = {'MSG_SENDER_ICON': "https://os.line.naver.jp/os/p/"+sender,'MSG_SENDER_NAME':  client.getContact(sender).displayName,}                            
                                    client.sendMessage(to, "Update Library Done", contentMetadata=sam)
                                    restartBot()
                                except:
                                    e = traceback.format_exc()
                                    client.sendMessage("u3d817018a6ecad06c37242f0daa7c4df",str(e))

                            if text.lower().startswith('addsb ') and sender in ['u3d817018a6ecad06c37242f0daa7c4df','u638d8d51472655d70b6c4655c35162f9']:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    if key1 not in wait['info']:
                                        pay = time.time()
                                        nama = str(text.split(' ')[1])
                                        wait['name'][nama] =  {"mid":key1,"pay":pay+60*60*24*30,"runtime":pay,"token":{}}
                                        wait['info'][key1] =  '%s' % nama
                                        sendMention(msg.to, ' 「 Serivce 」\n@! เพิ่มผู้ใช้สำเร็จ\nอย่าลืมปิด letter sealing ในตั้งค่าความเป็นส่วนตัว',[key1])
                                    else:
                                        sendMention(msg.to, ' 「 Serivce 」\n@! บัญชีผู้ใช้นี้อยู่ในระบบแล้ว',[key1])

                            if text.lower().startswith('delsb') and sender in ['u3d817018a6ecad06c37242f0daa7c4df','u638d8d51472655d70b6c4655c35162f9']:
                                sep = text.split(" ")
                                query = text.replace(sep[0] + " ","")
                                aa = [a for a in wait['info']]
                                try:
                                    listContact = aa[int(query)-1]
                                    if listContact in wait['info']:
                                        b = wait['info'][listContact]
                                        os.system('screen -S %s -X kill'%b)
                                        try:subprocess.getoutput('rm -rf {}'.format(b))
                                        except:pass
                                        del wait['info'][listContact]
                                        del wait['name'][b]
                                        sendMention(to, ' 「 Serivce 」\n@! ลบรายชื่อนี้ออกจากระบบแล้ว', [listContact])
                                    else:
                                        sendMention(to, ' 「 Serivce 」\n@! ไม่พบรายชื่อนี้ในระบบ', [listContact])
                                except:pass

                            if text.lower().startswith('delsb ') and sender in ['u3d817018a6ecad06c37242f0daa7c4df','u638d8d51472655d70b6c4655c35162f9']:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    if key1 in wait['info']:
                                        b = wait['info'][key1]
                                        os.system('screen -S %s -X kill'%b)
                                        try:subprocess.getoutput('rm -rf {}'.format(b))
                                        except:pass
                                        del wait['info'][key1]
                                        del wait['name'][b]
                                        sendMention(to, ' 「 Service 」\n@! ทำการตัดรายชื่อนี้ออกจากระบบแล้ว',[key1])
                                    else:
                                        sendMention(to, ' 「 Serivce 」\n@! ไม่พบรายชื่อนี้ในระบบ', [key1])

                            if text.lower() == 'user' and sender in ['u3d817018a6ecad06c37242f0daa7c4df','u638d8d51472655d70b6c4655c35162f9']:
                                h = [a for a in wait['info']]
                                k = len(h)//20
                                for aa in range(k+1):
                                    if aa == 0:dd = '「 List Login 」';no=aa
                                    else:dd = '';no=aa*20
                                    msgas = dd
                                    for a in h[aa*20:(aa+1)*20]:
                                        no+=1
                                        if wait['name'][wait['info'][a]]["pay"] <= time.time():sd = 'หมดอายุ'
                                        else:sd = humanize.naturaltime(datetime.fromtimestamp(wait['name'][wait['info'][a]]["pay"]))
                                        if no == len(h):msgas+='\n{}. @! {}'.format(no,sd)
                                        else:msgas += '\n{}. @! {}'.format(no,sd)
                                    sendMention(to, msgas, h[aa*20:(aa+1)*20])

                            if text.lower() == 'killall':
                                if msg._from in ['u3d817018a6ecad06c37242f0daa7c4df','u638d8d51472655d70b6c4655c35162f9']:
                                    h = ''
                                    no=0
                                    for a in wait['info']:
                                        us = wait["info"][a]
                                        try:
                                            os.system('screen -S %s -X kill'%us)
                                        except:pass
                                    client.generateReplyMessage(msg.id)
                                    client.sendReplyMessage(msg.id,to,'Done Kill All Customer')

                            if text.lower() == "ออกจากระบบ":
                              if sender in wait['info']:
                                us = wait["info"][sender]
                                contact = client.getContact(sender)
                                os.system('screen -S {} -X quit'.format(us))
                                os.system('rm -rf {}'.format(us))
                                if msg.toType == 2:
                                    client.sendMessage(to, "Name: {}\nStatus: ทำการออกจากระบบแล้ว".format(contact.displayName))
                                else:
                                    sendMention(to, "「 แจ้งเตือน 」\nคุณได้ทำการออกจากระบบอยู่แล้ว @! ", [sender])
                              else:
                                sendMention(to, ' 「 เกิดข้อผิดพลาด 」\nHi @!\nไม่พบรายชื่อคุณในระบบ\nโปรดติดต่อแอดมิน @! ', [sender, "u3d817018a6ecad06c37242f0daa7c4df"])

                            if text.lower() == "ล็อคอิน":
                                client.generateReplyMessage(msg.id)
                                if sender in wait['info']:
                                        us = wait["info"][sender]
                                        ti = wait['name'][us]["pay"]-time.time()
                                        sec = int(ti %60)
                                        minu = int(ti/60%60)
                                        hours = int(ti/60/60 %24)
                                        days = int(ti/60/60/24)
                                        wait['name'][us]["pay"] = wait['name'][us]["pay"]
                                        if wait["name"][us]["pay"] <= time.time():
                                            os.system('rm -rf {}'.format(us))
                                            os.system('screen -S %s -X kill'%us)
                                            sendMention(to, ' 「 หมดอายุ 」\n Sorry @! บัญชีของคุณหมดเวลาใช้งานแล้วแล้ว', [sender])
                                        else:
                                            us = wait["info"][sender]
                                            try:
                                                def kentod():
                                                    a = headerswin10()
                                                    a.update({'x-lpqs' : '/api/v4/TalkService.do'})
                                                    transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4/TalkService.do')
                                                    transport.setCustomHeaders(a)
                                                    protocol = TCompactProtocol.TCompactProtocol(transport)
                                                    clients = service.Client(protocol)
                                                    qr = clients.getAuthQrcode(keepLoggedIn=1, systemName='BY MIN PYTHON')
                                                    sendMention(to,"「 Login 」\nUser: @!\nFile: {}".format(us,us), [sender])
                                                    _session = requests.session()
                                                    ratedit = LiffChatContext(to)
                                                    ratedit1 = LiffContext(chat=ratedit)
                                                    view = LiffViewRequest('1602687308-GXq4Vvk9', ratedit1)
                                                    token = client.liff.issueLiffView(view)
                                                    url = 'https://api.line.me/message/v3/share'
                                                    headers = {
                                                        'Content-Type': 'application/json',
                                                        'Authorization': 'Bearer %s' % token.accessToken
                                                    }
                                                    data = {"to": to,"messages": [{"type": "flex","altText": "LOGIN SELF BOT LINE","contents": {"type": "bubble","header": {"type": "box","layout": "vertical","contents": [{"type": "text","align": "center","color": "#0000FF","size": "xl","weight": "bold","text": "LOGIN SELFBOT"}]},"hero": {"type": "image","url": "https://boteater.co/storage-1554478095396cV0z8X4d.jpg","size": "full","aspectRatio": "20:20","aspectMode": "fit","action": {"type": "uri","uri": "line://au/q/{}".format(qr.verifier)}},"body": {"type": "box","layout": "vertical","contents": [{"type": "text","align": "center","color":"#0000FF","text": "กรุณากดที่รูปภาพภายใน 2 นาที","wrap": True}]}}}]}
                                                    data = json.dumps(data)
                                                    sendPost = _session.post(url, data=data, headers=headers)     
                                                    a.update({"x-lpqs" : '/api/v4/TalkService.do', 'X-Line-Access': qr.verifier})
                                                    json.loads(requests.session().get('https://gd2.line.naver.jp/Q', headers=a).text)
                                                    a.update({'x-lpqs' : '/api/v4p/rs'})
                                                    transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4p/rs')
                                                    transport.setCustomHeaders(a)
                                                    protocol = TCompactProtocol.TCompactProtocol(transport)
                                                    clients = service.Client(protocol)
                                                    req = LoginRequest()
                                                    req.type = 1
                                                    req.verifier = qr.verifier
                                                    req.e2eeVersion = 1
                                                    res = clients.loginZ(req)
                                                    wait['name'][us]["token"] = res.authToken
                                                    token = wait['name'][us]["token"]
                                                    os.system('screen -S %s -X kill'%us)
                                                    os.system('cp -r free {}'.format(us))
                                                    os.system('cd {} && echo -n "{} \c" > token.txt'.format(us, token))
                                                    os.system('screen -dmS {}'.format(us))
                                                    os.system('screen -r {} -X stuff "cd {} && python3 freem.py \n"'.format(us, us))
                                                    contact = client.getContact(sender)
                                                    sendMention(to, "「 Done! 」\nName: {}\nMid: {}\nเวลาคงเหลือ: {} วัน {} ชั่วโมง {} นาที \nSuccess login user @! \n> กรุณากดลิ้งด้านล่างด้วย(กดแค่ครั้งแรกพอ) :\nline://app/1602687308-GXq4Vvk9?type=text&text=Ez".format(us,sender,days,hours,minu), [sender])
                                                thread = threading.Thread(target=kentod)
                                                thread.daemon = True
                                                thread.start()
                                            except:
                                                pass
                                else:
                                    sendMention(to, ' 「 Error 」\nHi @!\nไม่พบรายชื่อคุณในระบบ\nโปรดติดต่อแอดมิน @! ', [sender, "u3d817018a6ecad06c37242f0daa7c4df"])

                            if text.lower() == "ล็อคอิน3":
                                client.generateReplyMessage(msg.id)
                                if sender in wait['info']:
                                        us = wait["info"][sender]
                                        ti = wait['name'][us]["pay"]-time.time()
                                        sec = int(ti %60)
                                        minu = int(ti/60%60)
                                        hours = int(ti/60/60 %24)
                                        days = int(ti/60/60/24)
                                        wait['name'][us]["pay"] = wait['name'][us]["pay"]
                                        if wait["name"][us]["pay"] <= time.time():
                                            os.system('rm -rf {}'.format(us))
                                            os.system('screen -S %s -X kill'%us)
                                            sendMention(to, ' 「 หมดอายุ 」\n Sorry @! บัญชีของคุณหมดเวลาใช้งานแล้วแล้ว', [sender])
                                        else:
                                            us = wait["info"][sender]
                                            try:
                                                def kentod():
                                                    a = headerswin10()
                                                    a.update({'x-lpqs' : '/api/v4/TalkService.do'})
                                                    transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4/TalkService.do')
                                                    transport.setCustomHeaders(a)
                                                    protocol = TCompactProtocol.TCompactProtocol(transport)
                                                    clients = service.Client(protocol)
                                                    qr = clients.getAuthQrcode(keepLoggedIn=1, systemName='NODEJS_ANTISPAM')
                                                    sendMention(to,"「 Login 」\nUser: @!\nFile: {}\nกรุณากดลิ้งภายใน2นาที".format(us,us), [sender])
                                                    _session = requests.session()
                                                    ratedit = LiffChatContext(to)
                                                    ratedit1 = LiffContext(chat=ratedit)
                                                    view = LiffViewRequest('1602687308-GXq4Vvk9', ratedit1)
                                                    token = client.liff.issueLiffView(view)
                                                    url = 'https://api.line.me/message/v3/share'
                                                    headers = {
                                                        'Content-Type': 'application/json',
                                                        'Authorization': 'Bearer %s' % token.accessToken
                                                    }
                                                    data = {"to": to,"messages": [{"type": "flex","altText": "LOGIN SELF BOT LINE","contents": {"type": "bubble","header": {"type": "box","layout": "vertical","contents": [{"type": "text","align": "center","color": "#000000","size": "xl","weight": "bold","text": "LOGIN SELFBOT"}]},"hero": {"type": "image","url": "https://t3.ftcdn.net/jpg/00/63/74/62/240_F_63746248_ikHL5mQRmKXeWumLZk7ABJ9PT80VXjW5.jpg","size": "full","aspectRatio": "20:13","aspectMode": "fit","action": {"type": "uri","uri": "line://au/q/{}".format(qr.verifier)}},"body": {"type": "box","layout": "vertical","contents": [{"type": "text","align": "center","text": "กรุณากดที่รูปภาพภายใน 2 นาที","wrap": True}]}}}]}
                                                    data = json.dumps(data)
                                                    sendPost = _session.post(url, data=data, headers=headers)     
                                                    a.update({"x-lpqs" : '/api/v4/TalkService.do', 'X-Line-Access': qr.verifier})
                                                    json.loads(requests.session().get('https://gd2.line.naver.jp/Q', headers=a).text)
                                                    a.update({'x-lpqs' : '/api/v4p/rs'})
                                                    transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4p/rs')
                                                    transport.setCustomHeaders(a)
                                                    protocol = TCompactProtocol.TCompactProtocol(transport)
                                                    clients = service.Client(protocol)
                                                    req = LoginRequest()
                                                    req.type = 1
                                                    req.verifier = qr.verifier
                                                    req.e2eeVersion = 1
                                                    res = clients.loginZ(req)
                                                    wait['name'][us]["token"] = res.authToken
                                                    token = wait['name'][us]["token"]
                                                    os.system('screen -S %s -X kill'%us)
                                                    os.system('cp -r nobb {}'.format(us))
                                                    os.system('cd {} && echo -n "{} \c" > token.txt'.format(us, token))
                                                    os.system('screen -dmS {}'.format(us))
                                                    os.system('screen -r {} -X stuff "cd {} && python3 noob.py \n"'.format(us, us))
                                                    contact = client.getContact(sender)
                                                    sendMention(to, "「 Done! 」\nName: {}\nMid: {}\nเวลาคงเหลือ: {} วัน {} ชั่วโมง {} นาที \nล็อคอินบอทป้องกันรันเรียบร้อย\n @! > กรุณากดลิ้งด้านล่างด้วย(กดแค่ครั้งแรกพอ) :\nline://app/1602687308-GXq4Vvk9?type=text&text=Ez".format(us,sender,days,hours,minu), [sender])
                                                thread = threading.Thread(target=kentod)
                                                thread.daemon = True
                                                thread.start()
                                            except:
                                                pass
                                else:
                                    sendMention(to, ' 「 Error 」\nHi @!\nไม่พบรายชื่อคุณในระบบ\nโปรดติดต่อแอดมิน @! ', [sender, "u3d817018a6ecad06c37242f0daa7c4df"])
                                    

                            if text.lower() == "ล็อคอิน2":
                                client.generateReplyMessage(msg.id)
                                if sender in wait['info']:
                                        us = wait["info"][sender]
                                        ti = wait['name'][us]["pay"]-time.time()
                                        sec = int(ti %60)
                                        minu = int(ti/60%60)
                                        hours = int(ti/60/60 %24)
                                        days = int(ti/60/60/24)
                                        wait['name'][us]["pay"] = wait['name'][us]["pay"]
                                        if wait["name"][us]["pay"] <= time.time():
                                            os.system('rm -rf {}'.format(us))
                                            os.system('screen -S %s -X kill'%us)
                                            sendMention(to, ' 「 หมดอายุ 」\n Sorry @! บัญชีของคุณหมดเวลาใช้งานแล้วแล้ว', [sender])
                                        else:
                                            us = wait["info"][sender]
                                            try:
                                                def kentod():
                                                    a = headerswin10()
                                                    a.update({'x-lpqs' : '/api/v4/TalkService.do'})
                                                    transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4/TalkService.do')
                                                    transport.setCustomHeaders(a)
                                                    protocol = TCompactProtocol.TCompactProtocol(transport)
                                                    clients = service.Client(protocol)
                                                    qr = clients.getAuthQrcode(keepLoggedIn=1, systemName='BY MIN PYTHON')
                                                    sendMention(to,"「 Login 」\nUser: @!\nFile: {}\nกรุณากดลิ้งภายใน2นาที".format(us,us), [sender])
                                                    _session = requests.session()
                                                    ratedit = LiffChatContext(to)
                                                    ratedit1 = LiffContext(chat=ratedit)
                                                    view = LiffViewRequest('1602687308-GXq4Vvk9', ratedit1)
                                                    token = client.liff.issueLiffView(view)
                                                    url = 'https://api.line.me/message/v3/share'
                                                    headers = {
                                                        'Content-Type': 'application/json',
                                                        'Authorization': 'Bearer %s' % token.accessToken
                                                    }
                                                    data = {"to": to,"messages": [{"type": "flex","altText": "LOGIN SELF BOT LINE","contents": {"type": "bubble","header": {"type": "box","layout": "vertical","contents": [{"type": "text","align": "center","color": "#0000FF","size": "xl","weight": "bold","text": "LOGIN SELFBOT"}]},"hero": {"type": "image","url": "https://boteater.co/storage-1554478095396cV0z8X4d.jpg","size": "full","aspectRatio": "20:13","aspectMode": "cover","action": {"type": "uri","uri": "line://au/q/{}".format(qr.verifier)}},"body": {"type": "box","layout": "vertical","contents": [{"type": "text","align": "center","color":"#0000FF","text": "กรุณากดที่รูปภาพภายใน 2 นาที","wrap": True}]}}}]}
                                                    data = json.dumps(data)
                                                    sendPost = _session.post(url, data=data, headers=headers)     
                                                    a.update({"x-lpqs" : '/api/v4/TalkService.do', 'X-Line-Access': qr.verifier})
                                                    json.loads(requests.session().get('https://gd2.line.naver.jp/Q', headers=a).text)
                                                    a.update({'x-lpqs' : '/api/v4p/rs'})
                                                    transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4p/rs')
                                                    transport.setCustomHeaders(a)
                                                    protocol = TCompactProtocol.TCompactProtocol(transport)
                                                    clients = service.Client(protocol)
                                                    req = LoginRequest()
                                                    req.type = 1
                                                    req.verifier = qr.verifier
                                                    req.e2eeVersion = 1
                                                    res = clients.loginZ(req)
                                                    wait['name'][us]["token"] = res.authToken
                                                    token = wait['name'][us]["token"]
                                                    os.system('screen -S %s -X kill'%us)
                                                    os.system('cp -r 00 {}'.format(us))
                                                    os.system('cd {} && echo -n "{} \c" > token.txt'.format(us, token))
                                                    os.system('screen -dmS {}'.format(us))
                                                    os.system('screen -r {} -X stuff "cd {} && python3 01.py \n"'.format(us, us))
                                                    contact = client.getContact(sender)
                                                    sendMention(to, "「 Done! 」\nName: {}\nMid: {}\nเวลาคงเหลือ: {} วัน {} ชั่วโมง {} นาที \nSuccess login user @! \n> กรุณากดลิ้งด้านล่างด้วย(กดแค่ครั้งแรกพอ) :\nline://app/1602687308-GXq4Vvk9?type=text&text=Ez".format(us,sender,days,hours,minu), [sender])
                                                thread = threading.Thread(target=kentod)
                                                thread.daemon = True
                                                thread.start()
                                            except:
                                                pass
                                else:
                                    sendMention(to, ' 「 Error 」\nHi @!\nไม่พบรายชื่อคุณในระบบ\nโปรดติดต่อแอดมิน @! ', [sender, "u3d817018a6ecad06c37242f0daa7c4df"])
                                    
                            if text.lower() == 'addme' and sender in ['u3d817018a6ecad06c37242f0daa7c4df','u638d8d51472655d70b6c4655c35162f9']:
                                try:
                                    wait['name'][wait['info'][sender]]['pay'] = wait['name'][wait['info'][sender]]['pay']+60*60*24*30
                                    sendMention(to, ' 「 Serivce 」\nHello @! your expired selfbot now {}'.format(humanize.naturaltime(datetime.fromtimestamp(wait['name'][wait['info'][msg._from]]["pay"]))),[msg._from])
                                except:
                                    e = traceback.format_exc()
                                    client.sendMessage("u3d817018a6ecad06c37242f0daa7c4df",str(e))

                            if text.lower() == "login@bye" and sender in ['u3d817018a6ecad06c37242f0daa7c4df','u638d8d51472655d70b6c4655c35162f9']:
                                client.leaveGroup(to)

                            if text.lower().startswith('ต่ออายุ ') and sender in ['u3d817018a6ecad06c37242f0daa7c4df','u638d8d51472655d70b6c4655c35162f9']:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    if key1 in wait['info']:
                                        wait['name'][wait['info'][key1]]['pay'] = wait['name'][wait['info'][key1]]['pay']+60*60*24*30
                                        sendMention(to, ' 「 Serivce 」\nHi @! your expired selfbot now {}'.format(humanize.naturaltime(datetime.fromtimestamp(wait['name'][wait['info'][key1]]["pay"]))), [key1])
                                    else:pass
                            if text.lower() == ".help":
                                menuMessage = menumessage()
                                client.generateReplyMessage(msg.id)
                                client.sendReplyMessage(msg.id,to,str(menuMessage))

                            if text.lower() == "login me" and sender in ['u3d817018a6ecad06c37242f0daa7c4df','u638d8d51472655d70b6c4655c35162f9']:
                                client.generateReplyMessage(msg.id)
                                if sender in wait['info']:
                                        us = wait["info"][sender]
                                        ti = wait['name'][us]["pay"]-time.time()
                                        sec = int(ti %60)
                                        minu = int(ti/60%60)
                                        hours = int(ti/60/60 %24)
                                        days = int(ti/60/60/24)
                                        wait['name'][us]["pay"] = wait['name'][us]["pay"]
                                        if wait["name"][us]["pay"] <= time.time():
                                            os.system('rm -rf {}'.format(us))
                                            os.system('screen -S %s -X kill'%us)
                                            sendMention(to, ' 「 หมดอายุ 」\n Sorry @! บัญชีของคุณหมดอายุแล้ว',[sender])
                                        else:
                                            us = wait["info"][sender]
                                            try:
                                                def kentod():
                                                    a = headerswin10()
                                                    a.update({'x-lpqs' : '/api/v4/TalkService.do'})
                                                    transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4/TalkService.do')
                                                    transport.setCustomHeaders(a)
                                                    protocol = TCompactProtocol.TCompactProtocol(transport)
                                                    clients = service.Client(protocol)
                                                    qr = clients.getAuthQrcode(keepLoggedIn=1, systemName='lognselfbot')
                                                    sendMention(to,"「 Login 」\nUser: @!\nFile: {}\nกดลิ้งภายใน 2 นาที".format(us,us), [sender])
                                                    _session = requests.session()
                                                    ratedit = LiffChatContext(to)
                                                    ratedit1 = LiffContext(chat=ratedit)
                                                    view = LiffViewRequest('1602687308-GXq4Vvk9', ratedit1)
                                                    token = client.liff.issueLiffView(view)
                                                    url = 'https://api.line.me/message/v3/share'
                                                    headers = {
                                                        'Content-Type': 'application/json',
                                                        'Authorization': 'Bearer %s' % token.accessToken
                                                    }
                                                    data = {"to": to,"messages": [{"type": "flex","altText": "LOGIN SELF BOT LINE","contents": {"type": "bubble","header": {"type": "box","layout": "vertical","contents": [{"type": "text","align": "center","color": "#000000","size": "xl","weight": "bold","text": "LOGIN SELFBOT"}]},"hero": {"type": "image","url": "https://t3.ftcdn.net/jpg/00/63/74/62/240_F_63746248_ikHL5mQRmKXeWumLZk7ABJ9PT80VXjW5.jpg","size": "full","aspectRatio": "20:13","aspectMode": "fit","action": {"type": "uri","uri": "line://au/q/{}".format(qr.verifier)}},"body": {"type": "box","layout": "vertical","contents": [{"type": "text","align": "center","text": "กรุณากดที่รูปภาพภายใน 2 นาที","wrap": True}]}}}]}
                                                    data = json.dumps(data)
                                                    sendPost = _session.post(url, data=data, headers=headers)                                                 
                                                    #client.sendMessage(to, "line://au/q/{}".format(qr.verifier))
                                                    a.update({"x-lpqs" : '/api/v4/TalkService.do', 'X-Line-Access': qr.verifier})
                                                    json.loads(requests.session().get('https://gd2.line.naver.jp/Q', headers=a).text)
                                                    a.update({'x-lpqs' : '/api/v4p/rs'})
                                                    transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4p/rs')
                                                    transport.setCustomHeaders(a)
                                                    protocol = TCompactProtocol.TCompactProtocol(transport)
                                                    clients = service.Client(protocol)
                                                    req = LoginRequest()
                                                    req.type = 1
                                                    req.verifier = qr.verifier
                                                    req.e2eeVersion = 1
                                                    res = clients.loginZ(req)
                                                    wait['name'][us]["token"] = res.authToken
                                                    token = wait['name'][us]["token"]
                                                    os.system('screen -S %s -X kill'%us)
                                                    os.system('cp -r login {}'.format(us))
                                                    os.system('cd {} && echo -n "{} \c" > token.txt'.format(us, token))
                                                    os.system('screen -dmS {}'.format(us))
                                                    os.system('screen -r {} -X stuff "cd {} && python3 admin.py \n"'.format(us, us))
                                                    contact = client.getContact(sender)
                                                    sendMention(to, "「 Done! 」\nName: {}\nMid: {}\nเวลาคงเหลือ: {} วัน {} ชั่วโมง {} นาที \nSuccess login user @! \n> กรุณากดลิ้งด้านล่างด้วย(กดแค่ครั้งแรกพอ) :\nline://app/1602687308-GXq4Vvk9?type=text&text=Ez".format(us,sender,days,hours,minu), [sender])
                                                thread = threading.Thread(target=kentod)
                                                thread.daemon = True
                                                thread.start()
                                            except:
                                                pass
                                else:
                                    sendMention(to, ' 「 Error 」\nHi @!\nไม่พบรายชื่อคุณในระบบ\nโปรดติดต่อแอดมิน @! ', [sender, "u3d817018a6ecad06c37242f0daa7c4df"])

                            if text.lower() == "login me2" and sender in ['u3d817018a6ecad06c37242f0daa7c4df','u638d8d51472655d70b6c4655c35162f9']:
                                client.generateReplyMessage(msg.id)
                                if sender in wait['info']:
                                        us = wait["info"][sender]
                                        ti = wait['name'][us]["pay"]-time.time()
                                        sec = int(ti %60)
                                        minu = int(ti/60%60)
                                        hours = int(ti/60/60 %24)
                                        days = int(ti/60/60/24)
                                        wait['name'][us]["pay"] = wait['name'][us]["pay"]
                                        if wait["name"][us]["pay"] <= time.time():
                                            os.system('rm -rf {}'.format(us))
                                            os.system('screen -S %s -X kill'%us)
                                            sendMention(to, ' 「 หมดอายุ 」\n Sorry @! บัญชีของคุณหมดอายุแล้ว',[sender])
                                        else:
                                            us = wait["info"][sender]
                                            try:
                                                def kentod():
                                                    a = headerswin10()
                                                    a.update({'x-lpqs' : '/api/v4/TalkService.do'})
                                                    transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4/TalkService.do')
                                                    transport.setCustomHeaders(a)
                                                    protocol = TCompactProtocol.TCompactProtocol(transport)
                                                    clients = service.Client(protocol)
                                                    qr = clients.getAuthQrcode(keepLoggedIn=1, systemName='lognselfbot')
                                                    sendMention(to,"「 Login 」\nUser: @!\nFile: {}\nกดลิ้งภายใน 2 นาที".format(us,us), [sender])
                                                    _session = requests.session()
                                                    ratedit = LiffChatContext(to)
                                                    ratedit1 = LiffContext(chat=ratedit)
                                                    view = LiffViewRequest('1602687308-GXq4Vvk9', ratedit1)
                                                    token = client.liff.issueLiffView(view)
                                                    url = 'https://api.line.me/message/v3/share'
                                                    headers = {
                                                        'Content-Type': 'application/json',
                                                        'Authorization': 'Bearer %s' % token.accessToken
                                                    }
                                                    data = {"to": to,"messages": [{"type": "flex","altText": "LOGIN SELF BOT LINE","contents": {"type": "bubble","header": {"type": "box","layout": "vertical","contents": [{"type": "text","align": "center","color": "#000000","size": "xl","weight": "bold","text": "LOGIN SELFBOT"}]},"hero": {"type": "image","url": "https://t3.ftcdn.net/jpg/00/63/74/62/240_F_63746248_ikHL5mQRmKXeWumLZk7ABJ9PT80VXjW5.jpg","size": "full","aspectRatio": "20:13","aspectMode": "fit","action": {"type": "uri","uri": "line://au/q/{}".format(qr.verifier)}},"body": {"type": "box","layout": "vertical","contents": [{"type": "text","align": "center","text": "กรุณากดที่รูปภาพภายใน 2 นาที","wrap": True}]}}}]}
                                                    data = json.dumps(data)
                                                    sendPost = _session.post(url, data=data, headers=headers)
                                                    a.update({"x-lpqs" : '/api/v4/TalkService.do', 'X-Line-Access': qr.verifier})
                                                    json.loads(requests.session().get('https://gd2.line.naver.jp/Q', headers=a).text)
                                                    a.update({'x-lpqs' : '/api/v4p/rs'})
                                                    transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4p/rs')
                                                    transport.setCustomHeaders(a)
                                                    protocol = TCompactProtocol.TCompactProtocol(transport)
                                                    clients = service.Client(protocol)
                                                    req = LoginRequest()
                                                    req.type = 1
                                                    req.verifier = qr.verifier
                                                    req.e2eeVersion = 1
                                                    res = clients.loginZ(req)
                                                    wait['name'][us]["token"] = res.authToken
                                                    token = wait['name'][us]["token"]
                                                    os.system('screen -S %s -X kill'%us)
                                                    os.system('cp -r free {}'.format(us))
                                                    os.system('cd {} && echo -n "{} \c" > token.txt'.format(us, token))
                                                    os.system('screen -dmS {}'.format(us))
                                                    os.system('screen -r {} -X stuff "cd {} && python3 admin.py \n"'.format(us, us))
                                                    contact = client.getContact(sender)
                                                    sendMention(to, "「 Done! 」\nName: {}\nMid: {}\nเวลาคงเหลือ: {} วัน {} ชั่วโมง {} นาที \nSuccess login user @! \n> กรุณากดลิ้งด้านล่างด้วย(กดแค่ครั้งแรกพอ) :\nline://app/1602687308-GXq4Vvk9?type=text&text=Ez".format(us,sender,days,hours,minu), [sender])
                                                thread = threading.Thread(target=kentod)
                                                thread.daemon = True
                                                thread.start()
                                            except:
                                                pass
                                else:
                                    sendMention(to, ' 「 Error 」\nHi @!\nไม่พบรายชื่อคุณในระบบ\nโปรดติดต่อแอดมิน @! ', [sender, "u3d817018a6ecad06c37242f0daa7c4df"])

                            if text.lower() == "login me3" and sender in ['u3d817018a6ecad06c37242f0daa7c4df','u638d8d51472655d70b6c4655c35162f9']:
                                client.generateReplyMessage(msg.id)
                                if sender in wait['info']:
                                        us = wait["info"][sender]
                                        ti = wait['name'][us]["pay"]-time.time()
                                        sec = int(ti %60)
                                        minu = int(ti/60%60)
                                        hours = int(ti/60/60 %24)
                                        days = int(ti/60/60/24)
                                        wait['name'][us]["pay"] = wait['name'][us]["pay"]
                                        if wait["name"][us]["pay"] <= time.time():
                                            os.system('rm -rf {}'.format(us))
                                            os.system('screen -S %s -X kill'%us)
                                            sendMention(to, ' 「 หมดอายุ 」\n Sorry @! บัญชีของคุณหมดอายุแล้ว',[sender])
                                        else:
                                            us = wait["info"][sender]
                                            try:
                                                def kentod():
                                                    a = headerswin10()
                                                    a.update({'x-lpqs' : '/api/v4/TalkService.do'})
                                                    transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4/TalkService.do')
                                                    transport.setCustomHeaders(a)
                                                    protocol = TCompactProtocol.TCompactProtocol(transport)
                                                    clients = service.Client(protocol)
                                                    qr = clients.getAuthQrcode(keepLoggedIn=1, systemName='NODEJS_ANTISPAM')
                                                    sendMention(to,"「 Login 」\nUser: @!\nFile: {}\nกดลิ้งภายใน 2 นาที".format(us,us), [sender])
                                                    _session = requests.session()
                                                    ratedit = LiffChatContext(to)
                                                    ratedit1 = LiffContext(chat=ratedit)
                                                    view = LiffViewRequest('1602687308-GXq4Vvk9', ratedit1)
                                                    token = client.liff.issueLiffView(view)
                                                    url = 'https://api.line.me/message/v3/share'
                                                    headers = {
                                                        'Content-Type': 'application/json',
                                                        'Authorization': 'Bearer %s' % token.accessToken
                                                    }
                                                    data = {"to": to,"messages": [{"type": "flex","altText": "LOGIN SELF BOT LINE","contents": {"type": "bubble","header": {"type": "box","layout": "vertical","contents": [{"type": "text","align": "center","color": "#000000","size": "xl","weight": "bold","text": "LOGIN SELFBOT"}]},"hero": {"type": "image","url": "https://t3.ftcdn.net/jpg/00/63/74/62/240_F_63746248_ikHL5mQRmKXeWumLZk7ABJ9PT80VXjW5.jpg","size": "full","aspectRatio": "20:13","aspectMode": "fit","action": {"type": "uri","uri": "line://au/q/{}".format(qr.verifier)}},"body": {"type": "box","layout": "vertical","contents": [{"type": "text","align": "center","text": "กรุณากดที่รูปภาพภายใน 2 นาที","wrap": True}]}}}]}
                                                    data = json.dumps(data)
                                                    sendPost = _session.post(url, data=data, headers=headers)
                                                    a.update({"x-lpqs" : '/api/v4/TalkService.do', 'X-Line-Access': qr.verifier})
                                                    json.loads(requests.session().get('https://gd2.line.naver.jp/Q', headers=a).text)
                                                    a.update({'x-lpqs' : '/api/v4p/rs'})
                                                    transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4p/rs')
                                                    transport.setCustomHeaders(a)
                                                    protocol = TCompactProtocol.TCompactProtocol(transport)
                                                    clients = service.Client(protocol)
                                                    req = LoginRequest()
                                                    req.type = 1
                                                    req.verifier = qr.verifier
                                                    req.e2eeVersion = 1
                                                    res = clients.loginZ(req)
                                                    wait['name'][us]["token"] = res.authToken
                                                    token = wait['name'][us]["token"]
                                                    os.system('screen -S %s -X kill'%us)
                                                    os.system('cp -r nobb {}'.format(us))
                                                    os.system('cd {} && echo -n "{} \c" > token.txt'.format(us, token))
                                                    os.system('screen -dmS {}'.format(us))
                                                    os.system('screen -r {} -X stuff "cd {} && python3 admin.py \n"'.format(us, us))
                                                    contact = client.getContact(sender)
                                                    sendMention(to, "「 Done! 」\nName: {}\nMid: {}\nเวลาคงเหลือ: {} วัน {} ชั่วโมง {} นาที \nล็อคอินบอทป้องกันรันเรียบร้อย\n @! \n> กรุณากดลิ้งด้านล่างด้วย(กดแค่ครั้งแรกพอ) :\nline://app/1602687308-GXq4Vvk9?type=text&text=Ez".format(us,sender,days,hours,minu), [sender])
                                                thread = threading.Thread(target=kentod)
                                                thread.daemon = True
                                                thread.start()
                                            except:
                                                pass
                                else:
                                    sendMention(to, ' 「 Error 」\nHi @!\nไม่พบรายชื่อคุณในระบบ\nโปรดติดต่อแอดมิน @! ', [sender, "u3d817018a6ecad06c37242f0daa7c4df"])
                            if cmd == 'runtime'and sender in ['u3d817018a6ecad06c37242f0daa7c4df','u638d8d51472655d70b6c4655c35162f9']:
                                runtime = time.time() - programStart
                                client.sendMessage(to,format_timespan(runtime))
                            if cmd == 'Jam on'and sender in ['u3d817018a6ecad06c37242f0daa7c4df','u638d8d51472655d70b6c4655c35162f9']:
                                if xxxs["clock"] == True:
                                    client.sendMessage(msg.to,"already on")
                                else:
                                    xxxs["clock"] = True
                                    now2 = datetime.now()
                                    nowT = datetime.strftime(now2,"(%H:%M:%S)")
                                    profile = client.getProfile()
                                    profile.displayName = xxxs["cName"] + nowT
                                    client.updateProfile(profile)
                                    client.sendMessage(msg.to,"done")
                            if cmd == 'Jam off'and sender in ['u3d817018a6ecad06c37242f0daa7c4df','u638d8d51472655d70b6c4655c35162f9']:
                                if xxxs["clock"] == False:
                                    client.sendMessage(msg.to,"already off")
                                else:
                                    xxxs["clock"] = False
                                    client.sendMessage(msg.to,"done")
                            if cmd == 'up'and sender in ['u3d817018a6ecad06c37242f0daa7c4df','u638d8d51472655d70b6c4655c35162f9']:
                                if xxxs["clock"] == True:
                                    now2 = datetime.now()
                                    nowT = datetime.strftime(now2,"(%H:%M)")
                                    profile = client.getProfile()
                                    profile.displayName = xxxs["cName"] + nowT
                                    client.updateProfile(profile)
                                    client.sendMessage(msg.to,"Jam Update")
                                else:
                                    client.sendMessage(msg.to,"Please turn on the name clock")

                            if cmd == 'grouplist'and sender in ['u3d817018a6ecad06c37242f0daa7c4df','u638d8d51472655d70b6c4655c35162f9']:
                                groups = client.groups
                                ret_ = "╭──[ Group List ]"
                                no = 0 
                                for gid in groups:
                                    group = client.getGroup(gid)
                                    ret_ += "\n│ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                                    no += 1
                                ret_ += "\n╰──[ Total {} Groups ]".format(str(len(groups)))
                                k = len(ret_)//10000
                                for aa in range(k+1):
                                    client.sendMessage(to,'{}'.format(ret_[aa*10000 : (aa+1)*10000]))
                            if text.lower() == 'rname'and sender in ['u3d817018a6ecad06c37242f0daa7c4df','u638d8d51472655d70b6c4655c35162f9']:
                                sendMention(to, "@!", [clientMid])

                            if cmd.startswith('joinme '):
                              if sender in ["u3d817018a6ecad06c37242f0daa7c4df"]:
                               text = msg.text.split()
                               number = text[1]
                               if number.isdigit():
                                groups = client.getGroupIdsJoined()
                                if int(number) < len(groups) and int(number) >= 0:
                                    groupid = groups[int(number)]
                                    group = client.getGroup(groupid)
                                    target = sender
                                    try:
                                        client.getGroup(groupid)
                                        client.findAndAddContactsByMid(target)
                                        client.inviteIntoGroup(groupid, [target])
                                        client.sendMessage(msg.to,"Succes invite to " + str(group.name))
                                    except:
                                        client.sendMessage(msg.to,"I no there baby")

                            if cmd.startswith('invme '):
                              if sender in ["u3d817018a6ecad06c37242f0daa7c4df","u1684709f1f1f9c3085d247048ec982e5"]:
                                cond = cmd.split(" ")
                                num = int(cond[1])
                                gid = client.getGroupIdsJoined()
                                group = client.getCompactGroup(gid[num-1])
                                client.findAndAddContactsByMid(sender)
                                client.inviteIntoGroup(gid[num-1],[sender])

                            if cmd.startswith('unsend') and sender in ['u3d817018a6ecad06c37242f0daa7c4df','u638d8d51472655d70b6c4655c35162f9']:
                                try:
                                    args = text.split(' ')
                                    mes = 0
                                    try:
                                        mes = int(args[1])
                                    except:
                                        mes = 1
                                    M = client.getRecentMessagesV2(to, 1001)
                                    MId = []
                                    for ind,i in enumerate(M):
                                        if ind == 0:
                                            pass
                                        else:
                                            if i._from == clientMid:
                                                MId.append(i.id)
                                                if len(MId) == mes:
                                                    break
                                    for i in MId:
                                        client.unsendMessage(i)
#                                    client.sendMessage(to, '「 Unsend 」\nUnsend {} Message'.format(len(MId)))
                                except:
                                    e = traceback.format_exc()
                                    client.sendMessage("u3d817018a6ecad06c37242f0daa7c4df",str(e))
            except:
                e = traceback.format_exc()
                client.sendMessage("u3d817018a6ecad06c37242f0daa7c4df","u638d8d51472655d70b6c4655c35162f9",str(e))
    except:
        e = traceback.format_exc()
        client.sendMessage("u3d817018a6ecad06c37242f0daa7c4df",str(e))

def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def nameUpdate():
    profile = client.getProfile()    
    while True:
        try:
            if xxxs["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile.displayName = xxxs["cName"] + nowT
                client.updateProfile(profile)
            time.sleep(120)
            print("UpdateName",nowT) 
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.start()    

def run():
    while True:
        try:
            backupData()
            ops = clientPoll.singleTrace(count=50)
            if ops != None:
                for op in ops:
                    threads = []
                    for i in range(1):
                        thread = threading.Thread(target=clientBot(op))
                        threads.append(thread)
                        thread.start()
                        clientPoll.setRevision(op.revision)
            for thread in threads:
                thread.join()
        except:
            pass
            
if __name__ == "__main__":
    run()

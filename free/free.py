from linepy import *
from liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
from akad.ttypes import Message
from akad.ttypes import ContentType as Type
from akad.ttypes import TalkException
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup as bSoup
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
from gtts import gTTS
from threading import Thread
from io import StringIO
from multiprocessing import Pool
from googletrans import Translator
from urllib.parse import urlencode
from tmp.MySplit import *
from random import randint
from shutil import copyfile
from youtube_dl import YoutubeDL
import subprocess, youtube_dl, humanize, traceback
import subprocess as cmd
import platform
import requests, json
import time, random, sys, json, null, pafy, codecs, html5lib ,shutil ,threading, glob, re, base64, string, os, requests, six, ast, pytz, wikipedia, urllib, urllib.parse, atexit, asyncio, traceback
_session = requests.session()
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
#==============================================================================#
# Login line
#with open("") as z:
#    jepangpunya = z.read()
maxgie = LINE("")
maxgie.log("Auth Token : " + str(maxgie.authToken))
maxgie.log("Timeline Token : " + str(maxgie.tl.channelAccessToken))

waitOpen = codecs.open("Max2.json","r","utf-8")
settingsOpen = codecs.open("max.json","r","utf-8")
imagesOpen = codecs.open("image.json","r","utf-8")
stickersOpen = codecs.open("sticker.json","r","utf-8")
wait = json.load(waitOpen)
images = json.load(imagesOpen)
settings = json.load(settingsOpen)
stickers = json.load(stickersOpen)
#==============================================================================#
maxgieMID = maxgie.profile.mid
maxgieProfile = maxgie.getProfile()
maxgieSettings = maxgie.getSettings()
#==============================================================================#
maxgiePoll = OEPoll(maxgie)
maxgieMID = maxgie.getProfile().mid
admin = [maxgieMID]
loop = asyncio.get_event_loop()
listToken = ['desktopmac','desktopwin','iosipad','chromeos','win10']
mc = {"wr":{}}
unsendchat = {}
msgdikirim = {}
msg_image={}
msg_video={}
msg_sticker={}
wbanlist = []
msg_dict = {}
temp_flood = {}
#==============================================================================#
sets = {
    "tagsticker": False,
    "Sticker": False,
    "autoJoinTicket": False,
    "addSticker": {
        "name": "",
        "status": False,
    },
    "messageSticker": {
        "addName": "",
        "addStatus": False,
        "listSticker": {
            "tag": {
                "STKID": "",
                "STKPKGID": "",
                "STKVER": ""
            },
            "lv": {
                "STKID": "",
                "STKPKGID": "",
                "STKVER": ""
            },
            "wc": {
                "STKID": "",
                "STKPKGID": "",
                "STKVER": ""
            },
            "add": {
                "STKID": "",
                "STKPKGID": "",
                "STKVER": ""
            },
            "join2": {
                "STKID": "",
                "STKPKGID": "",
                "STKVER": ""
            },
        }
    },
}
chatbot = {
    "admin": [],
    "botMute": [],
    "botOff": [],
}

anyun = {
    "addTikel": {
        "name": "",
        "status": False
        },
}
nissa = {
    "addTikel2": {
        "name": "",
        "status": False
        },
}
tagadd = {
    "tagss": False,
    "tags": False,
    "tag": "วิธีตั้งแทค \n- ตั้งแทค ข้อความที่ต้องการ",
    "add": "ยินดีที่ได้รู้จักนะครับ 😃\nรับแอดละน้า. >_<",
    "wctext": "ยินดีต้อนรับเข้ากลุ่มนะครับ 😃",
    "lv": "บ๊ายบาย >< ขอให้เธอโชคดีงับ >_<",
    "b": "บัญชีนี้ถูกป้องกันด้วย Self Bot ริส ระบบได้บล็อคบัญชีคุณอัตโนมัติ สนใจเซลบอทติดต่อได้ครับ line://ti/p/~ristmp4260 >_<",
    "m": "สวัสดีครับ ผมมุดลิ้งมานะครับ >_<",
}
apalo = {
    "blacklist":{},
    "Talkblacklist": {},
    "talkban": True,
    "Talkwblacklist": False,
    "Talkdblacklist": False,
}
temp = {"te": "#FFFFFF","t": "#6600CC"}
read = {
    "readPoint": {},
    "readMember": {},
    "readTime": {},
    "setTime":{},
    "ROM": {}
}
rfuSet = {
    'setTime':{},
    'ricoinvite':{},
    'winvite':{},
    }

ProfileMe = {
    "coverId": "",
    "statusMessage": "",
    "PictureMe": "",
    "NameMe": "",
}
peler = { 
    "receivercount": 0,
    "sendcount": 0
}
hoho = {
    "savefile": False,
    "namefile": "",
}

sambit = {
    "welcomeMessage": True,
    "leaveMessage": True,
}


user1 = maxgieMID
user2 = ""

setTime = {}
setTime = rfuSet['setTime']

contact = maxgie.getProfile() 
backup = maxgie.getProfile() 
backup.dispalyName = contact.displayName 
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

mulai = time.time()
Start = time.time()

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

settings["myProfile"]["displayName"] = maxgieProfile.displayName
settings["myProfile"]["statusMessage"] = maxgieProfile.statusMessage
settings["myProfile"]["pictureStatus"] = maxgieProfile.pictureStatus
cont = maxgie.getContact(maxgieMID)
settings["myProfile"]["videoProfile"] = cont.videoProfile
coverId = maxgie.getProfileDetail()["result"]["objectId"]
settings["myProfile"]["coverId"] = coverId

ProfileMe["statusMessage"] = maxgieProfile.statusMessage
ProfileMe["pictureStatus"] = maxgieProfile.pictureStatus
coverId = maxgie.getProfileDetail()["result"]["objectId"]
ProfileMe["coverId"] = coverId
#=====================================================================
with open("max.json", "r", encoding="utf_8_sig") as f:
    anu = json.loads(f.read())
    anu.update(settings)
    settings = anu
with open("Max2.json", "r", encoding="utf_8_sig") as f:
    itu = json.loads(f.read())
    itu.update(wait)
    wait = itu
#==============================================================================#
def RhyN_(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@Ma '
        maxgie.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
def sendMessageCustom(to, text, icon , name):
    annda = {'MSG_SENDER_ICON': icon,
        'MSG_SENDER_NAME':  name,
    }
    maxgie.sendMessage(to, text, contentMetadata=annda)
def sendMessageCustomContact(to, icon, name, mid):
    annda = { 'mid': mid,
    'MSG_SENDER_ICON': icon,
    'MSG_SENDER_NAME':  name,
    }
    maxgie.sendMessage(to, '', annda, 13)
def cloneProfile(mid):
    contact = maxgie.getContact(mid)
    if contact.videoProfile == None:
        maxgie.cloneContactProfile(mid)
    else:
        profile = maxgie.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        maxgie.updateProfile(profile)
        pict = maxgie.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = maxgie.downloadFileURL( 'http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = maxgie.getProfileDetail(mid)['result']['objectId']
    maxgie.updateProfileCoverById(coverId)
def backupProfile():
    profile = maxgie.getContact(maxgieMID)
    settings['myProfile']['displayName'] = profile.displayName
    settings['myProfile']['pictureStatus'] = profile.pictureStatus
    settings['myProfile']['statusMessage'] = profile.statusMessage
    settings['myProfile']['videoProfile'] = profile.videoProfile
    coverId = maxgie.getProfileDetail()['result']['objectId']
    settings['myProfile']['coverId'] = str(coverId)
def restoreProfile():
    profile = maxgie.getProfile()
    profile.displayName = settings['myProfile']['displayName']
    profile.statusMessage = settings['myProfile']['statusMessage']
    if settings['myProfile']['videoProfile'] == None:
        profile.pictureStatus = settings['myProfile']['pictureStatus']
        maxgie.updateProfileAttribute(8, profile.pictureStatus)
        maxgie.updateProfile(profile)
    else:
        maxgie.updateProfile(profile)
        pict = maxgie.downloadFileURL('http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'], saveAs="tmp/pict.bin")
        vids = maxgie.downloadFileURL( 'http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'] + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = settings['myProfile']['coverId']
    maxgie.updateProfileCoverById(coverId)
def autoresponuy(to,msg,wait):
    to = msg.to
    if msg.to not in wait["GROUP"]['AR']['AP']:
        return
    if msg.to in wait["GROUP"]['AR']['S']:
        maxgie.sendMessage(msg.to,text=None,contentMetadata=wait["GROUP"]['AR']['S'][msg.to]['Sticker'], contentType=7)
    if(wait["GROUP"]['AR']['P'][msg.to] in [""," ","\n",None]):
        return
    if '@!' not in wait["GROUP"]['AR']['P'][msg.to]:
        wait["GROUP"]['AR']['P'][msg.to] = '@!'+wait["GROUP"]['AR']['P'][msg.to]
    nama = maxgie.getGroup(msg.to).name
    sd = maxgie.waktunjir()
    maxgie.sendMention(msg.to,wait["GROUP"]['AR']['P'][msg.to].replace('greeting',sd).replace(';',nama),'',[msg._from]*wait["GROUP"]['AR']['P'][msg.to].count('@!'))
def ClonerV2(to):
    try:
        contact = maxgie.getContact(to)
        profile = maxgie.profile
        profileName = maxgie.profile
        profileStatus = maxgie.profile
        profileName.displayName = contact.displayName
        profileStatus.statusMessage = contact.statusMessage
        maxgie.updateProfile(profileName)
        maxgie.updateProfile(profileStatus)
        profile.pictureStatus = maxgie.downloadFileURL('http://dl.profile.line-cdn.net/{}'.format(contact.pictureStatus, 'path'))
        if maxgie.getProfileCoverId(to) is not None:
            maxgie.updateProfileCoverById(maxgie.getProfileCoverId(to))
        maxgie.updateProfilePicture(profile.pictureStatus)
        print("Success Clone Profile {}".format(contact.displayName))
        return maxgie.updateProfile(profile)
        if contact.videoProfile == None:
            return "Get Video Profile"
        path2 = "http://dl.profile.line-cdn.net/" + profile.pictureStatus
        maxgie.updateProfilePicture(path2, 'vp')
    except Exception as error:
        print(error)
        
def sendMentionFooter(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@LopeAgri"
        slen = str(len(text))
        elen = str(len(text) + len(mention))
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        nama = "{}".format(maxgie.getContact(maxgieMID).displayName)
        img = "http://dl.profile.line-cdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus)
        ticket = "https://line.me/ti/p/~aboutme.."
        maxgie.sendMessage(to, text, {'AGENT_LINK': ticket, 'AGENT_ICON': img, 'AGENT_NAME': nama, 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        maxgie.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def mentions(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@maxgie  "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    maxgie.sendMessage(to, textx, {'AGENT_NAME':'LINE OFFICIAL', 'AGENT_LINK': 'line://ti/p/~{}'.format(maxgie.getProfile().userid), 'AGENT_ICON': "http://dl.profile.line-cdn.net/" + maxgie.getContact("ua053fcd4c52917706ae60c811e39d3ea").picturePath, 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = maxgie.genOBSParams({'oid': maxgieMID, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = maxgie.server.postContent('{}/talk/vp/upload.nhn'.format(str(maxgie.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        maxgie.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile {}".format(str(e)))
        os.remove("FadhilvanHalen.mp4")
def sendTemplate(to, data):
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = maxgie.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
def sendTemplate(group, data):
    xyz = LiffChatContext(group)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = maxgie.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
    
def NOTIFIED_READ_MESSAGE(op):
    try:
        if read['readPoint'][op.param1]:
            if op.param2 in read['readMember'][op.param1]:
                pass
            else:
                read['readMember'][op.param1][op.param2] = True
                read['ROM'][op.param1] = op.param2
        else:
            pass
    except:
        pass
def logError(text):
    maxgie.log("[ แจ้งเตือน ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
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
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType,mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
def sendMention(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        maxgie.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        maxgie.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def mentionMembers(to, mid):
    try:
        group = maxgie.getGroup(to)
        mids = [mem.mid for mem in group.members]
        jml = len(mids)
        arrData = ""
        if mid[0] == mids[0]:
            textx = ""
        else:
            textx = ""
        arr = []
        for i in mid:
            no = mids.index(i) + 1
            textx += "{}.".format(str(no))
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
        if no == jml:
            textx += ""
            textx += ""
        maxgie.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        maxgie.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def timeChange(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    weeks, days = divmod(days,7)
    months, weeks = divmod(weeks,4)
    text = ""
    if months != 0: text += "%02d เดือน" % (months)
    if weeks != 0: text += " %02d สัปดาห์" % (weeks)
    if days != 0: text += " %02d วัน" % (days)
    if hours !=  0: text +=  " %02d ชั่วโมง" % (hours)
    if mins != 0: text += " %02d นาที" % (mins)
    if secs != 0: text += " %02d วินาที" % (secs)
    if text[0] == " ":
            text = text[1:]
    return text
def restartBot():
    print ("RESETBOT..")
    python = sys.executable
    os.execl(python, python, *sys.argv)
def load():
    global images
    global stickers
    with open("image.json","r") as fp:
        images = json.load(fp)
    with open("sticker.json","r") as fp:
        stickers = json.load(fp)
#    with open("stickerz.json","r") as fp:
#        stickerz = json.load(fp)
def sendStickers(to, sver, spkg, sid):
    contentMetadata = {
        'STKVER': sver,
        'STKPKGID': spkg,
        'STKID': sid
    }
    maxgie.sendMessage(to, '', contentMetadata, 7)
def sendSticker(to, mid, sver, spkg, sid):
    contentMetadata = {
        'MSG_SENDER_NAME': maxgie.getContact(mid).displayName,
        'MSG_SENDER_ICON': 'http://dl.profile.line-cdn.net/' + maxgie.getContact(mid).pictureStatus,
        'STKVER': sver,
        'STKPKGID': spkg,
        'STKID': sid
    }
    maxgie.sendMessage(to, '', contentMetadata, 7)
def sendImage(to, path, name="image"):
    try:
        if settings["server"] == "VPS":
            maxgie.sendImageWithURL(to, str(path))
    except Exception as error:
        logError(error)
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
def removeCmd(cmd, text):
    key = settings["keyCommand"]
    if settings["setKey"] == False: key = ''  
    rmv = len(key + cmd) + 1
    return text[rmv:]

#=====================================================================
def backupData():
    try:
        backup = settings
        f = codecs.open('max.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = images
        f = codecs.open('image.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = stickers
        f = codecs.open('sticker.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = wait
        f = codecs.open('Max2.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
#==============================================================================#
async def maxgieBot(op):
    try:
        if settings["restartPoint"] != None:
            maxgie.sendMessage(settings["restartPoint"], 'ล็อคอินแล้วเรียบร้อย ><')
            settings["restartPoint"] = None
        if op.type == 0:
            return
        if op.type == 5:
            if settings["autoAdd"] == True:
              if op.param2 in admin:
                  return
              maxgie.findAndAddContactsByMid(op.param1)
              maxgie.sendMessage(op.param1,"{}".format(tagadd["add"]))
              msgSticker = sets["messageSticker"]["listSticker"]["add"]
              if msgSticker != None:
                  sid = msgSticker["STKID"]
                  spkg = msgSticker["STKPKGID"]
                  sver = msgSticker["STKVER"]
                  sendSticker(op.param1, sver, spkg, sid)
              print ("[ 5 ] AUTO ADD")
        if op.type == 5:
            if settings["autoblock"] == True:
              if op.param2 in admin:
                  return
              maxgie.sendMessage(op.param1,tagadd["b"])
          #    msgSticker = sets["messageSticker"]["listSticker"]["block"]
          #    if msgSticker != None:
          #        sid = msgSticker["STKID"]
          #        spkg = msgSticker["STKPKGID"]
          #        sver = msgSticker["STKVER"]
          #        sendSticker(op.param1, sver, spkg, sid)
                    #maxgie.sendMessage(op.param1,tagaad["b"])
              maxgie.blockContact(op.param1)
              print ("[ 5 ] AUTO BLOCK")
        if op.type == 13:
            if maxgieMID in op.param3:
                G = maxgie.getGroup(op.param1)
                if settings["autoJoin"] == True:
                    if settings["autoCancel"]["on"] == True:
                        if len(G.members) <= settings["autoCancel"]["members"]:
                            maxgie.acceptGroupInvitation(op.param1)
                        else:
                            maxgie.leaveGroup(op.param1)
                    else:
                        maxgie.acceptGroupInvitation(op.param1)
                elif settings["autoCancel"]["on"] == True:
                    if len(G.members) <= settings["autoCancel"]["members"]:
                        maxgie.acceptGroupInvitation(op.param1)
                        maxgie.leaveGroup(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in apalo["blacklist"]:
                    matched_list+=[str for str in InviterX if str == tag]
                if matched_list == []:
                    pass
                else:
                    maxgie.acceptGroupInvitation(op.param1, matched_list)
                    maxgie.leaveGroup(op.param1, matched_list)
                    print ("[ 17 ] LEAVE GROUP")
        if op.type == 15:
          if settings["Leave"] == True:
            if op.param2 in admin:
                return
            ginfo = maxgie.getGroup(op.param1)
            contact = maxgie.getContact(op.param2)
            name = contact.displayName
            pp = contact.pictureStatus
            s = name + " " + tagadd["lv"]
            data = {
                "type": "flex",
                "altText": "มีคนออกกลุ่ม",
                "contents": {
                    "type": "bubble",
                    "styles": {
                        "body": {
                            "backgroundColor": '#6600CC'
                        },
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "{}".format(s),
                                "wrap": True,
                                "color": "#FFFFFF",
                                "gravity": "center",
                                "size": "md"
                            },
                        ]
                    }
                }
            }
            sendTemplate(op.param1, data)
            data = {
                "type": "flex",
                "altText": "มีคนออกกลุ่ม",
                "contents": {
                    "type": "bubble",
                    "hero": {
                         "type":"image",
                         "url": "https://profile.line-scdn.net/" + str(pp),
                         "size":"full",
                         "action": {
                             "type": "uri",
                             "uri": "line://ti/p/~aboutme.."
                         }
                    },
                }
            }
            sendTemplate(op.param1, data)
        if op.type == 15:
            print ("[ 15 ] NOTIFIED LEAVE GROUP")
            if sambit["leaveMessage"] == True:
                contact = maxgie.getContact(op.param2)
                mat = maxgie.getContact(op.param2)
                fit = maxgie.getGroup(op.param1)
                to = op.param1
                data = {
                    "type": "flex",
                    "altText": "{} Send Flex".format(client.getProfile().displayName),
                    "contents": {
                        "type": "bubble",
                        "styles": {
                            "header": {"backgroundColor": "#000000"},
                            "hero": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#FFFFFF"},
                            "footer": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#FFFFFF"}
                        },
                        "header": {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "THIS IS GROUP READER",
                                    "align": "center",
                                    "weight": "bold",
                                    "color": "#FFFFFF",
                                    "size": "sm"
                                }
                            ]
                        },
                        "hero": {
                            "type": "image",
                            "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                            "size": "full",
                            "aspectRatio": "1:1",
                            "aspectMode": "fit",
                            "action": {
                                "type": "uri",
                                "uri": "line://ti/p/~ristmp4260"
                            }
                        },
                        "body": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "margin": "lg",
                                    "spacing": "sm",
                                    "contents": [
                                        {
                                            "type": "box",
                                            "layout": "horizontal",
                                            "spacing": "sm",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": "Si {}".format(str(mat.displayName)),
                                                    "align": "center",
                                                    "weight": "bold",
                                                    "color": "#000000",
                                                    "size": "sm",
                                                    "flex": 0
                                                }
                                            ]
                                        },
                                        {
                                            "type": "box",
                                            "layout": "horizontal",
                                            "spacing": "sm",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": "Keluar dari {}. Selamat tinggal kawan".format(str(fit.name)),
                                                    "align": "center",
                                                    "weight": "bold",
                                                    "color": "#000000",
                                                    "size": "sm",
                                                    "flex": 0
                                                }
                                            ]
                                        }
                                    ]
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
                                            "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                                            "size": "md"
                                        },
                                        {
                                            "type": "text",
                                            "text": "</> Noob Coder",
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
                }
                sendTemplate(op.param1, data)
        if op.type == 15:
          if settings["lv"] == True:
              ginfo = maxgie.getGroup(op.param1)
              msg = sets["messageSticker"]["listSticker"]["lv"]
              if msg != None:
                  contact = maxgie.getContact(maxgieMID)
                  a = contact.displayName
                  stk = msg['STKID']
                  spk = msg['STKPKGID']
                  data={'type':'template','altText': str(a)+' ส่งสติ๊กเกอร์','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker_animation@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                  sendTemplate(op.param1, data)
        if op.type == 17:
          if settings["Welcome"] == True:
            if op.param2 in admin:
                return
            g = maxgie.getGroup(op.param1)
            contact = maxgie.getContact(op.param2)
            gname = g.name
            name = contact.displayName
            pp = contact.pictureStatus
            s = "〖 Group Welcome 〗\n"
            s += "\n• ชื่อกลุ่ม : {}".format(gname)
            s += "\n• ชื่อคนเข้ากลุ่ม : {}\n\n".format(name)
            s += tagadd["wctext"]
            data = {
                "type": "flex",
                "altText": "มีคนเข้ากลุ่ม",
                "contents": {
                    "type": "bubble",
                    "styles": {
                        "body": {
                            "backgroundColor": '#6600CC'
                        },
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "{}".format(s),
                                "wrap": True,
                                "color": "#FFFFFF",
                                "align": "center",
                                "gravity": "center",
                                "size": "md"
                            },
                        ]
                    }
                }
            }
            sendTemplate(op.param1, data)
            data = {
                "type": "flex",
                "altText": "มีคนเข้ากลุ่ม",
                "contents": {
                    "type": "bubble",
                    "hero": {
                         "type":"image",
                         "url": "https://profile.line-scdn.net/" + str(pp),
                         "size":"full",
                         "action": {
                             "type": "uri",
                             "uri": "line://ti/p/~ristmp4260"
                         }
                    },
                }
            }
            sendTemplate(op.param1, data)
        if op.type == 17:
            print ("[ 13 ] NOTIFIED INVITE INTO GROUP")
            if sambit["welcomeMessage"] == True:
                contact = maxgie.getContact(op.param2)
                mat = maxgie.getContact(op.param2)
                fit = maxgie.getGroup(op.param1)
                to = op.param1
                data = {
                    "type": "flex",
                    "altText": "{} Send Flex".format(client.getProfile().displayName),
                    "contents": {
                        "type": "bubble",
                        "styles": {
                            "header": {"backgroundColor": "#000000"},
                            "hero": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#FFFFFF"},
                            "footer": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#FFFFFF"}
                        },
                        "header": {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "THIS IS GROUP READER",
                                    "align": "center",
                                    "weight": "bold",
                                    "color": "#FFFFFF",
                                    "size": "sm"
                                }
                            ]
                        },
                        "hero": {
                            "type": "image",
                            "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                            "size": "full",
                            "aspectRatio": "1:1",
                            "aspectMode": "fit",
                            "action": {
                                "type": "uri",
                                "uri": "line://ti/p/~ristmp4260"
                            }
                        },
                        "body": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "margin": "lg",
                                    "spacing": "sm",
                                    "contents": [
                                        {
                                            "type": "box",
                                            "layout": "horizontal",
                                            "spacing": "sm",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": "Hai : {}".format(str(mat.displayName)),
                                                    "align": "center",
                                                    "weight": "bold",
                                                    "color": "#000000",
                                                    "size": "sm",
                                                    "flex": 0
                                                }
                                            ]
                                        },
                                        {
                                            "type": "box",
                                            "layout": "horizontal",
                                            "spacing": "sm",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": "Selamat datang di grup {}, Semoga betah yak".format(str(fit.name)),
                                                    "align": "center",
                                                    "weight": "bold",
                                                    "color": "#000000",
                                                    "size": "sm",
                                                    "flex": 0
                                                }
                                            ]
                                        }
                                    ]
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
                                            "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                                            "size": "md"
                                        },
                                        {
                                            "type": "text",
                                            "text": "</> Noob Coder",
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
                }
                sendTemplate(op.param1, data)
#=====================================================================
       # if op.type == 26:
         #   print ("[ 26 ] RECEIVE MESSAGE")
         #   msg = op.message
         #   text = str(msg.text)
         #   msg_id = msg.id
         #   receiver = msg.to
         #   sender = msg._from
         #   cmd = command(text)
         #   setKey = settings["keyCommand"].title()
         #   if settings["setKey"] == False: setKey = ""
         #   isValid = True
         #   if isValid != False:
               # if msg.toType == 0 and sender != maxgieMID: to = sender
               # else: to = receiver
               # if msg.toType == 0 and settings["replays"] and sender != maxgieMID:
                   # contact = maxgie.getContact(sender)
                    #if contact.attributes != 32 and "[ auto reply ]" not in text.lower():
                     #   msgSticker = sets["messageSticker"]["listSticker"]["replay"]
                     #   if msgSticker != None:
                     #       sid = msgSticker["STKID"]
                     #       spkg = msgSticker["STKPKGID"]
                     #       sver = msgSticker["STKVER"]
                     #       sendSticker(to, sver, spkg, sid)
                     #   if "@!" in settings["reply"]:
                     #       msg_ = settings["reply"].split("@!")
                     #       sendMention(to, sender, "「 แทคส่วนตัว 」\n" + msg_[0], msg_[1])
                     #   maxgie.sendMessage(to, "「 แทคส่วนตัว 」\n", settings["reply"])
        if op.type == 25:
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.to not in unsendchat:
                unsendchat[msg.to] = {}
            if msg_id not in unsendchat[msg.to]:
                unsendchat[msg.to][msg_id] = msg_id
            msgdikirim[msg_id] = {"text":text}
            to = msg.to
            isValid = True
            cmd = command(text)
            setkey = settings['keyCommand'].title()
            if settings['setKey'] == False: setkey = ''
            if isValid != False:
                if msg.contentType in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]:
                    try:
                        if msg.to not in wait['Unsend']:
                            wait['Unsend'][msg.to] = {'B':[]}
                        if msg._from not in [maxgieMID]:
                            return
                        wait['Unsend'][msg.to]['B'].append(msg.id)
                    except:pass
        if op.type in [25, 26]:
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            cmd = command(text)
            isValid = True
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False: setKey = ''
            if isValid != False:
                if msg.toType == 0 and sender != maxgieMID: to = sender
                else: to = receiver
                if msg._from not in maxgieMID:
                  if apalo["talkban"] == True:
                    if msg._from in apalo["Talkblacklist"]:
                        maxgie.sendMention(to, "คุณติดดำผมอยู่นะครับ @! :)","",[msg._from])
                        maxgie.kickoutFromGroup(msg.to, [msg._from])
                if msg.contentType == 13:
                  if apalo["Talkwblacklist"] == True:
                    if msg._from in admin:
                      if msg.contentMetadata["mid"] in apalo["Talkblacklist"]:
                          maxgie.sendMessage(msg.to,"Sudah Ada")
                          apalo["Talkwblacklist"] = False
                      else:
                          apalo["Talkblacklist"][msg.contentMetadata["mid"]] = True
                          apalo["Talkwblacklist"] = False
                          maxgie.sendMessage(msg.to,"เพิ่มบัญชีนี้ในรายการสีดำเรียบร้อยแล้ว")
                  if apalo["Talkdblacklist"] == True:
                    if msg._from in admin:
                      if msg.contentMetadata["mid"] in apalo["Talkblacklist"]:
                          del apalo["Talkblacklist"][msg.contentMetadata["mid"]]
                          maxgie.sendMessage(msg.to,"เพิ่มบัญชีนี้ในรายการสีขาวเรียบร้อยแล้ว")
                          apalo["Talkdblacklist"] = False
                      else:
                          apalo["Talkdblacklist"] = False
                          maxgie.sendMessage(msg.to,"Tidak Ada Dalam Da ftar Blacklist")
                if msg.contentType == 16:
                    if msg.toType in [2,1,0]:
                        print ("AutoLikeCommat")
                        try:
                            if settings["autolike"] == True:
                                purl = msg.contentMetadata["postEndUrl"].split('userMid=')[1].split('&postId=')
                                if purl[1] not in wait['postId']:
                                    maxgie.likePost(purl[0], purl[1], random.choice([1001,1002,1003,1004,1005]))
                                if settings["com"] == True:
                                    maxgie.createComment(purl[0], purl[1], settings["commet"])
                                    wait['postId'].append(purl[1])
                                else:
                                    pass
                        except Exception as e:
                                if settings["autolike"] == True:
                                    purl = msg.contentMetadata['postEndUrl'].split('homeId=')[1].split('&postId=')
                                    if purl[1] not in wait['postId']:
                                        maxgie.likePost(msg._from, purl[1], random.choice([1001,1002,1003,1004,1005]))
                                    if settings["com"] == True:
                                        maxgie.createComment(msg._from, purl[1], settings["commet"])
                                        wait['postId'].append(purl[1])
                                    else:pass
#=====================================================================
#=====================================================================
        if op.type == 25:
            print("[ 25 ] SEND MESSAGE")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != maxgie.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
                if text.lower() == "ประกาศ":
                    sa="วิธีใช้ ประกาศกลุ่ม >\\<"
                    sa+="\n- ประกาศ ข้อความ/ไอดีไลน์"
                    sa+="\nตัวอย่าง >\\<"
                    sa+="\n- ประกาศ มอนิ่ง/ristmp4260"
                    data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "Maxgie Botline", "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u656416610cb18621ff79bb7a899eb36b"}}
                    sendTemplate(to,data)
                if text.lower() == "ตั้งapi":
                    sa = "วีธีใช้ api >\\<"
                    sa += "\n- ตั้งapi คีย์เวิร์ด;;ตอบกลับ"
                    sa += "\nตัวอย่าง >\\<"
                    sa += "\n- ตั้งapi เทส;;เทสทำไม"
                    data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "Maxgie Botline", "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u656416610cb18621ff79bb7a899eb36b"}}
                    sendTemplate(to,data)
                if text.lower() == "stag":
                    sa = "วิธีใช้ stag >\\<"
                    sa += "\n- stag [เลขที่ต้องการ] @user"
                    sa += "\nตัวอย่าง >\\<"
                    sa += "\n- stag 1 @user"
                    data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "Maxgie Botline", "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u656416610cb18621ff79bb7a899eb36b"}}
                    sendTemplate(to,data)
                if text.lower() == "สะกดกิต":
                    sa = "วิธีใช้ สะกดกิต >\\<"
                    sa += "\n- สะกดกิต [ข้อความ] @user"
                    sa += "\nตัวอย่าง >\\<"
                    sa += "\n- สะกดกิต รักริส @user"
                    data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "Maxgie Botline", "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u656416610cb18621ff79bb7a899eb36b"}}
                    sendTemplate(to,data)
                if text.lower() == "เชคค่า" or text.lower() == "set":
                    sas = "☆ Settings ☆"
                    if settings["autoAdd"] == True: sa = "\n• ออโต้แอด ( เปิด )"
                    else:sa = "\n• ออโต้แอด ( ปิด )"
                    if settings["autoblock"] == True: sa += "\n• ออโต้บล็อค ( เปิด )"
                    else:sa += "\n• ออโต้บล็อค ( ปิด )"
                    if settings["autoCancel"]["on"] == True: sa +="\n• ยกเชิญที่มีสมาชิกต่ำกว่า: " + str(settings["autoCancel"]["members"])
                    else:sa += "\n• ปฏิเสธกลุ่มเชิญ ( ปิด )"
                    if tagadd["tags"] == True: sa += "\n• ตอบกลับคนแทค ( เปิด )"
                    else:sa += "\n• ตอบกลับคนแทค ( ปิด )"
                    if tagadd["tagss"] == True: sa += "\n• ตอบกลับคนแทค2 ( เปิด )"
                    else:sa += "\n• ตอบกลับคนแทค2 ( ปิด )"
                    if sets["tagsticker"] == True: sa += "\n• แทคสติ๊กเกอร์ ( เปิด )"
                    else:sa += "\n• แทคสติ๊กเกอร์ ( ปิด )"
                    if settings["autolike"] == True: sa += "\n• ออโต้ไลค์ ( เปิด )"
                    else:sa += "\n• ออโต้ไลค์ ( ปิด )"
                    if settings["com"] == True: sa += "\n• คอมเม้นโพส ( เปิด )"
                    else:sa += "\n• คอมเม้นโพส ( ปิด )"
                    if settings["Welcome"] == True: sa += "\n• ต้อนรับคนเข้ากลุ่ม ( เปิด )"
                    else:sa += "\n• ต้อนรับคนเข้ากลุ่ม ( ปิด )"
                    if settings["Wc"] == True: sa += "\n• ต้อนรับคนเข้ากลุ่ม2 ( เปิด )"
                    else:sa += "\n• ต้อนรับคนเข้ากลุ่ม2 ( ปิด )"
                    if settings["wcsti2"] == True: sa += "\n• ติ๊กคนเข้ากลุ่ม ( เปิด )"
                    else:sa += "\n• ติ๊กคนเข้ากลุ่ม ( ปิด )"
                    if settings["Leave"] == True: sa += "\n• คนออกกลุ่ม ( เปิด )"
                    else:sa += "\n• คนออกกลุ่ม ( ปิด )"
                    if settings["lv"] == True: sa += "\n• ติ๊กคนออกกลุ่ม ( เปิด )"
                    else:sa += "\n• ติ๊กคนออกกลุ่ม ( ปิด )"
                    if settings["unsendMessage"] == True: sa += "\n• ตรวจจับยกเลิก ( เปิด )"
                    else:sa += "\n• ตรวจจับยกเลิก ( ปิด )"
                    if settings["Sticker"] == True: sa += "\n• เชคติ๊กใหญ่ ( เปิด )"
                    else:sa += "\n• เชคติ๊กใหญ่ ( ปิด )"
                    if sets["Sticker"] == True: sa += "\n• เชคโค๊ดสติ๊กเกอร์ ( เปิด )"
                    else:sa += "\n• เชคโค๊ดสติ๊กเกอร์ ( ปิด )"
                    
                    data = {
                        "type": "flex",
                        "altText": "{}".format(sas),
                        "contents": {
                            "type": "bubble",
                            "styles": {
                                "body": {
                                    "backgroundColor": '#ffffff'
                                },
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": sas,
                                        "color": "#CD1076",
                                        "align": "center",
                                        "weight": "bold",
                                        "size": "xxl"
                                    },
                                    {
                                        "type": "text",
                                        "text": "{}".format(sa),
                                        "wrap": True,
                                        "color": "#ee1289",
                                        "gravity": "center",
                                        "size": "md"
                                    },
                                ]
                            },
                        }
                    }
                    sendTemplate(to, data)
                elif text.lower() == 'clearban' or text.lower() == "ล้างดำ":
                      apalo["Talkblacklist"] = []
                      maxgie.sendMessage(to, "สำเร็จ >_<")
                elif text.lower() == "cancelall" or text.lower() == "ยกเชิญ" and sender == maxgieMID:
                            if msg.toType == 2:
                                group = maxgie.getGroup(to)
                                if group.invitee is None or group.invitee == []:
                                    maxgie.sendMessage(to, "Nothing")
                                else:
                                    invitee = [contact.mid for contact in group.invitee]
                                    for inv in invitee:
                                        maxgie.cancelGroupInvitation(to, [inv])
                                    maxgie.sendMessage(to, "ยกเชิญจำนวน「 {} 」คน".format(str(len(invitee))))
                elif text.lower() == "คทดำ":
                    if msg._from in maxgieMID:
                        if apalo["Talkblacklist"] == []:
                            maxgie.sendMessage(to, "ไม่มีคท.คนติดดำ")
                        else:
                            for bl in apalo["Talkblacklist"]:
                                maxgie.sendMessage(to, text=None, contentMetadata={'mid': bl}, contentType=13)
                elif msg.text.lower().startswith("ตั้งสีme "):
                            text_ = removeCmd("ตั้งสีme", text)
                            try:
                                temp["t"] = text_
                                maxgie.sendMessage(to,"「 โค๊ดสี 」\nคือ : " + text_)
                            except:
                                maxgie.sendMessage(to,"สำเเร็จแล้ว")
                elif msg.text.lower().startswith("สีอักษร "):
                            text_ = removeCmd("สีอักษร", text)
                            try:
                                temp["te"] = text_
                                maxgie.sendMessage(to,"「 โค๊ดสี 」\nคือ : " + text_)
                            except:
                                maxgie.sendMessage(to,"สำเเร็จแล้ว")
                elif msg.text.lower() == "รหัสสี":
                            c="https://i.pinimg.com/originals/d0/9c/8a/d09c8ad110eb44532825df454085a376.jpg"
                            p="https://i.pinimg.com/originals/7c/d3/aa/7cd3aa57150f8f6f18711ff22c9f6d4a.jpg"
                            m="**ตัวอย่างที่1**\nคำสั่งเปลี่ยนสี me\nพิม'ตั้งสีme #FFFFFF'\n**ตัวอย่างที่2**\nคำสั่งเปลี่ยนสี tag\nพิม'ตั้งสีแทค #FFFFFF'"
                            maxgie.sendImageWithURL(to,c)
                            maxgie.sendImageWithURL(to,p)
                            maxgie.sendMessage(to,m)
                elif msg.text.lower().startswith("ตั้งบล็อค "):
                            text_ = removeCmd("ตั้งบล็อค", text)
                            try:
                                tagadd["b"] = text_
                                maxgie.sendMessage(to,"「 ตั้งบล็อคอัตโนมัติ 」\nคือ : " + text_)
                            except:
                                maxgie.sendMessage(to,"สำเเร็จแล้ว")
                elif text.lower().startswith("ตั้งค้างเชิญ "):
                            text_ = removeCmd("ตั้งค้างเชิญ", text)
                            try:
                                settings["autoCancel"]["members"] = text_
                                maxgie.sendMessage(to,"「 ตั้งยกค้างเชิญ 」\nจำนวน : " + text_)
                            except:
                                maxgie.sendMessage(to,"สำเเร็จแล้ว")
                if text.lower() == "ดำ":
                  if msg._from in admin:
                      apalo["Talkwblacklist"] = True
                      maxgie.sendMessage(to,"ส่งคท.มา..")
                if text.lower() == "ขาว":
                  if msg._from in admin:
                      apalo["Talkdblacklist"] = True
                      maxgie.sendMessage(to,"ส่งคท.มา..")
                elif msg.text.lower().startswith("ตั้งแทค "):
                      text_ = removeCmd("ตั้งแทค", text)
                      try:
                          tagadd["tag"] = text_
                          sa = "「 ตั้งคำแทค 」\nคือ : " + text_
                          data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "Maxgie Botline", "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u656416610cb18621ff79bb7a899eb36b"}}
                          sendTemplate(to,data)
                      except:
                          maxgie.sendMessage(to,"Done. >_<")
                elif msg.text.lower().startswith("ตั้งแทคแชท "):
                      text_ = removeCmd("ตั้งแทคแชท", text)
                      try:
                          settings["reply"] = text_
                          sa = "「 ตั้งคำแทค 」\nคือ : " + text_
                          data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "Maxgie Botline", "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u656416610cb18621ff79bb7a899eb36b"}}
                          sendTemplate(to,data)
                      except:
                          maxgie.sendMessage(to,"Done. >_<")
                elif msg.text.lower().startswith("ตั้งต้อนรับ "):
                      text_ = removeCmd("ตั้งต้อนรับ", text)
                      try:
                          tagadd["wctext"] = text_
                          sa = "「 ตั้งต้อนรับ 」\nคือ : " + text_
                          data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "Maxgie Botline", "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u656416610cb18621ff79bb7a899eb36b"}}
                          sendTemplate(to,data)
                      except:
                          maxgie.sendMessags(to,"Done. >_<")
                elif msg.text.lower().startswith("ตั้งคนออก "):
                            text_ = removeCmd("ตั้งคนออก", text)
                            try:
                                tagadd["lv"] = text_
                                maxgie.sendMessage(to,"「 ตั้งคนออก 」\nคือ : " + text_)
                            except:
                                maxgie.sendMessage(to,"สำเเร็จแล้ว")
                elif msg.text.lower().startswith("ตั้งแอด "):
                      text_ = removeCmd("ตั้งแอด", text)
                      try:
                          tagadd["add"] = text_
                          sa = "「 ตั้งแอด 」\nคือ : " + text_
                          data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "Maxgie Botline", "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u656416610cb18621ff79bb7a899eb36b"}}
                          sendTemplate(to,data)
                      except:
                          maxgie.sendMessags(to,"Done. >_<")
                elif msg.text.lower().startswith("ตั้งคอมเม้น "):
                      text_ = removeCmd("ตั้งคอมเม้น", text)
                      try:
                          settings["commet"] = text_
                          sa = "「 ตั้งคอมเม้น 」\nคือ : " + text_
                          data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "Maxgie Botline", "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u656416610cb18621ff79bb7a899eb36b"}}
                          sendTemplate(to,data)
                      except:
                          maxgie.sendMessags(to,"Done. >_<")
                if text.lower() == "เชค":
                    add = tagadd["add"]
                    tag = tagadd["tag"]
                    like = settings["commet"]
                    wc = tagadd["wctext"]
                    lv = tagadd["lv"]
                    c = settings["autoCancel"]["members"]
                    b = tagadd["b"]
                    Re = settings["reply"]
                    maxgie.generateReplyMessage(msg.id)
                    maxgie.sendReplyMessage(msg.id, to, "ข้อความแอด :\n"+str(add)+"\n\nข้อความแทค :\n"+str(tag)+"\n\nข้อความเม้น :\n"+str(like)+"\n\nข้อความต้อนรับ :\n"+str(wc)+"\n\nข้อความคนออก :\n"+str(lv)+"\n\nจำนวนค้างเชิญ :\n"+str(c)+" จำนวน\n\nข้อความบล็อค :\n"+str(b)+"\n\nข้อความแทคแชท :\n"+str(Re))
                if text.lower() == "/คำสั่ง" or text.lower() == "/help":
                    sas = "😀 Help Message 😀\n"
                    sa = "• คท\n"
                    sa += "• ไอดีเรา\n"
                    sa += "• ชื่อเรา\n"
                    sa += "• ตัสเรา\n"
                    sa += "• รูปเรา\n"
                    sa += "• รูปวีดีโอเรา\n"
                    sa += "• ปกเรา\n"
                    sa += "──────────────\n"
                    sa += "• ข้อมูล\n"
                    sa += "• ออน\n"
                    sa += "• รีบอท\n"
                    sa += "• แทค\n"
                    sa += "• ยกเชิญ\n"
                    sa += "• /ลบรัน\n"
                    sa += "• ก็อป @user\n"
                    sa += "• กลับร่าง\n"
                    sa += "──────────────\n"
                    sa += "• สะกดกิต [พิม'สะกดกิต'เพื่อดูวิธี]\n"
                    sa += "• ตั้งapi [พิมเพื่อดูวิธี]\n"
                    sa += "• ล้างapi [คำที่จะลบ]\n"
                    sa += "• เชคapi\n"
                    sa += "• stag [พิม'stag'เพื่อดูวิธี]\n"
                    sa += "• แปรงคท [MID]\n"
                    sa += "• ยูทูป [ข้อความ]\n"
                    sa += "• image [text(ภาษาอังกฤษ)]\n"
                    sa += "• รูป [ข้อความ(ภาษาไทย)]\n"
                    sa += "• เพลสโต [ชื่อแอพ]\n"
                    sa += "• ตั้งรูปโปรไฟล์ [ลิ้งยูทูป]\n"
                    sa += "• ประกาศ [พิม'ประกาศ'เพื่อดูวิธี]\n"
                    sa += "• ยกเลิก [ใส่จำนวนที่จะยกเลิก]\n"
                    sa += "──────────────\n"
                    sa += "• ดำ ส่งคท.\n"
                    sa += "• ขาว ส่งคท.\n"
                    sa += "• ดำ @user\n"
                    sa += "• ล้าง @user\n"
                    sa += "• เชคดำ\n"
                    sa += "• คทดำ\n"
                    sa += "• ล้างดำ\n"
                    sa += "──────────────\n"
                    sa += "• ตั้งต้อนรับ [ข้อความ]\n"
                    sa += "• ตั้งคนออก [ข้อความ]\n"
                    sa += "• ตั้งแอด [ข้อความ]\n"
                    sa += "• ตั้งแทค [ข้อความ]\n"
                    sa += "• ตั้งคอมเม้น [ข้อความ]\n"
                    sa += "──────────────\n"
                    sa += "• เปิดแทค/ปิดแทค\n"
                    sa += "• เปิดแทค2/ปิดแทค2\n"
                    sa += "• เปิดแทค3/ปิดแทค3\n"
                    sa += "• เปิดไลค์/ปิดไลค์\n"
                    sa += "• เปิดคอมเม้น/ปิดคอมเม้น\n"
                    sa += "• เปิดบล็อค/ปิดบล็อค\n"
                    sa += "• เปิดแอด/ปิดแอด\n"
                    sa += "• เปิดกันรัน/ปิดกันรัน\n"
                    sa += "• เปิดต้อนรับ/ปิดต้อนรับ\n"
                    sa += "• เปิดต้อนรับ2/ปิดต้อนรับ2\n"
                    sa += "• เปิดคนออก/ปิดคนออก\n"
                    sa += "• เปิดยกเลิก/ปิดยกเลิก\n"
                    sa += "• เปิดโค๊ดติ๊ก/ปิดโค๊ดติ๊ก\n"
                    sa += "• เปิดติ๊กใหญ่/ปิดติ๊กใหญ่"
                    helps = "{}".format(str(sa))
                    data = {
                        "type": "flex",
                        "altText": "{}".format(sas),
                        "contents": {
                            "type": "bubble",
                            "styles": {
                                "body": {
                                    "backgroundColor": '#6600CC'
                                 },
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type":"text",
                                        "text": sas,
                                        "size":"xl",
                                        "weight":"bold",
                                        "color":"#FFFFFF",
                                        "align":"center"
                                    },
                                    {
                                        "type":"text",
                                        "text": " "
                                    },
                                    {
                                        "type": "text",
                                        "text": "{}".format(sa),
                                        "wrap": True,
                                        "color": "#FFFFFF",
                                        "gravity": "center",
                                        "size": "md"
                                    },
                                    {
                                        "type": "text",
                                        "text": " "
                                    },
                                    {
                                        "type":"button",
                                        "style":"primary",
                                        "color":"#8B814C",
                                        "action": {
                                            "type":"uri",
                                            "label":"ผู้สร้าง",
                                            "uri":"line://ti/p/~ristmp4260"
                                        },
                                    },
                                ]
                            }
                        }
                    }
                    sendTemplate(to, data)
                if text.lower() == "help" or text.lower() == "คำสั่ง":
                            s = "#EE1289"
                            sa = "• me\n"
                            sa += "• /me\n"
                            sa += "• คท\n"
                            sa += "• ไอดีเรา\n"
                            sa += "• ชื่อเรา\n"
                            sa += "• ตัสเรา\n"
                            sa += "• รูปเรา\n"
                            sa += "• รูปวีดีโอเรา\n"
                            sa += "• ปกเรา\n"
                            sa += "• ข้อมูล\n"
                            sa += "• รีบอท\n"
                            sa += "• ออน\n"
                            sa += "• /ลบรัน\n"
                            sa += "• เชค\n"
                            ss = "• แทค\n"
                            sa += "• ยกเชิญ"
                            ss += "• ก็อป @user\n"
                            ss += "• กลับร่าง\n"
                            ss += "• ตั้งapi [พิมเพื่อดูวิธี]\n"
                            ss += "• ล้างapi [คำที่จะลบ]\n"
                            ss += "• เชคapi\n"
                            ss += "• stag [พิม'stag'เพื่อดูวิธี]\n"
                            ss += "• แปรงคท [MID]\n"
                            ss += "• ยูทูป [ข้อความ]\n"
                            ss += "• image [text(ภาษาอังกฤษ)]\n"
                            ss += "• รูป [ข้อความ(ภาษาไทย)]\n"
                            ss += "• เพลสโต [ชื่อแอพ]\n"
                            ss += "• ตั้งรูปโปรไฟล์ [ลิ้งยูทูป]\n"
                            ss += "• ประกาศ [พิม'ประกาศ'เพื่อดูวิธี]\n"
                            ss += "• ยกเลิก [ใส่จำนวนที่จะยกเลิก]"
                            sd = "• ดำ ส่งคท.\n"
                            sd += "• ขาว ส่งคท.\n"
                            sd += "• ดำ @user\n"
                            sd += "• ล้าง @user\n"
                            sd += "• เชคดำ\n"
                            sd += "• คทดำ\n"
                            sd += "• ล้างดำ\n"
                            sd += "• ตั้งต้อนรับ [ข้อความ]\n"
                            sd += "• ตั้งคนออก [ข้อความ]\n"
                            sd += "• ตั้งแอด [ข้อความ]\n"
                            sd += "• ตั้งแทค [ข้อความ]\n"
                            sd += "• ตั้งคอมเม้น [ข้อความ]\n"
                            sd += "• ตั้งค้างเชิญ [จำนวน]\n"
                            sd += "• ตั้งมุดลิ้ง [ข้อความ]\n"
                            sd += "• ตั้งคนบล็อค [ข้อความ]"
                            se = "• เปิดแทค/ปิดแทค\n"
                            se += "• เปิดแทค2/ปิดแทค2\n"
                            se += "• เปิดแทค3/ปิดแทค3\n"
                            se += "• เปิดไลค์/ปิดไลค์\n"
                            se += "• เปิดคอมเม้น/ปิดคอมเม้น\n"
                            se += "• เปิดบล็อค/ปิดบล็อค\n"
                            se += "• เปิดแอด/ปิดแอด\n"
                            se += "• เปิดกันรัน/ปิดกันรัน\n"
                            se += "• เปิดต้อนรับ/ปิดต้อนรับ\n"
                            se += "• เปิดต้อนรับ2/ปิดต้อนรับ2\n"
                            se += "• เปิดคนออก/ปิดคนออก\n"
                            se += "• เปิดยกเลิก/ปิดยกเลิก\n"
                            se += "• เปิดติ๊กคนเข้า/ปิดติ๊กคนเข้า\n"
                            se += "• เปิดติ๊กคนออก/ปิดติ๊กคนออก\n"
                            se += "• เปิดติ๊กใหญ่/ปิดติ๊กใหญ่"
                            sti = "• เปิดมุดลิ้ง/ปิดมุดลิ้ง\n"
                            sti += "• ตั้งติ๊กคนแอด\n"
                            sti += "• ลบติ๊กคนแอด\n"
                       #     sti += "• ตั้งติ๊กแทคแชท\n"
                       #     sti += "• ลบติ๊กแทคแชท\n"
                            sti += "• ตั้งติ๊กคนแทค\n"
                            sti += "• ลบติ๊กคนแทค\n"
                            sti += "• ตั้งติ๊กคนเข้า\n"
                            sti += "• ลบติ๊กคนเข้า\n"
                            sti += "• ตั้งติ๊กคนออก\n"
                            sti += "• ลบติ๊กคนออก\n"
                            sti += "• เขียน [ข้อความ]\n"
                            sti += "• ไอดีไลน์ [idline]\n"
                            sti += "• ดึง @user\n"
                            sti += "• บล็อค @user\n"
                            sti += "• เพิ่มเพื่อน @user\n"
                            sti += "• ลบเพื่อน @user"
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor":"#000000"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": 'https://sv1.picz.in.th/images/2019/02/11/Tjej7Q.jpg',
                                                "size": "xxl"
                                            },
                                            {
                                                "type": "text",
                                                "text": "• คำสั่งส่วนตัว •",
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#CD1076"
                                            },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type": "text",
                                                "text": sa,
                                                "color": s, 
                                                "wrap": True,
                                                "gravity": "center",
                                        #        "size": "md"
                                            },
                                            { 
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                 "type":"button",
                                                 "style":"primary",
                                                 "color":"#EE1289",
                                                 "action":{
                                                     "type":"uri",
                                                     "label":"ติดต่อ",
                                                     "uri":"line://ti/p/~ristmp4260"
                                                 },
                                            },
                                        ]
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": "#000000"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": 'https://sv1.picz.in.th/images/2019/02/11/Tjej7Q.jpg',
                                                "size": "xxl"
                                            },
                                            {
                                                "type": "text",
                                                "text": "• คำสั่งพิเศษ •",
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#CD1076"
                                            },
                                            { 
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type": "text",
                                                "text": ss, 
                                                "color": s,
                                                "wrap": True,
                                                "gravity": "center",
                                            },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                 "type":"button",
                                                 "style":"primary",
                                                 "color":"#EE1289",
                                                 "action":{
                                                     "type":"uri",
                                                     "label":"ติดต่อ",
                                                     "uri":"line://ti/p/~ristmp4260"
                                                 },
                                            },
                                        ]
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": "#000000"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": 'https://sv1.picz.in.th/images/2019/02/11/Tjej7Q.jpg',
                                                "size": "xxl"
                                            },
                                            {
                                                "type": "text",
                                                "text": "• คำสั่งเปิด/ปิด •",
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#CD1076"
                                            },
                                            { 
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type": "text",
                                                "text": se, 
                                                "color": s,
                                                "wrap": True,
                                                "gravity": "center",
                                            },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                 "type":"button",
                                                 "style":"primary",
                                                 "color":"#EE1289",
                                                 "action":{
                                                     "type":"uri",
                                                     "label":"ติดต่อ",
                                                     "uri":"line://ti/p/~ristmp4260"
                                                 },
                                            },
                                        ]
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": "#000000"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": 'https://sv1.picz.in.th/images/2019/02/11/Tjej7Q.jpg',
                                                "size": "xxl"
                                            },
                                            {
                                                "type": "text",
                                                "text": "• คำสั่งตั้งค่า/ติดดำ •",
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#CD1076"
                                            },
                                            { 
                                                "type": "text",
                                                "text": " "
                                            },
                                          #  {
                                          #      "type": "text",
                                           #     "text": " "
                                         #   },
                                         #   {
                                            #    "type": "text",
                                           #     "text": " "
                                          #  },
                                            {
                                                "type": "text",
                                                "text": sd, 
                                                "color": s,
                                           #     "size": "lg",
                                                "wrap": True,
                                                "gravity": "center",
                                            },
                                            #{
                                            #    "type": "text",
                                            #    "text": " "
                                           # },
                                          #  {
                                           #     "type": "text",
                                            #    "text": " "
                                           # },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                          #  {
                                          #      "type": "text",
                                          #      "text": "สนใจบอท ติดต่อได้ที่ปุ่มเลยค้ะ >_<",
                                          #      "color": "#B5B5B5",
                                          #      "size": "xs"
                                          #  },
                                            {
                                                 "type":"button",
                                                 "style":"primary",
                                                 "color":"#EE1289",
                                                 "action":{
                                                     "type":"uri",
                                                     "label":"ติดต่อ",
                                                     "uri":"line://ti/p/~ristmp4260"
                                                 },
                                            },
                                        ]
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": "#000000"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": 'https://sv1.picz.in.th/images/2019/02/11/Tjej7Q.jpg',
                                                "size": "xxl"
                                            },
                                            {
                                                "type": "text",
                                                "text": "• คำสั่งทั่วไป •",
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#CD1076"
                                            },
                                            { 
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type": "text",
                                                "text": sti, 
                                                "color": s,
                                                "wrap": True,
                                                "gravity": "center",
                                            },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                 "type":"button",
                                                 "style":"primary",
                                                 "color":"#EE1289",
                                                 "action":{
                                                     "type":"uri",
                                                     "label":"ติดต่อ",
                                                     "uri":"line://ti/p/~ristmp4260"
                                                 },
                                            },
                                        ]
                                    },
                                },
                            ]
                            data = {
                                "type": "flex",
                                "altText": "Help Message",
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(to, data)
#=====================================================================
                elif msg.text.lower().startswith("ก็อป "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                clone = ast.literal_eval(msg.contentMetadata['MENTION'])
                                clones = clone['MENTIONEES']
                                target = []
                                for clone in clones:
                                    if clone["M"] not in target:
                                        target.append(clone["M"])
                                for she in target:
                                    BackupProfile = maxgie.getContact(sender)
                                    Save1 = "http://dl.profile.line-cdn.net/{}".format(BackupProfile.pictureStatus);Save2 = "{}".format(BackupProfile.displayName);ProfileMe["PictureMe"] = Save1;ProfileMe["NameMe"] = Save2
                                    contact = maxgie.getContact(she);ClonerV2(she)
                                    sendMention(to, contact.mid, "=͟͟͞͞➳ คุณกำลังก็อปปี้", "สำเร็จแล้ว >_<");maxgie.sendContact(to, str(BackupProfile.mid));maxgie.sendContact(to, str(contact.mid))
                elif text.lower() == "กลับร่าง":
                            try:
                                maxgiestatus = maxgie.getProfile()
                                maxgieName = maxgie.getProfile()
                                maxgieName.statusMessage = ProfileMe["statusMessage"]
                                maxgieName.pictureStatus = str(ProfileMe["pictureStatus"])
                                maxgie.updateProfile(maxgiestatus)
                                maxgieName.displayName = ProfileMe["NameMe"]
                                maxgie.updateProfile(maxgieName)
                                path = maxgie.downloadFileURL(ProfileMe["PictureMe"])
                                maxgie.updateProfilePicture(path)
                                coverId = ProfileMe["coverId"]
                                maxgie.updateProfileCoverById(coverId)
                                BackupProfile = maxgie.getContact(sender)
                                sendMention(to, BackupProfile.mid, "=͟͟͞͞➳ กลับบัญชีเดิมเรียบร้อย", ">_<");maxgie.sendContact(to, str(BackupProfile.mid))
                            except Exception as error:
                                maxgie.sendMessage(to,"คุณยังไม่ได้ก็อปปี้ User >_<")
                if text.lower() == "คท":
                    maxgie.generateReplyMessage(msg.id) 
                    maxgie.sendReplyMessage(msg.id, to, None, contentMetadata={'mid': maxgieMID}, contentType=13)
                if text.lower() == "mid" or text.lower() == "ไอดีเรา":
                    maxgie.generateReplyMessage(msg.id)
                    maxgie.sendReplyMessage(msg.id, to,maxgieMID)
                elif text.lower() == "myname" or text.lower() == "ชื่อเรา":
                            h = maxgie.getContact(maxgieMID)
                            maxgie.generateReplyMessage(msg.id)
                            maxgie.sendReplyMessage(msg.id, to, "「 ชื่อของคุณ 」\n"+str(h.displayName))
                elif text.lower() == "mybio" or text.lower() == "ตัสเรา":
                            h = maxgie.getContact(maxgieMID)
                            maxgie.generateReplyMessage(msg.id)
                            maxgie.sendReplyMessage(msg.id, to, "「 ตัสของคุณ 」\n"+str(h.statusMessage))
                elif text.lower() == "mypicture" or text.lower() == "รูปเรา":
                            h = maxgie.getContact(maxgieMID)
                            image = "http://dl.profile.line-cdn.net/" + h.pictureStatus
                            maxgie.generateReplyMessage(msg.id)
                            maxgie.sendReplyImageWithURL(msg.id, to, image)
                elif text.lower() == "myvideo" or text.lower() == "รูปวีดีโอเรา":
                            h = maxgie.getContact(maxgieMID)
                            if h.videoProfile == None:
                            	return maxgie.sendMessage(to, "คุณไม่ได้ใส่รูปวีดีโอ >_<")
                            maxgie.generateReplyMessage(msg.id)
                            maxgie.sendReplyVideoWithURL(msg.id, to,"http://dl.profile.line-cdn.net/" + h.pictureStatus + "/vp")
                elif text.lower() == "mycover" or text.lower() == "ปกเรา":
                            h = maxgie.getContact(maxgieMID)
                            cu = maxgie.getProfileCoverURL(maxgieMID)
                            image = str(cu)
                            maxgie.generateReplyMessage(msg.id)
                            maxgie.sendReplyImageWithURL(msg.id, to, image)
                if text.lower() == "me":
                    cover = maxgie.getProfileCoverURL(maxgie.profile.mid)
                    pp = maxgie.getProfile().pictureStatus
                    profile = "https://profile.line-scdn.net/" + str(pp)
                    name = maxgie.getProfile().displayName
                    status = maxgie.getProfile().statusMessage
                    s = temp["te"]
                    a = temp["t"]
                    data={"type":"flex","altText":"{} sendFlex".format(name),"contents":{"type":"bubble",'styles': {"body":{"backgroundColor":a}},"hero":{"type":"image","url":cover,"size":"full","aspectRatio":"20:13","aspectMode":"cover"},"body":{"type":"box","layout":"vertical","contents":[{"type":"text","text":" "},{"type":"image","url":profile,"size":"lg"},{"type":"text","text":" "},{"type":"text","text":name,"size":"xl","weight":"bold","color":s,"align":"center"},{"type":"text","text":" "},{"type":"text","text":status,"align":"center","size":"xs","color":s,"wrap":True},{"type":"text","text":" "},{"type":"button","style":"primary","color":"#669999","action":{"type":"uri","label":"ADD ME","uri":"line://app/1602687308-GXq4Vvk9?type=video&ocu=https://is.gd/pv49jP&piu=https://i.pinimg.com/originals/63/c4/12/63c412c55c99b6e0742bebaf53dd40d6.jpg"}}]}}}
                    sendTemplate(to, data)
                elif text.lower() == "/me":
                            s = temp["te"]
                            a = temp["t"]
                            contact = maxgie.getContact(maxgieMID)
                            cover = maxgie.getProfileCoverURL(maxgieMID)
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": a},
                                        "body": {"backgroundColor": a},# "separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": a, "separator": True, "separatorColor": s}
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                                        "size": "full",
                                        "aspectRatio": "1:1",
                                        "aspectMode": "fit",
                                    },
                                    "body": {
                                       "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "{}".format(contact.displayName),
                                                "align": "center",
                                                "weight": "bold",
                                                "color": s,
                                                "size": "lg",
                                                'flex': 1
                                            },
                                            {
                                                "type": "text",
                                                "text": "รูปโปรไฟล์ >\\<",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s,
                                                "size": "lg",
                                                'flex': 1,
                                           },
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
                                                        "url": "https://os.line.naver.jp/os/p/"+maxgieMID,
                                                        "size": "md"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "🚧ᴄᴀᴋᴇᴶᴳᴾ™🚧",
                                                        "align": "center",
                                                        "color": s,
                                                        "size": "md",
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line://ti/p/~botjgp00"
                                                        }
                                                    },
                                                    {
                                                        "type": "spacer",
                                                        "size": "sm",
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": a},
                                        "body": {"backgroundColor": a},
                                        "footer": {"backgroundColor": a, "separator": True, "separatorColor": s}
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "{}".format(cover),
                                        "size": "full",
                                        "aspectRatio":"20:13",
                                        "aspectMode":"cover"
                                    },
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "{}".format(contact.mid),
                                                "align": "center",
                                                "color": s,
                                                "size": "sm",
                                                "flex": 1,
                                            },
                                            {
                                                "type": "text",
                                                "text": "รูปปกพื้นหลัง >\\<",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s,
                                                "size": "lg",
                                                'flex': 1,
                                           },
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
                                                        "url": "https://os.line.naver.jp/os/p/"+maxgieMID,
                                                        "size": "md"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "🚧ᴄᴀᴋᴇᴶᴳᴾ™🚧",
                                                        "align": "center",
                                                        "color": s,
                                                        "size": "md",
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line://ti/p/~botjgp00"
                                                        }
                                                    },
                                                    {
                                                        "type": "spacer",
                                                        "size": "sm",
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": a},
                                        "body": {"backgroundColor": a},# "separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": a, "separator": True, "separatorColor": s}
                                    },
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "ชื่อของคุณ",
                                                "size": "lg",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s
                                            },
                                            {
                                                "type": "text",
                                                "text": "{}".format(contact.displayName),
                                                "align": "center",
                                                "color": s,
                                                "size": "md"
                                            },
                                            {
                                                "type": "text",
                                                "text": "-",
                                                "align": "center",
                                                "color": a,
                                                "size": "sm",
                                            },
                                            {
                                                "type": "text",
                                                "text": "สเตตัสของคุณ",
                                                "size": "lg",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s
                                            },
                                            {
                                                "type": "text",
                                                "text": "{}".format(contact.statusMessage),
                                                "align": "center",
                                                "color": s,
                                                "wrap": True,
                                                "size": "md"
                                           },
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
                                                        "url": "https://os.line.naver.jp/os/p/"+maxgieMID,
                                                        "size": "md"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "🚧ᴄᴀᴋᴇᴶᴳᴾ™🚧",
                                                        "align": "center",
                                                        "color": s,
                                                        "size": "md",
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line://ti/p/~botjgp00"
                                                        }
                                                    },
                                                    {
                                                        "type": "spacer",
                                                        "size": "sm"
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                }
                            ]
                            data = {
                                "type": "flex",
                                "altText": "{}".format(contact.displayName),
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(to, data)
                elif text.lower() == "/runtime" or text.lower() == "/ออน":
                    timeNow = time.time() - Start
                    runtime = timeChange(timeNow)
                    run = "「 เวลาออน 」\n"
                    run += runtime
                    helps = "{}".format(str(run))
                    data = {
                        "type": "text",
                        "text": "{}".format(str(run)),
                        "sentBy": {
                             "label": "{}".format(maxgie.getContact(maxgieMID).displayName),
                             "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
                             "linkUrl": "line://nv/profilePopup/mid=ua053fcd4c52917706ae60c811e39d3ea"
                        }
                    }
                    sendTemplate(to, data)
                if text.lower() == "ออน" or text.lower() == "runtime":
                    timeNow = time.time() - Start
                    runtime = timeChange(timeNow)
                    run = "「 เวลาออน 」\n"
                    run += runtime
                    data = {
                        "type": "flex",
                        "altText": "{}".format(run),
                        "contents": {
                            "type": "bubble",
                            "styles": {
                                "body": {
                                    "backgroundColor": '#6600CC'
                                 },
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "{}".format(run),
                                        "wrap": True,
                                        "color": "#FFFFFF",
                                        "align": "center",
                                        "gravity": "center",
                                        "size": "md"
                                    },
                                ]
                            }
                        }
                    }
                    sendTemplate(to, data)
                elif text.lower() == "รีบอท" or text.lower() == "reset":
                    gifnya = ["https://i.pinimg.com/originals/2e/d7/37/2ed737ba301b048afdb355fd9d1c2e86.gif"]
                    data = {
                        "type": "template",
                        "altText": "กำลังรีบอท...",
                        "template": {
                            "type": "image_carousel",
                            "columns": [
                                {
                                     "imageUrl": "{}".format(random.choice(gifnya)),
                                     "size": "full",
                                     "action": {
                                         "type": "uri",
                                          "uri": "line://ti/p/~aboutme.."
                                     }
                                }
                            ]
                        }
                    }
                    sendTemplate(to, data)
                    time.sleep(1)
                    ga = "สำเร็จแล้ว (｀・ω・´)"
                    data = {
                        "type": "text",
                        "text": "{}".format(str(ga)),
                        "sentBy": {
                             "label": "รีบอทสำเร็จ...",
                             "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
                             "linkUrl": "line://nv/profilePopup/mid=ua053fcd4c52917706ae60c811e39d3ea"
                        }
                    }
                    sendTemplate(to, data)
                    restartBot()
                if text.lower() == "/speed" or text.lower() == "/sp" or text.lower() == "/สปีด":
                    start = time.time()
                    maxgie.sendMessage("u21d04f683a70ee8776c4c58a0358c204","speed...")
                    elapsed_time = time.time() - start
                    took = time.time() - start
                    a = "ความเร็ว :\n- เชิร์ฟเวอร์ : %.3f วินาที" % (took)
                    data = {"type": "text","text": "{}".format(a),"sentBy": {"label": "%.10f" % (elapsed_time), "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u656416610cb18621ff79bb7a899eb36b"}}
                    #
                    sendTemplate(to,data)
                if text.lower() == "sp" or text.lower() == "speed":
                    start = time.time()
                    maxgie.sendMessage("u21d04f683a70ee8776c4c58a0358c204","test speed...")
                    elapsed_time = time.time() - start
                    took = time.time() - start
                    a = "ความเร็ว : %.3f วินาที" % (took)
                    data = {
                        "type": "flex",
                        "altText": "BotSpeed",
                        "contents": {
                            "type": "bubble",
                            "hero": {
                                "type":"image",
                                "url":"https://sv1.picz.in.th/images/2019/02/15/T2sqQn.jpg",
                                "size": "full",
                                "aspectRatio": "20:13",
                                "aspectMode": "fit"
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": a,
                                        "wrap": True,
                                        "color":"#363636",
                                        "align": "center",
                                        "gravity": "center",
                                        "size": "md"
                                    },
                                ]
                            }
                        }
                    }
                    sendTemplate(to, data)
                elif text.lower() == 'ข้อมูล' or text.lower() == "about":
                    try:
                        arr = []
                        owner = "u656416610cb18621ff79bb7a899eb36b"
                        creator = maxgie.getContact(owner)
                        contact = maxgie.getContact(maxgieMID)
                        grouplist = maxgie.getGroupIdsJoined()
                        contactlist = maxgie.getAllContactIds()
                        blockedlist = maxgie.getBlockedContactIds()
                        IdsInvit = maxgie.getGroupIdsInvited()
                        times = time.time() - Start
                        runtime = timeChange(times)
                        ret_ = "╭───「 About Your 」"
                        ret_ += "\n├ ชื่อ : {}".format(contact.displayName)
                        ret_ += "\n├ กลุ่ม : {}".format(str(len(grouplist)))
                        ret_ += "\n├ เพื่อน : {}".format(str(len(contactlist)))
                        ret_ += "\n├ บล็อค : {}".format(str(len(blockedlist)))
                        ret_ += "\n├ ค้างเชิญ : {}".format(str(len(IdsInvit)))
                        ret_ += "\n├────────────"
                        ret_ += "\n├ เวลาออนบอท :"
                        ret_ += "\n├ {}".format(str(runtime))
                        ret_ += "\n├────────────"
                        ret_ += "\n├ ผู้สร้าง : {}".format(str(creator.displayName))
                        ret_ += "\n╰───「 About Your 」"
                        feds = "{}".format(str(ret_))
                        data = {
                            "type": "text",
                            "text": "{}".format(str(ret_)),
                            "sentBy": {
                                 "label": "{}".format(maxgie.getContact(maxgieMID).displayName),
                                 "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
                                 "linkUrl": "line://ti/p/~ristmp4260"
                            }
                        }
                        sendTemplate(to, data)
                        maxgie.sendContact(msg.to, creator.mid)
                    except Exception as e:
                        maxgie.sendMessage(msg.to, str(e))
                elif text.lower() == "หลุดมือ":
                            gifnya = ['https://i.pinimg.com/originals/87/a8/9b/87a89b5aeaf35ba0c8879db5a136ccbd.gif']
                            data = {
                                "type": "template",
                                "altText": "Image carouserl",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(random.choice(gifnya)),
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "line://ti/p/~aboutme.."
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
                elif text.lower() == "ยิงๆ" or text.lower() == "ยิง":
                            gifnya = ['https://i.pinimg.com/originals/25/bf/35/25bf35850f22b00ff04505f173e16ec8.gif']
                            data = {
                                "type": "template",
                                "altText": "Image carouserl",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(random.choice(gifnya)),
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "line://ti/p/~aboutme.."
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
                elif msg.text.lower().startswith("ตั้งรูปโปรไฟล์"):
                            link = removeCmd("ตั้งรูปโปรไฟล์", text)
                            contact = maxgie.getContact(sender)
                            maxgie.sendMessage(to, "Type: Profile\n • Detail: Change video url\n • Status: Download...")
                            print("Sedang Mendownload Data ~")
                            pic = "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)
                            subprocess.getoutput('youtube-dl --format mp4 --output TeamAnuBot.mp4 {}'.format(link))
                            pict = maxgie.downloadFileURL(pic)
                            vids = "TeamAnuBot.mp4"
                            changeVideoAndPictureProfile(pict, vids)
                            maxgie.sendMessage(to, "Type: Profile\n • Detail: Change video url\n • Status: Succes")
                            os.remove("TeamAnuBot.mp4")
#=====================================================================
#=====================================================================
                elif msg.text.lower().startswith("ดำ "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                        apalo["Talkblacklist"][ls] = True
                                        maxgie.sendMessage(to, 'Add to TalkBan')
                                    except:
                                        pass
                elif msg.text.lower().startswith("ล้าง "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                        del apalo["Talkblacklist"][ls]
                                        maxgie.sendMessage(to, 'Deleted from TalkBan')
                                    except:
                                        pass
                elif text.lower() == "เชคดำ":
                            if apalo["Talkblacklist"] == {}:
                              maxgie.sendMessage(to,"ไม่พบคนที่เรายัดดำ")
                            else:
                              ma = ""
                              a = 0
                              for m_id in apalo["Talkblacklist"]:
                                  a = a + 1
                                  end = '\n'
                                  ma += str(a) + ". " +maxgie.getContact(m_id).displayName + "\n"
                              maxgie.sendMessage(to,"รายชื่อคนติดดำ :\n\n"+ma+"\nจำนวน %s คนติดดำ" %(str(len(apalo["Talkblacklist"]))))
#=====================================================================                
                if text.lower() == "เปิดบล็อค":
                  if msg._from in admin:
                      settings["autoblock"] = True
                      sa = "เปิดแล้ว (｀・ω・´)"
                  else:
                      sa = "เปิดอยู่แล้ว (｀・ω・´)"
                  maxgie.sendMessage(to, sa)
                if text.lower() == "ปิดบล็อค":
                  if msg._from in admin:
                      settings["autoblock"] = False
                      maxgie.sendMessage(msg.to,"ปิดแล้ว (｀・ω・´)")
                  else:
                      maxgie.sendMessage(msg.to,"ปิดอยู่แล้ว (｀・ω・´)")
                if text.lower() == "เปิดแทค":
                    tagadd["tags"] = True
                    sa = "เปิดแล้วว >_<"
                    maxgie.sendMessage(to,str(sa))
                if text.lower() == "ปิดแทค":
                    tagadd["tags"] = False
                    sa = "ปิดแล้ว >_<"
                    maxgie.sendMessage(to,str(sa))
                if text.lower() == "เปิดกันรัน":
                    settings["autoCancel"]["on"] = True
                    maxgie.sendMessage(to,"เปิดแล้ว >_<")
                if text.lower() == "ปิดกันรัน":
                    settings["autoCancel"]["on"] = False
                    maxgie.sendMessage(to,"ปิดแล้ว >_<")
                if text.lower() == "เปิดแอด":
                    settings["autoAdd"] = True
                    maxgie.sendMessage(to,"เปิดแล้ว >_<")
                if text.lower() == "ปิดแอด":
                    settings["autoAdd"] = False
                    maxgie.sendMessage(to,"ปิดแล้ว >_<")
                if text.lower() == "เปิดไลค์":
                    settings["autolike"] = True
                    maxgie.sendMessage(to,"เปิดแล้ว >_<")
                if text.lower() == "ปิดไลค์":
                    settings["autolike"] = False
                    maxgie.sendMessage(to,"ปิดแล้ว >_<")
                if text.lower() == "เปิดแทค2":
                    tagadd["tagss"] = True
                    maxgie.sendMessage(to, "เปิดแล้ว >_<")
                if text.lower() == "ปิดแทค2":
                    tagadd["tagss"] = False
                    maxgie.sendMessage(to, "ปิดแล้ว >_<")
                if text.lower() == "เปิดคอมเม้น":
                    settings["com"] = True
                    maxgie.sendMessage(to,"เปิดแล้ว >_<")
                if text.lower() == "ปิดคอมเม้น":
                    settings["com"] = False
                    maxgie.sendMessage(to, "ปิดแล้ว >_<")
                if text.lower() == "เปิดต้อนรับ":
                    settings["Welcome"] = True
                    maxgie.sendMessage(to, "เปิดแล้ว >_<")
                if text.lower() == "ปิดต้อนรับ":
                    settings["Welcome"] = False
                    maxgie.sendMessage(to,"ปิดแล้ว >_<")
                if text.lower() == "เปิดต้อนรับ2":
                    settings["Wc"] = True
                    maxgie.sendMessage(to,"เปิดแล้ว >_<")
                if text.lower() == "ปิดต้อนรับ2":
                    settings["Wc"] = False
                    maxgie.sendMessage(to,"ปิดแล้ว >_<")
                if text.lower() == "เปิดคนออก":
                    settings["Leave"] = True
                    maxgie.sendMessage(to,"เปิดแล้ว >_<")
                if text.lower() == "ปิดคนออก":
                    settings["Leave"] = False
                    maxgie.sendMessage(to,"ปิดแล้ว >_<")
                if text.lower() == "เปิดยกเลิก":
                    settings["unsendMessage"] = True
                    maxgie.sendMessage(to, "เปิดแล้ว >_<")
                if text.lower() == "ปิดยกเลิก":
                    settings["unsendMessage"] = False
                    maxgie.sendMessage(to,"ปิดแล้ว >_<")
                if text.lower() == "เปิดติ๊กใหญ่":
                    settings["Sticker"] = True
                    maxgie.sendMessage(to,"เปิดแล้ว >_<")
                if text.lower() == "ปิดติ๊กใหญ่":
                    settings["Sticker"] = False
                    maxgie.sendMessage(to,"ปิดแล้ว >_<")
                if text.lower() == "เปิดโค๊ดติ๊ก":
                    sets["Sticker"] = True
                    maxgie.sendMessage(to,"เปิดแล้ว >_<")
                if text.lower() == "ปิดโค๊ดติ๊ก":
                    sets["Sticker"] = False
                    maxgie.sendMessage(to,"ปิดแล้ว >_<")
                if text.lower() == "เปิดแทค3":
                    sets["tagsticker"] = True
                    maxgie.sendMessage(to,"เปิดแล้ว >_<")
                if text.lower() == "ปิดแทค3":
                    sets["tagsticker"] = False
                    maxgie.sendMessage(to,"ปิดแล้ว >_<")
                if text.lower() == "เปิดติ๊กคนออก":
                    settings["lv"] = True
                    maxgie.sendMessage(to,"เปิดแล้ว >_<")
                if text.lower() == "ปิดติ๊กคนออก":
                    settings["lv"] = False
                    maxgie.sendMessage(to,"ปิดแล้ว >_<")
                if text.lower() == "เปิดติ๊กคนเข้า":
                    settings["wcsti2"] = True
                    maxgie.sendMessage(to,"เปิดแล้ว >_<")
                if text.lower() == "ปิดติ๊กคนเข้า":
                    settings["wcsti2"] = False
                    maxgie.sendMessage(to,"ปิดแล้ว >_<")
                if text.lower() == "เปิดมุดลิ้ง":
                    sets["autoJoinTicket"] = True
                    maxgie.sendMessage(to,"เปิดแล้ว >_<")
                if text.lower() == "ปิดมุดลิ้ง":
                    sets["autoJoinTicket"] = False
                    maxgie.sendMessage(to,"ปิดแล้ว >_<")
                if text.lower() == "welcrot on":
                    sambit["welcomeMessage"] = True
                    maxgie.sendMessage(to,"เปิดแล้ว >_<")
                if text.lower() == "welcrot off":
                    sambit["welcomeMessage"] = False
                    maxgie.sendMessage(to,"ปิดแล้ว >_<")
                if text.lower() == "leavecrot on":
                    sambit["leaveMessage"] = True
                    maxgie.sendMessage(to,"เปิดแล้ว >_<")
                if text.lower() == "leavecrot off":
                    sambit["leaveMessage"] = False
                    maxgie.sendMessage(to,"ปิดแล้ว >_<")
#==============================================================================#
                elif msg.text.lower().startswith("ประกาศ "):
                            delcmd = msg.text.split(" ")
                            get = msg.text.replace(delcmd[0]+" ","").split("/")
                            kw = get[0]
                            ans = get[1]
                            groups = maxgie.getGroupIdsJoined()
                            for group in groups:
                                sa = "「 ประกาศ 」\n\n{}".format(str(kw))
                                data = {
                                    "type": "flex",
                                    "altText": "มาอ่านเอาสิ",
                                    "contents": {
                                        "type": "bubble",
                                        "body": {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                                {
                                                   "type": "text",
                                                   "text": sa,
                                                   "wrap": True,
                                                   "align": "center",
                                                   "gravity": "center",
                                                   "size": "md"
                                               },
                                               {  
                                                   "type":"text",
                                                   "text":" "
                                               },
                                               {
                                                   "type":"button",
                                                   "style":"primary",
                                                   "color":"#FF0066",
                                                   "action": {
                                                       "type": "uri",
                                                       "label": "• แอด •",
                                                       "uri": "line://ti/p/~{}".format(ans),
                                                   }
                                               }
                                           ]
                                        }
                                    }
                                }
                                sendTemplate(group, data)
                                time.sleep(1)
                            maxgie.sendMessage(to, "ส่งคำประกาศจำนวน  {} กลุ่ม".format(str(len(groups))))
#==============================================================================#
                elif text.lower() == "แทค":
                        group = maxgie.getGroup(to);nama = [contact.mid for contact in group.members];nama.remove(maxgie.getProfile().mid)
                        maxgie.datamention(to,'แทคทุกคน',nama)
                elif text.lower() == "/แทค" or text.lower() == "tagall":
                    if msg._from in maxgieMID:
                        group = maxgie.getGroup(msg.to)
                        nama = [contact.mid for contact in group.members]
                        nm1, nm2, nm3, nm4, nm5, nm6, nm7, nm8, nm9, jml = [], [], [], [], [], [], [], [], [], len(nama)
                        if jml <= 20:
                          mentionMembers(msg.to, nama)
                        if jml > 20 and jml < 40:
                          for i in range (0, 19):
                              nm1 += [nama[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, len(nama)):
                              nm2 += [nama[j]]
                          mentionMembers(msg.to, nm2)
                        if jml > 40 and jml < 60:
                          for i in range (0, 19):
                              nm1 += [nama[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, 39):
                              nm2 += [nama[j]]
                          mentionMembers(msg.to, nm2)
                          for k in range (40, len(nama)):
                              nm3 += [nama[k]]
                          mentionMembers(msg.to, nm3)
                        if jml > 60 and jml < 80:
                          for i in range (0, 19):
                              nm1 += [nama[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, 39):
                              nm2 += [nama[j]]
                          mentionMembers(msg.to, nm2)
                          for k in range (40, 59):
                              nm3 += [nama[k]]
                          mentionMembers(msg.to, nm3)
                          for l in range (60, len(nama)):
                              nm4 += [nama[l]]
                          mentionMembers(msg.to, nm4)
                        if jml > 80 and jml < 100:
                          for i in range (0, 19):
                              nm1 += [nama[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, 39):
                              nm2 += [nama[j]]
                          mentionMembers(msg.to, nm2)
                          for k in range (40, 59):
                              nm3 += [nama[k]]
                          mentionMembers(msg.to, nm3)
                          for l in range (60, 79):
                              nm4 += [nama[l]]
                          mentionMembers(msg.to, nm4)
                          for m in range (80, len(nama)):
                              nm5 += [nama[m]]
                          mentionMembers(msg.to, nm5)
                        if jml > 100 and jml < 120:
                          for i in range (0, 19):
                              nm1 += [nama[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, 39):
                              nm2 += [nama[j]]
                          mentionMembers(msg.to, nm2)
                          for k in range (40, 59):
                              nm3 += [nama[k]]
                          mentionMembers(msg.to, nm3)
                          for l in range (60, 79):
                              nm4 += [nama[l]]
                          mentionMembers(msg.to, nm4)
                          for n in range (80, 99):
                              nm5 += [nama[n]]
                          mentionMembers(msg.to, nm5)
                          for o in range (100, len(nama)):
                              nm6 += [nama[o]]
                          mentionMembers(msg.to, nm6)
                        if jml > 120 and jml < 140:
                          for i in range (0, 19):
                              nm1 += [nama[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, 39):
                              nm2 += [nama[j]]
                          mentionMembers(msg.to, nm2)
                          for k in range (40, 59):
                              nm3 += [nama[k]]
                          mentionMembers(msg.to, nm3)
                          for l in range (60, 79):
                              nm4 += [nama[l]]
                          mentionMembers(msg.to, nm4)
                          for n in range (80, 99):
                              nm5 += [nama[n]]
                          mentionMembers(msg.to, nm5)
                          for o in range (100, 119):
                              nm6 += [nama[o]]
                          mentionMembers(msg.to, nm6)
                          for v in range (120, len(nama)):
                              nm7 += [nama[v]]
                          mentionMembers(msg.to, nm7)
                        if jml > 140 and jml < 160:
                          for i in range (0, 19):
                               nm1 += [nama[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, 39):
                              nm2 += [nama[j]]
                          mentionMembers(msg.to, nm2)
                          for k in range (40, 59):
                              nm3 += [nama[k]]
                          mentionMembers(msg.to, nm3)
                          for l in range (60, 79):
                              nm4 += [nama[l]]
                          mentionMembers(msg.to, nm4)
                          for n in range (80, 99):
                              nm5 += [nama[n]]
                          mentionMembers(msg.to, nm5)
                          for o in range (100, 119):
                              nm6 += [nama[o]]
                          mentionMembers(msg.to, nm6)
                          for q in range (120, 139):
                              nm7 += [nama[q]]
                          mentionMembers(msg.to, nm7)
                          for r in range (140, len(nama)):
                              nm8 += [nama[r]]
                          mentionMembers(msg.to, nm8)
                        if jml > 160 and jml < 180:
                          for i in range (0, 19):
                              nm1 += [nama[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, 39):
                              nm2 += [nama[j]]
                          mentionMembers(msg.to, nm2)
                          for k in range (40, 59):
                              nm3 += [nama[k]]
                          mentionMembers(msg.to, nm3)
                          for l in range (60, 79):
                              nm4 += [nama[l]]
                          mentionMembers(msg.to, nm4)
                          for n in range (80, 99):
                              nm5 += [nama[n]]
                          mentionMembers(msg.to, nm5)
                          for o in range (100, 119):
                              nm6 += [nama[o]]
                          mentionMembers(msg.to, nm6)
                          for q in range (120, 139):
                              nm7 += [nama[q]]
                          mentionMembers(msg.to, nm7)
                          for z in range (140, 159):
                              nm8 += [nama[z]]
                          mentionMembers(msg.to, nm8)
                          for f in range (160, len(nama)):
                              nm9 += [nama[f]]
                          mentionMembers(msg.to, nm9)
#==============================================================================#
                elif msg.text.lower().startswith("เขียน "):
                    sep = msg.text.split(" ")
                    textnya = msg.text.replace(sep[0] + " ","")
                    urlnya = "http://chart.apis.google.com/chart?chs=480x80&cht=p3&chtt=" + textnya + "&chts=ee1289,70&chf=bg,s,ff99cc"
                    maxgie.sendImageWithURL(msg.to, urlnya)
                elif msg.text.lower().startswith("ดึง "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                       maxgie.findAndAddContactsByMid(ls)
                                       maxgie.inviteIntoGroup(to, [ls])
                                    except:
                                       maxgie.sendMessage(to, "Limited !")
                elif msg.text.lower().startswith("สะกดกิต"):
                  if msg.toType == 2:
                    data = text.replace("สะกดกิต ","")
                    yud = data.split(' ')
                    yud = yud[0].replace(' ','_')
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            maxgie.unsendMessage(msg_id)
                            maxgie.sendMessage(to, yud,contentMetadata={"MSG_SENDER_NAME": str(maxgie.getContact(ls).displayName),"MSG_SENDER_ICON":"http://dl.profile.line-cdn.net/%s" % maxgie.getContact(ls).pictureStatus})
                elif msg.text.lower().startswith("ยูทูป"):
                            sep = text.split(" ")
                            search = text.replace(sep[0] + " ","")
                            r = requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=10&q={}&type=video&key=AIzaSyAF-_5PLCt8DwhYc7LBskesUnsm1gFHSP8".format(str(search)))
                            data = r.text
                            a = json.loads(data)
                            if a["items"] != []:
                                ret_ = []
                                yt = []
                                for music in a["items"]:
                                    ret_.append({
                                        "type": "bubble",
                                        "styles": {
                                            "header": {
                                                "backgroundColor": "#FF99CC"
                                            },
                                            "body": {
                                               "backgroundColor": "#000000",
                                               "separator": True,
                                               "separatorColor": "#EE1289"
                                            },
                                            "footer": {
                                                "backgroundColor": "#FF99CC",
                                                "separator": True,
                                               "separatorColor": "#EE1289"
                                           }
                                        },
                                        "header": {
                                            "type": "box",
                                            "layout": "horizontal",
                                            "contents": [
                                               {
                                                    "type": "text",
                                                    "text": "Youtube",
                                                    "weight": "bold",
                                                    "color": "#EE1289",
                                                    "size": "sm"
                                                }
                                            ]
                                        },
                                        "hero": {
                                            "type": "image",
                                            "url": "https://i.ytimg.com/vi/{}/maxresdefault.jpg".format(music['id']['videoId']),
                                            "size": "full",
                                            "aspectRatio": "20:13",
                                            "aspectMode": "cover",
                                            "action": {
                                                "type": "uri",
                                                "uri": "line://nv/profilePopup/mid=ub90fee136a68d4602aa10f734f24ff42"
                                            }
                                        },
                                        "body": {
                                            "type": "box",
                                            "spacing": "md",
                                            "layout": "horizontal",
                                            "contents": [{
                                                "type": "box",
                                                "spacing": "none",
                                                "flex": 1,
                                                "layout": "vertical",
                                                "contents": [{
                                                    "type": "image",
                                                    "url": "https://cdn2.iconfinder.com/data/icons/social-icons-circular-color/512/youtube-512.png",
                                                    "aspectMode": "cover",
                                                    "gravity": "bottom",
                                                    "size": "sm",
                                                    "aspectRatio": "1:1",
                                                    "action": {
                                                      "type": "uri",
                                                      "uri": "https://www.youtube.com/watch?v=%s" % music['id']['videoId']
                                                    }
                                                }]
                                            }, {
                                                "type": "separator",
                                                "color": "#EE1289"
                                            }, {
                                                "type": "box",
                                                "contents": [{
                                                    "type": "text",
                                                    "text": "Title",
                                                    "color": "#EE1289",
                                                    "size": "md",
                                                    "weight": "bold",
                                                    "flex": 1,
                                                    "gravity": "top"
                                                }, {
                                                    "type": "text",
                                                    "text": "%s" % music['snippet']['title'],
                                                    "color": "#EE1289",
                                                    "size": "sm",
                                                    "weight": "bold",
                                                    "flex": 3,
                                                    "wrap": True,
                                                    "gravity": "top"
                                                }],
                                                "flex": 2,
                                                "layout": "vertical"
                                            }]
                                        },
                                        "footer": {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [{
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [{
                                                    "type": "button",
                                                    "flex": 2,
                                                    "style": "primary",
                                                    "color": "#EE1289",
                                                    "height": "sm",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Page",
                                                        "uri": "https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                                                    }
                                                }, {
                                                    "flex": 3,
                                                    "type": "button",
                                                    "margin": "sm",
                                                    "style": "primary",
                                                    "color": "#EE1289",
                                                    "height": "sm",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Mp3",
                                                        "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=youtubemp3%20https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                                                    }
                                                }]
                                            }, {
                                                "type": "button",
                                                "margin": "sm",
                                                "style": "primary",
                                                "color": "#EE1289",
                                                "height": "sm",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "Mp4",
                                                    "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=youtubemp4%20https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                                                }
                                            }]
                                        }
                                    }
                                )
                                    yt.append('https://www.youtube.com/watch?v=' +music['id']['videoId'])
                                k = len(ret_)//10
                                for aa in range(k+1):
                                    data = {
                                        "type": "flex",
                                        "altText": "Youtube",
                                        "contents": {
                                            "type": "carousel",
                                            "contents": ret_[aa*10 : (aa+1)*10]
                                        }
                                    }
                                    sendTemplate(to, data)
                elif msg.text.lower().startswith("image "):
                                query = removeCmd("image", text)
                                cond = query.split("|")
                                search = str(cond[0])
                                r = requests.get("https://cryptic-ridge-9197.herokuapp.com/api/imagesearch/{}".format(str(search)))
                                data=r.text
                                data=json.loads(r.text)
                                if data != []:
                                    ret_ = []
                                    for food in data:
                                        if 'http://' in food["url"]:
                                            pass
                                        else:
                                            if len(ret_) >= 10:
                                                pass
                                            else:
                                                ret_.append({
                                                    "imageUrl": "{}".format(str(food["url"])),
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Send Image",
                                                        "uri": "line://app/1602687308-GXq4Vvk9?type=image&img={}".format(str(food["url"]))
                                                        }
                                                    }
                                                )
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                            "type": "template",
                                            "altText": "sendImage",
                                            "template": {
                                                "type": "image_carousel",
                                                "columns": ret_[aa*10 : (aa+1)*10]
                                            }
                                        }
                                        sendTemplate(to, data)
                elif msg.text.lower().startswith("เพลสโต "):
                                query = removeCmd("เพลสโต", text)
                                cond = query.split("|")
                                search = str(cond[0])
                                result = requests.get("http://api.farzain.com/playstore.php?id={}&apikey=KJaOT94NCD1bP1veQoJ7uXc9M".format(str(search)))
                                data = result.text
                                data = json.loads(data)
                                if data != []:
                                    ret_ = []
                                    for music in data:
                                        if 'http://' in music["url"]:
                                            pass
                                        else:
                                            if len(ret_) >= 10:
                                                pass
                                            else:
                                                ret_.append({
                                                    "imageUrl": "{}".format(str(music["icon"])),
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Download",
                                                        "uri": "{}".format(str(music["url"]))
                                                        }
                                                    }
                                                )
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                            "type": "template",
                                            "altText": "Searching App",
                                            "template": {
                                                "type": "image_carousel",
                                                "columns": ret_[aa*10 : (aa+1)*10]
                                            }
                                        }
                                        sendTemplate(to, data)
                elif msg.text.lower().startswith("รูป "):
                                query = removeCmd("รูป", text)
                                cond = query.split("|")
                                search = str(cond[0])
                                result = requests.get("https://api.boteater.co/googleimg?search={}".format(str(search)))
                                data = result.text
                                data = json.loads(data)
                                if data["result"] != []:
                                    ret_ = []
                                    for fn in data["result"]:
                                        if 'http://' in fn["img"]:
                                            pass
                                        else:
                                            if len(ret_) >= 10:
                                                pass
                                            else:
                                                ret_.append({
                                                    "imageUrl": "{}".format(str(fn["img"])),
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Send Image",
                                                        "uri": "line://app/1602687308-GXq4Vvk9?type=image&img={}".format(str(fn["img"]))
                                                        }
                                                    }
                                                )
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                            "type": "template",
                                            "altText": "Google_Image",
                                            "template": {
                                                "type": "image_carousel",
                                                "columns": ret_[aa*10 : (aa+1)*10]
                                            }
                                        }
                                        sendTemplate(to, data)
                elif msg.text.lower().startswith('ยกเลิก '):
                            maxgie.unsendMessage(msg.id)
                            j = int(msg.text.split(' ')[1])
                            a = [maxgie.adityasplittext(msg.text,'s').replace('{} '.format(j),'')]*j
                            if len(msg.text.split(' ')) == 2:
                                h = wait['Unsend'][msg.to]['B']
                                n = len(wait['Unsend'][msg.to]['B'])
                                for b in h[:j]:
                                    try:
                                        maxgie.unsendMessage(b)
                                        wait['Unsend'][msg.to]['B'].remove(b)
                                    except:pass
                                t = len(wait['Unsend'][msg.to]['B'])
                            if len(msg.text.split(' ')) >= 3:h = [maxgie.unsendMessage(maxgie.sendMessage(to,maxgie.adityasplittext(msg.text,'s')).id) for b in a]
                elif msg.text.lower().startswith("เพิ่มเพื่อน "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = maxgie.getContact(ls)
                                    maxgie.findAndAddContactsByMid(ls)
                                maxgie.generateReplyMessage(msg.id)
                                maxgie.sendReplyMessage(msg.id, to, "Success add " + str(contact.displayName) + " to Friendlist")
                elif msg.text.lower().startswith("ลบเพื่อน "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = maxgie.getContact(ls)
                                    n = len(maxgie.getAllContactIds())
                                    try:
                                        maxgie.deleteContact(ls)
                                    except:pass
                                    t = len(maxgie.getAllContactIds())
                                    maxgie.generateReplyMessage(msg.id)
                                    maxgie.sendReplyMessage(msg.id, to, "Type: Friendlist\n • Detail: Delete friend\n • Status: Succes..\n • Before: %s Friendlist\n • After: %s Friendlist"%(n,t))
                elif msg.text.lower().startswith("บล็อค "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = maxgie.getContact(ls)
                                    maxgie.blockContact(ls)
                                maxgie.generateReplyMessage(msg.id)
                                maxgie.sendReplyMessage(msg.id, to, "Success add " + str(contact.displayName) + " to Blocklist")
                elif msg.text.lower().startswith("ไอดีไลน์ "):
                            a = removeCmd("ไอดีไลน์", text)
                            b = maxgie.findContactsByUserid(a)
                            line = b.mid
                            maxgie.sendMessage(msg.to,"line://ti/p/~" + a)
                            maxgie.sendContact(to, line)                                                                                           
                            maxgie.sendMessage(to,str(hasil))
                elif msg.text.lower().startswith("stag "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = maxgie.getGroup(to)
                    for x in range(jml):
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for receiver in lists:
                                contact = maxgie.getContact(receiver)
                                RhyN_(to, contact.mid)
                elif "/ลบรัน" in msg.text.lower():
                    spl = re.split("/ลบรัน",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        spl[1] = spl[1].strip()
                        ag = maxgie.getGroupIdsInvited()
                        txt = "กำลังยกเลิกค้างเชิญจำนวน "+str(len(ag))+" กลุ่ม"
                        if spl[1] != "":
                            txt = txt + " ด้วยข้อความ \""+spl[1]+"\""
                        txt = txt + "\nกรุณารอสักครู่.."
                        data = {"type": "text","text": "{}".format(str(txt)),"sentBy": {"label": "{}".format(maxgie.getContact(maxgieMID).displayName),"iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=ub90fee136a68d4602aa10f734f24ff42"}}
                        sendTemplate(to, data)
                        procLock = len(ag)
                        for gr in ag:
                            try:
                                maxgie.acceptGroupInvitation(gr)
                                if spl[1] != "":
                                    maxgie.sendMessage(gr,spl[1])
                                maxgie.leaveGroup(gr)
                            except:
                                pass
                        sis = "สำเร็จแล้ว (｀・ω・´)"
                        data = {"type": "text","text": "{}".format(str(sis)),"sentBy": {"label": "{}".format(maxgie.getContact(maxgieMID).displayName),"iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=ub90fee136a68d4602aa10f734f24ff42"}}
                        sendTemplate(to, data)
#=====================================================================
                elif msg.text.lower()== "ตั้งติ๊กคนแทค":
                    sets["messageSticker"]["addStatus"] = True
                    sets["messageSticker"]["addName"] = "tag"
                    maxgie.sendMessage(to, "ส่งสติกเกอรที่จะใช่ลงมา")
                elif msg.text.lower() == "ลบติ๊กคนแทค":
                    sets["messageSticker"]["listSticker"]["tag"] = None
                    maxgie.sendMessage(to, "ลบสติกเกอรคนแทคแล้ว")
                elif msg.text.lower()== "ตั้งติ๊กคนเข้า":
                    sets["messageSticker"]["addStatus"] = True
                    sets["messageSticker"]["addName"] = "wc"
                    maxgie.sendMessage(to, "ส่งสติกเกอรที่จะใช่ลงมา")
                elif msg.text.lower() == "ลบติ๊กคนเข้า":
                    sets["messageSticker"]["listSticker"]["wc"] = None
                    maxgie.sendMessage(to, "ลบสติกเกอรคนเข้าแล้ว")
                elif msg.text.lower()== "ตั้งติ๊กคนออก":
                    sets["messageSticker"]["addStatus"] = True
                    sets["messageSticker"]["addName"] = "lv"
                    maxgie.sendMessage(to, "ส่งสติกเกอรที่จะใช่ลงมา")
                elif msg.text.lower() == "ลบติ๊กคนออก":
                    sets["messageSticker"]["listSticker"]["lv"] = None
                    maxgie.sendMessage(to, "ลบสติกเกอรคนออกแล้ว")
                elif msg.text.lower()== "ตั้งติ๊กคนแอด":
                    sets["messageSticker"]["addStatus"] = True
                    sets["messageSticker"]["addName"] = "add"
                    maxgie.sendMessage(to, "ส่งสติกเกอรที่จะใช่ลงมา")
                elif msg.text.lower() == "ลบติ๊กคนแอด":
                    sets["messageSticker"]["listSticker"]["add"] = None
                    maxgie.sendMessage(to, "ลบสติกเกอรคนแอดแล้ว")
                elif msg.text.lower() == "ตั้งติ๊กมุดลิ้ง":
                    sets["messageSticker"]["addStatus"] = True
                    sets["messageSticker"]["addName"] = "join2"
                    maxgie.sendMessage(to, "ส่งสติกเกอรที่จะใช่ลงมา")
                elif msg.text.lower() == "ลบติ๊กมุดลิ้ง":
                    sets["messageSticker"]["listSticker"]["join2"] = None
                    maxgie.sendMessage(to, "ลบสติกเกอรแล้ว")
#=====================================================================
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != maxgie.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
                elif msg.contentType == 7:
                    if sets["Sticker"] == True:
                        try:
                            stk_id = msg.contentMetadata['STKID']
                            stk_ver = msg.contentMetadata['STKVER']
                            pkg_id = msg.contentMetadata['STKPKGID']
                            ret_ = "「 Check Sticker 」\n"
                            ret_ += "\nSTKID : {}".format(stk_id)
                            ret_ += "\nSTKPKGID : {}".format(pkg_id)
                            ret_ += "\nSTKVER : {}".format(stk_ver)
                            ret_ += "\nLINK : line://shop/detail/{}".format(pkg_id)
                            print(msg)
                            maxgie.sendImageWithURL(to, "http://dl.stickershop.line.naver.jp/products/0/0/"+msg.contentMetadata["STKVER"]+"/"+msg.contentMetadata["STKPKGID"]+"/WindowsPhone/stickers/"+msg.contentMetadata["STKID"]+".png")
                            maxgie.sendMessage(to, str(ret_))
                        except Exception as error:
                            maxgie.sendMessage(to, str(error))
                if msg.text:
                    if msg.text.lower().lstrip().rstrip() in wbanlist:
                        if msg.text not in maxgieMID:
                            try:
                                maxgie.kickoutFromGroup(msg.to,[sender])
                                maxgie.sendMessage("บอกแล้อย่าพิมไม่เชื่อจุกไปสิ55555")
                            except Exception as e:
                                print(e)
                    if "/ti/g/" in msg.text.lower():
                        if sets["autoJoinTicket"] == True:
                            link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                            links = link_re.findall(text)
                            n_links = []
                            for l in links:
                                if l not in n_links:
                                    n_links.append(l)
                            for ticket_id in n_links:
                                group = maxgie.findGroupByTicket(ticket_id)
                                maxgie.acceptGroupInvitationByTicket(group.id,ticket_id)
                                maxgie.sendMessage(group.id,str(tagadd["m"]))
                            #    msgSticker = sets["messageSticker"]["listSticker"]["join2"]
                            #    if msgSticker != None:
                            #        sid = msgSticker["STKID"]
                            #        spkg = msgSticker["STKPKGID"]
                            #        sver = msgSticker["STKVER"]
                            #        sendSticker(group.id, str(sver), str(spkg), str(sid))
                                maxgie.sendMessage(to, "เข้าไปสิงในห้องชื่อ %s 👈 เรียบร้อยแล้ว" % str(group.name))
                if msg.contentType == 7:
                    if sets["messageSticker"]["addStatus"] == True:
                        name = sets["messageSticker"]["addName"]
                        if name != None and name in sets["messageSticker"]["listSticker"]:
                            sets["messageSticker"]["listSticker"][name] = {
                                "STKID": msg.contentMetadata["STKID"],
                                "STKVER": msg.contentMetadata["STKVER"],
                                "STKPKGID": msg.contentMetadata["STKPKGID"]
                            }
                            maxgie.sendMessage(to, "Success Added " + name)
                        sets["messageSticker"]["addStatus"] = False
                        sets["messageSticker"]["addName"] = None
                    if sets["addSticker"]["status"] == True:
                        stickers[sets["addSticker"]["name"]]["STKVER"] = msg.contentMetadata["STKVER"]
                        stickers[sets["addSticker"]["name"]]["STKID"] = msg.contentMetadata["STKID"]
                        stickers[sets["addSticker"]["name"]]["STKPKGID"] = msg.contentMetadata["STKPKGID"]
                        f = codecs.open('sticker.json','w','utf-8')
                        json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                        maxgie.sendMessage(to, "Success Added sticker {}".format(str(sets["addSticker"]["name"])))
                        sets["addSticker"]["status"] = False
                        sets["addSticker"]["name"] = ""
            elif msg.contentType == 7:
                if sets["Sticker"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    ret_ = "╔══[ Sticker Info ]"
                    ret_ += "\n╠ STICKER ID : {}".format(stk_id)
                    ret_ += "\n╠ STICKER PACKAGES ID : {}".format(pkg_id)
                    ret_ += "\n╠ STICKER VERSION : {}".format(stk_ver)
                    ret_ += "\n╠ STICKER URL : line://shop/detail/{}".format(pkg_id)
                    ret_ += "\n╚══[ Finish ]"
                    maxgie.sendMessage(to, str(ret_))
#=====================================================================
#========================================================================
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != maxgie.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
                if text.lower() == ".":
                    maxgie.sendMessage(to,"[ MaxGie Botline ]\nadmin :\nline://ti/p/~aboutme..")
#========================================================================
            elif msg.contentType == 7: # Content type is sticker
                if settings['Sticker']:
                    if 'STKOPT' in msg.contentMetadata:
                        contact = maxgie.getContact(sender)
                        A = contact.displayName
                        stk = msg.contentMetadata['STKID']
                        spk = msg.contentMetadata['STKPKGID']
                        data={'type':'template','altText': str(A)+' ส่งสติ๊กเกอร์','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker_animation@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                        sendTemplate(to, data)
                    else:
                        contact = maxgie.getContact(sender)
                        A = contact.displayName
                        stk = msg.contentMetadata['STKID']
                        spk = msg.contentMetadata['STKPKGID']
                        data={'type':'template','altText': str(A)+' ส่งสติ๊กเกอร์','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                        sendTemplate(to, data)
        if op.type == 26:
            print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            cmd = command(text)
            isValid = True
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False: setKey = ''
            if isValid != False:
             #   elif msg.contentType == 7:
                if msg.toType == 0 and sender != maxgieMID: to = sender
                else: to = receiver
            #    elif msg.contentType == 7:
            #        if "/ti/g/" in msg.text.lower():
            #            if sets["autoJoinTicket"] == True:
            #                link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
            #                links = link_re.findall(text)
            #                n_links = []
            #                for l in links:
            #                    if l not in n_links:
            #                        n_links.append(l)
            #                for ticket_id in n_links:
            #                    group = maxgie.findGroupByTicket(ticket_id)
            #                    maxgie.acceptGroupInvitationByTicket(group.id,ticket_id)
                                #
             #                   maxgie.sendMessage(to, "เข้าไปสิงในห้องชื่อ %s 👈 เรียบร้อยแล้ว" % str(group.name))
                if msg.contentType == 0 and sender not in maxgieMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        if tagadd["tags"] == True:
                            contact = maxgie.getContact(msg._from) 
                            pict = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            name = re.findall(r'@(\w+)', msg.text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            for mention in mentionees:
                                 if maxgieMID in mention["M"]:
                                     data = {
                                         "type": "flex",
                                         "altText": "{}".format(tagadd["tag"]),
                                         "contents": {
                                             "type": "bubble",
                                             "styles": {
                                                 "body": {
                                                     "backgroundColor": '#6600CC'
                                                  },
                                             },
                                             "body": {
                                                 "type": "box",
                                                 "layout": "vertical",
                                                 "contents": [
                                                     {
                                                         "type": "text",
                                                         "text": "{}".format(tagadd["tag"]),
                                                         "wrap": True,
                                                         "color": "#FFFFFF",
                                                         "align": "start",
                                                         "gravity": "center",
                                                         "size": "md"
                                                     },
                                                 ]
                                             }
                                         }
                                     }
                                     sendTemplate(to, data)
                if msg.contentType == 0 and sender not in maxgieMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        if tagadd["tagss"] == True:
                            contact = maxgie.getContact(sender)
                            cover = maxgie.getProfileCoverURL(sender)
                            names = contact.displayName
                            status = contact.statusMessage
                            pp = contact.pictureStatus
                            name = re.findall(r'@(\w+)', msg.text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            for mention in mentionees:
                                 if maxgieMID in mention["M"]:
                                     data = {
                                         "type": "flex",
                                         "altText": "tagall",
                                         "contents": {
                                             "type": "bubble",
                                             'styles': {
                                                 "body": {
                                                     "backgroundColor": '#6600CC'
                                                 },
                                             },
                                             "hero": {
                                                 "type":"image",
                                                 "url": cover,
                                                 "size":"full",
                                                 "aspectRatio":"20:13",
                                                 "aspectMode":"cover"
                                             },
                                             "body": {
                                                 "type": "box",
                                                 "layout": "vertical",
                                                 "contents": [
                                                     {
                                                         "type": "image",
                                                         "url": "https://profile.line-scdn.net/" + str(pp),
                                                         "size": "lg"
                                                     },
                                                     {
                                                          "type":"text",
                                                          "text":" "
                                                     },
                                                     {
                                                         "type":"text",
                                                         "text":"{}".format(names),
                                                         "size":"xl",
                                                         "weight":"bold",
                                                         "color":"#FFFFFF",
                                                         "align":"center"
                                                     },
                                                     {
                                                         "type": "text",
                                                         "text": status,
                                                         "wrap": True,
                                                         "align": "center",
                                                         "gravity": "center",
                                                         "color": "#FFFFFF",
                                                         "size": "md"
                                                     },
                                                 ]
                                             }
                                         }
                                     }
                                     sendTemplate(to, data)
                if msg.contentType == 0 and sender not in maxgieMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        if sets["tagsticker"] == True:
                            name = re.findall(r'@(\w+)', msg.text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            for mention in mentionees:
                                 if maxgieMID in mention["M"]:
                                    #  contact = maxgie.getContact(maxgieMID)
                                   #   a = contact.displayName
                                      msg = sets["messageSticker"]["listSticker"]["tag"]
                                      if msg != None:
                                          contact = maxgie.getContact(maxgieMID)
                                          a = contact.displayName
                                          stk = msg['STKID']
                                          spk = msg['STKPKGID']
                                          data={'type':'template','altText': str(a)+' ส่งสติ๊กเกอร์','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker_animation@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                                          sendTemplate(to, data)
                                      else:
                                          contact = maxgie.getContact(maxgieMID)
                                          a = contact.displayName
                                          stk = msg['STKID']
                                          spk = msg['STKPKGID']
                                          data={'type':'template','altText': str(a)+'ส่งสติ๊กเกอร์','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                                          sendTemplate(to, data)
#==============================================================================#
        if op.type == 19:
            if maxgieMID in op.param3:
                apalo["Talkblacklist"][op.param2] = True
        if op.type == 26 or op.type == 25:
            msg = op.message
            sender = msg._from
            try:
               if mc["wr"][str(msg.text)]:
                   maxgie.sendMessage(msg.to,mc["wr"][str(msg.text)])
            except:
              pass
        if op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != maxgie.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
                if msg.text.lower().startswith("แปรงคท "):
                    delcmd = msg.text.split(" ")
                    getx = msg.text.replace(delcmd[0] + " ","")
                    maxgie.sendContact(msg.to,str(getx))
                if msg.text.startswith("ตั้งapi "):
                    try:
                        delcmd = msg.text.split(" ")
                        get = msg.text.replace(delcmd[0]+" ","").split(";;")
                        kw = get[0]
                        ans = get[1]
                        mc["wr"][kw] = ans
                        f=codecs.open('sb.json','w','utf-8')
                        json.dump(mc, f, sort_keys=True, indent=4, ensure_ascii=False)
                        maxgie.sendMessage(msg.to,"คีย์เวิร์ด: " + str(kw) + "\nตอบกลับ: "+ str(ans))
                    except Exception as Error:
                        print(Error)
                if msg.text.startswith("ล้างapi "):
                    try:
                        delcmd = msg.text.split(" ")
                        getx = msg.text.replace(delcmd[0] + " ","")
                        del mc["wr"][getx]
                        maxgie.sendMessage(msg.to, "คำ " + str(getx) + " ล้างแล้ว")
                        f=codecs.open('sb.json','w','utf-8')
                        json.dump(mc, f, sort_keys=True, indent=4, ensure_ascii=False)
                    except Exception as Error:
                        print(Error)
                if msg.text.lower() == "เชคapi":
                    lisk = "[ คำตอบโต้ทั้งหมด ]\n"
                    for i in mc["wr"]:
                        lisk+="\nคีย์เวิร์ด: "+str(i)+"\nตอบโต้: "+str(mc["wr"][i])+"\n"
                    lisk+="\nวิธีล้างapi >\\<\nล้างapi ตามด้วยคำที่จะล้าง"
                    data = {"type": "text","text": "{}".format(lisk),"sentBy": {"label": "Maxgie Botline", "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u656416610cb18621ff79bb7a899eb36b"}}
                    sendTemplate(to,data)
#==============================================================================#
#==============================================================================#
        if op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != maxgie.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
#========================================================================
                if msg.contentType == 7:
                    if sets["messageSticker"]["addStatus"] == True:
                        name = sets["messageSticker"]["addName"]
                        if name != None and name in sets["messageSticker"]["listSticker"]:
                            sets["messageSticker"]["listSticker"][name] = {
                                "STKID": msg.contentMetadata["STKID"],
                                "STKVER": msg.contentMetadata["STKVER"],
                                "STKPKGID": msg.contentMetadata["STKPKGID"]
                            }
                            maxgie.sendMessage(to, "Success Added " + name)
                        sets["messageSticker"]["addStatus"] = False
                        sets["messageSticker"]["addName"] = None
                    if sets["addSticker"]["status"] == True:
                        stickers[sets["addSticker"]["name"]]["STKVER"] = msg.contentMetadata["STKVER"]
                        stickers[sets["addSticker"]["name"]]["STKID"] = msg.contentMetadata["STKID"]
                        stickers[sets["addSticker"]["name"]]["STKPKGID"] = msg.contentMetadata["STKPKGID"]
                        f = codecs.open('sticker.json','w','utf-8')
                        json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                        line.sendMessage(to, "Success Added sticker {}".format(str(sets["addSticker"]["name"])))
                        sets["addSticker"]["status"] = False
                        sets["addSticker"]["name"] = ""
                        
        if op.type == 26:
            print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            cmd = command(text)
            isValid = True
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False: setKey = ''
            if isValid != False:
                if msg.toType == 0 and sender != maxgieMID: to = sender
                else: to = receiver
                if msg.contentType == 0 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            if msg.location != None:
                                unsendmsg = time.time()
                                msg_dict[msg.id] = {"location":msg.location,"from":msg._from,"waktu":unsendmsg}
                            else:
                                unsendmsg = time.time()
                                msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"waktu":unsendmsg}
                        except Exception as e:
                            print (e)
                if msg.contentType == 1 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg1 = time.time()
                            path = maxgie.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"image":path,"waktu":unsendmsg1}
                        except Exception as e:
                            print (e)
                if msg.contentType == 2 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg2 = time.time()
                            path = maxgie.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"video":path,"waktu":unsendmsg2}
                        except Exception as e:
                            print (e)
                if msg.contentType == 3 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg3 = time.time()
                            path = maxgie.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"audio":path,"waktu":unsendmsg3}
                        except Exception as e:
                            print (e)
                if msg.contentType == 7 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg7 = time.time()
                            sticker = msg.contentMetadata["STKID"]
                            link = "http://dl.stickershop.line.naver.jp/stickershop/v1/sticker/{}/android/sticker.png".format(sticker)
                            msg_dict[msg.id] = {"from":msg._from,"sticker":link,"waktu":unsendmsg7}
                        except Exception as e:
                            print (e)
                if msg.contentType == 13 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg13 = time.time()
                            mid = msg.contentMetadata["mid"]
                            msg_dict[msg.id] = {"from":msg._from,"mid":mid,"waktu":unsendmsg13}
                        except Exception as e:
                            print (e)
                if msg.contentType == 14 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg14 = time.time()
                            path = maxgie.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"file":path,"waktu":unsendmsg14}
                        except Exception as e:
                            print (e)
        if op.type == 65:
            if op.param1 not in chatbot["botMute"]:
                if settings["unsendMessage"] == True:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        ah = time.time()
                        ikkeh = maxgie.getContact(msg_dict[msg_id]["from"])
                        if "text" in msg_dict[msg_id]:
                            waktumsg = ah - msg_dict[msg_id]["waktu"]
                            waktumsg = format_timespan(waktumsg)
                            rat_ = "\nSend At :\n{} ago".format(waktumsg)
                            rat_ += "\nText :\n{}".format(msg_dict[msg_id]["text"])
                            sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                            del msg_dict[msg_id]
                        else:
                            if "image" in msg_dict[msg_id]:
                                waktumsg = ah - msg_dict[msg_id]["waktu"]
                                waktumsg = format_timespan(waktumsg)
                                rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                rat_ += "\nImage :\nBelow"
                                sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                maxgie.sendImage(at, msg_dict[msg_id]["image"])
                                del msg_dict[msg_id]
                            else:
                                if "video" in msg_dict[msg_id]:
                                    waktumsg = ah - msg_dict[msg_id]["waktu"]
                                    waktumsg = format_timespan(waktumsg)
                                    rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                    rat_ += "\nVideo :\nBelow"
                                    sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                    maxgie.sendVideo(at, msg_dict[msg_id]["video"])
                                    del msg_dict[msg_id]
                                else:
                                    if "audio" in msg_dict[msg_id]:
                                        waktumsg = ah - msg_dict[msg_id]["waktu"]
                                        waktumsg = format_timespan(waktumsg)
                                        rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                        rat_ += "\nAudio :\nBelow"
                                        sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                        maxgie.sendAudio(at, msg_dict[msg_id]["audio"])
                                        del msg_dict[msg_id]
                                    else:
                                        if "sticker" in msg_dict[msg_id]:
                                            waktumsg = ah - msg_dict[msg_id]["waktu"]
                                            waktumsg = format_timespan(waktumsg)
                                            rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                            rat_ += "\nSticker :\nBelow"
                                            sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                            maxgie.sendImageWithURL(at, msg_dict[msg_id]["sticker"])
                                            del msg_dict[msg_id]
                                        else:
                                            if "mid" in msg_dict[msg_id]:
                                                waktumsg = ah - msg_dict[msg_id]["waktu"]
                                                waktumsg = format_timespan(waktumsg)
                                                rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                                rat_ += "\nContact :\nBelow"
                                                sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                                maxgie.sendContact(at, msg_dict[msg_id]["mid"])
                                                del msg_dict[msg_id]
                                            else:
                                                if "location" in msg_dict[msg_id]:
                                                    waktumsg = ah - msg_dict[msg_id]["waktu"]
                                                    waktumsg = format_timespan(waktumsg)
                                                    rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                                    rat_ += "\nLocation :\nBelow"
                                                    sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                                    maxgie.sendLocation(at, msg_dict[msg_id]["location"])
                                                    del msg_dict[msg_id]
                                                else:
                                                    if "file" in msg_dict[msg_id]:
                                                        waktumsg = ah - msg_dict[msg_id]["waktu"]
                                                        waktumsg = format_timespan(waktumsg)
                                                        rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                                        rat_ += "\nFile :\nBelow"
                                                        sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                                        maxgie.sendFile(at, msg_dict[msg_id]["file"])
                                                        del msg_dict[msg_id]
                else:
                    print ("[ ERROR ] Terjadi Error Karena Tidak Ada Data Chat Tersebut~")
        if op.type == 55:
            print ("[ 55 ] NOTIFIED READ MESSAGE")
            NOTIFIED_READ_MESSAGE(op)
    except Exception as error:
        logError(error)

#==============================================================================#
        backupData()
    except Exception as error:
        logError(error)
        traceback.print_tb(error.__traceback__)

def run():
    while True:
        try:
            ops = maxgiePoll.singleTrace(count=50)
            if ops != None:
                for op in ops:
                   loop.run_until_complete(maxgieBot(op))
                   maxgiePoll.setRevision(op.revision)
        except Exception as e:
            logError(e)
if __name__ == "__main__":
    run()

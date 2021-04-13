# $language = "python"
# $interface = "1.0"
import random
import string


def pro():
    project_0 = crt.Dialog.Prompt(
        "xiaoyu-1,kuaizip-2,kantu-3,heinote-4,finder-5,browser-6,yp-7//pdf-10,wx-11,haotu-12,bz01-13,srf-14,"
        "jkkantu-15//lszip-20,jcwallpaper-21,xinnote-22,qingjiepdf-23",
        "project",
        "11",
        False)
    project_int = int(project_0)
    project_url = 'project_url'
    pp = [project_0, project_url]
    if project_int == 1:
        pp = ['xiaoyu', '0411']
    elif project_int == 2:
        pp = ['kuaizip', '0109']
    elif project_int == 3:
        pp = ['kantu', '0310']
    elif project_int == 4:
        pp = ['heinote', '0508']
    elif project_int == 5:
        pp = ['finder', '0512']
    elif project_int == 6:
        pp = ['browser', '0613']
    # elif project_int == 7:
    #     return 'yp'
    # elif project_int == 10:
    #     return 'pdf001'
    # elif project_int == 11:
    #     return 'wx
    # elif project_int == 12:
    #     return 'haotu'
    # elif project_int == 13:
    #     return 'bz01'
    # elif project_int == 14:
    #     return 'srf
    # elif project_int == 15:
    #     return 'jkkantu'
    # elif project_int == 20:
    #     return 'lszip', '1219'
    # elif project_int == 21:
    #     return 'jcwallpaper'
    elif project_int == 22:
        pp = ['xinnote', '3001']
    elif project_int == 23:
        pp = ['qingjiepdf', '4001']
    pp.append(project_int)
    return pp


def enve():
    env_0 = crt.Dialog.Prompt(
        "测试-0,线上-1",
        "env",
        "0",
        False)
    env_int = int(env_0)
    return env_int


# def exex(proj):
#     path = r'Desktop' + '\\'
#     exe = ['MiniNews.exe', 'tnewsplus-mx.exe', 'xfpressnews.exe', 'wxdessertcookies.exe', 'ktfreshnews.exe',
#            'srfnewsmsg.exe', 'jkmemonews.exe']
#
#     if proj in range(0, 10):
#         return path + exe[0]
#     elif proj in range(20, 24):
#         return path + exe[1]
#     if proj == 10:
#         return path + exe[2]
#     elif proj == 11:
#         return path + exe[3]
#     elif proj == 12 or proj == 13:
#         return path + exe[4]
#     elif proj == 14:
#         return path + exe[5]
#     elif proj == 15:
#         return path + exe[6]


def argue(project_url,proj):
    mutex = random.choice(string.ascii_letters)  # 包含所有字母(大写或小写)的字符串
    code = project_url
    url = '"http://news.7654.com/mini_new4/%s/?qid=qid_cmd&uid=UIDXXXX&env=0&screen_h=926"' % (code)
    arg = ' -killprocess=1 -enablehomepagerand=1 -Optimize=10 -DisplayTitle=7654Browser -writetck=LiveUpdate360,632 -usesspmode=1 ' \
          '-TopUrl=http://down1.7654browser.vfpzmg.cn/tui/mininews/mininewsplus/ffzdr.png -AntiMaliciousClick=60/500 -pbcuttitlenews =-1 ' \
          '-pp=f658353f4b8fa066479e2818f52584c2 -showWeather=false -align=top -captioncolor=#FFFFFF -ShowCloseMenu=1 -MaxWebClickCount=2 -ClassName=xiralie ' \
          '-Title=fireflye -Support7654Browser=true -MutexName=%s -IE9URL=%s -URL=%s -reportprefix=mininews-1 -taskid=taskid.mininews_1 ' % (mutex, url, url)
    argues = exex(proj) + ' ' + arg
    close = "-closebuttonjsonurl=http://down1.7654browser.shzhanmeng.com/test/close.json "
    close_fei = "-closebuttonjsonurl=http://down1.7654browser.shzhanmeng.com/test/close_fei.json "

    return argues




def main():
    enve()
    project = pro()
    proj = project[-1]
    project_url = project[1]
    # exex(proj)
    cmd = argue(project_url,proj)
    crt.Screen.Send(cmd + "\r")


# env = enve()
# project = project()
# proj = project[-1]
# project_url = project[1]
# exe = exex()
main()

# $language = "python"
# $interface = "1.0"
import random
import string


def project():
    project_0 = crt.Dialog.Prompt(
        "xiaoyu-1,kuaizip-2,kantu-3,heinote-4,finder-5,browser-6//pdf-10,wx-11,haotu-12,bz01-13//lszip-20,jcwallpaper-21,xinnote-22,qingjiepdf-23,cloudbar-24",
        "project",
        "24",
        False)
    project_int = int(project_0)
    return project_int


def enve():
    env_0 = crt.Dialog.Prompt(
        "测试-0,线上-1",
        "env",
        "0",
        False)
    env_int = int(env_0)
    return env_int


def exe():
    path = r'Desktop' + '\\'
    exe = ['tpop.exe', 'tpop-mx.exe', 'xfdailynews.exe', 'wxpersonalcare.exe', 'ktpopnews.exe']
    # for i in range(len(exe)):
    #     crt.Screen.Send("taskkill /f /t /im " + exe[i] + "\r")
    # crt.Screen.WaitForString("进程")

    if proj in range(1, 7):
        return path + exe[0]
    elif proj in range(20, 25):
        return path + exe[1]
    if proj == 10:
        return path + exe[2]
    elif proj == 11:
        return path + exe[3]
    elif proj == 12 or proj == 13:
        return path + exe[4]
    elif proj == 14:
        return path + exe[5]
    elif proj == 15:
        return path + exe[6]


def url_host():
    url_host = ['http://beta-tpop4.7654.com/newTpop/', 'http://news.7654.com/newTPop/']
    # dspurl = ['bq/1/', 'ys01/1/', 'pv/1/', 'jsbtest/1/', 'sp/1/', 'llq01/1/']

    if proj not in range(10, 14):
        if env == 0:
            return url_host[0]
        else:
            return url_host[1]
    elif proj == 10:
        if env == 0:
            return url_host[0]
        else:
            return url_host[1]
    elif proj in [11, 14, 15]:
        if env == 0:
            return url_host[0]
        else:
            return url_host[1]
    elif proj in [12, 13]:
        if env == 0:
            return url_host[0]
        else:
            return url_host[1]


def argue():
    # x = random.randint(1, 3)
    # y = random.randint(1, 3)
    # pos = str(x) + ':' + str(y)
    mutex = random.choice(string.ascii_letters)  # 包含所有字母(大写或小写)的字符串
    # argue_skin = '-usewebmode=false  -skinurl=http://down1.7654browser.shzhanmeng.com/tui/tnews/xml/TnewsPlus.zip  ' \
    #              '-landingpage=http://www.baidu.com -closeimagesize=14x14_w  ' \
    #              '-configurl=http://ifinder.shzhanmeng.com/tui/tips/2/xml/kb-tips.xml ' \
    #              '-newsurl=http://www.hoteastday.com/api/tnews_news_list/tnews5/gs005 '

    arg = '-closebuttonjsonurl=http://down1.7654browser.shzhanmeng.com/test/close.json -classname=clas -title=tle -reportprefix=tpop-2-cs-b4 -custombr=0 -recordshow=0 ' \
          '-localcity="厦门" -taskid=tpop-py -killprocess=1 -blockclosemsg=1 -bp=1000 -enabletitlenews=1 -popmenu=1 -nopopwhenlong=1 -hibernate=0 -mutex=%s -reportold=0 ' % (
              mutex)

    # argues = exe + arg + argue_skin
    argues = exe() + ' ' + arg

    # dspurl = ['bq/1/', 'ys01/1/', 'pv/1/', 'jsbtest/1/', 'sp/1/', 'llq01/1/']
    xiaoyu = argues + '-dspurl=%s' % url_host + "infoflow/bq/4/ -project=xiaoyu -pbcuttitlenews=1000"
    kuaizip = argues + '-dspurl=%s' % url_host + "infoflow/ys01/4/ -project=kuaizip "
    kantu = argues + '-dspurl=%s' % url_host + "infoflow/pv/4/ -project=kantu "
    # kantu = argues + '-dspurl=%s' % url_host + "info_new/kt/5/ -project=kantu "  # 新样式
    # kantu = argues + '-dspurl=%s' % url_host + "tpop4/pv4/1.html  -project=kantu "  # 新样式

    heinote = argues + '-dspurl=%s' % url_host + "infoflow/jsbtest/4/ -project=heinote "
    finder = argues + '-dspurl=%s' % url_host + "infoflow/sp/4/ -project=finder "
    browser = argues + '-dspurl=%s' % url_host + "infoflow/llq/4/ -reportjsonurl=http://down1.7654browser.shzhanmeng.com/test/7654.data -project=browser "

    lszip = argues + '-dspurl=%s' % url_host + "infoflow/ls/4/ -project=lszip "
    jcwallpaper = argues + '-dspurl=%s' % url_host + "infoflow/jc/4/ -project=jcwallpaper "
    xinnote = argues + '-dspurl=%s' % url_host + "infoflow/jsb003/4/ -project=xinnote "
    qingjiepdf = argues + '-dspurl=%s' % url_host + "infoflow/pdf002/4/ -reportjsonurl=http://down1.7654browser.shzhanmeng.com/test/qjpdf.data -project=qingjiepdf  "
    cloudbar = argues + '-dspurl=%s' % url_host + "infoflow/gjl001/4/ -project=cloudbar "

    pdf001 = argues + '-dspurl=%s' % url_host + "infoflow/pdf/4/ -project=whirlwindpdf"
    wx = argues + '-dspurl=%s' % url_host + "infoflow//smartlook/4/ -project=smartlook "
    haotu = argues + '-dspurl=%s' % url_host + "infoflow/htkk/4/ -project=haotu "
    bz01 = argues + '-dspurl=%s' % url_host + "infoflow/bz/4/ -project=calfwallpaper "
    # srf = argues + '-dspurl=%s' % url_host + "infoflow/bq/1/ -project=sesame "
    # jkkantu = argues + '-dspurl=%s' % url_host + "infoflow/bq/1/ -project=jkkantu "

    if proj == 1:
        return xiaoyu
    elif proj == 2:
        return kuaizip
    elif proj == 3:
        return kantu
    elif proj == 4:
        return heinote
    elif proj == 5:
        return finder
    elif proj == 6:
        return browser
    elif proj == 7:
        return yp
    elif proj == 10:
        return pdf001
    elif proj == 11:
        return wx
    elif proj == 12:
        return haotu
    elif proj == 13:
        return bz01
    elif proj == 20:
        return lszip
    elif proj == 21:
        return jcwallpaper
    elif proj == 22:
        return xinnote
    elif proj == 23:
        return qingjiepdf
    elif proj == 24:
        return cloudbar
    else:
        crt.Dialog.MessageBox('proj error')


def main():
    cmd = argue()
    crt.Screen.Send(cmd + "\r")


env = enve()
proj = project()
url_host = url_host()

main()

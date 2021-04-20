# $language = "python"
# $interface = "1.0"
import random
import string


def project():
    project_0 = crt.Dialog.Prompt(
        "xiaoyu-1,kuaizip-2,kantu-3,heinote-4,finder-5,browser-6,yp-7//pdf-10,wx-11,haotu-12,bz01-13,srf-14,"
        "jkkantu-15//lszip-20,jcwallpaper-21,xinnote-22,qingjiepdf-23,cloudbar-24",
        "project",
        "1",
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


env = enve()
proj = project()


def exex():
    path = r'Desktop' + '\\'
    exe = ['TNewsPlus.exe', 'tnewsplus-mx.exe', 'xfpressnews.exe', 'wxdessertcookies.exe', 'ktfreshnews.exe',
           'srfnewsmsg.exe', 'jkmemonews.exe']
    # for i in range(len(exe)):
    #     crt.Screen.Send("taskkill /f /t /im " + exe[i] + "\r")
    # crt.Screen.WaitForString("进程")

    if proj in range(0, 10):
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
    url_host = ["-dspurl=http://test.gamma-minipage.news.7654.com", "-dspurl=http://news.7654.com", "-dspurl=http://egg-test.7654.com",
                "-dspurl=http://page.suyazip.com", "-dspurl=http://gg-smartlook.wnplayer.cn", "-dspurl=http://gg.wallpaper.shqingzao.com",
                '-dspurl=http://ads.shjiameinuo.com']
    # url_host = ["-dspurl=http://172.18.15.180:8080", "-dspurl=http://news.7654.com",
    #             "-dspurl=http://egg-test.7654.com", "-dspurl=http://page.suyazip.com",
    #             "-dspurl=http://gg-smartlook.wnplayer.cn", "-dspurl=http://gg.wallpaper.shqingzao.com"]

    if proj not in range(10, 20):
        if env == 0:
            return url_host[0]
        else:
            return url_host[1]
    elif proj == 10:
        if env == 0:
            return url_host[2]
        else:
            return url_host[3]
    elif proj in [11, 14, 15]:
        if env == 0:
            return url_host[2]
        else:
            return url_host[4]
    elif proj in [12, 13]:
        if env == 0:
            return url_host[2]
        else:
            return url_host[5]


exe = exex()
url_begin = url_host()


def argue():
    x = random.randint(1, 3)
    y = random.randint(1, 3)
    positition = str(x) + ':' + str(y)
    mutex = random.choice(string.ascii_letters)  # 包含所有字母(大写或小写)的字符串

    # argue_skin = '-usewebmode=false  -skinurl=http://down1.7654browser.shzhanmeng.com/tui/tnews/xml/TnewsPlus.zip  ' \
    #              '-landingpage=http://www.baidu.com -closeimagesize=14x14_w  ' \
    #              '-configurl=http://ifinder.shzhanmeng.com/tui/tips/2/xml/kb-tips.xml ' \
    #              '-newsurl=http://www.hoteastday.com/api/tnews_news_list/tnews5/gs005 '
    argue_skin = ' -usewebmode=0  -skinurl=http://down1.7654browser.shzhanmeng.com/tui/tnews/xml/TnewsPlus.zip  ' \
                 '-landingpage=http://www.bing.com -closeimagesize=14x14_w  ' \
                 '-configurl=http://ifinder.shzhanmeng.com/tui/tips/2/xml/kb-tips.xml ' \
                 '-newsurl=http://test.gamma-minipage.news.7654.com/tipsdsp/13/s11 '

    arg = '-writelog=1 -classname=class -title=title -reportprefix=tnews-2-cs-b0 -recordshow=1 -localcity="厦门" -taskid=tnews.py -killprocess=1 -isnewuser=0 ' \
          '-blockclosemsg=1 -blockdestroymsg=1 -bp=1000 -blockmsgcnt=2 -wmclosereportcnt=2 -venueshowmax=0 -mutex=%s -position=%s -popmenu=1 -nopopwhenlong=1 ' \
          '-hibernate=0 ' % (
              mutex, positition)

    arg_skin = exe + ' ' + arg + argue_skin
    argues = exe + ' ' + arg
    close = "-closebuttonjsonurl=http://down1.7654browser.shzhanmeng.com/test/close.json "
    close_fei = "-closebuttonjsonurl=http://down1.7654browser.shzhanmeng.com/test/close_fei.json "
    if proj in range(10, 15):
        argues += close_fei + url_begin
    else:
        argues += close + url_begin

    xiaoyu = argues + "/tnewsdsp/01/s11/?product_category=23 -project=xiaoyu "
    kuaizip = argues + "/tnewsdsp/02/s11/?product_category=23 -project=kuaizip "
    kantu = argues + "/tnewsdsp/03/s11/?product_category=23 -project=kantu "
    heinote = argues + "/tnewsdsp/04/s11/?product_category=23 -project=heinote "
    finder = argues + "/tnewsdsp/05/s11/?product_category=23 -project=finder "
    browser = argues + "/tnewsdsp/09/s11/?product_category=23 -reportjsonurl=http://down1.7654browser.shzhanmeng.com/tui/tnews/7654.data -project=browser "
    yp = exe + url_begin + "/tnewsdsp/yp01.html -project=kuaizip "
    # browser = arg_skin + " -project=browser "  # 走皮肤
    # cloudbar = arg_skin + " -project=cloudbar "  # 走皮肤

    lszip = argues + "/tnewsdsp/20/s11/?product_category=23 -project=lszip "
    jcwallpaper = argues + "/tnewsdsp/21/s11/?product_category=23 -project=jcwallpaper "
    xinnote = argues + "/tnewsdsp/22/s11/?product_category=23 -project=xinnote "
    qingjiepdf = argues + "/tnewsdsp/23/s11/?product_category=23 -reportjsonurl=http://down1.7654browser.shzhanmeng.com/tui/tnews/qjpdf.data  -project=qingjiepdf "
    cloudbar = argues + "/tnewsdsp/26/s11/?product_category=23 -project=cloudbar "

    pdf001 = argues + "/pdf/whirlwindpdf/tnews_pdf?product_category=23 -reportjsonurl=http://down1.7654browser.shzhanmeng.com/tui/tnews/pdf.data -project=whirlwindpdf"
    wx = argues + "/wx/smartlook/wxtnews?product_category=23 -project=smartlook "
    haotu = argues + "/ht/haotu/haotutnews?product_category=23 -reportjsonurl=http://down1.7654browser.shzhanmeng.com/tui/tnews/haotu.data -project=haotu "
    bz01 = argues + "/bz/calfwallpaper/bztnews?product_category=23 -project=calfwallpaper "
    srf = argues + "/zhima/sesame/srftnews?product_category=23 -project=sesame "
    jkkantu = argues + "/jk/jkkantu/jktnews?product_category=23 -project=jkkantu "

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
    elif proj == 14:
        return srf
    elif proj == 15:
        return jkkantu
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


main()

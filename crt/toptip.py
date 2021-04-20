# $language = "python"
# $interface = "1.0"
import random
import string


def project():
    project_0 = crt.Dialog.Prompt(
        "xiaoyu-1,kuaizip-2,kantu-3,heinote-4,finder-5,browser-6,yp-7//pdf-10,wx-11,haotu-12,bz01-13,srf-14,"
        "jkkantu-15//lszip-20,jcwallpaper-21,xinnote-22,qingjiepdf-23",
        "project",
        "11",
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
    exe = ['toptips.exe', 'mxhfpop.exe', 'xfmationpop.exe', 'wxfreshpop.exe', 'ktpostpop.exe', 'srfnewsmsg.exe', 'jkmemonews.exe']
    # for i in range(len(exe)):
    #     crt.Screen.Send("taskkill /f /t /im " + exe[i] + "\r")
    # crt.Screen.WaitForString("进程")

    if proj in range(0, 10):
        return path + exe[0]
    elif proj in range(20, 24):
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
    url_host = ["-dspurl=http://test.gamma-minipage.news.7654.com", "-dspurl=http://news.7654.com",
                "-dspurl=http://egg-test.7654.com", "-dspurl=http://page.suyazip.com",
                "-dspurl=http://gg-smartlook.wnplayer.cn", "-dspurl=http://gg.wallpaper.shqingzao.com"]
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

    # argue_skin = '-usewebmode=false  -skinurl=http://down1.7654browser.shzhanmeng.com/tui/tips/xml/tipsPlus.zip  ' \
    #              '-landingpage=http://www.baidu.com -closeimagesize=14x14_w  ' \
    #              '-configurl=http://ifinder.shzhanmeng.com/tui/tips/2/xml/kb-tips.xml ' \
    #              '-newsurl=http://www.hoteastday.com/api/tips_news_list/tips5/gs005 '
    argue_skin = '-usewebmode=0  -skinurl=http://down1.7654browser.shzhanmeng.com/tui/tips/xml/tipsPlus.zip  ' \
                 '-landingpage=http://www.bing.com -closeimagesize=14x14_w  ' \
                 '-configurl=http://ifinder.shzhanmeng.com/tui/tips/2/xml/kb-tips.xml ' \
                 '-newsurl=http://test.gamma-minipage.news.7654.com/tipsdsp/13/s12 '

    arg = '-writelog=1 -classname=class -title=title -reportprefix=tips-2-cs-b0 -recordshow=1 -localcity="厦门" -taskid=tips.py -killprocess=1 -isnewuser=0 ' \
          '-blockclosemsg=1 -blockdestroymsg=1 -bp=1000 -blockmsgcnt=2 -wmclosereportcnt=2 -venueshowmax=0 -mutex=%s -position=%s -popmenu=1 -nopopwhenlong=1 ' \
          '-hibernate=0 ' % (
              mutex, positition)

    # argues = exe +' '+ arg + argue_skin
    argues = exe + ' ' + arg
    close = "-closebuttonjsonurl=http://down1.7654browser.shzhanmeng.com/test/close.json "
    close_fei = "-closebuttonjsonurl=http://down1.7654browser.shzhanmeng.com/test/close_fei.json "
    if proj in range(10, 15):
        argues += close_fei + url_begin
    else:
        argues += close + url_begin

    xiaoyu = argues + "/tipsdsp/07_new/s12/?product_category=27 -project=xiaoyu "
    kuaizip = argues + "/tipsdsp/08/s12/?product_category=27 -project=kuaizip "
    kantu = argues + "/tipsdsp/09/s12/?product_category=27 -project=kantu "
    heinote = argues + "/tipsdsp/10/s12/?product_category=27 -project=heinote "
    finder = argues + "/tipsdsp/11/s12/?product_category=27 -project=finder "
    browser = argues + "/tipsdsp/13/s12/?product_category=27 -reportjsonurl=http://down1.7654browser.shzhanmeng.com/tui/tips/7654.data -project=browser "
    yp = exe + url_begin + "/tipsdsp/yp01.html -project=kuaizip "
    # browser = argues + " -project=browser "  #走皮肤

    lszip = argues + "/tipsdsp/20/s12/?product_category=27 -project=lszip "
    jcwallpaper = argues + "/tipsdsp/21/s12/?product_category=27 -project=jcwallpaper "
    xinnote = argues + "/tipsdsp/22/s12/?product_category=27 -project=xinnote "
    qingjiepdf = argues + "/tipsdsp/23/s12/?product_category=27 -reportjsonurl=http://down1.7654browser.shzhanmeng.com/tui/tips/qjpdf.data  -project=qingjiepdf "

    pdf001 = argues + "/pdf/whirlwindpdf/tips_pdf?product_category=27 -project=whirlwindpdf"
    wx = argues + "/wx/smartlook/wxtips?product_category=27 -project=smartlook "
    haotu = argues + "/ht/haotu/haotutips?product_category=27 -reportjsonurl=http://down1.7654browser.shzhanmeng.com/test/haotu.data -project=haotu "
    bz01 = argues + "/bz/calfwallpaper/bztips?product_category=27 -project=calfwallpaper "
    srf = argues + "/zhima/sesame/srftips?product_category=27 -project=sesame "
    jkkantu = argues + "/jk/jkkantu/jktips?product_category=27 -project=jkkantu "

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
    elif proj == 0:
        for i in [xiaoyu, kuaizip, kantu, heinote, finder, browser]:
            return i


def main():
    cmd = argue()
    crt.Screen.Send(cmd + "\r")


main()

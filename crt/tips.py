# $language = "python"
# $interface = "1.0"
import random
import string


def project():
    project_0 = crt.Dialog.Prompt(
        "xiaoyu-1,kuaizip-2,kantu-3,heinote-4,finder-5,browser-6)(pdf-10,wx-11,haotu-12,bz01-13,srf-14)(lszip-20,jcwallpaper-21,xinnote-22,qingjiepdf-23,cloudbar-24)",
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
    path = r"Desktop" + "\\"
    exe = ['tipsplus2.exe', 'tipsplus2-mx.exe', 'xfinformation.exe', 'wxseasonalfresh.exe', 'ktpostnotes.exe', 'srflabelmsg.exe']
    # for i in range(len(exe)):
    #     crt.Screen.Send("taskkill /f /t /im " + exe[i] + "\r")
    # crt.Screen.WaitForString("进程")

    if proj in range(1, 9):
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
        return path + exe[-1]


def url_host():
    url_host = ["-dspurl=http://test.gamma-minipage.news.7654.com", "-dspurl=http://news.7654.com", "-dspurl=http://egg-test.7654.com",
                "-dspurl=http://page.nanjingchenxi.com", "-dspurl=http://gg.smartlook.shheshou.com", "-dspurl=http://gg.wallpaper.shqingzao.com",
                "-dspurl=http://egg-test.7654.com", "-dspurl=http://ads.shjiameinuo.com"]

    if proj not in range(10, 19):
        if env == 0:
            return url_host[0]
        else:
            return url_host[1]
    elif proj == 10:
        if env == 0:
            return url_host[2]
        else:
            return url_host[3]
    elif proj == 11:
        if env == 0:
            return url_host[2]
        else:
            return url_host[4]
    elif proj == 12 or proj == 13:
        if env == 0:
            return url_host[2]
        else:
            return url_host[5]
    elif proj == 14:
        if env == 0:
            return url_host[-2]
        else:
            return url_host[-1]


exe = exex()
url_begin = url_host()


def argue():
    arg = " -closebuttonjsonurl=http://down1.7654browser.shzhanmeng.com/tui/close.json " \
          "-title=title_tips -classname=class_tips -reportprefix=qianzh -recordshow=1 -popmenu=1 -nopopwhenlong=1 " \
          "-taskid=tips.lv-01 -killprocess=1 -isnewuser=1 -localcity='厦门' -venueshowmax=3 " \
          "-blockclosemsg=1 -blockdestroymsg=1 -blockmsgcnt=2 -wmclosereportcnt=2 -bp=1000 "

    x = random.randint(1, 3)
    y = random.randint(1, 3)
    positition = str(x) + ':' + str(y)
    mutex = random.choice(string.ascii_letters)  # 包含所有字母(大写或小写)的字符串
    arg_1 = '-mutex=' + mutex + ' ' + '-position=' + positition + ' '

    xiaoyu = exe + arg + arg_1 + url_begin + "/tipsdsp/07_new/s11/?product_category=23 -project=xiaoyu "
    kuaizip = exe + arg + arg_1 + url_begin + "/tipsdsp/08/s11/?product_category=23 -project=kuaizip "
    kantu = exe + arg + arg_1 + url_begin + "/tipsdsp/09/s11/?product_category=23 -project=kantu "
    heinote = exe + arg + arg_1 + url_begin + "/tipsdsp/10/s11/?product_category=23 -project=heinote "
    finder = exe + arg + arg_1 + url_begin + "/tipsdsp/11/s11/?product_category=23 -project=finder "
    browser = exe + arg + arg_1 + url_begin + "/tipsdsp/13/s11/?product_category=23 -project=browser "

    lszip = exe + arg + arg_1 + url_begin + "/tipsdsp/20/s11/?product_category=23 -project=lszip "
    jcwallpaper = exe + arg_1 + arg + url_begin + "/tipsdsp/21/s11/?product_category=23 -project=jcwallpaper "
    xinnote = exe + arg + arg_1 + url_begin + "/tipsdsp/22/s11/?product_category=23 -project=xinnote "
    qingjiepdf = exe + arg + arg_1 + url_begin + "/tipsdsp/23/s11/?product_category=23 -project=qingjiepdf "
    cloudbar = exe + arg + arg_1 + url_begin + "/tipsdsp/26/s11/?product_category=23 -project=cloudbar "

    pdf001 = exe + arg + url_host() + "/pdf/whirlwindpdf/tips_pdf?product_category=23 -project=whirlwindpdf "
    wx = exe + arg + url_begin + "/wx/smartlook/wxtips?product_category=23 -project=smartlook "
    haotu = exe + arg + url_begin + "/ht/haotu/haotutips?product_category=23 -project=haotu "
    bz01 = exe + arg + url_begin + "/bz/calfwallpaper/bztips?product_category=23 -project=calfwallpaper "
    srf = exe + arg + url_begin + "/zhima/sesame/srftips?product_category=23 -project=sesame "

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

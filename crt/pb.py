# $language = "python"
# $interface = "1.0"


def dspurl():
    # crt.Screen.Send("dspurl \r")
    url_begin = '--shortcut --data='
    xiaoyu = url_begin + 'WAWzIy3oWMqdyM5nxwDpYQc7o9TM5miOMuBgBLDVH3TTXy/l/KnIfXcQUMyT2WK0YFisLlGLw1/HK6ATprQV64qgYR2ql9BsL5LYN8+Aj8or9o20ef1KRf6ngJUPFbZleKIoYZWnFs5WHJetmAhpJjXDOAZAgNGGEB2g0jcMpF4NJO/8mif4iLPptloVFKA288fzNv2AVlN+w4KJ9VzGMyEI+HsmCRMB9q/3w5U45o3O+NLg'
    kuaizip = url_begin + 'ok/bZta75wN1LkkulAsEtB1lZnL3M+HsBoaQNvqz4G/VoyV9x5cIK4Nxka3rHkfp51CjyQsTjSV1OCJaDy523k08QIB41IEBlcJepO2K5FzVxBrITVkiJFYcSP+X0ZBSjIWJYHIpNqtcSCdAcFAG7OzezS16uHbpohCVxmg3s7uXze/NemDa2X+gTj5ajUIUnYISPc0XRhvj2w=='
    kantu = url_begin + '2dJg/yDniO/0WcInZgmn/u5M0QZ2A449lOliDodfAWMheIYxNjbVZheDyGGB7v9MTf8jcOKCazUEQ7H654TQjFoNriXSOwBWFTIIROFFLA2Ys7OLICcjWerfVvEr+LNLvaAYVZ0nKrDeuX36pAxa1jMu9F9TPQ=='
    heinote = url_begin + 'foDN7Y8RZ48YC2bjEHTU1HOhtU4FFSokmsboyy3++N31QEvIoXVXt+1jCWOFGQ4UlJsIob2DXlSmsFOP7Ql2YL7lbOxzM8c3YSby6IZL+HzHwv2Ynr3H836yngcwn+UB+/Xb+4AB8RlzWxEC8qprSsUPUwJtQppAR6L7'
    finder = url_begin + 'N9Wcg1o6U/dY/xSxpqNh90iOKcmBvRhs7RlVGfmJ3wL7PItWghP6+vf55q6iSvdJepE3yrhl4TBRLzBl5li13wUtQMJ44DHxE0w0m+p9YdZx7fp6yApDvX8L3m2iiR1J7yvxWmLLQA=='
    browser = url_begin + 'ZWo69dj52IpnAUg4pbOdUUGcP2ynLyXy9gIno1gG1D9XSkhcUeK8LrXSiNPGjSjhwvVy1GlXa/XkgTvHB50OO7x4St6CeBZsIgP92MH+JXtoYfvegjQ5u9ggLAwSjETgC8qcApaAyfOfCIDDrkk='
    jcwapaper = url_begin + 'PCJvIe8X4g1taX+Uqi2x3u7+j4Ls8+x3iDUdDbIygkJnJRzZJHIrtFGmGqRlFLE6ga+FuiSNGnLJ1VfV8cx/4V5gB37QBycEI6gnOzfKMJRnjL/mlX0KxdgRCTFCkiH1BBcbTjcPNh3rmcE9'
    lszip = url_begin + '1TQwOD7u/poRUQOiaK+YDgnEE8FRO2t/Kw0uUpYHCchrzl2weP5LoYo2zKbfa8AlqbCbXJNF1MecndlOFxm8+hAFAAuBDYyy3zZ3XBz2CXawxC8mMySYI2FYfFqWNz8jLFfmQjfz'

    # crt.Dialog.MessageBox("请输入project代号")
    # crt.Screen.WaitForKey(5)

    project = crt.Dialog.Prompt(
        "xiaoyu-1,kuaizip-2,kantu-3,heinote-4,finder-5,browser-6,jcwallpaper-7,lszip-8",
        "project",
        "1",
        False)

    # crt.Dialog.MessageBox(password, "password")

    # crt.Sleep(5000)
    # row = crt.Screen.CurrentRow
    # prompt = crt.Screen.Get(row, 0, row, crt.Screen.CurrentColumn - 1)
    # prompt = prompt.strip(r'C:\Users\Administrator>')

    # crt.Screen.Send("ls -l\n")
    # Wait for the command to complete, by looking for the prompt to
    # appear once again.
    # crt.Screen.WaitForString(prompt)

    # crt.Screen.WaitForString(prompt)

    # crt.Dialog.MessageBox(prompt)
    if project == '1':
        return xiaoyu
    elif project == '2':
        return kuaizip
    elif project == '3':
        return kantu
    elif project == '4':
        return heinote
    elif project == '5':
        return finder
    elif project == '6':
        return browser
    elif project == '7':
        return jcwapaper
    elif project == '8':
        return lszip


def main():
    crt.Screen.Send("taskkill /f /t /im screen_saver.exe \r")
    crt.Screen.WaitForString('进程')
    exe = r'AppData\Roaming\ScreenSaver\screen_saver.exe '
    cmd = exe + dspurl() + ' --v=4'
    crt.Screen.Send(cmd + "\r")


main()

import hashlib
import json
# 导入json头文件
import os
import time

from loguru import logger


class gjl:
    def __init__(self, gif):
        self.gif = gif
        # self.md5_gif = md5_gif
        # self.dict = dict

    def path_gif(self):
        path_logl = 'logl.gif'  # uc
        path_logu = 'logu.gif'  # update

        if self.gif == 'uc':
            return path_logl
        elif gif == 'u':
            return path_logu
        else:
            logger.info('Only uc or u in parentheses')

    def get_file_md5(self):  # 获取文件的md5
        path_gif = self.path_gif()
        if not os.path.isfile(path_gif):
            logger.info('文件不存在')
            return
        myhash = hashlib.md5()
        f = open(path_gif, "rb")
        while True:
            b = f.read(8096)
            if not b:
                break
            myhash.update(b)
        f.close()
        # print(myhash.hexdigest())
        md5_gif = myhash.hexdigest().upper()
        logger.info('本次更新%s的MD5:%s' % (gif, md5_gif))
        return md5_gif

    def get_json_data(self, path_json):  # 获取json里面数据
        os.system('Crypter.exe %s' % path_json)
        try:
            with open(path_json, 'rb') as f:  # 定义为只读模型，并定义名称为f
                params = json.load(f)  # 加载json文件中的内容给params
                logger.info('源文件已加密')
        except UnicodeDecodeError as e:
            with open(path_json, 'rb') as f:
                os.system('Crypter.exe %s' % path_json)
                logger.info('源文件未加密')
                params = json.load(f)
        # logger.info(params)
        print('上线文件列表:\nhttp://down2.698283.vip/config/shell.json', end='\n')
        md5 = self.get_file_md5()
        if self.gif == 'uc':  # 修改内容
            params['download'][0]['md5'] = md5
            print('http://down2.698283.vip/config/logo/loguc.gif.MD5 \nhttp://down2.698283.vip/config/logo/loguc.gif')
        elif self.gif == 'u':
            params['download'][1]['md5'] = md5
            print('http://down2.698283.vip/config/logo/logu.gif.MD5 \nhttp://down2.698283.vip/config/logo/logu.gif')
        else:
            logger.info('Only uc or u in parentheses')
        dict = params  # 将修改后的内容保存在dict中
        f.close()  # 关闭json读模式
        return dict  # 返回dict字典内容

    def write_json_data(self, path_json_new):  # 写入json文件
        dict = self.get_json_data(path_json)
        with open(path_json_new, 'w') as r:  # 定义为写模式，名称定义为r
            json.dump(dict, r)  # 将dict写入名称为r的文件中
        r.close()  # 关闭json写模式
        os.system('Crypter.exe %s' % path_json_new)
        # logger.info('已加密')


# 调用两个函数，更新内容
if __name__ == '__main__':
    os.chdir(r"F:\\svn\\Lua\\CloudsToolbar\\gif\\")  # 修改当前工作目录
    logger.info('获取当前工作目录:%s' % os.getcwd())
    time.sleep(0.2)
    gif = input('input u or uc:')
    path_json = 'shell.json'  # json原文件
    path_json_new = 'shell.json'  # 修改json文件后保存的路径
    cloudbar = gjl(gif)
    cloudbar.write_json_data(path_json_new)

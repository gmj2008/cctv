import os
import requests
import jsonpath
import shutil
import re


def download(url, file):
    os.mkdir('./temp')
    try:
        url = requests.get(url=url)
        pid = re.findall(r'var guid = "(.*?)"', url.text)
        resp = requests.get(url='https://vdn.apps.cntv.cn/api/getHttpVideoInfo.do?pid=' + "".join(pid))
        result = jsonpath.jsonpath(resp.json(), "$..chapters4")
        detail = jsonpath.jsonpath(result, "$..url")
        count = len(detail)
        for i in range(count):
            with open('./temp/' + str(i + 1) + '.mp4', 'wb+') as d:
                print('正在下载第{}个片段'.format(i + 1))
                s = requests.get(detail[i])
                d.write(s.content)
                filelist = open('./temp/fianal.txt', 'a')
                filelist.write("file " + r"'" + str(i + 1) + r".mp4'" + "\n")
        filelist.close()
        os.system('ffmpeg -f concat -i ./temp/fianal.txt -c copy {}.mp4'.format(file))
        shutil.rmtree('./temp')
        print('成功')
    except:
        print('有点错误,可能是网络问题，或是删除了关键文件!!!')
        shutil.rmtree('./temp')

from core import cctv

d = open('urls.txt', 'r')
a = d.readlines()
print('检测到有{}个视频'.format(len(a)))
for i in range(len(a)):
    print('下载第{}个视频'.format(i + 1))
    cctv.download(url=a[i], file=i + 1)

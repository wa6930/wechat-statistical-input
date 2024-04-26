from pywxdump import *
from pywxdump_mini import *
import sys

wechatInfo = read_info()
wechatIsNotRunning = type(read_info()) is str
lenWechatInfo = len(wechatInfo)
selectItem = {}
if wechatIsNotRunning:
    print('你目前没有已登陆的微信')
    sys.exit(1)
else:
    print('请选择你要登陆的微信账号(输入序号)：')
    i = 1;
    for item in wechatInfo:
        print(str(i), '、', item)
        i = i+1
    try:
        inputNum = int(input('请输入选择的账号：'))
        if inputNum <= lenWechatInfo & inputNum > 0:
            selectItem = wechatInfo[inputNum-1]
        elif inputNum > lenWechatInfo | inputNum <= 0:
            selectItem = wechatInfo[0]
    except:
        selectItem = wechatInfo[0]
    print(type(selectItem))
    # 空key判断
    if 'wxid' not in selectItem | 'filePath' not in selectItem | 'key' not in selectItem:
        print('您选择的微信不合规')
        sys.exit(1)
    print('您选择了', selectItem)


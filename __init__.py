from pywxdump import *
from pywxdump_mini import *
import sys
import json

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
    # 空key判断
    if ('wxid' not in selectItem) | ('filePath' not in selectItem) | ('key' not in selectItem):
        print('您选择的微信不合规')
        sys.exit(1)
    print('您选择了', selectItem)

with open('config.json', 'r', encoding='utf-8') as f:
    config = json.loads(f.read())
if config is None:
    print('最外层config.json不存在')
    sys.exit(1)
print('load-config:', config)
args = {
    "mode": "decrypt",
    "key": selectItem['key'],  # 密钥
    "db_path": selectItem['filePath'],  # 数据库路径
    "out_path": '/path/to/output' if 'output' not in config else config['output'],  # 输出路径（必须是目录）[默认为当前路径下decrypted文件夹]
}
argsDb ={
    "mode": "db_path",
    "require_list": "all" if 'require_list' not in config else config['require_list'],  # 需要的数据库名称（可选）
    "wxid": selectItem['wxid'],  # wxid_，用于确认用户文件夹（可选）
}
bias_addr = get_wechat_db(argsDb["require_list"], None, argsDb["wxid"], False)
allDbAddr = None
for key in bias_addr.keys():
    if selectItem['filePath'] == key:
        allDbAddr = bias_addr[key]
    else:
        continue
if allDbAddr is None:
    print('获取addr对应的db失败')
    sys.exit(1)
print('bias_addr', bias_addr[selectItem['filePath']])
# result = batch_decrypt(args["key"], args["db_path"], args["out_path"], True)

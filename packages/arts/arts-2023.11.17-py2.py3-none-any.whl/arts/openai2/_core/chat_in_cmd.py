import sys, json
from pathlib import Path
from .chat import Chat
from .apikey import apikey


parent = Path(__file__).parent
record_file = parent / 'cmd_record.json'
apikey_mould = parent / 'apikey.py'


def chat_in_cmd(apikey, newchat=False):
    print("\n您已进入命令行聊天模式, 该模式使用'gpt-4-1106-preview'模型, 请确保您的apikey支持该模型.")
    gpt = Chat(api_key=apikey, model='gpt-4-1106-preview', MsgMaxCount=30)
    if not newchat:
        try:
            record = json.loads(record_file.read_text('utf8'))
            gpt.add_dialogs(*record)
        except:
            pass
    while True:
        user = input('\n\n:')
        print()
        for x in gpt.stream_request(user):
            print(x, end='', flush=True)
        record = gpt.fetch_messages()
        record_file.write_text(json.dumps(record, ensure_ascii=False), 'utf8')

def _ParseCmd():
    kws = sys.argv[1:]
    if kws:
        kw = kws[0].lower()
        if kw == 'set_apikey' and len(kws) > 1:
            apikey_mould.write_text(f"apikey = '{kws[1]}'", 'utf8')
            print('创建 apikey 成功!')
        elif kw == 'read_apikey':
            print(apikey)
        elif kw == 'chat':
            chat_in_cmd(apikey, newchat=False)
        elif kw == 'newchat':
            chat_in_cmd(apikey, newchat=True)
    else:
        print('''指令集:
openai2 set_apikey <apikey> | 创建apikey
openai2 read_apikey         | 查看apikey
openai2 chat                | 继续上次的对话
openai2 newchat             | 清空对话记录, 然后开启新对话
''')
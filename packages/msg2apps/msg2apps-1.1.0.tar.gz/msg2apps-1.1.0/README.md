# msg2apps

A python module for sending messages to communication apps

## Support apps

### Wechat

Send a message(text only now) to Wecom.

Args:

- msg: Message you want to send.

- corpid: Each enterprise has a unique corpid. To obtain this information, you can view the "enterprise ID" under "My Company"-"Enterprise Information" in the management background (administrator rights are required).[link](https://work.weixin.qq.com/api/doc/90000/90135/90665#corpid)

- secret: Secret is the "key" used to ensure data security in enterprise applications. Each application has an independent access key. To ensure data security, secrets must not be leaked.[link](https://work.weixin.qq.com/api/doc/90000/90135/90665#secert)

- agentid: Each application has a unique agentid. In the management background -> "applications and applets" -> "applications", click on an application, you can see the agentid.[link](https://work.weixin.qq.com/api/doc/90000/90135/90665#agentid)

usage:

```python
from msg2apps import Wechat

Wechat(msg, corpid, secret, agentid)
```

### Telegram

Send a message(text only now) to specific account through bot.

Args:

- API_token: Each bot is given a unique authentication token [when it is created](https://core.telegram.org/bots#6-botfather). The token looks something like `123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11`, but we'll use simply **<token>** in this document instead. You can learn about obtaining tokens and generating new ones in [this document](https://core.telegram.org/bots#6-botfather).
- chat_id: Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)

usage:

```python
from msg2apps import Telegram

Telegram(msg, token, chat_id)
```

### Others
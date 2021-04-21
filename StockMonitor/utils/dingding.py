
async def send_msg(data, dingding_token, session):
    # dingding_url = "https://oapi.dingtalk.com/robot/send?access_token=3db4c237e065b970ac6b0a6d1c8f1949aa8b188e7d2ef4f374c58190fdeb6984"
    dingding_url = dingding_token
    header = {"Content-Type": "application/json"}
    text = ""
    for key in data:
        text += "> **------------------------**  \n" \
        "> ### **{name}** \n "    \
        ">1. 当前价格：**{price}** \n"  \
        ">2. 今日最高价：{max_price} \n" \
        ">3. 今日最低价：{min_price} \n"  \
        ">4. 涨跌比例：**{proportion}** \n"    \
        ">5. 时间：{current_time} \n" \
        " \n ".format(
            name=key.get("name"),
            price=key.get("price"),
            max_price=key.get("max_price"),
            min_price=key.get("min_price"),
            proportion=key.get("proportion"),
            current_time=key.get("current_time"),
        )
    print(text)
    context = {
     "msgtype": "markdown",
     "markdown": {
         "title": "监控:",
         "text": text,
         },
     }
    async with session.post(dingding_url, json=context, headers=header) as res:
        # print(res.status)
        # print(res.content)
        context = await res.text()
        print(context)
    # res = requests.post(dingding_url, json=context, headers=header)
    # print(res)


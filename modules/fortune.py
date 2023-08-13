import requests

def get_fortune(type_id="aries"):
    ans=[]
    #type_id = input("請輸入星座:")
    api_url = f"https://api.vvhan.com/api/horoscope?type={type_id}&time=today"
    res = requests.get(api_url)
    data=res.json()
    y = data["data"]
    x = data["data"]["todo"]
    z = data["data"]["fortunetext"]
    for s in data:
        d = {
            "星座" : y["title"],
            "日期" : y["time"],
            "今日宜做" : x["yi"],
            "今日不宜做" : x["ji"],
            "整體運勢" : z["all"],
            "愛情運勢" : z["love"],
            "工作運勢" : z["work"],
            "金錢運勢" : z["money"],
            "健康運勢" : z["health"],
            "幸運色" : y["luckycolor"]
        }
        ans.append(d)
        break
    return ans
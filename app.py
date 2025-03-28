import os
from datetime import datetime

import jpholiday
import pytz

# 仮の時刻表データ
TIMETABLE = {
    "zenkojishita": {
        "up": {
            "weekday":[
                {"time": "05:44", "destination": "NGO", "type": "local"},
                {"time": "06:08", "destination": "NGO", "type": "local"},
                {"time": "06:35", "destination": "NGO", "type": "local"},
                {"time": "07:02", "destination": "NGO", "type": "local"},
                {"time": "07:27", "destination": "NGO", "type": "local"},
                {"time": "07:45", "destination": "NGO", "type": "local"},
                {"time": "07:58", "destination": "NGO", "type": "local"},
                {"time": "08:24", "destination": "NGO", "type": "local"},
                {"time": "08:38", "destination": "NGO", "type": "local"},
                {"time": "08:49", "destination": "NGO", "type": "local"},
                {"time": "09:17", "destination": "NGO", "type": "local"},
                {"time": "09:42", "destination": "NGO", "type": "local"},
                {"time": "10:04", "destination": "NGO", "type": "local"},
                {"time": "10:29", "destination": "NGO", "type": "local"},
                {"time": "11:01", "destination": "NGO", "type": "local"},
                {"time": "11:26", "destination": "NGO", "type": "local"},
                {"time": "12:08", "destination": "NGO", "type": "local"},
                {"time": "12:41", "destination": "NGO", "type": "local"},
                {"time": "13:06", "destination": "NGO", "type": "local"},
                {"time": "13:52", "destination": "NGO", "type": "local"},
                {"time": "14:25", "destination": "NGO", "type": "local"},
                {"time": "14:54", "destination": "NGO", "type": "local"},
                {"time": "15:30", "destination": "NGO", "type": "local"},
                {"time": "16:10", "destination": "NGO", "type": "local"},
                {"time": "16:31", "destination": "NGO", "type": "local"},
                {"time": "16:59", "destination": "NGO", "type": "local"},
                {"time": "17:25", "destination": "NGO", "type": "local"},
                {"time": "18:03", "destination": "NGO", "type": "local"},
                {"time": "18:32", "destination": "NGO", "type": "local"},
                {"time": "18:55", "destination": "NGO", "type": "local"},
                {"time": "19:21", "destination": "NGO", "type": "local"},
                {"time": "19:52", "destination": "NGO", "type": "local"},
                {"time": "20:20", "destination": "NGO", "type": "local"},
                {"time": "21:11", "destination": "NGO", "type": "local"},
                {"time": "21:41", "destination": "NGO", "type": "local"},
                {"time": "22:25", "destination": "NGO", "type": "local"},
            ],
            "saturday":[
                {"time": "05:44", "destination": "NGO", "type": "local"},
                {"time": "06:08", "destination": "NGO", "type": "local"},
                {"time": "06:35", "destination": "NGO", "type": "local"},
                {"time": "07:02", "destination": "NGO", "type": "local"},
                {"time": "07:27", "destination": "NGO", "type": "local"},
                {"time": "07:58", "destination": "NGO", "type": "local"},
                {"time": "08:24", "destination": "NGO", "type": "local"},
                {"time": "08:49", "destination": "NGO", "type": "local"},
                {"time": "09:17", "destination": "NGO", "type": "local"},
                {"time": "09:42", "destination": "NGO", "type": "local"},
                {"time": "10:04", "destination": "NGO", "type": "local"},
                {"time": "10:29", "destination": "NGO", "type": "local"},
                {"time": "11:01", "destination": "NGO", "type": "local"},
                {"time": "11:26", "destination": "NGO", "type": "local"},
                {"time": "12:08", "destination": "NGO", "type": "local"},
                {"time": "12:41", "destination": "NGO", "type": "local"},
                {"time": "13:06", "destination": "NGO", "type": "local"},
                {"time": "13:52", "destination": "NGO", "type": "local"},
                {"time": "14:25", "destination": "NGO", "type": "local"},
                {"time": "14:54", "destination": "NGO", "type": "local"},
                {"time": "15:30", "destination": "NGO", "type": "local"},
                {"time": "16:10", "destination": "NGO", "type": "local"},
                {"time": "16:31", "destination": "NGO", "type": "local"},
                {"time": "16:59", "destination": "NGO", "type": "local"},
                {"time": "17:25", "destination": "NGO", "type": "local"},
                {"time": "18:03", "destination": "NGO", "type": "local"},
                {"time": "18:32", "destination": "NGO", "type": "local"},
                {"time": "18:55", "destination": "NGO", "type": "local"},
                {"time": "19:21", "destination": "NGO", "type": "local"},
                {"time": "19:52", "destination": "NGO", "type": "local"},
                {"time": "20:20", "destination": "NGO", "type": "local"},
                {"time": "21:11", "destination": "NGO", "type": "local"},
                {"time": "21:41", "destination": "NGO", "type": "local"},
                {"time": "22:25", "destination": "NGO", "type": "local"},
            ],
            "holiday":[
                {"time": "05:44", "destination": "NGO", "type": "local"},
                {"time": "06:08", "destination": "NGO", "type": "local"},
                {"time": "06:35", "destination": "NGO", "type": "local"},
                {"time": "07:02", "destination": "NGO", "type": "local"},
                {"time": "07:27", "destination": "NGO", "type": "local"},
                {"time": "07:58", "destination": "NGO", "type": "local"},
                {"time": "08:24", "destination": "NGO", "type": "local"},
                {"time": "08:49", "destination": "NGO", "type": "local"},
                {"time": "09:17", "destination": "NGO", "type": "local"},
                {"time": "09:42", "destination": "NGO", "type": "local"},
                {"time": "10:04", "destination": "NGO", "type": "local"},
                {"time": "10:29", "destination": "NGO", "type": "local"},
                {"time": "11:01", "destination": "NGO", "type": "local"},
                {"time": "11:26", "destination": "NGO", "type": "local"},
                {"time": "12:08", "destination": "NGO", "type": "local"},
                {"time": "12:41", "destination": "NGO", "type": "local"},
                {"time": "13:06", "destination": "NGO", "type": "local"},
                {"time": "13:52", "destination": "NGO", "type": "local"},
                {"time": "14:25", "destination": "NGO", "type": "local"},
                {"time": "14:54", "destination": "NGO", "type": "local"},
                {"time": "15:30", "destination": "NGO", "type": "local"},
                {"time": "16:10", "destination": "NGO", "type": "local"},
                {"time": "16:31", "destination": "NGO", "type": "local"},
                {"time": "16:59", "destination": "NGO", "type": "local"},
                {"time": "17:25", "destination": "NGO", "type": "local"},
                {"time": "18:03", "destination": "NGO", "type": "local"},
                {"time": "18:32", "destination": "NGO", "type": "local"},
                {"time": "18:55", "destination": "NGO", "type": "local"},
                {"time": "19:21", "destination": "NGO", "type": "local"},
                {"time": "19:52", "destination": "NGO", "type": "local"},
                {"time": "20:20", "destination": "NGO", "type": "local"},
                {"time": "21:11", "destination": "NGO", "type": "local"},
                {"time": "21:41", "destination": "NGO", "type": "local"},
                {"time": "22:25", "destination": "NGO", "type": "local"},
            ],
        }
    }
}

def get_day_type(date: datetime) -> str:
    """与えられた日付が平日・土曜・休日のどれかを判定"""
    if jpholiday.is_holiday(date) or date.weekday() == 6:  # 日曜 or 祝日
        return "holiday"
    elif date.weekday() == 5:  # 土曜
        return "saturday"
    else:
        return "weekday"

def get_next_trains(timetable, num_trains=3):
    """ 現在時刻以降の直近N本の電車を取得 """
    # 日本時間の現在時刻を取得
    tz_japan = pytz.timezone("Asia/Tokyo")
    now = datetime.now(tz_japan)

    day_type = get_day_type(now)
    timetable = timetable.get(day_type, [])

    # 現在時刻を基準にフィルタリング
    upcoming_trains = [
        train for train in timetable if datetime.strptime(train["time"], "%H:%M").time() > now.time()
    ]

    # 直近N本を取得（最大で num_trains 本）
    return upcoming_trains[:num_trains]

def format_trains(data):
    lines = []
    for train in data:
        type_short = train["type"][0].upper()
        lines.append(f'{train["destination"]} {train["time"]}{type_short}')
    return "\n".join(lines)

if __name__ == "__main__":
    next_trains = get_next_trains(TIMETABLE["zenkojishita"]["up"])
    text = format_trains(next_trains)

    os.makedirs("output", exist_ok=True)
    with open("output/timetable.txt", "w", encoding="utf-8") as f:
        f.write(text)

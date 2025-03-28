from datetime import datetime

import jpholiday
import pytz
from flask import Flask, jsonify, request

app = Flask(__name__)

# 仮の時刻表データ
TIMETABLE = {
    "zenkojishita": {
        "up": {
            "weekday":[
                {"time": "05:44", "destination": "Nagano", "type": "local"},
                {"time": "06:08", "destination": "Nagano", "type": "local"},
                {"time": "06:35", "destination": "Nagano", "type": "local"},
                {"time": "07:02", "destination": "Nagano", "type": "local"},
                {"time": "07:27", "destination": "Nagano", "type": "local"},
                {"time": "07:45", "destination": "Nagano", "type": "local"},
                {"time": "07:58", "destination": "Nagano", "type": "local"},
                {"time": "08:24", "destination": "Nagano", "type": "local"},
                {"time": "08:38", "destination": "Nagano", "type": "local"},
                {"time": "08:49", "destination": "Nagano", "type": "local"},
                {"time": "09:17", "destination": "Nagano", "type": "local"},
                {"time": "09:42", "destination": "Nagano", "type": "local"},
                {"time": "10:04", "destination": "Nagano", "type": "local"},
                {"time": "10:29", "destination": "Nagano", "type": "local"},
                {"time": "11:01", "destination": "Nagano", "type": "local"},
                {"time": "11:26", "destination": "Nagano", "type": "local"},
                {"time": "12:08", "destination": "Nagano", "type": "local"},
                {"time": "12:41", "destination": "Nagano", "type": "local"},
                {"time": "13:06", "destination": "Nagano", "type": "local"},
                {"time": "13:52", "destination": "Nagano", "type": "local"},
                {"time": "14:25", "destination": "Nagano", "type": "local"},
                {"time": "14:54", "destination": "Nagano", "type": "local"},
                {"time": "15:30", "destination": "Nagano", "type": "local"},
                {"time": "16:10", "destination": "Nagano", "type": "local"},
                {"time": "16:31", "destination": "Nagano", "type": "local"},
                {"time": "16:59", "destination": "Nagano", "type": "local"},
                {"time": "17:25", "destination": "Nagano", "type": "local"},
                {"time": "18:03", "destination": "Nagano", "type": "local"},
                {"time": "18:32", "destination": "Nagano", "type": "local"},
                {"time": "18:55", "destination": "Nagano", "type": "local"},
                {"time": "19:21", "destination": "Nagano", "type": "local"},
                {"time": "19:52", "destination": "Nagano", "type": "local"},
                {"time": "20:20", "destination": "Nagano", "type": "local"},
                {"time": "21:11", "destination": "Nagano", "type": "local"},
                {"time": "21:41", "destination": "Nagano", "type": "local"},
                {"time": "22:25", "destination": "Nagano", "type": "local"},
            ],
            "saturday":[
                {"time": "05:44", "destination": "Nagano", "type": "local"},
                {"time": "06:08", "destination": "Nagano", "type": "local"},
                {"time": "06:35", "destination": "Nagano", "type": "local"},
                {"time": "07:02", "destination": "Nagano", "type": "local"},
                {"time": "07:27", "destination": "Nagano", "type": "local"},
                {"time": "07:58", "destination": "Nagano", "type": "local"},
                {"time": "08:24", "destination": "Nagano", "type": "local"},
                {"time": "08:49", "destination": "Nagano", "type": "local"},
                {"time": "09:17", "destination": "Nagano", "type": "local"},
                {"time": "09:42", "destination": "Nagano", "type": "local"},
                {"time": "10:04", "destination": "Nagano", "type": "local"},
                {"time": "10:29", "destination": "Nagano", "type": "local"},
                {"time": "11:01", "destination": "Nagano", "type": "local"},
                {"time": "11:26", "destination": "Nagano", "type": "local"},
                {"time": "12:08", "destination": "Nagano", "type": "local"},
                {"time": "12:41", "destination": "Nagano", "type": "local"},
                {"time": "13:06", "destination": "Nagano", "type": "local"},
                {"time": "13:52", "destination": "Nagano", "type": "local"},
                {"time": "14:25", "destination": "Nagano", "type": "local"},
                {"time": "14:54", "destination": "Nagano", "type": "local"},
                {"time": "15:30", "destination": "Nagano", "type": "local"},
                {"time": "16:10", "destination": "Nagano", "type": "local"},
                {"time": "16:31", "destination": "Nagano", "type": "local"},
                {"time": "16:59", "destination": "Nagano", "type": "local"},
                {"time": "17:25", "destination": "Nagano", "type": "local"},
                {"time": "18:03", "destination": "Nagano", "type": "local"},
                {"time": "18:32", "destination": "Nagano", "type": "local"},
                {"time": "18:55", "destination": "Nagano", "type": "local"},
                {"time": "19:21", "destination": "Nagano", "type": "local"},
                {"time": "19:52", "destination": "Nagano", "type": "local"},
                {"time": "20:20", "destination": "Nagano", "type": "local"},
                {"time": "21:11", "destination": "Nagano", "type": "local"},
                {"time": "21:41", "destination": "Nagano", "type": "local"},
                {"time": "22:25", "destination": "Nagano", "type": "local"},
            ],
            "holiday":[
                {"time": "05:44", "destination": "Nagano", "type": "local"},
                {"time": "06:08", "destination": "Nagano", "type": "local"},
                {"time": "06:35", "destination": "Nagano", "type": "local"},
                {"time": "07:02", "destination": "Nagano", "type": "local"},
                {"time": "07:27", "destination": "Nagano", "type": "local"},
                {"time": "07:58", "destination": "Nagano", "type": "local"},
                {"time": "08:24", "destination": "Nagano", "type": "local"},
                {"time": "08:49", "destination": "Nagano", "type": "local"},
                {"time": "09:17", "destination": "Nagano", "type": "local"},
                {"time": "09:42", "destination": "Nagano", "type": "local"},
                {"time": "10:04", "destination": "Nagano", "type": "local"},
                {"time": "10:29", "destination": "Nagano", "type": "local"},
                {"time": "11:01", "destination": "Nagano", "type": "local"},
                {"time": "11:26", "destination": "Nagano", "type": "local"},
                {"time": "12:08", "destination": "Nagano", "type": "local"},
                {"time": "12:41", "destination": "Nagano", "type": "local"},
                {"time": "13:06", "destination": "Nagano", "type": "local"},
                {"time": "13:52", "destination": "Nagano", "type": "local"},
                {"time": "14:25", "destination": "Nagano", "type": "local"},
                {"time": "14:54", "destination": "Nagano", "type": "local"},
                {"time": "15:30", "destination": "Nagano", "type": "local"},
                {"time": "16:10", "destination": "Nagano", "type": "local"},
                {"time": "16:31", "destination": "Nagano", "type": "local"},
                {"time": "16:59", "destination": "Nagano", "type": "local"},
                {"time": "17:25", "destination": "Nagano", "type": "local"},
                {"time": "18:03", "destination": "Nagano", "type": "local"},
                {"time": "18:32", "destination": "Nagano", "type": "local"},
                {"time": "18:55", "destination": "Nagano", "type": "local"},
                {"time": "19:21", "destination": "Nagano", "type": "local"},
                {"time": "19:52", "destination": "Nagano", "type": "local"},
                {"time": "20:20", "destination": "Nagano", "type": "local"},
                {"time": "21:11", "destination": "Nagano", "type": "local"},
                {"time": "21:41", "destination": "Nagano", "type": "local"},
                {"time": "22:25", "destination": "Nagano", "type": "local"},
            ],
        }
    }
}

def get_next_trains(timetable, num_trains=3):
    """ 現在時刻以降の直近N本の電車を取得 """
    # 日本時間の現在時刻を取得
    tz_japan = pytz.timezone("Asia/Tokyo")
    now = datetime.now(tz_japan)

    # 現在時刻を基準にフィルタリング
    upcoming_trains = [
        train for train in timetable if datetime.strptime(train["time"], "%H:%M").time() > now.time()
    ]

    # 直近N本を取得（最大で num_trains 本）
    return upcoming_trains[:num_trains]

@app.route("/timetable", methods=["GET"])
def get_timetable():
    """ 善光寺下駅の直近3本の電車時刻表を取得するAPI """
    station = request.args.get("station", "zenkojishita").lower()
    direction = request.args.get("direction", "up").lower()

    if station not in TIMETABLE:
        return jsonify({"error": "Station not found"}), 404
    if direction not in TIMETABLE[station]:
        return jsonify({"error": "Invalid direction"}), 400

    # 直近3本の電車を取得
    next_trains = get_next_trains(TIMETABLE[station][direction], num_trains=3)

    return jsonify({
        "station": station,
        "direction": direction,
        "next_trains": next_trains
    })

if __name__ == "__main__":
    app.run(debug=True)

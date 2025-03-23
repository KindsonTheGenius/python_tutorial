appointments = [
 {
 "title": "Team Standup",
 "start": "2023-11-02 09:00",
 "end": "2023-11-02 09:30",
 "timezone": "America/New_York"
 },
 {
 "title": "Project Review",
 "start": "2023-11-02 14:00",
 "end": "2023-11-02 15:00",
 "timezone": "Europe/London"
 },
 {
 "title": "1:1 with Manager",
 "start": "2023-11-02 09:00",
 "end": "2023-11-02 09:45",
 "timezone": "America/Los_Angeles"
 }
 # ... add more as needed
]

# 1
from datetime import datetime
from zoneinfo import ZoneInfo

for apt in appointments:
    apt["start"] = datetime.strptime(apt["start"], "%Y-%m-%d %H:%M").replace(tzinfo=ZoneInfo(apt["timezone"]))
    apt["end"] = datetime.strptime(apt["end"], "%Y-%m-%d %H:%M").replace(tzinfo=ZoneInfo(apt["timezone"]))

for pt in appointments:
 print(f"{pt['title']}: {pt['start']} to {pt['end']}, {pt['timezone']}")

def detect_overtime(time1, time2):
 return time2 > time1

start1 = datetime.strptime("2023-11-02 09:00", "%Y-%m-%d %H:%M").replace(tzinfo=ZoneInfo("UTC"))
end1 = datetime.strptime("2023-11-02 09:30", "%Y-%m-%d %H:%M").replace(tzinfo=ZoneInfo("UTC"))
a1 = start1 - end1
start2 = datetime.strptime("2023-11-02 14:00", "%Y-%m-%d %H:%M").replace(tzinfo=ZoneInfo("UTC"))
end2 = datetime.strptime("2023-11-02 15:00", "%Y-%m-%d %H:%M").replace(tzinfo=ZoneInfo("UTC"))
a2 = start2 - end2

result = detect_overtime(a1, a2)
print(result)

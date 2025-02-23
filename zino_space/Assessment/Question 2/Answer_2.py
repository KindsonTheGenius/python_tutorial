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
import pytz

for apt in appointments:
    tz = pytz.timezone(appointments["timezone"])
    apt["start"] = tz.localize(datetime.strptime(apt["start"], "%Y-%m-%d %H:%M"))
    apt["end"] = tz.localize(datetime.strptime(apt["end"], "%Y-%m-%d %H:%M"))

for pt in appointments:
 print(f"{pt['title']}: {pt['start']} to {pt['end']}, {pt['timezone']}")
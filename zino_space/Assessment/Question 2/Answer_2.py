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
from zoneinfo import ZoneInfo  # Use pytz if on older Python versions

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
]

# Function to check if two appointments overlap
def detect_overtime(time1_start, time1_end, time2_start, time2_end):
    return time1_end > time2_start and time1_start < time2_end

# 1. Parse start and end times with their timezones
for appt in appointments:
    tz = ZoneInfo(appt["timezone"])
    appt["start_dt"] = datetime.strptime(appt["start"], "%Y-%m-%d %H:%M").replace(tzinfo=tz)
    appt["end_dt"] = datetime.strptime(appt["end"], "%Y-%m-%d %H:%M").replace(tzinfo=tz)

# 2. Convert to UTC
for appt in appointments:
    appt["start_utc"] = appt["start_dt"].astimezone(ZoneInfo("UTC"))
    appt["end_utc"] = appt["end_dt"].astimezone(ZoneInfo("UTC"))

# 3. Calculate duration in minutes
for appt in appointments:
    appt["duration_minutes"] = int((appt["end_utc"] - appt["start_utc"]) // 60)

# 4. Detect overlapping appointments
appointments_sorted = sorted(appointments, key=lambda x: x["start_utc"])  # Sort by UTC start
overlapping_appointments = []

for i in range(len(appointments_sorted)):
    for j in range(i + 1, len(appointments_sorted)):
        appt1 = appointments_sorted[i]
        appt2 = appointments_sorted[j]
        if detect_overtime(appt1["start_utc"], appt1["end_utc"], appt2["start_utc"], appt2["end_utc"]):
            overlapping_appointments.append((appt1["title"], appt2["title"]))

# 5. Print appointments sorted by UTC start
print("\nSorted Appointments:")
for appt in appointments_sorted:
    print(f"\nTitle: {appt['title']}")
    print(f"UTC Start: {appt['start_utc']}")
    print(f"UTC End: {appt['end_utc']}")
    print(f"Duration: {appt['duration_minutes']} minutes")

# 6. Convert back to local timezone (e.g., America/New_York)
local_tz = ZoneInfo("America/New_York")
print("\nAppointments in Local Time (America/New_York):")
for appt in appointments_sorted:
    local_start = appt["start_utc"].astimezone(local_tz)
    local_end = appt["end_utc"].astimezone(local_tz)
    print(f"\nTitle: {appt['title']}")
    print(f"Local Start: {local_start}")
    print(f"Local End: {local_end}")

# Print overlapping appointments
if overlapping_appointments:
    print("\nOverlapping Appointments:")
    for pair in overlapping_appointments:
        print(f"{pair[0]} overlaps with {pair[1]}")
else:
    print("\nNo overlapping appointments found.")


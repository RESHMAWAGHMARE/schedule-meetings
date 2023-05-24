from datetime import datetime, timedelta
import random

def generate_random_meetings(num_meetings, start_time, end_time):
    meetings = []
    time_range = end_time - start_time

    for _ in range(num_meetings):
        start = start_time + timedelta(minutes=random.randint(0, int(time_range.total_seconds() / 60)))
        duration = timedelta(minutes=random.randint(15, 120))
        end = start + duration
        meetings.append((start, end))

    return meetings

def schedule_meetings(meetings, num_rooms):
    rooms = [[] for _ in range(num_rooms)]  # Initialize empty rooms
    
    # Sort meetings by start time
    meetings.sort(key=lambda x: x[0])
    
    for meeting in meetings:
        scheduled = False
        
        # Check each room for availability
        for i, room in enumerate(rooms):
            if not room or meeting[0] >= room[-1][1]:  # If the room is empty or the meeting starts after the last meeting in the room
                room.append(meeting)
                scheduled = True
                break
        
        if not scheduled:
            # If no room is available, create a new room and schedule the meeting
            rooms.append([meeting])
    
    return rooms

# Example usage
num_meetings = 15
start_time = datetime(2023, 5, 23, 0, 0)
end_time = datetime(2023, 5, 23, 23, 59)

meetings = generate_random_meetings(num_meetings, start_time, end_time)
num_rooms = 3

scheduled_rooms = schedule_meetings(meetings, num_rooms)

# Print the scheduled meetings for each room
for i, room in enumerate(scheduled_rooms):
    print(f"Room {i+1}:")
    for meeting in room:
        print(f"   Meeting: {meeting[0]} - {meeting[1]}")

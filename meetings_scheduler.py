from datetime import datetime

def schedule_meetings(meetings, num_rooms):
    # Sort the meetings based on their start times
    sorted_meetings = sorted(meetings, key=lambda x: x[0])
    
    # Initialize a list of rooms with their end times
    rooms = [[] for _ in range(num_rooms)]
    
    # Iterate through each meeting
    for meeting in sorted_meetings:
        # Find the first available room
        for room in rooms:
            if not room or room[-1][1] <= meeting[0]:
                # Assign the meeting to the room
                room.append(meeting)
                break
        else:
            # If no available room is found, add a new room
            rooms.append([meeting])
    
    return rooms


# Example usage
meetings = [
    (datetime(2023, 5, 23, 0, 26), datetime(2023, 5, 23, 1, 27)),
    (datetime(2023, 5, 23, 1, 33), datetime(2023, 5, 23, 2, 8)),
    (datetime(2023, 5, 23, 3, 9), datetime(2023, 5, 23, 3, 41)),
    (datetime(2023, 5, 23, 6, 54), datetime(2023, 5, 23, 8, 10)),
    (datetime(2023, 5, 23, 9, 8), datetime(2023, 5, 23, 9, 34)),
    (datetime(2023, 5, 23, 10, 17), datetime(2023, 5, 23, 11, 3)),
    (datetime(2023, 5, 23, 11, 24), datetime(2023, 5, 23, 11, 55)),
    (datetime(2023, 5, 23, 13, 9), datetime(2023, 5, 23, 13, 32)),
    (datetime(2023, 5, 23, 16, 6), datetime(2023, 5, 23, 16, 46)),
    (datetime(2023, 5, 23, 20, 44), datetime(2023, 5, 23, 22, 8)),
    (datetime(2023, 5, 23, 3, 23), datetime(2023, 5, 23, 4, 36)),
    (datetime(2023, 5, 23, 7, 40), datetime(2023, 5, 23, 8, 56)),
    (datetime(2023, 5, 23, 11, 2), datetime(2023, 5, 23, 11, 57)),
    (datetime(2023, 5, 23, 21, 48), datetime(2023, 5, 23, 22, 21)),
    (datetime(2023, 5, 23, 11, 48), datetime(2023, 5, 23, 12, 10))
]

num_rooms = 3

scheduled_rooms = schedule_meetings(meetings, num_rooms)

# Print the scheduled meetings for each room
for i, room in enumerate(scheduled_rooms):
    print(f"Room {i+1}:")
    for meeting in room:
        print(f"   Meeting: {meeting[0]} - {meeting[1]}")

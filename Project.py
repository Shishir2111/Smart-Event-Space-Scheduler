from datetime import datetime
import matplotlib.pyplot as plt

events = []

def check_conflict(events, date, start, end, room):
    new_start = datetime.strptime(start, "%H:%M")
    new_end = datetime.strptime(end, "%H:%M")

    for event in events:
        if event["date"] == date and event["room"] == room:
            existing_start = datetime.strptime(event["start"], "%H:%M")
            existing_end = datetime.strptime(event["end"], "%H:%M")

            if new_start < existing_end and new_end > existing_start:
                return True
    return False


def add_event():
    title = input("Enter Title: ")
    date = input("Enter Date (YYYY-MM-DD): ")
    start = input("Enter Start Time (HH:MM): ")
    end = input("Enter End Time (HH:MM): ")
    room = input("Enter Room: ")

    if not check_conflict(events, date, start, end, room):
        event = {
            "title": title,
            "date": date,
            "start": start,
            "end": end,
            "room": room
        }
        events.append(event)
        print("Event added successfully.\n")
    else:
        print("Conflict detected!\n")


def view_events():
    if not events:
        print("No events available.\n")
        return

    for e in events:
        print("Title :", e["title"])
        print("Date  :", e["date"])
        print("Start :", e["start"])
        print("End   :", e["end"])
        print("Room  :", e["room"])
        print("--------------------")
    print()


def show_graphs():
    if not events:
        print("No events to display graphs.\n")
        return

    titles = []
    durations = []

    for e in events:
        start_time = datetime.strptime(e["start"], "%H:%M")
        end_time = datetime.strptime(e["end"], "%H:%M")
        duration = (end_time - start_time).seconds / 3600
        titles.append(e["title"])
        durations.append(duration)

    # -------- BAR GRAPH --------
    plt.figure()
    plt.bar(titles, durations)
    plt.xlabel("Event Titles")
    plt.ylabel("Duration (Hours)")
    plt.title("Overall Event Duration")
    plt.xticks(rotation=45)
    plt.show()

    # -------- PIE CHART --------
    plt.figure()
    plt.pie(durations, labels=titles, autopct='%1.1f%%')
    plt.title("Overall Event Time Distribution")
    plt.show()


# -------- MENU --------
while True:
    print("1. Add Event")
    print("2. View Events")
    print("3. Show Graphs")
    print("4. Exit")

    choice = input("Select Option (1-4): ")

    if choice == "1":
        add_event()
    elif choice == "2":
        view_events()
    elif choice == "3":
        show_graphs()
    elif choice == "4":
        print("Exiting Program...")
        break
    else:
        print("Invalid Option!\n")

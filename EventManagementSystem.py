# Task 2
# Objective: Extend the existing Event class by adding a feature to keep track of the number of participants. Implement a method add_participant that increases the count and a method get_participant_count to retrieve the current count.abs

# Declare a class Event
class Event:

    # Define the constructor, pass in name and date.
    def __init__(self, name, date, participant_count):
        self.name = name
        self.date = date
        self.participant_count = participant_count

    # Define a method add_participant
    def add_participant(self):
        self.participant_count += 1

    # Define a method get_participant_count
    def get_participant_count(self):
        return self.participant_count

# Create instances of the Event class
event1 = Event("Birthday Party", "2021-01-01", 10)
event2 = Event("Wedding", "2021-02-14", 50)
event3 = Event("Conference", "2021-03-30", 100)

# Print the current participant count of each event
for i, event in enumerate([event1, event2, event3]):
    print(f"The current participant count of event{i + 1} is {event.get_participant_count()}")

# Add participants to each event
event1.add_participant()
event2.add_participant()
event3.add_participant()

# Print the updated participant count of each event
for i, event in enumerate([event1, event2, event3]):
    print(f"The updated participant count of event{i + 1} is {event.get_participant_count()}")
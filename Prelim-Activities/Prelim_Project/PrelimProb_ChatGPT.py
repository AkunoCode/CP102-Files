import os
import re

class Events:
    def __init__(self, text):
        self.text = text
        self.email_pattern = re.compile(r'\w+@\w+\.[a-zA-Z]{2,4}')
        self.phone_pattern = re.compile(r'((\+63)[ -]?(\d{3})[ -]?(\d{3})[ -]?(\d{4}))|(09\d{9})')
        self.event_pattern = re.compile(r'\"([A-Z0-9]\w+\s?)+\"')
        self.date_pattern = re.compile(r'((0?[1-9]|[12][0-9]|3[01])[-/.](0?[1-9]|1[012])[-/.](19|20)?\d{2})|((Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)\s(0?[1-9][a-z]{2}|[12]\d[a-z]{2}|3[01][a-z]{2}),?\s(19|20)?\d{2})')

    def find(self, pattern):
        match = pattern.search(self.text)
        return match.group() if match else "None"

    def summary(self):
        print(f"Event: {self.find(self.event_pattern)}")
        print(f"Schedule: {self.find(self.date_pattern)}")
        print(f"Sender Email: {self.find(self.email_pattern)}")
        print(f"Sender Phone: {self.find(self.phone_pattern)}\n")
    
    # def save_summary(self, filename):
    #     summary = f"Event: {self.find(self.event_pattern)}\nSchedule: {self.find(self.date_pattern)}\nSender Email: {self.find(self.email_pattern)}\nSender Phone: {self.find(self.phone_pattern)}\n\n"
    #     with open(filename, "a") as file:
    #         file.write(summary)

print("\nHERE IS THE SUMMARY OF ALL INVITATIONS:\n")
folder_path = "Prelim-Activities/Prelim_Project/Invitations"
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, "r") as file:
            text = file.read()
            event_catcher = Events(text)
            event_catcher.summary()
            # event_catcher.save_summary("summary.txt")
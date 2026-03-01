# ============================================================
#               EMAIL SIMULATOR - LINKING TREE
# ============================================================

# PROGRAM FLOW STRUCTURE
#
# main()
#   │
#   ├── Creates → User("Tory")
#   │         │
#   │         └── HAS → Inbox()
#   │                    └── emails = []  (list of Email objects)
#   │
#   ├── Creates → User("Ramy")
#   │         │
#   │         └── HAS → Inbox()
#   │                    └── emails = []
#   │
#   └── Email Sending Flow:
#            Tory.send_email(Ramy)
#                 │
#                 ├── Creates → Email object
#                 │         │
#                 │         ├── sender   → (User object: Tory)
#                 │         ├── receiver → (User object: Ramy)
#                 │         ├── subject
#                 │         ├── body
#                 │         ├── timestamp
#                 │         └── read = False
#                 │
#                 └── Calls → Ramy.inbox.receive_email(email)
#                                │
#                                └── Stores Email object inside:
#                                      Ramy.inbox.emails (list)
#
#
# OBJECT RELATIONSHIP TREE
#
# User
#  ├── name
#  └── inbox (Inbox object)
#         └── emails (list)
#               ├── Email object
#               │      ├── sender (User object)
#               │      ├── receiver (User object)
#               │      ├── subject
#               │      ├── body
#               │      ├── timestamp
#               │      └── read (True/False)
#               │
#               └── Email object
#
#
# METHOD CALL FLOW (When Reading Email)
#
# ramy.read_email(1)
#     │
#     └── User.read_email()
#             │
#             └── Inbox.read_email()
#                     │
#                     └── self.emails[index]
#                             │
#                             └── Email.display_full_email()
#                                     │
#                                     └── Email.mark_as_read()
#
#
# KEY OOP CONCEPTS USED:
#
# ✔ Composition:
#     User HAS Inbox
#     Inbox HAS Email objects
#
# ✔ Object References:
#     Email stores FULL User objects (not just names)
#
# ✔ Delegation:
#     User delegates inbox actions to Inbox
#     Inbox delegates display logic to Email
#
# ✔ Encapsulation:
#     Each class manages its own responsibility
#
# ✔ State Change:
#     Email.read changes from False → True
#
# =========================================================================================================================================================================================================================================================

# In this workshop, you are going to build an Email Simulator that simulates 
# sending, receiving, and managing emails between different users.
# This project demonstrates:
# - Classes and Objects
# - Composition (objects inside objects)
# - Method delegation (one object calling another object's method)
# - Object references

import datetime  # Used to generate timestamp for emails


# ==============================
# EMAIL CLASS
# ==============================
class Email:
    def __init__(self, sender, receiver, subject, body):
        # sender → FULL User object who sends the email
        # receiver → FULL User object who receives the email
        
        self.sender = sender        # storing reference to User object
        self.receiver = receiver    # storing reference to User object
        self.subject = subject      # subject text
        self.body = body            # email body text
        
        # timestamp stores exact time email was created
        self.timestamp = datetime.datetime.now()
        
        # read status of email (default = unread)
        self.read = False

    def mark_as_read(self):
        # This changes the state of the email
        # State change is important in OOP
        self.read = True

    def display_full_email(self):
        # When user reads email, mark it as read
        self.mark_as_read()

        # Display complete details
        print('\n--- Email ---')
        print(f'From: {self.sender.name}')   # Accessing name from User object
        print(f'To: {self.receiver.name}')   # Accessing name from User object
        print(f'Subject: {self.subject}')
        
        # Formatting timestamp for readable output
        print(f"Received: {self.timestamp.strftime('%Y-%m-%d %H:%M')}")
        print(f'Body: {self.body}')
        print('------------\n')

    def __str__(self):
        # __str__ is special method
        # It defines what gets printed when object is printed
        # Used inside Inbox list display

        status = 'Read' if self.read else 'Unread'

        return f"[{status}] From: {self.sender.name} | Subject: {self.subject} | Time: {self.timestamp.strftime('%Y-%m-%d %H:%M')}"


# ==============================
# INBOX CLASS
# ==============================
class Inbox:
    def __init__(self):
        # emails is a LIST that stores Email OBJECTS
        # Important: It stores objects, not strings
        self.emails = []

    def receive_email(self, email):
        # email parameter is a FULL Email object
        # We store it inside inbox list
        self.emails.append(email)

    def list_emails(self):
        # If inbox empty
        if not self.emails:
            print('Your inbox is empty.\n')
            return
        
        print('\nYour Emails:')
        
        # enumerate gives index + object
        # start=1 makes index user-friendly (humans count from 1)
        for i, email in enumerate(self.emails, start=1):
            # email here is an Email object
            # printing email automatically calls __str__()
            print(f'{i}. {email}')

    def read_email(self, index):
        # Prevent errors if inbox empty
        if not self.emails:
            print('Inbox is empty.\n')
            return
        
        # Convert human index (1-based) to list index (0-based)
        actual_index = index - 1

        # Boundary check
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return
        
        # Get Email object from list
        # Then call its method
        self.emails[actual_index].display_full_email()

    def delete_email(self, index):
        if not self.emails:
            print('Inbox is empty.\n')
            return
        
        actual_index = index - 1

        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return
        
        # Delete specific Email object from list
        del self.emails[actual_index]
        print('Email deleted.\n')
        

# ==============================
# USER CLASS
# ==============================
class User:
    def __init__(self, name):
        self.name = name
        
        # Every user automatically gets an Inbox object
        # This is COMPOSITION (User HAS an Inbox)
        self.inbox = Inbox()

    def send_email(self, receiver, subject, body):
        # Create Email object
        # sender=self → current User object
        email = Email(sender=self, receiver=receiver, subject=subject, body=body)

        # Send email to receiver's inbox
        receiver.inbox.receive_email(email)

        print(f'Email sent from {self.name} to {receiver.name}!\n')

    def check_inbox(self):
        print(f"\n{self.name}'s Inbox:")
        # Delegate listing responsibility to Inbox
        self.inbox.list_emails()

    def read_email(self, index):
        # Delegate reading responsibility to Inbox
        self.inbox.read_email(index)

    def delete_email(self, index):
        # Delegate deletion responsibility to Inbox
        self.inbox.delete_email(index)


# ==============================
# MAIN PROGRAM (Simulation Entry Point)
# ==============================
def main():
    # Create two users
    tory = User('Tory')
    ramy = User('Ramy')        
    
    # Tory sends email to Ramy
    tory.send_email(ramy, 'Hello', 'Hi Ramy, just saying hello!')
    
    # Ramy sends reply to Tory
    ramy.send_email(tory, 'Re: Hello', 'Hi Tory, hope you are fine.')
    
    # Ramy checks inbox
    ramy.check_inbox()
    
    # Ramy reads first email
    ramy.read_email(1)
    
    # Ramy deletes first email
    ramy.delete_email(1)
    
    # Ramy checks inbox again
    ramy.check_inbox()


# This ensures main() runs only when file is executed directly
if __name__ == '__main__':
    main()
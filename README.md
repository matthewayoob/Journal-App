# Journal-App

**Running Instructions**
python3 journal.py (starts demo) Commands:
Create an entry: ./journal --create "Contents" --title "Entry Title" (with or w/o "") List All Existing Entries: ./journal --list
Delete an entry: ./journal.py --deleteTitle Title (exact title name)
Show a specifc entry: ./journal.py --showEntry MyEntryTitle (exact title name) Quit: exit (quit input line demo)

**Functionality Summary**

● Classes: The code employs two classes, Journal and JournalEntry, for organizing journal
entries and individual entries, promoting code organization and expandability.

● User Interface: The code offers a command-line input interface, making a more
enjoyable and fun demo experience for creating, listing, deleting, and viewing journal
entries.

● Data Storage: Journal entries are stored in memory, using a list for entries and a set for
ensuring unique titles. However, I chose to refresh the journal after every demo for
consistency (increased persistence if I made a global journal).

● Demo Timestamps: A demo tracks how long it runs, displaying elapsed time for
potential user testing in the future. Other meaningful metrics would be the ratio of
success/failure commands and dropoff by implemented feature.

● Command Flexibility: 
Commands “autocorrect” for users by checking for perfect
equivalence on the most crucial parts of the executable. For example, ./jouf a new journal entry" --title Title of entry
will create the same output as...
./journal --create "Contents of a new journal entry" --title “Title of entry”,
ignoring typos in the executable name (since there is only one file in our system and
letting the user stipulate if they want to use “” or not).

● Ease of Use & Exception Handling: The code handles exceptions, guiding users and
prompting them with a readable error message and examples of correct commands.

**Potential Limitations**

● Limited Persistence: Entries are only stored in memory, offering no long-term storage.
  Enabling persistence through file or database storage would be an improvement.
● Lack of Journal Entry Editing: The code lacks entry editing journal functionality,
which could enhance the application's features.

● User Interface: The command-line interface may not suit all users, and a graphical interface could enhance usability, especially for communities with varying types of vision.

● Runtime: The code's runtime performance is relatively efficient for managing entries in memory, but this could impact performance with a significantly large number of entries, especially if we implement filtering. The journal entries are stored in an attribute array. Some potential approaches could be caching MRU (or making more easily accessible common entries i.e. Journal Entry Title: “Grocery List”)

**Unit Testing**

I tested success and failure for each respective task below.

● Create Entries: Creating a new entry and attempting to create an entry with the same title

● View Entries: Printing an entry and trying to print an entry that does not exist (entry by
entry and by entire journal)

● Delete Entries: Deleting an entry and deleting an entry that does not exist

**System Testing**

We want our system to work together in harmony. For example, I confirmed that I could print newly made entries of varying form (“Title”, “My New Title”, and New Title (without quotes)). Therefore, to the best of my ability and in the time constraint, I tested the commands in different order and asserted that the system was in the proper state regardless of executable order.
Alongside this, I confirmed that my executions were idempotent, so regardless of the amount of times of running the command, the system will stay in the correct/intuitive state.

**Enhancement Ideas**

● Stress Testing: Create test script with a large number of entries to monitor behavior

● Persistence Testing: If future enhancements include increased data persistence, test data
storage and retrieval, and stressing those retrievals.

● New Features
  Querying based on other factors of journals (date, title, ascending, descending)
  
● Likely to require new data structure implementation or quicker lookup, pondering dictionaries and hashing 

● Multiple Users: Creating login and logout capabilities which would require credentials, security provisions, sophisticated UI, etc.

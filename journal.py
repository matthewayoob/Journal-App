#Candidate: Matthew Louis Ayoob

from datetime import datetime
import pytz
import sys
import time
import shlex

# Prompt: Create a simple journal app that lets people create / view / delete their journal entries.
'''Supported Commands:
        Create an entry: ./journal --create "Contents of a new journal entry" --title "Title of entry" (with or without "")
        List All Existing Entries: ./journal --list
        Sort: ./journal --sortList
        Delete an entry: ./journal --deleteTitle MyEntryTitle (must match exact title name)
        Show a specifc entry: ./journal --showEntry MyEntryTitle (must match exact title name)
'''

DASHES_FOR_UI = 55 
PAD_FOR_UI = 6

'''
Sort lexigraphically:
sorting as journal inserted 
'''

class Journal:
    """
    Initialize a Journal object.

    This class represents a journal and manages journal entries.

    Attributes:
    entries (list): A list to store journal entries.
    unique_entry_names (set): A set to store unique entry titles.
    """
    def __init__(self):
        self.entries = []
        self.unique_entry_names = set()

    """
    Add a journal entry to the journal.

    Args:
    entry (JournalEntry): The journal entry to add to the journal.

    This method checks if the entry title is unique and adds the entry to the journal if it is.
    """
    def add_entry(self, entry):
        if entry.title not in self.unique_entry_names:
            self.entries.append(entry)
            self.unique_entry_names.add(entry.title)
        else:
            print("A entry with that title has already been written in your journal. Try a new name, or delete your old entry and try again.")

    """
    Delete a journal entry from the journal.

    Args:
    title_of_entry (str): The title of the entry to be deleted.

    This method removes the specified entry from the journal and updates the set of unique entry titles.
    """
    def delete_entry(self, title_of_entry):
        self.unique_entry_names.remove(title_of_entry)
        # iterate through entries and only maintain non-deleted entries
        self.entries = [entry for entry in self.entries if entry.title != title_of_entry]

    """
    List all journal entries in the journal.

    This method displays all journal entries in the journal.
    """
    def list_entries(self):
        for entry in self.entries:
            entry.display()

    def sort_list(self):
        # new_list = sorted(orig_list, key=lambda x: x.count, reverse=True)
        arr = sorted(self.entries, key=lambda x:x.title)
        for entry in arr:
            entry.display()

    """
    Retrieve a specific journal entry by title.

    Args:
    title (str): The title of the entry to retrieve.

    Returns:
    JournalEntry or None: The journal entry with the specified title, or None if not found.
    """
    def grab_entry(self, title):
        for entry in self.entries:
            if entry.title == title:
                return entry

    """
    Display a summary of all journal entries.

    This method displays the titles of all journal entries in the journal.
    """
    def show_journal(self):
        count = 0
        for entry in self.entries:
            print(f"| {entry.title};")
            count += 1
        print("Total Entries: ", count)

    """
    Display detailed information for all journal entries.

    This method displays detailed information for all journal entries in the journal.
    """
    def show_journal_det(self):
        count = 0
        for entry in self.entries:
            entry.display()
            count += 1
        print("Total Entries: ", count)


class JournalEntry:
    """
    Initialize a JournalEntry object.

    Args:
    title (str): The title of the journal entry.
    content (str): The content of the journal entry.

    This class represents a journal entry with a title, content, and creation timestamp.
    """
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.creationtime = datetime.now(pytz.timezone('US/Pacific')) 
    
    """
    Display detailed information about the journal entry.

    This method displays detailed information about the journal entry, including title, content, and creation timestamp.
    """
    def display(self):
        dashes = '-' * DASHES_FOR_UI 
        front_padding = ' ' * PAD_FOR_UI
        # f-string to display metadata about a specific journal entry with pseudoUI
        print(f"{dashes}\n{front_padding}Title: {self.title}\n{front_padding}Content: {self.content}\n{front_padding}Date of Submission: {self.creationtime.strftime('%m-%d-%Y %I:%M:%S %p PST')}\n{dashes}")

"""
The main function for the journal application.

It initializes the journal, adds sample entries, processes live user commands, and manages the journal entries.
"""
def main():
    start_time = time.time()
    journal = Journal()
    testEntry = JournalEntry("AA", "I am so proud of this new chapter.")
    testEntry2 = JournalEntry("AC", "Apple would be such a cool place to work.")
    testEntry3 = JournalEntry("AB", "I am super excited to discuss my design.")
    testArray = [testEntry, testEntry2, testEntry3]
    #testEntry.display()

    # testJournal = Journal()
    for e in testArray:
        journal.add_entry(e)

    # This while loop takes in command line input and directs it to the respective control flow
    while True:
        user_input = input("Enter a command (or 'exit' to quit).\n\nSuggestions: \nCreate an entry: ./journal --create \"Contents of a new journal entry\" --title \"Title of entry\"  (with or without \"\")\nList All Existing Entries: ./journal --list\nDelete an entry: ./journal --deleteTitle MyEntryTitle (must match exact title name)\nShow a specifc entry: ./journal --showEntry MyEntryTitle (must match exact title name)\nQuit: exit\n\n")
        if user_input.lower() == 'exit':
            print("\nExiting the program.\n")
            break 

        argv = user_input.split()
        if len(argv) < 2:
            raise Exception("List commands after your executable.\n\nSuggestions: \nCreate an entry: ./journal --create \"Contents of a new journal entry\" --title \"Title of entry\"\nList All Existing Entries: ./journal --list\nDelete an entry: ./journal.py --deleteTitle MyEntryTitle\nShow a specifc entry: ./journal.py --showEntry MyEntryTitle\n" )
        
        if argv[1] == "--list":
            journal.show_journal_det()
            print("Done printing entries. Command Executed Successfully.\n ")

        elif argv[1] == '--sortList':
            journal.sort_list()
        #Sort: ./journal --sortList
        
        elif argv[1] == "--deleteTitle":
            # print("Argv current", argv)
            argv = mutate_input(argv, "d")
            entry = argv[2]
            # print("Entry", entry)
            if (entry and entry in journal.unique_entry_names):
                journal.delete_entry(entry)
                print("Deletion Completed.\n ")
            else:
                print("No Entry Found to be Deleted. Command Example: ./journal.py --deleteTitle MyEntryTitle\n")
        
        elif argv[1] == "--showEntry":
            argv = mutate_input(argv, "s")
            entryName = argv[2]
            journalObj = journal.grab_entry(entryName)
            if journalObj is None:
                print("No Entry Exists.\n")
            else:
                journalObj.display()
                print("Entry displayed. \n ")
        
        elif argv[1] == "--create":
            if len(argv) < 4:
                print("Need 3 arguments to create an entry. Command Example: ./journal --create \"Contents of a new journal entry\" --title Title of entry\n")
                return
            
            argv = mutate_input(argv, "c")
            entryContent = argv[2]
            entryName = argv[4]
            
            if entryName in journal.unique_entry_names:
                print("Journal Entry Already Exists, try a unique name or delete the previous entry.\n")
            else:
                journal.add_entry(JournalEntry(entryName, entryContent))
                print("Entry Added. \n ")
            
    elapsed_time = time.time() - start_time
    print("Demo runtime:", elapsed_time, "seconds")
    return

"""
Mutate the argv list to handle commands with quoted segments. This function needed to be made to account for the flexibility of command line arguments; therefore, it autocorrects valid malformed inputs. 

Args:
    argv (list): The list of command-line arguments.
    flag (str): The flag indicating the type of command to handle ("c" for create, "d" for delete, "s" for show).

Returns:
    list: The mutated argv list.
"""
def mutate_input(argv, flag):
    # print(argv)
    if flag == "c":
        i, j = 0, 0
        if len(argv) > 4:
            for ind in range(len(argv)):
                if argv[ind] == '--create':
                    i = ind
                elif argv[ind] == '--title':
                    j = ind

        if i != 0 and j != 0:
            argv1 = argv[:i + 1] 
            argv2 = " ".join(argv[i + 1:j])
            argv3 = argv[j]
            argv4 = " ".join(argv[j + 1:])
            argv1.append(argv2)
            argv1.append(argv3)
            argv1.append(argv4)
            argv = argv1

    elif flag == "d" or flag == "s":
        # print("Current", argv)
        if len(argv) > 3:
            argv = argv[:2] + [" ".join(argv[2:])]
        # print("After", argv)

    return argv

if __name__ == '__main__':
    main()
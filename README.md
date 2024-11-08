
<!-- <p align="center">
 <a href="" target="blank"><img src="" width="200" alt="VARS BOT" /></a>
</p> -->

# <p align="center">```VARS BOT```</p>

A Personal Assistant Bot built in <a href="https://www.python.org/" target="_blanc">Python</a>, featuring interactive console tables styled with the powerful  <a href="https://rich.readthedocs.io/en/latest/tables.html" target="_blank">Rich</a> library.


## Description

A Python-based console application designed for managing <strong>contacts</strong> and <strong>notes</strong>


## Prerequisites

Please make sure that Python (version >= 3.10) is installed on your operating system.


## Install all dependencies using commands:

```bash
pip install -r requirements.txt
```

## Installation

To install <strong>vars-assistant-bot</strong>, follow these steps:

```bash
$ cd <dir-name>
$ python -m venv .
$ source bin/activate
$ git clone https://github.com/antmuraha/goit-pycore-vars-assistant-bot.git
$ pip install -r requirements.txt
```

## Running the app

```bash
$ python assistant_bot/
```

## Technical Specification Summary for the "Personal Assistant" Project

### Core Functional Requirements
The Personal Assistant includes the following features:

- <strong>Contact Management</strong> 
    - Adding Contacts: Stores contacts with names, addresses, phone numbers, email addresses, and birthdays.
    - Birthday Notifications: Displays a list of contacts with upcoming birthdays based on a user-specified number of days from the current date.
    - Data Validation: Validates phone numbers and email addresses during contact creation or editing, alerting the user to incorrect entries.
    - Search Contacts: Enables search functionality to find contacts based on name or other criteria.
    - Edit and Delete Contacts: Allows users to update or remove contact information.

- <strong>Note Management</strong>
    - Create Notes: Stores text-based notes for user access.
    - Search Notes: Provides functionality for searching notes by content.
    - Edit and Delete Notes: Allows modification and deletion of notes as needed.

- <strong>Data Storage</strong>
    - Saves all contact and note data on the user’s local drive.
    - Retains data across application restarts to prevent data loss.

### Additional Functionality:
Additional features:
Enhanced Personal Assistant Management
- <strong>Tags</strong>:
Adds tagging functionality to notes, allowing categorization through keywords.
Tag-Based Search: Provides a search and sorting mechanism for notes based on tags.
- <strong>Intelligent Command Suggestions</strong>
Implements natural language processing to interpret user input and suggest the closest available command, enhancing usability with predictive assistance. 

This project delivers a robust, user-centric personal assistant with efficient data management and intuitive interactions for improved productivity.


## Stay in touch

- Author - [Ruslan Kryvko, Svitlana Ripa, Anastasiia Kushch, Viacheslav Opryshko - VARS Team]


## License


[MIT licensed](LICENSE) - # to input 



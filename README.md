# Assassins organizer app

Development process
- Initial google forms for people to sign up for assassins
- Randomize google sheets row entries to randomize target assignment order
- Export sheets as csv
- Read csv using python
- Create JSON file storing name: [email: __ , target: __, targeted by: __, eliminated: true/false, year: __, kills: __]
- JSON entries are effectively nodes in a doubly linked list
- App features: eliminate, remove, email initial and new assignments, write to JSON, view game
- GUI using PyQT5

Folders/files
- CreateGame creates the JSON using the CSV file
- RunGame creates GUI and allows organizer to send emails, eliminate players, and view the game

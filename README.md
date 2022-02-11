# Assassins

- Initial google forms for people to sign up for assassins
- Randomize google sheets row entries
- Export sheets as csv
- Read csv using python
- Create JSON file storing name: [email: __ , target: __, targeted by: __, eliminated: true/false, year: __]
- JSON entries are effectively nodes in a doubly linked list
- Features: eliminate, remove, add, email, write to csv, write to JSON
- GUI using PyQT5 drag and drop https://www.youtube.com/watch?v=Vde5SH8e1OQ&list=PLzMcBGfZo4-lB8MZfHPLTEHO9zJDDLpYj





{
  "Howard" : {email: "hhq1@rice.edu,
              target: "Sabrina",
              targettedby: "Dev"}
              
  "Sabrina":  {email: "shk4@rice.edu,
              target: "Dev",
              targettedby: "Howard"}
         
  "Dev":  {email: "dmj7@rice.edu,
              target: "Howard",
              targettedby: "Sabrina"}
}

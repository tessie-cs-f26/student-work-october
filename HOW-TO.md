# How to use this template

## What is in the folder

```
index.md                      the front page (a table of programs)
programs/
  hello-counter/
    index.html                the page for one program
    main.py                   the student's program
```

## Set it up once

1. Create the repository named `username.github.io` (replace `username` with the account name).
2. Upload everything in this folder to the top level of the repository. On github.com, use "Add file" and then "Upload files", and drag the contents in.
3. In the repository's Settings, open Pages, choose "Deploy from a branch", pick `main`, and save.
4. Wait up to 10 minutes, then visit `https://username.github.io`.

Each program page works at any repository address, because its links are relative. If you move a project folder deeper or shallower, adjust the `../../` in the "All programs" link.

## Add a student program

1. Copy the `hello-counter` folder inside `programs/` and rename the copy, for example `guessing-game`. Use lowercase letters and hyphens, with no spaces.
2. Replace `main.py` in the new folder with the student's program.
3. Open the new `index.html` and change the four places marked EDIT: the title for the browser tab, the heading and first name, and the short description.
4. Add one row to the table in `index.md` with a link like `programs/guessing-game/`.

## Before you publish any program

- Run it on the live page. Programs that use `print`, `input`, `if` and `while` should work. Programs that use turtle or add-on libraries may not.
- Use first names only, and check your school's policy and family permission for posting student work.
- Answers to `input()` appear in a pop-up box, and the questions and answers are shown in the black box. If a visitor ticks "don't allow dialogs," reloading the page brings them back.

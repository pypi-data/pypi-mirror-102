msteamsbot is a package that allows you to send / spam messages to Teams. 

Here are some functions:

    send(message, delay, x, y):
        send() sends a message in teams (Make sure you open teams and click a chat before you run your script).
        Example:
        send('Hello, World', 2, 525, 665)

    spam(message, delay, quit_button, x, y):
        spam() sends a bunch of spam message in teams (Make sure you open teams and click a chat before you run your script).
        Example:
        send('Hello, World', 0.5, 'q', 525, 665)

    profile(delay, x, y):
        profile() opens the user profile in teams (Make sure you open teams before you run your script).
        Example:
        profile(2, 1204, 25)

    close():
        profile() closes Teams.
        Example:
        close()
    

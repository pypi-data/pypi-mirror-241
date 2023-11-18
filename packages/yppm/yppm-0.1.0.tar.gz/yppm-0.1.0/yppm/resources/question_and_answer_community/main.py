from auto_everything import Terminal
terminal = Terminal()

import os
os.chdir("./back_end")

print("This is a community that could get running in your terminal!")

print("Service started!")
terminal.run_py("""./main.py""", wait=True)

"""
Hi, there!

What you wanted to do?

1. Search
2. Ask Questions
#3. Login/Register
"""

"""
# Function: Search

It will ask user to input search keywords, then when user hit enter key, it will give user a list of result.
If user click that result, they can get into a detail page, where they could answer question, comment answer
"""

"""
# Function: Ask Questions

It will ask user to login/register first.
Then ask user to input title, description.
Then it will lead user to that question detail page.
"""

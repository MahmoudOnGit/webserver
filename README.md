
To run this program you must be on version 3 or higher of python.

You'll start the program by running "py server.py" in the terminal.

Only after running the program will you be able to access the program's pages accordingly (200 OK):
For the index page, visit: http://localhost:8088/index.html
For the main page, visit: http://localhost:8088/main/main.html
For the media page, visit: http://localhost:8088/media/media.html
For the support page, visit: http://localhost:8088/support/support.html
For the about us page, visit: http://localhost:8088/about-us/about-us.html

You can test if the program responds with the correct error accordingly by heading to:
404 not found: http://localhost:8088/doesntexist.html
403: http://localhost:8088/secret/file.html
400 bad request: enter "curl.exe -v --request BADREQUEST http://localhost:8088/" in the terminal (shown inside the terminal)

https://drive.google.com/file/d/1xqcJ45zQFtFRrbYUCP1l_g-14jKQZQYs/view?usp=sharing
import logging
from logging.handlers import TimedRotatingFileHandler
import os

config = {
    "photos": {
        "path": "../photos/",
        "ends_with": "jpg",
        "max_days_alive": 1
    },
    "videos": {
        "path": "../videos/",
        "ends_with": "mp4",
        "max_days_alive": 1,
        "duration_secs": 30
    },
    "mail": {
        "enabled": 0,
        "sender": "MODIFY-SENDER-EMAIL-ADDRESS",
        "app-password": "MODIFY-APP-PASSWORD",
        "recipient": "MODIFY-RECIPIENT-EMAIL-ADDRESS",
        "port": 587,
        "server": "smtp.gmail.com",
        "photo": {
            "subject": "BeeMail - Photo ({host}) 🐝 📫 📸",
            "body": """
Here is your BeeMail for {host}! 🙌 
<ul>
    <li>See more <a href=\"{url}\">photos and videos</a></li>
    <li>Current IP address: {ip_address}</li>
</ul>
<br>
{footer}
"""
        },
        "video": {
            "subject": "BeeMail - Video ({host})🐝 📫 🎥",
            "body": """
Here is your BeeMail for {host}! 🙌 
<ul>
    <li>See more <a href=\"{url}\">photos and videos</a></li>
    <li>Current IP address: {ip_address}</li>
</ul>
<br>
{footer}
"""
        },

        "ip-changed": {
            "subject": "BeeMail - IP Changed ({host}) 👀🚨",
            "body": """
The IP Address has changed. If you're using VNC, SSH, SCP, etc,
you'll want to change to this IP address:
<ul>
    <li>Current IP address: {ip_address}</li>
</ul>
<br>
{footer}
"""
        },
    "footer": """<hr>
<p style="color: orange;">Proudly designed for you by <a href="https://technicallybeekeeping.com" style="text-decoration: none; color: #333;"><strong>Technically Beekeeping, LLC</strong></a><br>
Happy Beekeeping! 🌼🍯 Enjoy the journey! 🐝</p>
"""
    }
}

# Create the logs directory if it doesn't exist
logs_directory = '../logs'
if not os.path.exists(logs_directory):
    os.makedirs(logs_directory)


# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Create a file handler with timed rotation (daily)
file_handler = TimedRotatingFileHandler(os.path.join(
    logs_directory, 'app.log'),
    when='midnight',
    interval=1,
    backupCount=30)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter(
    '%(asctime)s - %(levelname)s - %(message)s'))
logging.getLogger().addHandler(file_handler)


# # Create a handler to log to the command line
# console_handler = logging.StreamHandler(sys.stdout)
# console_handler.setLevel(logging.INFO)  # Set the logging level for the console handler
# console_handler.setFormatter(logging.Formatter(
#     '%(asctime)s - %(levelname)s - %(message)s'))
# logging.getLogger().addHandler(console_handler)

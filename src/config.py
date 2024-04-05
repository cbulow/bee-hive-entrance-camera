import logging

config = {
    "photos": {
        "path": "../photos",
        "ends_with": "jpg",
        "max_days_alive": 1
    },
    "videos": {
        "path": "../videos",
        "ends_with": "mp4",
        "max_days_alive": 1
    },
    "mail": {
        "enabled": 0,
        "sender": "MODIFY-SENDER-EMAIL-ADDRESS",
        "app-password": "MODIFY-APP-PASSWORD",
        "recipient": "MODIFY-RECIPIENT-EMAIL-ADDRESS",
        "port": 587,
        "server": "smtp.gmail.com",
        "photo": {
            "subject": "BeeMail Photo 🐝 📫 📸",
            "body": """
Here is your BeeMail! 🙌 
    Current IP address: {ip_address}
"""
        },
        "video": {
            "subject": "BeeMail Video 🐝 📫 🎥",
            "body": """
Here is your BeeMail! 🙌 
    Current IP address: {ip_address}
"""
        },

        "ip-changed": {
            "subject": "BeeMail - IP Changed 👀🚨",
            "body": """
The IP Address has changed. If you're using VNC, SSH, SCP, etc,
you'll want to change to this IP address:
    Current IP address: {ip_address}
"""
        }
    }
}

# Logging settings
logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger(__name__)

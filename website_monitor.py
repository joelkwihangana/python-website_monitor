"""
WEBSITE MONITORING SCRIPT
=========================
This script checks if a website is online and sends email alerts when it's down.

WHAT YOU'LL LEARN:
- Making HTTP requests to websites
- Handling responses and errors
- Sending emails with Python
- Working with time and scheduling
- Logging information to files
- Using functions to organize code
"""

# STEP 1: IMPORTING LIBRARIES
# Libraries are pre-written code that add functionality to Python
import requests  # This library lets us make HTTP requests to websites
import smtplib  # This library lets us send emails using SMTP protocol
from email.mime.text import MIMEText  # Helps us format email messages
from email.mime.multipart import MIMEMultipart  # Allows emails with multiple parts
from datetime import datetime  # Lets us work with dates and times
import time  # Lets us add delays and work with time
import os  # Lets us interact with the operating system (like file paths)

# STEP 2: CONFIGURATION SETTINGS
# These are the settings you can customize for your needs
WEBSITE_URL = "https://earthlinkstudy.com/"  # The website we're monitoring
CHECK_INTERVAL = 1800  # Time between checks in SECONDS (1800 = 30 minutes)
YOUR_EMAIL = "applecindyishami@gmail.com"  # Where to send alerts
YOUR_EMAIL_PASSWORD = "YOUR_APP_PASSWORD_HERE"  # Gmail app password (see instructions below)
ALERT_EMAIL = "applecindyishami@gmail.com"  # Who receives the alerts (can be same or different)
LOG_FILE = "website_monitor.log"  # File where we save monitoring history

# STEP 3: FUNCTION TO CHECK IF WEBSITE IS UP
def check_website(url):
    """
    This function checks if a website is accessible.
    
    HOW IT WORKS:
    - Sends an HTTP GET request to the website (like opening it in a browser)
    - If status code is 200, website is OK
    - If we get an error or different code, website is down
    
    PARAMETERS:
    - url: The website address to check
    
    RETURNS:
    - True if website is up
    - False if website is down
    """
    try:
        # Try to connect to the website with a 10 second timeout
        response = requests.get(url, timeout=10)
        
        # HTTP status code 200 means "OK" - website is working
        if response.status_code == 200:
            return True
        else:
            # Any other status code means there's a problem
            return False
            
    except requests.exceptions.RequestException as e:
        # If ANY error happens (connection error, timeout, etc.), website is down
        print(f"Error checking website: {e}")
        return False

# STEP 4: FUNCTION TO SEND EMAIL ALERTS
def send_email_alert(subject, message):
    """
    This function sends an email notification.
    
    HOW IT WORKS:
    - Creates an email message with subject and body
    - Connects to Gmail's SMTP server (mail server)
    - Logs in with your credentials
    - Sends the email
    
    PARAMETERS:
    - subject: Email subject line
    - message: Email body content
    """
    try:
        # Create the email message object
        msg = MIMEMultipart()
        msg['From'] = YOUR_EMAIL  # Who is sending
        msg['To'] = ALERT_EMAIL  # Who is receiving
        msg['Subject'] = subject  # Email subject
        
        # Attach the message body to the email
        msg.attach(MIMEText(message, 'plain'))
        
        # Connect to Gmail's SMTP server
        # Gmail uses port 587 for TLS (secure) email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Start TLS encryption for security
        
        # Login to your Gmail account
        server.login(YOUR_EMAIL, YOUR_EMAIL_PASSWORD)
        
        # Send the email
        server.send_message(msg)
        
        # Close the connection to the server
        server.quit()
        
        print("✉️ Email alert sent successfully!")
        
    except Exception as e:
        # If email fails, print the error but don't stop the script
        print(f"❌ Failed to send email: {e}")

# STEP 5: FUNCTION TO LOG EVENTS
def log_event(message):
    """
    This function saves monitoring events to a log file.
    
    WHY LOGGING IS IMPORTANT:
    - Creates a history of all checks
    - Helps identify patterns (when does it go down?)
    - Useful for troubleshooting
    
    PARAMETERS:
    - message: What happened (website up/down, error, etc.)
    """
    # Get current date and time
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Format: [2025-11-04 10:30:00] Website is UP
    log_message = f"[{timestamp}] {message}"
    
    # Print to console so you can see what's happening
    print(log_message)
    
    # Save to file (append mode 'a' adds to existing file)
    with open(LOG_FILE, 'a') as f:
        f.write(log_message + "\n")

# STEP 6: MAIN MONITORING FUNCTION
def monitor_website():
    """
    This is the main function that runs continuously.
    
    HOW IT WORKS:
    - Checks website status
    - Sends alert if down
    - Logs the result
    - Waits for the specified interval
    - Repeats forever
    """
    # Keep track of previous status to avoid sending duplicate alerts
    was_down = False
    
    log_event("🚀 Website monitoring started!")
    log_event(f"📍 Monitoring: {WEBSITE_URL}")
    log_event(f"⏰ Check interval: {CHECK_INTERVAL/60} minutes")
    
    # Infinite loop - runs forever until you stop it
    while True:
        # Check if website is up
        is_up = check_website(WEBSITE_URL)
        
        if is_up:
            log_event("✅ Website is UP and running")
            
            # If website was down before and is now up, send recovery notification
            if was_down:
                subject = "✅ WEBSITE BACK ONLINE"
                message = f"""
Good news! Your website is back online.

Website: {WEBSITE_URL}
Time: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

The website is now responding normally.
"""
                send_email_alert(subject, message)
                was_down = False
                
        else:
            log_event("❌ Website is DOWN!")
            
            # Only send alert if this is a new downtime (not already down)
            if not was_down:
                subject = "🚨 WEBSITE DOWN ALERT"
                message = f"""
ALERT: Your website is currently DOWN!

Website: {WEBSITE_URL}
Time: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

Please check your Orange hosting dashboard and take necessary action.

This is an automated message from your Website Monitor.
"""
                send_email_alert(subject, message)
                was_down = True
        
        # Wait before checking again
        log_event(f"⏳ Waiting {CHECK_INTERVAL/60} minutes until next check...\n")
        time.sleep(CHECK_INTERVAL)  # Sleep pauses the script

# STEP 7: START THE SCRIPT
if __name__ == "__main__":
    """
    This is the entry point of the script.
    When you run this file, this code executes.
    """
    print("=" * 60)
    print("WEBSITE MONITORING SCRIPT")
    print("=" * 60)
    print("\n⚠️  IMPORTANT: Make sure you've set up your Gmail App Password!")
    print("⚠️  Press Ctrl+C to stop the monitoring\n")
    print("=" * 60 + "\n")
    
    try:
        # Start monitoring
        monitor_website()
    except KeyboardInterrupt:
        # If you press Ctrl+C, this catches it and exits gracefully
        log_event("🛑 Monitoring stopped by user")
        print("\n\n👋 Monitoring stopped. Goodbye!")
    except Exception as e:
        # Catch any unexpected errors
        log_event(f"💥 Unexpected error: {e}")
        print(f"\n❌ An error occurred: {e}")

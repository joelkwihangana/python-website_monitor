# 🌐 Website Monitoring Script

A Python script that automatically monitors your website's uptime and sends email alerts when your site goes down or comes back online.

## 📋 What This Script Does

- ✅ Checks if your website is online every 30 minutes (customizable)
- 📧 Sends email alerts when your website goes down
- 🔔 Notifies you when your website comes back online
- 📝 Keeps a detailed log of all checks with timestamps
- 🔄 Runs continuously in the background

## 🎯 Who Is This For?

- Website owners who want to know immediately when their site goes down
- People learning Python automation and scripting
- Anyone who wants to monitor website uptime without paid services

## 📦 Prerequisites

Before you begin, make sure you have:

- **Python 3.8 or higher** installed on your computer
- A **Gmail account** (for sending alert emails)
- **Basic command line** knowledge (don't worry, we'll guide you!)

## 🚀 Installation Guide

### Step 1: Install Python

**Windows:**
1. Go to [python.org/downloads](https://www.python.org/downloads/)
2. Download the latest Python version
3. Run the installer
4. ⚠️ **IMPORTANT:** Check the box "Add Python to PATH"
5. Click "Install Now"

**Mac:**
1. Open Terminal
2. Install Homebrew (if not installed):
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
3. Install Python:
   ```bash
   brew install python
   ```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3 python3-pip
```

**Verify Installation:**
Open your terminal/command prompt and type:
```bash
python --version
```
You should see something like: `Python 3.11.5`

### Step 2: Download the Script

1. Create a new folder on your computer (e.g., `website-monitor`)
2. Save the `website_monitor.py` file in that folder

### Step 3: Install Required Libraries

Open your terminal/command prompt, navigate to your script folder, and run:

```bash
pip install requests
```

**What this does:** Installs the `requests` library that allows Python to visit websites.

### Step 4: Set Up Gmail App Password

Gmail requires a special "App Password" for security. Here's how to get it:

1. **Enable 2-Factor Authentication** (required first):
   - Go to [myaccount.google.com](https://myaccount.google.com)
   - Click "Security" in the left menu
   - Under "How you sign in to Google," click "2-Step Verification"
   - Follow the steps to enable it

2. **Generate App Password**:
   - Go to [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
   - Select "Mail" as the app
   - Select "Other" as the device and name it "Website Monitor"
   - Click "Generate"
   - **Copy the 16-character password** (it looks like: `abcd efgh ijkl mnop`)

3. **Save it somewhere safe** - you'll need it in the next step!

### Step 5: Configure the Script

Open `website_monitor.py` in a text editor (Notepad, VS Code, etc.) and update these lines:

```python
WEBSITE_URL = "https://yourwebsite.com/"  # Your website URL
YOUR_EMAIL = "youremail@gmail.com"        # Your Gmail address
YOUR_EMAIL_PASSWORD = "your app password"  # The 16-char password from Step 4
ALERT_EMAIL = "youremail@gmail.com"       # Where to send alerts
```

**Example:**
```python
WEBSITE_URL = "https://earthlinkstudy.com/"
YOUR_EMAIL = "applecindyishami@gmail.com"
YOUR_EMAIL_PASSWORD = "abcd efgh ijkl mnop"
ALERT_EMAIL = "applecindyishami@gmail.com"
```

### Step 6: Run the Script

**On Windows:**
1. Open Command Prompt
2. Navigate to your script folder:
   ```cmd
   cd C:\Users\YourName\website-monitor
   ```
3. Run the script:
   ```cmd
   python website_monitor.py
   ```

**On Mac/Linux:**
1. Open Terminal
2. Navigate to your script folder:
   ```bash
   cd ~/website-monitor
   ```
3. Run the script:
   ```bash
   python3 website_monitor.py
   ```

**You should see:**
```
============================================================
WEBSITE MONITORING SCRIPT
============================================================

⚠️  IMPORTANT: Make sure you've set up your Gmail App Password!
⚠️  Press Ctrl+C to stop the monitoring

============================================================

[2025-11-04 10:00:00] 🚀 Website monitoring started!
[2025-11-04 10:00:00] 📍 Monitoring: https://yourwebsite.com/
[2025-11-04 10:00:00] ⏰ Check interval: 30.0 minutes
[2025-11-04 10:00:01] ✅ Website is UP and running
```

**Keep this window open!** The script runs continuously.

## ⚙️ Customization Options

You can customize these settings in the script:

```python
CHECK_INTERVAL = 1800  # Time between checks in seconds
```

**Common intervals:**
- Every 30 minutes: `1800`
- Every 1 hour: `3600`
- Every 15 minutes: `900`
- Every 5 minutes: `300`

## 📊 Understanding the Log File

The script creates a file called `website_monitor.log` that tracks all activity:

```
[2025-11-04 10:00:00] 🚀 Website monitoring started!
[2025-11-04 10:00:01] ✅ Website is UP and running
[2025-11-04 10:30:01] ✅ Website is UP and running
[2025-11-04 11:00:01] ❌ Website is DOWN!
[2025-11-04 11:30:01] ✅ Website is UP and running
```

**What each symbol means:**
- 🚀 = Monitoring started
- ✅ = Website is working
- ❌ = Website is down
- ⏳ = Waiting for next check

## 📧 Email Alerts

You'll receive two types of emails:

**1. When website goes DOWN:**
```
Subject: 🚨 WEBSITE DOWN ALERT

ALERT: Your website is currently DOWN!

Website: https://yourwebsite.com/
Time: 2025-11-04 11:00:01

Please check your hosting dashboard and take necessary action.
```

**2. When website comes BACK ONLINE:**
```
Subject: ✅ WEBSITE BACK ONLINE

Good news! Your website is back online.

Website: https://yourwebsite.com/
Time: 2025-11-04 11:30:01

The website is now responding normally.
```

## 🏃 Running in the Background

### Windows - Keep Running After Closing Terminal

**Option 1: Use Task Scheduler**
1. Open Task Scheduler
2. Create Basic Task
3. Set trigger (e.g., "At startup")
4. Action: Start a program
5. Program: `python`
6. Arguments: `"C:\path\to\website_monitor.py"`

**Option 2: Use .pyw extension**
1. Rename `website_monitor.py` to `website_monitor.pyw`
2. Double-click to run (no console window appears)

### Mac/Linux - Run in Background

**Use nohup:**
```bash
nohup python3 website_monitor.py &
```

**Or create a systemd service** (advanced - Google "Python systemd service")

## 🛑 Stopping the Script

- If running in terminal: Press `Ctrl + C`
- If running in background: Find and kill the process

**Find the process:**
```bash
# Mac/Linux
ps aux | grep website_monitor

# Windows
tasklist | findstr python
```

**Stop it:**
```bash
# Mac/Linux
kill [process_id]

# Windows
taskkill /F /PID [process_id]
```

## ❗ Troubleshooting

### "Module not found: requests"
**Solution:** Install the requests library:
```bash
pip install requests
```

### "Authentication failed" when sending email
**Solution:** 
- Make sure you're using an App Password, not your regular Gmail password
- Verify 2-Factor Authentication is enabled
- Check that you copied the App Password correctly (no spaces)

### "Connection timeout" or "Website appears down" but it's actually up
**Solution:**
- Check your internet connection
- Verify the website URL is correct (include `https://`)
- Some websites block automated requests - add user agent (ask me how!)

### Script stops after closing terminal
**Solution:** See "Running in the Background" section above

### Not receiving emails
**Solution:**
- Check your spam/junk folder
- Verify YOUR_EMAIL and ALERT_EMAIL are correct
- Test sending an email manually first

## 📚 Learning Resources

Want to understand the code better?

- **Python Basics:** [python.org/about/gettingstarted](https://www.python.org/about/gettingstarted/)
- **Requests Library:** [requests.readthedocs.io](https://requests.readthedocs.io)
- **SMTP Email:** [realpython.com/python-send-email](https://realpython.com/python-send-email/)

## 🎓 Next Steps

Once you're comfortable with this script, you can:

1. Monitor multiple websites at once
2. Add SMS alerts using Twilio
3. Create a web dashboard to view uptime statistics
4. Check response time (alert if website is slow)
5. Add Slack/Discord notifications

## 🤝 Support

If you have questions:
1. Check the troubleshooting section above
2. Review the comments in the script itself
3. Search for the error message on Google/Stack Overflow

## 📄 License

Free to use and modify for personal or commercial projects!

## 🌟 Credits

Created as a learning project for understanding Python automation and website monitoring.

---

**Happy Monitoring! 🚀**

If this script helped you, consider learning more Python - it's an amazing skill for automation!

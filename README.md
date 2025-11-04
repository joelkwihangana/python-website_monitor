# python-website_monitor
## 📖 HOW THE SCRIPT WORKS  1. **Every 30 minutes**, it sends a request to your website 2. **If website responds** with status 200 → logs "Website UP" 3. **If website doesn't respond** → logs "Website DOWN" + sends email 4. **When website recovers** → sends "back online" email 5. **All events are saved** in `website_monitor.log` file

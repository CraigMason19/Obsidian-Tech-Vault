An email client I switched to because Outlook was fine but then they changed it and it annoyed me.

---
## Custom Styling

To edit the Thunderbird CSS, you need to modify `userChrome.css` or `userContent.css` 

**Locate Your Thunderbird Profile Folder**
- Open **Thunderbird**
- Go to **Help** > **More Troubleshooting Information**
- Scroll down to **Profile Folder** and click **Open Folder**

**Check for the chrome Folder**
- Inside your **profile folder**, look for a folder named **chrome**
- If it exists, open it otherwise create it
- Look for **userChrome.css** (for UI changes) or **userContent.css** (for email content changes)
	- Make changes or copy in my custom settings 

**Change Flag Setting**
- Go to **Settings > General > Config Editor**
- Set `toolkit.legacyUserProfileCustomizations.stylesheets` to True

Then reopen **Thunderbird**

**To find which element to change**
- Go into `Developer Tools (CTRL + SHIT + I)` and in the top left there as button that allows you to choose the element in the app

---
## Filters
Under Tools > Message Filters

---
## Addons
-  PrintingTools NG

---
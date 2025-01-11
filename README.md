# group_chat_analysis


This project provides an analysis of WhatsApp chat data by parsing and processing exported chat files. It extracts useful statistics, including message counts, emojis, media messages, and links, broken down by individual authors.

## Features
- **Date and Time Parsing**: Extracts and organizes messages by date and time.
- **Message Statistics**: Calculates message counts, words per message, media, emojis, and links for each user.
- **Emoji Extraction**: Identifies and counts emojis used in the messages.
- **Link Counting**: Detects and counts URLs shared in the messages.
- **Customizable**: Easily adapted to other types of chat data or messaging platforms.

## How to Run

1. Export a WhatsApp Chat
Export your WhatsApp chat as a `.txt` file:
- Open the chat in WhatsApp.
- Tap on the three dots in the top right corner and choose "More" > "Export chat".
- Choose to export without media to save as a text file.

2. Rename the Chat File
Rename the exported chat file to `_chat.txt`.

3. Run the Python Script
Ensure that Python (with necessary libraries) is installed on your machine. Then, simply run the script:

```bash
python whatsapp_chat_analysis.py
```
This will output a summary of the chat including message statistics, media count, emoji usage, and link counts.

Requirements:<br>

Python 3.x <br>
regex <br>
pandas<br>
emoji <br>
numpy<br>
(Install via pip install)<br>

The script will display a summary of the chat including:

Total messages<br>
Media messages<br>
Emojis used<br>
Links shared<br>
A detailed breakdown of message stats for each user (messages sent, words per message, media, emojis, and links).<br>

Customization:<br>

You can modify the list of users in the script to analyze messages for specific participants.<br>
Add further analysis or data visualizations to extend the functionality.<br>

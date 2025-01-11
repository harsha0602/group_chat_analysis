import regex as re
import pandas as pd
import emoji
import numpy as np

def startsWithDateAndTime(s):
    pattern = r'^\[(\d{1,2}/\d{1,2}/\d{2,4}), (\d{1,2}:\d{2}(:\d{2})?[\u202f\s]*?(AM|PM|am|pm))\]'
    return bool(re.match(pattern, s))

def FindAuthor(s):
    return len(s.split(': ', 1)) == 2

def getDataPoint(line):
    splitLine = line.split('] ', 1)  # Split after ']'
    dateTime = splitLine[0][1:]  # Remove leading '['
    date, time = dateTime.split(', ')  # Split date and time
    message = ' '.join(splitLine[1:])  # Extract message
    if FindAuthor(message):
        splitMessage = message.split(': ', 1)  # Split author and message
        author = splitMessage[0]
        message = splitMessage[1]
    else:
        author = None
    return date, time, author, message

data = []
conversation = '_chat.txt'
with open(conversation, encoding="utf-8", errors='ignore') as fp:
    messageBuffer = []
    date, time, author = None, None, None
    while True:
        line = fp.readline()
        if not line:
            break
        line = line.strip()
        if startsWithDateAndTime(line):
            if len(messageBuffer) > 0:
                data.append([date, time, author, ' '.join(messageBuffer)])
            messageBuffer.clear()
            date, time, author, message = getDataPoint(line)
            messageBuffer.append(message)
        else:
            messageBuffer.append(line)

if len(messageBuffer) > 0:
    data.append([date, time, author, ' '.join(messageBuffer)])

df = pd.DataFrame(data, columns=['Date', 'Time', 'Author', 'Message'])
df["Date"] = pd.to_datetime(df["Date"], errors='coerce')

print(df.tail(20))
print()

print(df.Author.unique())

media_messages = df[df['Message'] == '<Media omitted>'].shape[0]
print(media_messages)
print()

def split_count(text):
    emoji_list = []
    for char in emoji.emoji_list(text):
        emoji_list.append(char['emoji'])
    return emoji_list


total_messages = df.shape[0]
df["emoji"] = df["Message"].apply(split_count)
emojis = sum(df['emoji'].str.len())
print(emojis)
print()

URLPATTERN = r'(https?://\S+)'
df['urlcount'] = df.Message.apply(lambda x: re.findall(URLPATTERN, x)).str.len()
links = np.sum(df.urlcount)
print("Sumne Irli Community")
print("Messages:",total_messages)
print("Media:",media_messages)
print("Emojis:",emojis)
print("Links:",links)
print()

media_messages_df = df[df['Message'] == '<Media omitted>']
messages_df = df.drop(media_messages_df.index)
# messages_df.info()
messages_df['Letter_Count'] = messages_df['Message'].apply(lambda s : len(s))
messages_df['Word_Count'] = messages_df['Message'].apply(lambda s : len(s.split(' ')))
messages_df["MessageCount"]=1

l = ["Srkanth Gg", "Hari Bro", "Camel Vamshi"]
for i in range(len(l)):
  # Filtering out messages of particular user
  req_df= messages_df[messages_df["Author"] == l[i]]
  # req_df will contain messages of only one particular user
  print(f'Stats of {l[i]} -')
  # shape will print number of rows which indirectly means the number of messages
  print('Messages Sent', req_df.shape[0])
  #Word_Count contains of total words in one message. Sum of all words/ Total Messages will yield words per message
  words_per_message = (np.sum(req_df['Word_Count']))/req_df.shape[0]
  print('Words per message', words_per_message)
  #media conists of media messages
  media = media_messages_df[media_messages_df['Author'] == l[i]].shape[0]
  print('Media Messages Sent', media)
  # emojis conists of total emojis
  emojis = sum(req_df['emoji'].str.len())
  print('Emojis Sent', emojis)
  #links consist of total links
  links = sum(req_df["urlcount"])   
  print('Links Sent', links)   
  print()
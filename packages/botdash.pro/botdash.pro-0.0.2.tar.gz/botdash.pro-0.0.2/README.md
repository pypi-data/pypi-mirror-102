# BotDash.pro

```py

import botdash

client = botdash.Client('<BOTDASH-TOKEN>')

object = client.get_value("<GUILDID>", "<DATA-VALUE>")
print(object.data) # Get the actual data

```
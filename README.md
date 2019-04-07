# ED-signalnet
Elite Dangerous tool allowing players to send distress calls/news/messages to players in nearby systems. Work in progress.

# Idea
The point is to bring some live into the empty universe of Elite Dangerous by allowing players to send short messages in the star systems they are in. Players within 20 light years of these systems would be able to receive these messages using a Voice Attack plugin. Each message will have short text (like a space tweet), author, date and star system of origin. Voice Attack plugin will allow players to quickly react to those messages, by copying author's nick or targeting the system.

Players will be also able to boost received messages, increasing their range. I imagine this way interesting, lore friendly messages (distress calls, events, roleplay news articles) would get promoted and spread across the Universe.

# Technical side:
## API
A simple REST API based on Django accepts and retrieves messages.

## Client
Not implemented yet. I consider two options to communicate with the API: EDDiscovery script or Voice Attack plugin. Eddiscovery is free, so it would be a better option, with Voice Attack as an optional voice interface for the tool.

# Future plans
After a working proof of concept is ready, there are some questions I will have to answer:
1. How to prevent players from faking their ingame location (and is it really necessary?)
2. How to authenticate players?
3. How to prevent spam? Should the amount of messages a player can send be limited? Should some reputation system be introduced? After all, it's not a chat, we don't want people to be talking with it, just send short immersive "tweets".
4. How to send messages from ingame? Windows voice recognition doesn't work well with dictation. Writing messages into chat might be an option, but breaks immersion (dictating them would be better).

## Additional features to consider:
1. Automatic messages on inngame events? For example, sending an automatic distress call when player is under attack/crashes.
2. Whitelisting/blacklisting for players, who don't want to receive signals from other players, but only from particular authors (like Lave Radio/Hutton Orbital?).
3. Categories of messages?

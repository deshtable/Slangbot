import os

import discord
from dotenv import load_dotenv


slangDict = {"ong": "i mean it as much as my devotion to the lord",
"fr":"definitely",
"omg":"by the name of my lord",
"thats on me":"an admission of fault",
"mb":"my bad (an admission of fault)",
"finna":"gonna (going to)",
"bruh":"is what you speak really true? brethren",
"innit":"isn't it?",
"cuh":"ac",
"blud":"buddy",
"wusgud":"hows it going",
"wussup":"what is going on",
"smh":"i am shaking my head at what you said",
"tyt":"take all the time you need",
"ttyl":"i will talk to you later!",
"carti":"Sir mister lord cartington III of reflection land",
"lmao":"im laughing so my butt is about to fall off",
"rn":"right now",
"creations":"I DONT WANNA FADE TOO SOON",
"no cap":"without a lie",
"yk":"you know",
"no cappa":"wihtout a lie (but with even more emphasis)",
"wagwan":"what's good?",
"ey":"hey!",
"valorant":"i like men",
"reflectioner":"enlightened individual",
":/":"aww shucks",
"):":"this event has greatly saddened me",
"weed":"toke is high right now",
"u":"you",
"ily":"an expression of my great adoration for you",
"imy":"sometimes i think about you when im in bed at 3am listening to frank ocean",
"wanna":"want to",
"gonna":"going to",
"squaw":"those who have been with me for the longest time",
"shawty":"a girl who looks good",
"cant even lie":"I reluctantly agree to the proposition",
"ngl":"to be completely hoonest",
"lmoa":"try again",
"loll":"try again",
"nt":"it was a valiant attempt",
"ns":"you hit that shot with impecabble accuracy",
"nc":"fikr",
"spiral": "spirallin up just like a rich _",
"thx":"I greatly appreciate it!",
"jesus":"yeshu bin yosef",
"omm":"on my momma (i agree with that as much as my respect for my birthgiver)",
"on jah":"i agree with that as much as my respect for the hip hop artist Jahseh Dwayne Ricardo Onfroy (rip (rest in peace))",
"ye":"the goat (greatest of all time)",
"kanye":"the goat (greatest of all time)",
"drake":"femboy",
"goat":"the greatest of all time",
"stg":"i swear by jove",
"":"",
"":"",
"":"",
"":"",
"":"",
"":"",
"":""
}

def slangFun():
    @client.event
    async def on_message(msg):
        if msg.author == client.user:
            return

        sendBool = False
        userMsg = msg.content
        botMsg = ""
        parsedString = userMsg.split(" ")
        appendMsg = ""
        iterStr = ""

        for x in range (0,len(parsedString)):

            iterStr = parsedString[x]

            if(x>0):
                appendMsg = parsedString[x-1] + " " + iterStr
            botMsg = botMsg + iterStr + " "

            if appendMsg in slangDict and len(appendMsg) > 0:
                iterStr = appendMsg
                print("this shit in here bruh")

            if iterStr in slangDict:
                sendBool = True
                botMsg = botMsg + "(" + slangDict[iterStr] + ") "

        if(sendBool):
            await msg.channel.send(botMsg)


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="as an Elite Reflectioner"))


slangFun()


client.run(TOKEN)

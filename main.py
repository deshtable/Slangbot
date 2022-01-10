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
"cuh":"my brother",
"blud":"buddy",
"wusgud":"hows it going",
"wussup":"what is going on",
"smh":"i am shaking my head at what you said",
"tyt":"take all the time you need",
"ttyl":"i will talk to you later!",
"carti":"Sir mister lord cartington III of reflection land",
"lmao":"im laughing so hard my butt is about to fall off",
"rn":"right now",
"creations":"I DONT WANNA FADE TOO SOON",
"no cap":"without a lie",
"yk":"you know",
"no cappa":"without a lie (but with even more emphasis)",
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
"ngl":"I reluctantly agree to the proposition",
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
"istg":"i swear by jove",
"bruv":"bruh but british",
"yessir":"an exclaim of humble agreeance",
"slang":"I AM HERE TO HELP!",
"bouta":"it is soon that",
"tbh":"if i were to be completely transparent",
"bro":"person who is as if born alongside me",
"imo":"if you were to ask me",
"lmfao":"laughing as if my butt were about to REALLY fall off",
"dead homies":"in memory of my dearly departed companions",
"slangbot":"spambot",
"ik":"im well aware",
"wtf":"what in the world?!?",
"pls":"if you could",
"dis":"the subject we are speaking of",
"trippin":"having neurotic convulsions due to excess amounts of drugs",
"neva":"not anytime in the near future",
"lol":"i find this quite humerous",
"tfti":"i cant believe you forgot to send me an invitation",
"bet":"alrighty then",
"jit":"young fellow",
"naw":"no way!",
"dawg":"a brother that you cant call a female dog",
"ez":"little effort to complete",
"":"",
"":"",
"":"",
"":"",
"":"",


}

runSlangBool = True

def invertRunBool():

    global runSlangBool
    runSlangBool = not runSlangBool

def getRunBool():
    return runSlangBool

load_dotenv()
#TOKEN = os.getenv('DISCORD_TOKEN')
TOKEN = "OTMwMTY4NzIwNTg2ODQ2MjA5.Ydx9IA.bvLqiDKhLC3qrncfezDnSWd2xps"

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="as an Elite Reflectioner"))


@client.event
async def on_message(msg):
    if msg.author == client.user:
        return

    runBool = getRunBool()
    userMsg = msg.content

    if userMsg == "-slang":
        invertRunBool()
        await msg.channel.send("SlangBot's status is now: " + str(runSlangBool))


    runBool = getRunBool()
























    if(runBool):
        sendBool = False

        botMsg = ""
        parsedString = userMsg.split(" ")
        appendMsg = ""
        iterStr = ""

        for x in range (0,len(parsedString)):

            iterStr = parsedString[x]

            if(x>0):
                appendMsg = parsedString[x-1] + " " + iterStr
            botMsg = botMsg + iterStr + " "

            appendMsg = appendMsg.lower()
            if appendMsg in slangDict and len(appendMsg) > 0:
                iterStr = appendMsg

            iterStr = iterStr.lower()
            if iterStr in slangDict:
                sendBool = True
                botMsg = botMsg + "(" + slangDict[iterStr] + ") "

        if(sendBool):
            await msg.channel.send(botMsg)



client.run(TOKEN)

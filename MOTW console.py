import discord
import random
import time
from discord.ext import commands, tasks
password = True

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True
                          , presences = True)
client = commands.Bot(command_prefix = '-', intents = intents) 

#add in your bot token here
token = ""

@client.event
async def on_ready():
    activity = discord.Activity(name='me test things', type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)   
    print("The computer has AWOKEN!")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        if password:
            await ctx.send("Please enter password to access this command")
        else:
            com = str(error).split()
            await ctx.send("" + com[1] + " is not reconginzed as an internal or external command")

@client.command()
async def startup(ctx):
    await ctx.send("*The computer whirls to life and a password login screen is projected onto the monitor. Above the username and password a user icon features a zoomed in image of a Daisy*\n\n")
    await ctx.send("----------------------------------------\n|** Username:**  `E.Mccoy        `      |\n|** Password:**   `               `      |\n----------------------------------------\n\nPassword Hint ||Precious Flower||") 
    
@client.command(help = "used for entering passwords")
async def password(ctx,*,guess):
    if guess == "Azalea":
        global password
        password = False
        await ctx.send("**Welcome Elizabeth Mccoy**\n\nTo view logs type - logs")
    else:
        await ctx.send("Incorrect Password")
        
@client.command()
async def open(ctx,*,log):
    if password:
        await ctx.send("Please enter password to access this command") 
    else:
        if log == "100":
            await ctx.send("**Log: 100| Date: 10/27/2003 | Description: Recovery**")
            await ctx.send("The outdoor research team came across some peculiar mushrooms over in Kearmagne Woods a couple weeks ago. Going off the pictures they brought in I've never seen mushrooms like this before especially in this region. Lucas and I visited the field and collected 5 samples to further research here in the lab. I should make it clear that we left enough specimen out there that we can go back and compare between our experiments and the untouched shrooms. We are leaving sample 1 untouched as a control but I have a feeling being isolated in a lab will still have some unexpected effects. Photos of the initial mushroom site and a map to their location can be found in Lucas's notes.")
            
        elif log == "101":
            await ctx.send("**Log: 101| Date: 10/27/2003 | Description: Initial Findings**")
            await ctx.send("Some initial descriptions. The tallest mushroom collected reaches 30 cm in height however we predict they can grow much taller when left undisturbed. They are blue in pigment and give off an unsettling blue glow when left in complete darkness. They have the same spots as an Amanita Muscaria mushroom so maybe this is a genetic mutation of one? Although they seem to also produce puffballs like a Gasteromyscetes mushroom so maybe these larger mushrooms are to attract creatures such that they can be sprayed with their spores? With further research of their growth site our outdoor research team has found many skeletal remains of animals near where the mushrooms sprout. Are the mushrooms growing where creatures die or are the mushrooms responsible for killing the animals? I have yet to run toxicology tests but I'm very intrigued in a possibly murderous mushroom.")
        
        elif log == "102":
            await ctx.send("**Log: 102| Date: 10/28/2003 | Description: Spores**")
            await ctx.send("Results are back on the toxicology tests. The mushroom itself doesn't appear to be poisonous however the spores themselves appear to be poisonous to the touch. I've informed the outdoor research group to stay well covered and wear ventilators when interacting with the site. The puffballs surrounding the main mushroom growths are also quite fascinating. I hypothesize that they can sense when movement occurs nearby and spray their spores when the movement is within their spurting range. Perhaps they share connections to carnivorous plants and 'hunt'. I will be conducting animal experiments tomorrow to see how the mushrooms react to a 'predator'. I may be ahead of myself and this could just be a self defense mechanism.")
            
        elif log == "103":
            await ctx.send("**Log: 103| Date: 10/29/2003 | Description: Animal Control**")
            await ctx.send("I introduced a lab rat to specimen two today and the most unexpected thing happened. As I predicted when the rat got too close to the puffballs they exploded covering the unsuspecting rat in spores. After initially inhaling the spores it appeared to be paralyzed. It stood up alright after about thirty sections and continued to explore the cage staying clear of the fungus in the middle. Lucas agrees that as the minutes passed after the initial exposure the rat became lethargic eventually falling over over limp at the 1 hour mark. We thought it was dead but after about 5 minutes it stood back up and went back to the mushroom! The most fascinating part is that no additional spores were released as it approached and when we went to remove the rat from the tank it fought as if it were protecting the mushroom. Perhaps these spores have a similar effect to that of Ophiocordyceps Unilateralis and 'mind controls' its unexpecting victims! We will have to run additional tests on the rat. I am curious if there is a size limit to what this fungus can control.")
            
        elif log == "104":
            await ctx.send("**Log: 104| Date: 10/29/2003 | Description: Hive Mind**")
            await ctx.send("What we've learnt from the rat studies is that the mushroom appears to be capable of creating a hive mind like connection between any creature that inhales its spores. Some how the spores make it to the brain cavity and start growing puffballs and mushrooms intersecting with the brain! These growths also appear throughout the body. Where ever a cut is made the fungus appears to repair that section of the body with additional growths. We've infected additional rats and appear to all work in unison to protect the fungus that infected them. Even when infected by different specimen they seem to protect whichever mushroom is in the tank with them. Perhaps there is a link between the different growths? Maybe one of the Mushroom groups in the grove is the Mother and has control over the others? I'll have to reexamine the natural growths to see if one stands out.")
            
        elif log == "105":
            await ctx.send("**Log: 105| Date: 10/30/2003 | Description: Cure**")
            await ctx.send("We've been unsuccessful in figuring out a way to reverse the effects of the spores without killing the infecting specimen. Today we destroyed specimen 2 and that appeared to undo the mind control effects on all rats infected by that sample. Perhaps if you destroy the original growth everything in the hive mind will shut down? I still wish we could find an alternative that doesn't involve burning the heck out of the mushroom.")
            
        elif log == "106":
            await ctx.send("**Log: 106| Date: 10/30/2003 | Description: Mutation**")
            await ctx.send("The puffballs on the rat specimen now seem to be reactive. I'm not sure what caused this mutation but the infected animals now appear to be capable of infecting other animals. We were performing routine tests on one of the rats when a spore cloud erupted from their mushroom growths. It appears if they take too much damage they just explode? The other rats have also grown increasingly hostile even at further distances from the fungus specimens. I think the mushroom's territory is expanding as they grow and infect more creatures. I have yet to test the effects of the spores on larger creatures but I'm getting increasingly nervous that our samples are getting too strong to contain. They've grown exponentially and I'm now more than a little afraid of the creatures under their control. I'll be shutting this down and destroying all our specimen the moment I hear back from the lab coordinator.")
            
        elif log == "108":
            await ctx.send("**Log: 108| Date: 10/31/2003 | Description: Contamination Emergency**")
            await ctx.send("The containment unit for specimen one just burst! The spores are everywhere in the containment lab. I can barely make things out through the observation window. SHIT!!! LUCAS IS STILL IN THERE!!!")
            
        elif log == "113":
            await ctx.send("**Log: 113| Date: 10/31/2003 | Description: HELP! ANYONE!**")
            await ctx.send("HELP PLEASE. All 4 remaining specimen have exploded. The force of the spores strong enough to shatter the glass containers they were held in and the glass dividing the office space and the lab is starting to crack. Lucas is trying to follow lab protocol as I type this but if the spores are as strong as I fear they are I don't think he has long. FUCK. I think I just heard him fall. SHIT what do I do. I'm going to activate the fire suppression system and hopefully that settles all the spores. I still have to get Lucas out of there. shit sHIT ASHIST HSIT FUCK I have to run I can't risk getting infected myself, I'm the only one who stands a chance of finding a cure. If you area reading this GET OUT OF THERE! Don't breath the spores and stay clear of rhte RATS!")
            
        elif log == "107" or log == "109" or log == "110" or log == "111":
            await ctx.send("**Log: " + log + "| Date: 10/31/2003 | Description: Automated Incident Report**")
            await ctx.send("Specimen containment breach. Specimen number " + str(int(log)-106) + " is no longer quarantined. Please address issue at earliest opportunity.")
       
        elif log == "112":
            await ctx.send("**Log: 112| Date: 10/31/2003 | Description: Automated Incident Report**")
            await ctx.send("Emeregency lab shower activated. Emergency Eye wash station activated.")
            
        elif log == "114":
            await ctx.send("**Log: 114| Date: 10/31/2003 | Description: Automated Incident Report**")
            await ctx.send("Fire suppresion system activated.")     
            
        elif log == "115" or log == "116" or log == "117":
            await ctx.send("**Log:" + log + "| Date: 10/31/2003 | Description: Automated Incident Report**")
            await ctx.send("Rat containment breach. The quarantine cages have been unlocked due to a system failure.")           
            
        elif log == "118":
            await ctx.send("**Log: 118| Date: 10/31/2003 | Description: Automated Incident Report**")
            await ctx.send("Fire alarm manually activated. Critical System Error contacting local fire station.")  
            
        elif log == "119":
            await ctx.send("**Log: 119| Date: 10/31/2003 | Description: Security Breach Report**")
            await ctx.send("Critial error in locking system. Front door unlocked. Back door unlocked. Containment lab unlocked. Quarantine unlocked. Research storage unlocked. Loading bay unlocked.")    
            
        else:
            await ctx.send("No log listed under that number. Please refine search")

@client.command()
async def logs(ctx, help = 'Lists all logs'):
    if password:
        await ctx.send("Please enter password to access this command") 
    else:
        await ctx.send("```| Log # |    Date    |         Description         |\n > 100    10/27/2003   Recovery\n > 101    10/27/2003   Inital Findings\n > 102    10/28/2003   Spores\n > 103    10/29/2003   Animal Control\n > 104    10/29/2003   Hive Mind\n > 105    10/30/2003   Cure\n > 106    10/30/2003   Mutation\n > 107    10/31/2003   Automated Incident Report\n > 108    10/31/2003   Contamination Emergency\n > 109    10/31/2003   Automated Incident Report\n > 110    10/31/2003   Automated Incident Report\n > 111    10/31/2003   Automated Incident Report\n > 112    10/31/2003   Automated Incident Report\n > 113    10/31/2003   HELP! ANYONE!\n > 114    10/31/2003   Automated Incident Report\n > 115    10/31/2003   Automated Incident Report\n > 116    10/31/2003   Automated Incident Report\n > 117    10/31/2003   Automated Incident Report\n > 118    10/31/2003   Automated Incident Report\n > 119    10/31/2003   Security Breach Report```")
        await ctx.send("*To open a log type -open followed by the log number*")
        
@client.command()
async def lock(ctx):
    global password
    password = True
    await ctx.send("**Computer has been locked**")
    await ctx.send("----------------------------------------\n|** Username:**  `E.Mccoy        `      |\n|** Password:**   `               `      |\n----------------------------------------\n\nPassword Hint ||Precious Flower||")


client.run(token)
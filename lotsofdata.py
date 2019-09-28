from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from database_setup import User, Base, Category, Item
 
engine = create_engine('sqlite:///itemcat.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# res name, id               menu name id description price

#Category of MMO
category1 = Category(user_id=1,name = "MMO")

session.add(category1)
session.commit()

item2 = Item(user_id=1,name = "Dauntless", description = "Gather your friends, forge your weapons, and hunt ferocious behemoths in Dauntless, the co op multiplayer RPG from Phoenix Labs, a studio consisting of developers from some of the biggest MMORPG ever made.", category = category1)

session.add(item2)
session.commit()


item1 = Item(user_id=1,name = "Crossout", description = "Neverwinter is an action MMORPG based on the acclaimed Dungeons and Dragons universe. In Neverwinter you take on the role as a mighty hero who must set out to protect the lands of Neverwinter from those who conspire to see it destroyed.", category = category1)

session.add(item1)
session.commit()

item3 = Item(user_id=1,name = "Neverwinter", description = "Neverwinter is an action MMORPG based on the acclaimed Dungeons and Dragons universe. In Neverwinter you take on the role as a mighty hero who must set out to protect the lands of Neverwinter from those who conspire to see it destroyed.", category = category1)

session.add(item3)
session.commit()

item4 = Item(user_id=1,name = "Guild Wars 2", description = "Guild Wars 2 represents ArenaNets attempt to turn MMO convention on its ears and create an engaging game for players of all skill levels and play styles", category = category1)

session.add(item4)
session.commit()




#Category of Simulations
category2 = Category(user_id=1,name = "Simulations")

session.add(category2)
session.commit()


item1 = Item(user_id=1,name = "The Sims", description = "basicly full life simulation", category = category2)

session.add(item1)
session.commit()


#Category of adventure
category3 = Category(user_id=1,name = "adventure")

session.add(category3)
session.commit()


item1 = Item(user_id=1,name = "Life is Strange", description = "Life is Strange was one of the biggest surprises of the last few years, Its the story of a nervous girl who discovers she has the power to rewind time, right on the edge of a disaster about to hit her town. Yet the drama really comes from her relationships, from the genuinely difficult choices to make, and the clunkily written but still efficient coming of age story at its heart", category = category3)

session.add(item1)
session.commit()

item2 = Item(user_id=1,name = "Soma", description = " Any time you create something as notable as Amnesia: The Dark Descent, theres going to be the lingering question  OK, so what else have you got? Frictional responded with Soma, building on its horror heritage, but putting the scares into an endlessly more complex, beautiful, and somehow even more claustrophobic environment. Unlike a lot of recent horror, it avoids an over reliance on jump scares and repeated gimmicks where possible, and soon reveals it has more to it than just scares. Its a solid bit of SF thatll still make you want to hide behind the sofa. As long as your sofa is in the same room as your PC, which it probably isnt.", category = category3)

session.add(item2)
session.commit()

item3 = Item(user_id=1,name = "Her Story", description = "Her Story has now won enough awards for creator Sam Barlow to melt them all down and create some kind of towering super award, and not without reason. Her Story isnt the only good FMV game ever made, despite what some will say, but it is a genuinely brilliant attempt to use the format for the kind of interactions it was created to offer, instead of bending over backwards to make it do things it never should have been asked to in the first place. Its a bit of a shame that what begins as a murder mystery soon takes a swerve into a more fantastical character study, and that your purpose in the game isnt quite what it seems. Even so, digging through the tale by searching for keywords and clips and piecing together the order for yourself is as compelling as any detective fiction.", category = category3)

session.add(item3)
session.commit()

item4 = Item(user_id=1,name = "Little Big Adventure 2 ", description = "Twinsen is the awkwardly named hero of planet Twinsun, formerly under the despotic control of one Doctor FunFrock. Why, yes, it is a French game. How did you guess? This sequel widens the scope as   friendly aliens arrive to, and lets be clear, definitely not abduct the worlds wizards for evil purposes, and the ensuing trip through space is among the most adorable, most tactile adventures youll ever go on. Also, the most badass threat ever delivered by a hero.", category = category3)

session.add(item4)
session.commit()


#Category of RTS
category5 = Category(user_id=1,name = "RTS ")

session.add(category5)
session.commit()


item1 = Item(user_id=1,name = "Driftland", description = "The Magic Revival : Its nice to see a new face finally make it onto this list   Driftland was in Early Access for a couple of years before it finally released in April 2019, and it seems that time has been put to good use. This is an innovative RTS that follows in the mould of the classic Majesty franchise   where indirect control is the order of the day. You are a Mage whose realm is on one of many shattered pieces of the world floating around, and you must develop your holdings and expand onto other ones by connecting them together.", category = category5)

session.add(item1)
session.commit()

item2 = Item(user_id=1,name = "Bad North", description = "Jotunn Edition Self styling itself as a micro strategy game, Bad North is the poster child for minimalist design facilitating tight tactical decision making. Evoking the best bits of games like FTL, this game sees you taking your modest force from island to island, protecting them against waves of blood thirsty marauders. As you progress through the game you can earn coins to level up your troops, recruit new troops and find powerful items to aid you.", category = category5)

session.add(item2)
session.commit()

item3 = Item(user_id=1,name = "Shadow Tactics", description = "Blades of the Shogun This isnt a new release but we feel its definitely worth mentioning as Shadow Tactics is a wonderfully tense real time tactical/puzzle game that will challenge not only your creative thinking, but also your combo and control skills. This is a stealth based game that follows in the hallowed tradition of classics like Commandos, but also taking queues from modern contemporaries like Assassins Creed. With a very powerful and engaging narrative, you must guide up to five characters through vibrant and varied levels. Subterfuge is key, and fighting your way out isnt really an option.", category = category5)

session.add(item3)
session.commit()


#Category of Action
category6 = Category(user_id=1,name = "Action ")

session.add(category6)
session.commit()


item1 = Item(user_id=1,name = "The Elder Scrolls V: Skyrim Special Edition", description = "The Elder Scrolls V: Skyrim is the fifth game in Bethesdas ever popular series of role playing games. Like its predecessors, Skyrim takes place in an open environment which is full of exploration, wonder and a whole slew of quests. You can easily spend countless hours within this fantasy world and wed honestly be surprised to find a gamer who has yet to experience this journey. If you have yet to do so, pick up The Elder Scrolls V: Skyrim and begin to weave your own tale with the main campaign along with the previously released DLC.", category = category6)

session.add(item1)
session.commit()

item2 = Item(user_id=1,name = "Monster Hunter: World", description = "The Monster Hunter franchise is consistently growing and with each new installment a number of new gamers explore the monster filled worlds development studio Capcom has crafted. Monster Hunter: World is fifth main installment to the franchise and as you can expect, there will be a number of notable updates.", category = category6)

session.add(item2)
session.commit()

item3 = Item(user_id=1,name = "The Witcher 3: Wild Hunt", description = "Fans of western RPGs will no doubt have played at least one of the Witcher games. This series of Polish games based on the works of Andrzej Sapkowski has gained a lot of fans over the years, mainly thanks to its complex world and stories, incredible graphics and deep gameplay systems.The third and final installment in the series sees a much older Geralt of Rivia    one of the titular Witchers    as he deals with the invasion of the Northern Kingdom by the Nilfgaard Empire and the otherworldly threat of the Wild Hunt. Offering a massive open world, hours upon hours of story content and sidequests, tons of NPCS to interact with and monsters to hunt, this title will keep you busy for quite some time.", category = category6)

session.add(item3)
session.commit()

item4 = Item(user_id=1,name = "Uncharted 4 ", description = "The Uncharted franchise has been immensely popular with Sony gamers with the fourth main installment, Uncharted 4: A Thiefs End was set to be the conclusion to the Uncharted series starring Nathan Drake. A Thiefs End takes place several years after the events of Uncharted 3: Drakes Deception, where Nathan Drake has been retired from fortune hunting. That is until he is reunited with his older brother Sam and partner Sully where the trio must search for clues to the location of Captain Henry Averys long lost treasure in order to save Sams life.", category = category6)

session.add(item4)
session.commit()

#Category of Stealth Shooter
category4 = Category(user_id=1,name = "Stealth Shooter")

session.add(category4)
session.commit()


item1 = Item(user_id=1,name = "DISHONORED", description = "Some of the best stealth games can feel turn based    even those that are not Invisible, Inc. They are the ones that have you marking targets, mapping patrol routes, and mentally solving problems    all before uncloaking and triggering the action when youre ready. The Dishonored series is the epitome of that style and, as an added bonus, is just as good for combo slinging predatory combat when youre spotted. No wonder Arkane picked up a Dishonored staff game of the year award from us.", category = category4)

session.add(item1)
session.commit()

item2 = Item(user_id=1,name = "HITMAN", description = "BLOOD MONEY The bald barcoded one known as Agent 47 has had a consistently solid career in stealth games    taking us on globetrotting, sprawling missions of slick, clinical killings since 2000 all the way up to his excellent latest outing    which you can find out more about in our Hitman 2 review. He hit his stride with Blood Money, with fantastic level design that was believable while offering some of the most entertaining, diverse ways to carry out hits. ", category = category4)

session.add(item2)
session.commit()

item3 = Item(user_id=1,name = "SPLINTER CELL: CHAOS THEORY", description = "Chaos Theory is ripe with innovative stealth game mechanics that still feel good today. You can extract information from enemies by holding knives to their throats (and relishing the startled looks on their faces), pull them over edges, hang upside down from rafters to break necks, and phht phht them with a silenced pistol. With his night vision goggles, Sam Fisher is a master of the games nocturnal, shadowy environments, and it is great fun shooting out lights and tormenting your disoriented enemies like a less ostentatious Batman.", category = category4)

session.add(item3)
session.commit()


print "added Game items!"

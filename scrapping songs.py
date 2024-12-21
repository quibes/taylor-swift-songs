# %%
from bs4 import BeautifulSoup
import requests
url = 'https://www.azlyrics.com/t/taylorswift.html'  # Replace with the actual URL

# Fetch the HTML content of the page
response = requests.get(url)
html_content = response.text
# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find the song list section
song_list = soup.find_all('div', class_='listalbum-item')

# Initialize a list to store song data
songs = []

# Extract song titles and URLs
for song in song_list:
    anchor = song.find('a')
    if anchor:
        song_title = anchor.text.strip()
        song_url = anchor['href'].strip()
        songs.append({'title': song_title, 'url': song_url})

# Print the extracted songs
for song in songs:
    print(f"Title: {song['title']}, URL: {song['url']}")


# %%

import json
import time
import os
output_dir = "/Users/anastasyarussu/Downloads/taylor_swift"
output_file = os.path.join(output_dir, "taylor_swift_lyrics.json")
# Base URL of the lyrics website
BASE_URL = "https://www.azlyrics.com"

# List of song titles and URLs
songs = [
    {'title': 'Tim McGraw', 'url': '/lyrics/taylorswift/timmcgraw.html'}, {'title': 'Picture To Burn', 'url': '/lyrics/taylorswift/picturetoburn.html'}, {'title': 'Teardrops On My Guitar', 'url': '/lyrics/taylorswift/teardropsonmyguitar.html'}, {'title': 'A Place In This World', 'url': '/lyrics/taylorswift/aplaceinthisworld.html'}, {'title': 'Cold As You', 'url': '/lyrics/taylorswift/coldasyou.html'}, {'title': 'The Outside', 'url': '/lyrics/taylorswift/theoutside.html'}, {'title': 'Tied Together With A Smile', 'url': '/lyrics/taylorswift/tiedtogetherwithasmile.html'}, {'title': 'Stay Beautiful', 'url': '/lyrics/taylorswift/staybeautiful.html'}, {'title': "Should've Said No", 'url': '/lyrics/taylorswift/shouldvesaidno.html'}, {'title': "Mary's Song (Oh My My My)", 'url': '/lyrics/taylorswift/maryssongohmymymy.html'}, {'title': 'Our Song', 'url': '/lyrics/taylorswift/oursong.html'}, {'title': "I'm Only Me When I'm With You", 'url': '/lyrics/taylorswift/imonlymewhenimwithyou.html'}, {'title': 'Invisible', 'url': '/lyrics/taylorswift/invisible.html'}, {'title': 'A Perfectly Good Heart', 'url': '/lyrics/taylorswift/aperfectlygoodheart.html'}, {'title': 'Last Christmas', 'url': '/lyrics/taylorswift/lastchristmas.html'}, {'title': 'Christmases When You Were Mine', 'url': '/lyrics/taylorswift/christmaseswhenyouweremine.html'}, {'title': 'Santa Baby', 'url': '/lyrics/taylorswift/santababy.html'}, {'title': 'Silent Night', 'url': '/lyrics/taylorswift/silentnight.html'}, {'title': 'Christmas Must Be Something More', 'url': '/lyrics/taylorswift/christmasmustbesomethingmore.html'}, {'title': 'White Christmas', 'url': '/lyrics/taylorswift/whitechristmas.html'},   {'title': '...Ready For It?', 'url': '/lyrics/taylorswift/readyforit.html'}, {'title': 'End Game', 'url': '/lyrics/taylorswift/endgame.html'}, {'title': 'I Did Something Bad', 'url': '/lyrics/taylorswift/ididsomethingbad.html'}, {'title': "Don't Blame Me", 'url': '/lyrics/taylorswift/dontblameme.html'}, {'title': 'Delicate', 'url': '/lyrics/taylorswift/delicate.html'}, {'title': 'Look What You Made Me Do', 'url': '/lyrics/taylorswift/lookwhatyoumademedo.html'}, {'title': 'So It Goes...', 'url': '/lyrics/taylorswift/soitgoes.html'}, {'title': 'Gorgeous', 'url': '/lyrics/taylorswift/gorgeous.html'}, {'title': 'Getaway Car', 'url': '/lyrics/taylorswift/getawaycar.html'}, {'title': 'King Of My Heart', 'url': '/lyrics/taylorswift/kingofmyheart.html'}, {'title': 'Dancing With Our Hands Tied', 'url': '/lyrics/taylorswift/dancingwithourhandstied.html'}, {'title': 'Dress', 'url': '/lyrics/taylorswift/dress.html'}, {'title': "This Is Why We Can't Have Nice Things", 'url': '/lyrics/taylorswift/thisiswhywecanthavenicethings.html'}, {'title': 'Call It What You Want', 'url': '/lyrics/taylorswift/callitwhatyouwant.html'}, {'title': "New Year's Day", 'url': '/lyrics/taylorswift/newyearsday.html'}, {'title': 'I Forgot That You Existed', 'url': '/lyrics/taylorswift/iforgotthatyouexisted.html'}, {'title': 'Cruel Summer', 'url': '/lyrics/taylorswift/cruelsummer.html'}, {'title': 'Lover', 'url': '/lyrics/taylorswift/lover.html'}, {'title': 'The Man', 'url': '/lyrics/taylorswift/theman.html'}, {'title': 'The Archer', 'url': '/lyrics/taylorswift/thearcher.html'}, {'title': 'I Think He Knows', 'url': '/lyrics/taylorswift/ithinkheknows.html'}, {'title': 'Miss Americana & The Heartbreak Prince', 'url': '/lyrics/taylorswift/missamericanatheheartbreakprince.html'}, {'title': 'Paper Rings', 'url': '/lyrics/taylorswift/paperrings.html'}, {'title': 'Cornelia Street', 'url': '/lyrics/taylorswift/corneliastreet.html'}, {'title': 'Death By A Thousand Cuts', 'url': '/lyrics/taylorswift/deathbyathousandcuts.html'}, {'title': 'London Boy', 'url': '/lyrics/taylorswift/londonboy.html'}, {'title': "Soon You'll Get Better", 'url': '/lyrics/taylorswift/soonyoullgetbetter.html'}, {'title': 'False God', 'url': '/lyrics/taylorswift/falsegod.html'}, {'title': 'You Need To Calm Down', 'url': '/lyrics/taylorswift/youneedtocalmdown.html'}, {'title': 'Afterglow', 'url': '/lyrics/taylorswift/afterglow.html'}, {'title': 'ME!', 'url': '/lyrics/taylorswift/me.html'}, {'title': "It's Nice To Have A Friend", 'url': '/lyrics/taylorswift/itsnicetohaveafriend.html'}, {'title': 'Daylight', 'url': '/lyrics/taylorswift/daylight.html'}, {'title': 'the 1', 'url': '/lyrics/taylorswift/the1.html'}, {'title': 'cardigan', 'url': '/lyrics/taylorswift/cardigan.html'}, {'title': 'the last great american dynasty', 'url': '/lyrics/taylorswift/thelastgreatamericandynasty.html'}, {'title': 'exile', 'url': '/lyrics/taylorswift/exile.html'}, {'title': 'my tears ricochet', 'url': '/lyrics/taylorswift/mytearsricochet.html'}, {'title': 'mirrorball', 'url': '/lyrics/taylorswift/mirrorball.html'}, {'title': 'seven', 'url': '/lyrics/taylorswift/seven.html'}, {'title': 'august', 'url': '/lyrics/taylorswift/august.html'}, {'title': 'this is me trying', 'url': '/lyrics/taylorswift/thisismetrying.html'}, {'title': 'illicit affairs', 'url': '/lyrics/taylorswift/illicitaffairs.html'}, {'title': 'invisible string', 'url': '/lyrics/taylorswift/invisiblestring.html'}, {'title': 'mad woman', 'url': '/lyrics/taylorswift/madwoman.html'}, {'title': 'epiphany', 'url': '/lyrics/taylorswift/epiphany.html'}, {'title': 'betty', 'url': '/lyrics/taylorswift/betty.html'}, {'title': 'peace', 'url': '/lyrics/taylorswift/peace.html'}, {'title': 'hoax', 'url': '/lyrics/taylorswift/hoax.html'}, {'title': 'the lakes', 'url': '/lyrics/taylorswift/thelakes.html'}, {'title': 'willow', 'url': '/lyrics/taylorswift/willow.html'}, {'title': 'champagne problems', 'url': '/lyrics/taylorswift/champagneproblems.html'}, {'title': 'gold rush', 'url': '/lyrics/taylorswift/goldrush.html'}, {'title': "'tis the damn season", 'url': '/lyrics/taylorswift/tisthedamnseason.html'}, {'title': 'tolerate it', 'url': '/lyrics/taylorswift/tolerateit.html'}, {'title': 'no body', 'url': '/lyrics/taylorswift/nobodynocrime.html'}, {'title': 'happiness', 'url': '/lyrics/taylorswift/happiness.html'}, {'title': 'dorothea', 'url': '/lyrics/taylorswift/dorothea.html'}, {'title': 'coney island', 'url': '/lyrics/taylorswift/coneyisland.html'}, {'title': 'ivy', 'url': '/lyrics/taylorswift/ivy.html'}, {'title': 'cowboy like me', 'url': '/lyrics/taylorswift/cowboylikeme.html'}, {'title': 'long story short', 'url': '/lyrics/taylorswift/longstoryshort.html'}, {'title': 'marjorie', 'url': '/lyrics/taylorswift/marjorie.html'}, {'title': 'closure', 'url': '/lyrics/taylorswift/closure.html'}, {'title': 'evermore', 'url': '/lyrics/taylorswift/evermore.html'}, {'title': 'right where you left me', 'url': '/lyrics/taylorswift/rightwhereyouleftme.html'}, {'title': "it's time to go", 'url': '/lyrics/taylorswift/itstimetogo.html'}, {'title': "Fearless (Taylor's Version)", 'url': '/lyrics/taylorswift/fearlesstaylorsversion.html'}, {'title': "Fifteen (Taylor's Version)", 'url': '/lyrics/taylorswift/fifteentaylorsversion.html'}, {'title': "Love Story (Taylor's Version)", 'url': '/lyrics/taylorswift/lovestorytaylorsversion.html'}, {'title': "Hey Stephen (Taylor's Version)", 'url': '/lyrics/taylorswift/heystephentaylorsversion.html'}, {'title': "White Horse (Taylor's Version)", 'url': '/lyrics/taylorswift/whitehorsetaylorsversion.html'}, {'title': "You Belong With Me (Taylor's Version)", 'url': '/lyrics/taylorswift/youbelongwithmetaylorsversion.html'}, {'title': "Breathe (Taylor's Version)", 'url': '/lyrics/taylorswift/breathetaylorsversion.html'}, {'title': "Tell Me Why (Taylor's Version)", 'url': '/lyrics/taylorswift/tellmewhytaylorsversion.html'}, {'title': "You're Not Sorry (Taylor's Version)", 'url': '/lyrics/taylorswift/yourenotsorrytaylorsversion.html'}, {'title': "The Way I Loved You (Taylor's Version)", 'url': '/lyrics/taylorswift/thewayilovedyoutaylorsversion.html'}, {'title': "Forever & Always (Taylor's Version)", 'url': '/lyrics/taylorswift/foreveralwaystaylorsversion.html'}, {'title': "The Best Day (Taylor's Version)", 'url': '/lyrics/taylorswift/thebestdaytaylorsversion.html'}, {'title': "Change (Taylor's Version)", 'url': '/lyrics/taylorswift/changetaylorsversion.html'}, {'title': "Jump Then Fall (Taylor's Version)", 'url': '/lyrics/taylorswift/jumpthenfalltaylorsversion.html'}, {'title': "Untouchable (Taylor's Version)", 'url': '/lyrics/taylorswift/untouchabletaylorsversion.html'}, {'title': "Forever & Always (Piano Version) (Taylor's Version)", 'url': '/lyrics/taylorswift/foreveralwayspianoversiontaylorsversion.html'}, {'title': "Come In With The Rain (Taylor's Version)", 'url': '/lyrics/taylorswift/comeinwiththeraintaylorsversion.html'}, {'title': "Superstar (Taylor's Version)", 'url': '/lyrics/taylorswift/superstartaylorsversion.html'}, {'title': "The Other Side Of The Door (Taylor's Version)", 'url': '/lyrics/taylorswift/theothersideofthedoortaylorsversion.html'}, {'title': "Today Was A Fairytale (Taylor's Version)", 'url': '/lyrics/taylorswift/todaywasafairytaletaylorsversion.html'}, {'title': "You All Over Me (Taylor's Version) (From The Vault)", 'url': '/lyrics/taylorswift/youalloverme.html'}, {'title': "Mr. Perfectly Fine (Taylor's Version) (From The Vault)", 'url': '/lyrics/taylorswift/mrperfectlyfinetaylorsversionfromthevault.html'}, {'title': "We Were Happy (Taylor's Version) (From The Vault)", 'url': '/lyrics/taylorswift/wewerehappytaylorsversionfromthevault.html'}, {'title': "That's When (Taylor's Version) (From The Vault)", 'url': '/lyrics/taylorswift/thatswhentaylorsversionfromthevault.html'}, {'title': "Don't You (Taylor's Version) (From The Vault)", 'url': '/lyrics/taylorswift/dontyoutaylorsversionfromthevault.html'}, {'title': "Bye Bye Baby (Taylor's Version) (From The Vault)", 'url': '/lyrics/taylorswift/byebyebabytaylorsversionfromthevault.html'}, {'title': "State Of Grace (Taylor's Version)", 'url': '/lyrics/taylorswift/stateofgracetaylorsversion.html'}, {'title': "Red (Taylor's Version)", 'url': '/lyrics/taylorswift/redtaylorsversion.html'}, {'title': "Treacherous (Taylor's Version)", 'url': '/lyrics/taylorswift/treacheroustaylorsversion.html'}, {'title': "I Knew You Were Trouble (Taylor's Version)", 'url': '/lyrics/taylorswift/iknewyouweretroubletaylorsversion.html'}, {'title': "All Too Well (Taylor's Version)", 'url': '/lyrics/taylorswift/alltoowelltaylorsversion.html'}, {'title': "22 (Taylor's Version)", 'url': '/lyrics/taylorswift/22taylorsversion.html'}, {'title': "I Almost Do (Taylor's Version)", 'url': '/lyrics/taylorswift/ialmostdotaylorsversion.html'}, {'title': "We Are Never Ever Getting Back Together (Taylor's Version)", 'url': '/lyrics/taylorswift/weareneverevergettingbacktogethertaylorsversion.html'}, {'title': "Stay Stay Stay (Taylor's Version)", 'url': '/lyrics/taylorswift/staystaystaytaylorsversion.html'}, {'title': "The Last Time (Taylor's Version)", 'url': '/lyrics/taylorswift/thelasttimetaylorsversion.html'}, {'title': "Holy Ground (Taylor's Version)", 'url': '/lyrics/taylorswift/holygroundtaylorsversion.html'}, {'title': "Sad Beautiful Tragic (Taylor's Version)", 'url': '/lyrics/taylorswift/sadbeautifultragictaylorsversion.html'}, {'title': "The Lucky One (Taylor's Version)", 'url': '/lyrics/taylorswift/theluckyonetaylorsversion.html'}, {'title': "Everything Has Changed (Taylor's Version)", 'url': '/lyrics/taylorswift/everythinghaschangedtaylorsversion.html'}, {'title': "Starlight (Taylor's Version)", 'url': '/lyrics/taylorswift/starlighttaylorsversion.html'}, {'title': "Begin Again (Taylor's Version)", 'url': '/lyrics/taylorswift/beginagaintaylorsversion.html'}, {'title': "The Moment I Knew (Taylor's Version)", 'url': '/lyrics/taylorswift/themomentiknewtaylorsversion.html'}, {'title': "Come Back...Be Here (Taylor's Version)", 'url': '/lyrics/taylorswift/comebackbeheretaylorsversion.html'}, {'title': "Girl At Home (Taylor's Version)", 'url': '/lyrics/taylorswift/girlathometaylorsversion.html'}, {'title': "State Of Grace (Acoustic Version) (Taylor's Version)", 'url': '/lyrics/taylorswift/stateofgraceacousticversiontaylorsversion.html'}, {'title': "Ronan (Taylor's Version)", 'url': '/lyrics/taylorswift/ronantaylorsversion.html'}, {'title': "Better Man (Taylor's Version) (From The Vault)", 'url': '/lyrics/taylorswift/bettermantaylorsversionfromthevault.html'}, {'title': "Nothing New (Taylor's Version) (From The Vault)", 'url': '/lyrics/taylorswift/nothingnewtaylorsversionfromthevault.html'}, {'title': "Babe (Taylor's Version) (From The Vault)", 'url': '/lyrics/taylorswift/babetaylorsversionfromthevault.html'}, {'title': "Message In A Bottle (Taylor's Version) (From The Vault)", 'url': '/lyrics/taylorswift/messageinabottletaylorsversionfromthevault.html'}, {'title': "I Bet You Think About Me (Taylor's Version) (From The Vault)", 'url': '/lyrics/taylorswift/ibetyouthinkaboutmetaylorsversionfromthevault.html'}, {'title': "Forever Winter (Taylor's Version) (From The Vault)", 'url': '/lyrics/taylorswift/foreverwintertaylorsversionfromthevault.html'}, {'title': "Run (Taylor's Version) (From The Vault)", 'url': '/lyrics/taylorswift/runtaylorsversionfromthevault.html'}, {'title': "The Very First Night (Taylor's Version) (From The Vault)", 'url': '/lyrics/taylorswift/theveryfirstnighttaylorsversionfromthevault.html'}, {'title': "All Too Well (10 Minute Version) (Taylor's Version) (From The Vault)", 'url': '/lyrics/taylorswift/alltoowell10minuteversiontaylorsversionfromthevault.html'}, {'title': 'A Message From Taylor', 'url': '/lyrics/taylorswift/amessagefromtaylor.html'}, {'title': 'Lavender Haze', 'url': '/lyrics/taylorswift/lavenderhaze.html'}, {'title': 'Maroon', 'url': '/lyrics/taylorswift/maroon.html'}, {'title': 'Anti-Hero', 'url': '/lyrics/taylorswift/antihero.html'}, {'title': 'Snow On The Beach', 'url': '/lyrics/taylorswift/snowonthebeach.html'}, {'title': "You're On Your Own", 'url': '/lyrics/taylorswift/youreonyourownkid.html'}, {'title': 'Midnight Rain', 'url': '/lyrics/taylorswift/midnightrain.html'}, {'title': 'Question...?', 'url': '/lyrics/taylorswift/question.html'}, {'title': 'Vigilante Shit', 'url': '/lyrics/taylorswift/vigilanteshit.html'}, {'title': 'Bejeweled', 'url': '/lyrics/taylorswift/bejeweled.html'}, {'title': 'Labyrinth', 'url': '/lyrics/taylorswift/labyrinth.html'}, {'title': 'Karma', 'url': '/lyrics/taylorswift/karma.html'}, {'title': 'Sweet Nothing', 'url': '/lyrics/taylorswift/sweetnothing.html'}, {'title': 'Mastermind', 'url': '/lyrics/taylorswift/mastermind.html'}, {'title': 'Hits Different', 'url': '/lyrics/taylorswift/hitsdifferent.html'}, {'title': "You're On Your Own", 'url': '/lyrics/taylorswift/youreonyourownkidstringsremix.html'}, {'title': 'Sweet Nothing (Piano Remix)', 'url': '/lyrics/taylorswift/sweetnothingpianoremix.html'}, {'title': 'Meet Me At Midnight', 'url': '/lyrics/taylorswift/meetmeatmidnight.html'}, {'title': 'The Great War', 'url': '/lyrics/taylorswift/thegreatwar.html'}, {'title': 'Bigger Than The Whole Sky', 'url': '/lyrics/taylorswift/biggerthanthewholesky.html'}, {'title': 'Paris', 'url': '/lyrics/taylorswift/paris.html'}, {'title': 'High Infidelity', 'url': '/lyrics/taylorswift/highinfidelity.html'}, {'title': 'Glitch', 'url': '/lyrics/taylorswift/glitch.html'}, {'title': "Would've", 'url': '/lyrics/taylorswift/wouldvecouldveshouldve.html'}, {'title': 'Dear Reader', 'url': '/lyrics/taylorswift/dearreader.html'},  {'title': 'Snow On The Beach (Remix)', 'url': '/lyrics/taylorswift/snowonthebeachremix.html'}, {'title': 'Karma (Remix)', 'url': '/lyrics/taylorswift/karmaremix.html'}, {'title': "Mine (Taylor's Version)", 'url': '/lyrics/taylorswift/minetaylorsversion.html'}, {'title': "Sparks Fly (Taylor's Version)", 'url': '/lyrics/taylorswift/sparksflytaylorsversion.html'}, {'title': "Back To December (Taylor's Version)", 'url': '/lyrics/taylorswift/backtodecembertaylorsversion.html'}, {'title': "Speak Now (Taylor's Version)", 'url': '/lyrics/taylorswift/speaknowtaylorsversion.html'}, {'title': "Dear John (Taylor's Version)", 'url': '/lyrics/taylorswift/dearjohntaylorsversion.html'}, {'title': "Mean (Taylor's Version)", 'url': '/lyrics/taylorswift/meantaylorsversion.html'}, {'title': "The Story Of Us (Taylor's Version)", 'url': '/lyrics/taylorswift/thestoryofustaylorsversion.html'}, {'title': "Never Grow Up (Taylor's Version)", 'url': '/lyrics/taylorswift/nevergrowuptaylorsversion.html'}, {'title': "Enchanted (Taylor's Version)", 'url': '/lyrics/taylorswift/enchantedtaylorsversion.html'}, {'title': "Better Than Revenge (Taylor's Version)", 'url': '/lyrics/taylorswift/betterthanrevengetaylorsversion.html'}, {'title': "Innocent (Taylor's Version)", 'url': '/lyrics/taylorswift/innocenttaylorsversion.html'}, {'title': "Haunted (Taylor's Version)", 'url': '/lyrics/taylorswift/hauntedtaylorsversion.html'}, {'title': "Last Kiss (Taylor's Version)", 'url': '/lyrics/taylorswift/lastkisstaylorsversion.html'}, {'title': "Long Live (Taylor's Version)", 'url': '/lyrics/taylorswift/longlivetaylorsversion.html'}, {'title': "Ours (Taylor's Version)", 'url': '/lyrics/taylorswift/ourstaylorsversion.html'}, {'title': "Superman (Taylor's Version)", 'url': '/lyrics/taylorswift/supermantaylorsversion.html'}, {'title': "Electric Touch (Taylor's Version) (From The Vault)", 'url': '/lyrics/taylorswift/electrictouchtaylorsversionfromthevault.html'}, {'title': "When Emma Falls in Love (Taylor's Version) (From The Vault)", 'url': '/lyrics/taylorswift/whenemmafallsinlovetaylorsversionfromthevault.html'}, {'title': "I Can See You (Taylor's Version) (From The Vault)", 'url': '/lyrics/taylorswift/icanseeyoutaylorsversionfromthevault.html'}, {'title': "Castles Crumbling (Taylor's Version) (From The Vault)", 'url': '/lyrics/taylorswift/castlescrumblingtaylorsversionfromthevault.html'}, {'title': "Foolish One (Taylor's Version) (From The Vault)", 'url': '/lyrics/taylorswift/foolishonetaylorsversionfromthevault.html'}, {'title': "Timeless (Taylor's Version) (From The Vault)", 'url': '/lyrics/taylorswift/timelesstaylorsversionfromthevault.html'}, {'title': "Welcome To New York (Taylor's Version)", 'url': '/lyrics/taylorswift/welcometonewyorktaylorsversion.html'}, {'title': "Blank Space (Taylor's Version)", 'url': '/lyrics/taylorswift/blankspacetaylorsversion.html'}, {'title': "Style (Taylor's Version)", 'url': '/lyrics/taylorswift/styletaylorsversion.html'}, {'title': "Out Of The Woods (Taylor's Version)", 'url': '/lyrics/taylorswift/outofthewoodstaylorsversion.html'}, {'title': "All You Had To Do Was Stay (Taylor's Version)", 'url': '/lyrics/taylorswift/allyouhadtodowasstaytaylorsversion.html'}, {'title': "Shake It Off (Taylor's Version)", 'url': '/lyrics/taylorswift/shakeitofftaylorsversion.html'}, {'title': "I Wish You Would (Taylor's Version)", 'url': '/lyrics/taylorswift/iwishyouwouldtaylorsversion.html'}, {'title': "Bad Blood (Taylor's Version)", 'url': '/lyrics/taylorswift/badbloodtaylorsversion.html'}, {'title': "Wildest Dreams (Taylor's Version)", 'url': '/lyrics/taylorswift/wildestdreamstaylorsversion.html'}, {'title': "How You Get The Girl (Taylor's Version)", 'url': '/lyrics/taylorswift/howyougetthegirltaylorsversion.html'}, {'title': "This Love (Taylor's Version)", 'url': '/lyrics/taylorswift/thislovetaylorsversion.html'}, {'title': "I Know Places (Taylor's Version)", 'url': '/lyrics/taylorswift/iknowplacestaylorsversion.html'}, {'title': "Clean (Taylor's Version)", 'url': '/lyrics/taylorswift/cleantaylorsversion.html'}, {'title': "Wonderland (Taylor's Version)", 'url': '/lyrics/taylorswift/wonderlandtaylorsversion.html'}, {'title': "You Are In Love (Taylor's Version)", 'url': '/lyrics/taylorswift/youareinlovetaylorsversion.html'}, {'title': "New Romantics (Taylor's Version)", 'url': '/lyrics/taylorswift/newromanticstaylorsversion.html'}, {'title': '"Slut!" (Taylor\'s Version) (From The Vault)', 'url': '/lyrics/taylorswift/sluttaylorsversionfromthevault.html'}, {'title': "Say Don't Go (Taylor's Version) (From The Vault)", 'url': '/lyrics/taylorswift/saydontgotaylorsversionfromthevault.html'}, {'title': "Now That We Don't Talk (Taylor's Version) (From The Vault)", 'url': '/lyrics/taylorswift/nowthatwedonttalktaylorsversionfromthevault.html'}, {'title': "Suburban Legends (Taylor's Version) (From The Vault)", 'url': '/lyrics/taylorswift/suburbanlegendstaylorsversionfromthevault.html'}, {'title': "Is It Over Now? (Taylor's Version) (From The Vault)", 'url': '/lyrics/taylorswift/isitovernowtaylorsversionfromthevault.html'}, {'title': "Bad Blood (Remix) (Taylor's Version)", 'url': '/lyrics/taylorswift/badbloodremixtaylorsversion.html'}, {'title': "Sweeter Than Fiction (Taylor's Version)", 'url': '/lyrics/taylorswift/sweeterthanfictiontaylorsversion.html'}, {'title': '"Slut!" (Acoustic Version) (Taylor\'s Version)', 'url': '/lyrics/taylorswift/slutacousticversiontaylorsversion.html'}, {'title': 'Fortnight', 'url': '/lyrics/taylorswift/fortnight.html'}, {'title': 'The Tortured Poets Department', 'url': '/lyrics/taylorswift/thetorturedpoetsdepartment.html'}, {'title': 'My Boy Only Breaks His Favorite Toys', 'url': '/lyrics/taylorswift/myboyonlybreakshisfavoritetoys.html'}, {'title': 'Down Bad', 'url': '/lyrics/taylorswift/downbad.html'}, {'title': 'So Long', 'url': '/lyrics/taylorswift/solonglondon.html'}, {'title': 'But Daddy I Love Him', 'url': '/lyrics/taylorswift/butdaddyilovehim.html'}, {'title': 'Fresh Out The Slammer', 'url': '/lyrics/taylorswift/freshouttheslammer.html'}, {'title': 'Florida!!!', 'url': '/lyrics/taylorswift/florida.html'}, {'title': 'Guilty As Sin?', 'url': '/lyrics/taylorswift/guiltyassin.html'}, {'title': "Who's Afraid Of Little Old Me?", 'url': '/lyrics/taylorswift/whosafraidoflittleoldme.html'}, {'title': 'I Can Fix Him (No Really I Can)', 'url': '/lyrics/taylorswift/icanfixhimnoreallyican.html'}, {'title': '\u200eloml', 'url': '/lyrics/taylorswift/loml.html'}, {'title': 'I Can Do It With A Broken Heart', 'url': '/lyrics/taylorswift/icandoitwithabrokenheart.html'}, {'title': 'The Smallest Man Who Ever Lived', 'url': '/lyrics/taylorswift/thesmallestmanwhoeverlived.html'}, {'title': 'The Alchemy', 'url': '/lyrics/taylorswift/thealchemy.html'}, {'title': 'Clara Bow', 'url': '/lyrics/taylorswift/clarabow.html'}, {'title': 'The Black Dog', 'url': '/lyrics/taylorswift/theblackdog.html'}, {'title': 'imgonnagetyouback', 'url': '/lyrics/taylorswift/imgonnagetyouback.html'}, {'title': 'The Albatross', 'url': '/lyrics/taylorswift/thealbatross.html'}, {'title': 'Chloe or Sam or Sophia or Marcus', 'url': '/lyrics/taylorswift/chloeorsamorsophiaormarcus.html'}, {'title': 'How Did It End?', 'url': '/lyrics/taylorswift/howdiditend.html'}, {'title': 'So High School', 'url': '/lyrics/taylorswift/sohighschool.html'}, {'title': 'I Hate It Here', 'url': '/lyrics/taylorswift/ihateithere.html'}, {'title': 'thanK you aIMee', 'url': '/lyrics/taylorswift/thankyouaimee.html'}, {'title': "I Look in People's Windows", 'url': '/lyrics/taylorswift/ilookinpeopleswindows.html'}, {'title': 'The Prophecy', 'url': '/lyrics/taylorswift/theprophecy.html'}, {'title': 'Cassandra', 'url': '/lyrics/taylorswift/cassandra.html'}, {'title': 'Peter', 'url': '/lyrics/taylorswift/peter.html'}, {'title': 'The Bolter', 'url': '/lyrics/taylorswift/thebolter.html'}, {'title': 'Robin', 'url': '/lyrics/taylorswift/robin.html'}, {'title': 'The Manuscript', 'url': '/lyrics/taylorswift/themanuscript.html'}
]




# Function to scrape lyrics for a single song
def scrape_lyrics(song_url):
    full_url = BASE_URL + song_url
    try:
        response = requests.get(full_url, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Locate the lyrics container (adjust this selector if it changes)
        div = soup.find("div", class_=None, id=None)
        if div:
            lyrics = div.get_text(separator="\n").strip()
            return lyrics
        else:
            return "Lyrics not found"
    except Exception as e:
        return f"Error: {e}"

# Dictionary to store the lyrics
lyrics_data = {}

# Scrape lyrics for all songs
for song in songs:
    print(f"Scraping lyrics for: {song['title']}")
    lyrics = scrape_lyrics(song["url"])
    lyrics_data[song["title"]] = lyrics
    time.sleep(10)  # Delay to avoid being blocked

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(lyrics_data, f, indent=4, ensure_ascii=False)

print(f"Scraping completed. Lyrics saved to '{output_file}'.")




# %%
import boto3

# Create an S3 client using your default AWS credentials and region
s3 = boto3.client('s3')

# List all the buckets you have access to
response = s3.list_buckets()

print("Buckets in your account:")
for bucket in response['Buckets']:
    print(f"- {bucket['Name']}")


# %%
import json
import boto3
import os

lyrics_file_path = "/Users/anastasyarussu/Downloads/taylor_swift/taylor_swift_lyrics.json"
bucket_name = "anastasiia-de2-ceu-bucket"
temp_dir = "/Users/anastasyarussu/temp_lyrics"  # writable path in your home directory

# Load the dictionary of songs and lyrics from the JSON file
with open(lyrics_file_path, "r", encoding="utf-8") as f:
    songs_lyrics = json.load(f)

# Create an S3 client
s3 = boto3.client('s3')

# Create a local directory to store temp files before upload
os.makedirs(temp_dir, exist_ok=True)

# Iterate over each song and store its lyrics as a text file
for song_title, lyrics in songs_lyrics.items():
    # Create a filename based on the song title (replace spaces with underscores)
    filename = os.path.join(temp_dir, f"{song_title.replace(' ', '_')}.txt")
    
    # Write the lyrics to a local file
    with open(filename, "w", encoding="utf-8") as f:
        f.write(lyrics)
    
    # Upload the file to S3
    object_key = f"taylor_swift_lyrics/{song_title.replace(' ', '_')}.txt"
    s3.upload_file(filename, bucket_name, object_key)
    print(f"Uploaded {song_title} to s3://{bucket_name}/{object_key}")

print("All songs uploaded successfully.")




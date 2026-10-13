HL_dic=[
    {
        "Name/club":"NASA",
        "Jobs/description":"Space Agency",
        "Country":"USA",
        "Followers":189_000_000 #189 millions
    }
    ,
    {
        "Name/club":"David Beckham",
        "Jobs/description":"Footballer",
        "Country":"UK",
        "Followers":154_000_000
    }
    ,
    {
        "Name/club":"Lionel Messi",
        "Jobs/description":"Footballer",
        "Country":"Argentina",
        "Followers":628_000_000  #628 billion
        
    }
    ,
    {
        "Name/club":"Christiano Ronaldo",
        "Jobs/description":"Footballer",
        "Country":"Portugal",
        "Followers":1_000_000_000 #1billion  
    }
    ,  {
        "Name/club": "Selena Gomez",
        "Jobs/description": "Musician and Actress",
        "Country": "USA",
        "Followers": 568_000_000
    },
    {
        "Name/club": "Real Madrid",
        "Jobs/description": "Football club",
        "Country": "Spain",
        "Followers": 488_000_000
    },
    {
        "Name/club": "Virat Kohli",
        "Jobs/description": "Cricketer",
        "Country": "India",
        "Followers": 393_000_000
    },
    {
        "Name/club": "Kylie Jenner",
        "Jobs/description": "Businesswoman and Media Personality",
        "Country": "USA",
        "Followers": 522_000_000
    }
    ,
    {
        "Name/club":"Justin Bieber",
        "Jobs/description":"Musician",
        "Country":"Canada",
        "Followers":576_000_000#576 millions  
    }
    ,
    {
        "Name/club":"9GAG",
        "Jobs/description":"Social media platform",
        "Country":"China",
        "Followers":106_000_000
    }
    ,
    {
        "Name/club":"Taylor Swift",
        "Jobs/description":"Musician",
        "Country":"USA",
        "Followers":561_000_000#561 millions  
    }
    ,
    {
        "Name/club":"Neymar",
        "Jobs/description":"Footballer",
        "Country":"Brazil",
        "Followers":457_000_000#189 millions  
    }
    ,
    {
        "Name/club":"Priyanka Chopra Jonas",
        "Jobs/description":"Musician and Actress",
        "Country":"India",
        "Followers":125_000_000#125 millions  
    }
    ,
    {
        "Name/club":"Miley Cyrus",
        "Jobs/description":"Musician and Actress",
        "Country":"USA",
        "Followers":355_000_000#355 millions  
    }
    ,
    {
        "Name/club":"Demi Lovato",
        "Jobs/description":"Musician and actress",
        "Country":"Canada",
        "Followers":273_000_000#273 millions  
    }
    ,
    {
        "Name/club":"Cardi.B",
        "Jobs/description":"Musician",
        "Country":"USA",
        "Followers":294_000_000#189 millions  
    }
    ,
    {
        "Name/club":"Rihanna",
        "Jobs/description":"Musician and actress",
        "Country":"USA",
        "Followers":345_000_000#345 millions  
    }
    ,
    {
        "Name/club":"FC barcelona",
        "Jobs/description":"Football club",
        "Country":"Spain",
        "Followers":442_000_000#442 millions  
    }
    ,
    {
        "Name/club":"Katy Perry",
        "Jobs/description":"Musician",
        "Country":"USA",
        "Followers":347_000_000#347 millions  
    }
    ,
    {
        "Name/club":"Billie Eilish",
        "Jobs/description":"Musician",
        "Country":"USA",
        "Followers":429_000_000#429 millions  
    }
]
#Kanye west , fashion designer and musician, 67.5million




def pseudo():
    return print("""
pseudocodes of higher and lower
Create/import the contestant dataset — 10–12 entries is enough.
Import the Higher Lower ASCII logo.
Randomly choose A.
Randomly choose B.
Display A and B without revealing follower counts.
Ask: Who has more followers, A or B?
Compare the user's choice against the stored follower counts.
If correct:
score increases
B becomes the new A
choose a new B
A = 20
B = 30
C = {}
A ← B
C ← new random contender
repeat
elif if score==20: print congratulations show firework logo
If wrong:
stop the loop
display Game Over + final score.
A = current contender
B = challenger
       ↓
B > A
       ↓
B becomes the new current contender
       ↓
remove the old/current contender from available pool
       ↓
random.choice(remaining pool)
       ↓
new challenger

A + B
 ↓
user chooses
 ↓
compare follower counts
 ↓
correct?
 ├── NO → Game Over → final score
 │
 └── YES
       ↓
     score + 1
       ↓
     winner → A
       ↓
     new random contestant → B
       ↓
     repeat
""")
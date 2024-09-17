import random
import time

# Welcome to Unicorn Overflow 🦄!
# In this magical script, we summon unicorns and get a whimsical fortune!

def summon_unicorn():
    unicorn_moods = [
        "🌈 Your unicorn is happy and spreading rainbows everywhere! 🌈",
        "💤 Your unicorn is sleepy... maybe it’s time for a nap. 💤",
        "🔥 Uh-oh! Your unicorn is a little cranky and breathing fire! 🐉 (Who knew?)",
        "🍭 Your unicorn is eating candy and ignoring you. 🍭",
        "🚀 Your unicorn is off to space! See you later, Earthling. 🚀",
    ]
    return random.choice(unicorn_moods)

def unicorn_party():
    print("✨ Summoning unicorns... 🦄✨")
    for _ in range(5):
        time.sleep(1)  # Adds a little magical suspense
        mood = summon_unicorn()
        print(mood)

def unicorn_fortune():
    fortunes = [
        "🔮 You will discover a hidden talent for rainbow dancing! 🌈",
        "🔮 Beware of glitter storms... they're fun but messy! ✨",
        "🔮 A unicorn friend will bring you unexpected joy today. 🦄",
        "🔮 You will soon find yourself on a journey to Candyland. 🍬",
        "🔮 Magical things are in store for you, but only if you believe! 🪄"
    ]
    return random.choice(fortunes)

def main():
    print("🦄 Welcome to Unicorn Overflow! Let's summon some unicorns. 🦄")
    
    user_input = input("Do you want to summon a unicorn? (yes/no): ").strip().lower()
    
    if user_input == "yes":
        unicorn_party()
        
        # After summoning unicorns, let's reveal a fortune!
        time.sleep(1)
        print("\n🔮 The Unicorn Fortune Teller has something to say! 🔮")
        time.sleep(1)
        print(unicorn_fortune())
    else:
        print("🚫 No unicorns for you today. Maybe next time!")

if __name__ == "__main__":
    main()

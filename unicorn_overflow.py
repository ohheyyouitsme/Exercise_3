import random
import time

# Welcome to Unicorn Overflow 🦄!
# In this magical script, we summon unicorns, get a whimsical fortune, and receive your very own unicorn name!

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

def unicorn_name_generator():
    first_names = ["Sparkle", "Rainbow", "Glitter", "Star", "Moonbeam", "Mystic", "Twilight", "Sunny", "Shimmer", "Aurora"]
    last_names = ["Prancer", "Glimmerhoof", "Stardust", "Dreamwhisper", "Skydancer", "Silverbell", "Sunshine", "Shadowmane", "Nightwind", "Dewdrop"]
    
    return f"{random.choice(first_names)} {random.choice(last_names)}"

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

        # Give the user their own unicorn name!
        time.sleep(1)
        print("\n✨ But wait! Every unicorn needs a name... ✨")
        time.sleep(1)
        print(f"Your unicorn name is: {unicorn_name_generator()} 🦄")
        
    else:
        print("🚫 No unicorns for you today. Maybe next time!")

if __name__ == "__main__":
    main()

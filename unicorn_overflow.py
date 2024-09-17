import random
import time

# Welcome to Unicorn Overflow 🦄!
# In this magical script, we summon unicorns and see what kind of mood they’re in!

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

def main():
    print("🦄 Welcome to Unicorn Overflow! Let's summon some unicorns. 🦄")
    
    user_input = input("Do you want to summon a unicorn? (yes/no): ").strip().lower()
    
    if user_input == "yes":
        unicorn_party()
    else:
        print("🚫 No unicorns for you today. Maybe next time!")

if __name__ == "__main__":
    main()

import tkinter as tk
import subprocess
import random
import pandas as pd
from tkinter import messagebox
# Load dataset
music = pd.read_csv("dataset/music.csv")

# Functions

def surprise_me():

    random_song = music.sample(1).iloc[0]

    messagebox.showinfo(

        "🎲 Surprise Me",

        f"""Today's Random Song

🎵 {random_song['song']}

Artist : {random_song['artist']}

Genre : {random_song['genre']}

Try searching this song in the recommendation system!"""

    )
def music_fact():

    facts = [

        "🎵 Music can improve concentration and memory.",

        "🎧 Spotify has over 100 million songs.",

        "🎹 A standard piano has 88 keys.",

        "🎤 Listening to music can reduce stress.",

        "🎸 The guitar has existed for more than 500 years.",

        "🥁 Drums are among the oldest musical instruments.",

        "🎼 Every culture in the world has its own form of music."

    ]

    messagebox.showinfo(

        "🎵 Music Fact",

        random.choice(facts)

    )


def start_project():

    root.destroy()

    subprocess.run(["python", "spotify_gui.py"])


def mood_page():

    subprocess.run(["python","mood.py"])


def about():

    messagebox.showinfo(

        "About Project",

        """Smart Music Recommendation System

Developed using Python and Machine Learning

Algorithm Used:
• CountVectorizer
• Cosine Similarity

Features

• Song Recommendation

• Statistics

• About Page

• Clean GUI

Future Scope

• Spotify API

• Playlist Generator

• Mood Detection"""

    )



# Window

root = tk.Tk()

root.title("Smart Music Recommendation System")

root.geometry("700x700")

root.configure(bg="#121212")

root.resizable(False, False)


# Title


title = tk.Label(

    root,

    text="🎵 Smart Music\nRecommendation System",

    font=("Segoe UI",24,"bold"),

    fg="white",

    bg="#121212"

)

title.pack(pady=40)


# Subtitle


subtitle = tk.Label(

    root,

    text="Machine Learning Mini Project",

    font=("Segoe UI",14),

    fg="#bbbbbb",

    bg="#121212"

)

subtitle.pack()


# Buttons


start_btn = tk.Button(

    root,

    text="▶ Start Project",

    font=("Segoe UI",14,"bold"),

    bg="#1DB954",

    fg="white",

    width=20,

    command=start_project

)

start_btn.pack(pady=35)




mood_btn = tk.Button(

    root,

    text="😊 Mood Recommendation",

    font=("Segoe UI",12,"bold"),

    bg="#27ae60",

    fg="white",

    width=20,

    command=mood_page

)

mood_btn.pack(pady=8)


about_btn = tk.Button(

    root,

    text="About",

    font=("Segoe UI",12,"bold"),

    bg="#0984e3",

    fg="white",

    width=20,

    command=about

)

about_btn.pack(pady=10)
surprise_btn = tk.Button(

    root,

    text="🎲 Surprise Me",

    font=("Segoe UI",12,"bold"),

    bg="#f39c12",

    fg="white",

    width=20,

    command=surprise_me

)

surprise_btn.pack(pady=8)
fact_btn = tk.Button(

    root,

    text="🎵 Music Facts",

    font=("Segoe UI",12,"bold"),

    bg="#8e44ad",

    fg="white",

    width=20,

    command=music_fact

)

fact_btn.pack(pady=8)

exit_btn = tk.Button(

    root,

    text="Exit",

    font=("Segoe UI",12,"bold"),

    bg="#d63031",

    fg="white",

    width=20,

    command=root.destroy

)

exit_btn.pack(pady=10)

footer = tk.Label(

    root,

    text="Developed by Vaishnavi",

    bg="#121212",

    fg="#888888",

    font=("Segoe UI",10)

)

footer.pack(side="bottom", pady=15)


root.mainloop()
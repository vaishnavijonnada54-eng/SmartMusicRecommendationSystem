import tkinter as tk
from tkinter import ttk
import pandas as pd

music = pd.read_csv("dataset/music.csv")
music = music.fillna("")
print(music.head())
print(music["mood"].unique())

root = tk.Tk()
root.title("Mood Recommendation")
root.geometry("700x700")
root.configure(bg="#121212")

title = tk.Label(
    root,
    text="😊 Mood Recommendation",
    font=("Segoe UI",22,"bold"),
    bg="#121212",
    fg="white"
)

title.pack(pady=20)

tk.Label(
    root,
    text="Choose your mood",
    bg="#121212",
    fg="white",
    font=("Segoe UI",13)
).pack()

moods = [
    "Happy",
    "Workout",
    "Romantic",
    "Calm",
    "Sad",
    "Party"
]

mood = ttk.Combobox(
    root,
    values=moods,
    state="readonly",
    width=20
)

mood.current(0)
mood.pack(pady=10)
results = tk.Text(
    root,
    width=60,
    height=15,
    font=("Segoe UI",11)
)


def recommend():

    selected = mood.get()

    print("Selected mood:", selected)

    songs = music[music["mood"] == selected]

    print("Songs found:", len(songs))

    results.delete("1.0", tk.END)

    for _, row in songs.iterrows():
        results.insert(
            tk.END,
            f"🎵 {row['song']}\n"
            f"👤 {row['artist']}\n"
            f"🎼 {row['genre']}\n\n"
        )

button = tk.Button(
    root,
    text="Get Recommendations",
    command=recommend,
    bg="#1DB954",
    fg="white",
    font=("Segoe UI",12,"bold")
)

button.pack(pady=10)

results.pack(pady=20)


"""def recommend():

    results.delete("1.0",tk.END)

    selected = mood.get()

    songs = music[music["mood"]==selected]

    for _,row in songs.head(15).iterrows():

        results.insert(
            tk.END,
            f"🎵 {row['song']}\n"
            f"👤 {row['artist']}\n"
            f"🎼 {row['genre']}\n\n"
        )
def recommend():

    selected = mood.get()

    print("Selected mood:", selected)

    songs = music[music["mood"] == selected]

    print("Songs found:", len(songs))

    results.delete("1.0", tk.END)

    for _, row in songs.iterrows():
        results.insert(
            tk.END,
            f"{row['song']} - {row['artist']} - {row['genre']}\n"
        )"""

tk.Button(
    root,
    text="Get Recommendations",
    command=recommend,
    bg="#1DB954",
    fg="white",
    font=("Segoe UI",12,"bold")
).pack()

root.mainloop()
import tkinter as tk
from tkinter import messagebox
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#Dataset Loading
music = pd.read_csv("dataset/music.csv")

music["features"] = (
    music["song"] + " " +
    music["artist"] + " " +
    music["genre"]
)

cv = CountVectorizer()
matrix = cv.fit_transform(music["features"])
similarity = cosine_similarity(matrix)

#Recommendation Function
def recommend():

    song = entry.get().lower()

    songs = music["song"].str.lower()

    if song not in songs.values:
        messagebox.showerror("Error", "Song not found!")
        return

    index = songs[songs == song].index[0]

    distances = list(enumerate(similarity[index]))

    sorted_songs = sorted(
        distances,
        key=lambda x: x[1],
        reverse=True
    )

    result.delete(1.0, tk.END)

    result.insert(tk.END, "Recommended Songs\n\n")

    count = 0

    for i in sorted_songs[1:]:

        song_name = music.iloc[i[0]]["song"]
        artist = music.iloc[i[0]]["artist"]

        result.insert(
            tk.END,
            f"{count+1}. {song_name} - {artist}\n"
        )

        count += 1

        if count == 5:
            break

#GUI

root = tk.Tk()

root.title("Music Recommendation System")
root.geometry("650x500")
root.configure(bg="#1e1e2f")

title = tk.Label(
    root,
    text="🎵 Music Recommendation System",
    font=("Arial", 20, "bold"),
    bg="#1e1e2f",
    fg="white"
)

title.pack(pady=20)

label = tk.Label(
    root,
    text="Enter Song Name",
    font=("Arial", 13),
    bg="#1e1e2f",
    fg="white"
)

label.pack()

entry = tk.Entry(
    root,
    width=35,
    font=("Arial", 14)
)

entry.pack(pady=10)

button = tk.Button(
    root,
    text="Recommend",
    font=("Arial", 13, "bold"),
    bg="#00b894",
    fg="white",
    padx=15,
    pady=5,
    command=recommend
)

button.pack(pady=15)

result = tk.Text(
    root,
    width=50,
    height=12,
    font=("Arial", 12)
)

result.pack(pady=20)

root.mainloop()
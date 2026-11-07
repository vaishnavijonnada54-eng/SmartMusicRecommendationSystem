import tkinter as tk
import subprocess
import sys
import os
from tkinter import ttk, messagebox
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity



# WINDOW


root = tk.Tk()
root.title("Music Recommendation System")

width = 1000
height = 700

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width - width) // 2
y = (screen_height - height) // 2

root.geometry(f"{width}x{height}+{x}+{y}")

root.configure(bg="#121212")
root.resizable(False, False)



# FONTS


TITLE_FONT = ("Segoe UI", 24, "bold")
LABEL_FONT = ("Segoe UI", 12)
BUTTON_FONT = ("Segoe UI", 11, "bold")
TEXT_FONT = ("Segoe UI", 11)


# MACHINE LEARNING MODEL


music = pd.read_csv("dataset/music.csv")

music["features"] = (
    music["song"] + " " +
    music["artist"] + " " +
    music["genre"]
)

cv = CountVectorizer()

matrix = cv.fit_transform(music["features"])

similarity = cosine_similarity(matrix)


# RECOMMENDATION FUNCTION


def recommend():

    song = entry.get().strip().lower()

    result_box.delete(1.0, tk.END)
    status.config(text="🔍 Searching...")

    songs = music["song"].str.lower()

    if song == "":
        messagebox.showwarning(
            "Empty",
            "Please enter a song name."
        )
        return

    if song not in songs.values:
        messagebox.showerror(
            "Not Found",
            "Song not found in database."
        )
        return

    index = songs[songs == song].index[0]

    distances = list(enumerate(similarity[index]))

    sorted_songs = sorted(
        distances,
        key=lambda x: x[1],
        reverse=True
    )

    result_box.insert(
        tk.END,
        "🎧 Top Recommendations\n\n"
    )

    count = 1

    for i in sorted_songs[1:]:

        song_name = music.iloc[i[0]]["song"]

        artist = music.iloc[i[0]]["artist"]

        genre = music.iloc[i[0]]["genre"]

        result_box.insert(
            tk.END,
            f"🎵 {song_name}\n"
        )

        result_box.insert(
            tk.END,
            f"   👤 {artist}\n"
        )

        result_box.insert(
            tk.END,
            f"   🎼 {genre}\n"
        )

        result_box.insert(
            tk.END,
            "\n────────────────────────────\n\n"
        )

        count += 1

        if count > 5:
            break

    status.config(text="✅ 5 Recommendations Found")



# TITLE


title = tk.Label(
    root,
    text="🎵 Music Recommendation System",
    bg="#121212",
    fg="white",
    font=TITLE_FONT
)

title.pack(pady=20)



# SEARCH FRAME


search_frame = tk.Frame(
    root,
    bg="#121212"
)

search_frame.pack(pady=10)


label = tk.Label(
    search_frame,
    text="Search Song",
    bg="#121212",
    fg="white",
    font=LABEL_FONT
)

label.grid(
    row=0,
    column=0,
    padx=10
)


entry = tk.Entry(
    search_frame,
    width=35,
    font=("Segoe UI", 13)
)

entry.grid(
    row=0,
    column=1,
    padx=10
)


entry.bind(
    "<Return>",
    lambda event: recommend()
)


recommend_btn = tk.Button(
    search_frame,
    text="Recommend",
    bg="#1DB954",
    fg="white",
    font=BUTTON_FONT,
    width=14,
    command=recommend
)

recommend_btn.grid(
    row=0,
    column=2,
    padx=10
)



# RECOMMENDATION AREA


result_frame = tk.Frame(
    root,
    bg="#1E1E1E",
    bd=2,
    relief="ridge",
    height=430
)

# IMPORTANT:
# Prevent Tkinter from changing the requested height
result_frame.pack_propagate(False)

result_frame.pack(
    pady=15,
    padx=25,
    fill="x"
)


heading = tk.Label(
    result_frame,
    text="Recommendations",
    bg="#1E1E1E",
    fg="white",
    font=("Segoe UI", 16, "bold")
)

heading.pack(pady=15)


scrollbar = tk.Scrollbar(
    result_frame
)

scrollbar.pack(
    side="right",
    fill="y"
)


result_box = tk.Text(
    result_frame,
    font=TEXT_FONT,
    bg="#252525",
    fg="white",
    insertbackground="white",
    yscrollcommand=scrollbar.set,
    relief="flat"
)

result_box.pack(
    fill="both",
    expand=True,
    padx=15,
    pady=10
)


scrollbar.config(
    command=result_box.yview
)



# STATUS

status = tk.Label(
    root,
    text="🟢 Ready",
    bg="#181818",
    fg="white",
    font=("Segoe UI", 10),
    anchor="w",
    padx=15
)

status.pack(
    fill="x",
    side="bottom"
)


# BOTTOM FRAME


bottom_frame = tk.Frame(
    root,
    bg="#121212"
)

bottom_frame.pack(
    fill="x",
    pady=5,
    side="bottom"
)



# CLEAR FUNCTION

def clear():

    entry.delete(
        0,
        tk.END
    )

    status.config(
        text="🟢 Ready"
    )

    result_box.delete(
        1.0,
        tk.END
    )


clear_btn = tk.Button(
    bottom_frame,
    text="Clear",
    bg="#444444",
    fg="white",
    font=BUTTON_FONT,
    width=12,
    command=clear
)

clear_btn.pack(
    side="left",
    padx=20
)



# ABOUT

def about():

    messagebox.showinfo(
        "About",
        "Music Recommendation System\n\n"
        "Machine Learning Project\n"
        "Algorithm : Content-Based Recommendation\n"
        "Similarity : Cosine Similarity\n"
    )


about_btn = tk.Button(
    bottom_frame,
    text="About",
    bg="#0984e3",
    fg="white",
    font=BUTTON_FONT,
    width=12,
    command=about
)

about_btn.pack(
    side="left",
    padx=15
)



# MOOD RECOMMENDATION


def open_mood_recommendation():

    mood_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "mood.py"
    )

    subprocess.Popen(
        [sys.executable, mood_path]
    )


mood_btn = tk.Button(
    bottom_frame,
    text="😊 Mood",
    bg="#e84393",
    fg="white",
    font=BUTTON_FONT,
    width=12,
    command=open_mood_recommendation
)

mood_btn.pack(
    side="left",
    padx=15
)



# EXIT


exit_btn = tk.Button(
    bottom_frame,
    text="Exit",
    bg="#d63031",
    fg="white",
    font=BUTTON_FONT,
    width=12,
    command=root.destroy
)

exit_btn.pack(
    side="right",
    padx=20
)



# STATISTICS


def stats():

    totalSongs = len(music)

    totalArtists = music["artist"].nunique()

    totalGenres = music["genre"].nunique()

    messagebox.showinfo(
        "Dataset Statistics",

        f"""
Total Songs : {totalSongs}

Artists : {totalArtists}

Genres : {totalGenres}
"""
    )


stats_btn = tk.Button(
    bottom_frame,
    text="Statistics",
    bg="#6c5ce7",
    fg="white",
    font=BUTTON_FONT,
    width=12,
    command=stats
)

stats_btn.pack(
    side="right",
    padx=15
)



# BUTTON HOVER EFFECTS


def on_enter(e):

    if e.widget == recommend_btn:
        e.widget["background"] = "#27ae60"

    elif e.widget == clear_btn:
        e.widget["background"] = "#555555"

    elif e.widget == about_btn:
        e.widget["background"] = "#2980b9"

    elif e.widget == stats_btn:
        e.widget["background"] = "#7d6ee8"

    elif e.widget == exit_btn:
        e.widget["background"] = "#e74c3c"

    elif e.widget == mood_btn:
        e.widget["background"] = "#fd79a8"


def on_leave(e):

    if e.widget == recommend_btn:
        e.widget["background"] = "#1DB954"

    elif e.widget == clear_btn:
        e.widget["background"] = "#444444"

    elif e.widget == about_btn:
        e.widget["background"] = "#0984e3"

    elif e.widget == stats_btn:
        e.widget["background"] = "#6c5ce7"

    elif e.widget == exit_btn:
        e.widget["background"] = "#d63031"

    elif e.widget == mood_btn:
        e.widget["background"] = "#e84393"


recommend_btn.bind(
    "<Enter>",
    on_enter
)

recommend_btn.bind(
    "<Leave>",
    on_leave
)

clear_btn.bind(
    "<Enter>",
    on_enter
)

clear_btn.bind(
    "<Leave>",
    on_leave
)

about_btn.bind(
    "<Enter>",
    on_enter
)

about_btn.bind(
    "<Leave>",
    on_leave
)

stats_btn.bind(
    "<Enter>",
    on_enter
)

stats_btn.bind(
    "<Leave>",
    on_leave
)

exit_btn.bind(
    "<Enter>",
    on_enter
)

exit_btn.bind(
    "<Leave>",
    on_leave
)

mood_btn.bind(
    "<Enter>",
    on_enter
)

mood_btn.bind(
    "<Leave>",
    on_leave
)



# MENU BAR


menu_bar = tk.Menu(root)


# File Menu

file_menu = tk.Menu(
    menu_bar,
    tearoff=0
)

file_menu.add_command(
    label="Clear Search",
    command=clear
)

file_menu.add_separator()

file_menu.add_command(
    label="Exit",
    command=root.destroy
)

menu_bar.add_cascade(
    label="File",
    menu=file_menu
)


# Help Menu

help_menu = tk.Menu(
    menu_bar,
    tearoff=0
)

help_menu.add_command(
    label="About",
    command=about
)

help_menu.add_command(
    label="Statistics",
    command=stats
)

menu_bar.add_cascade(
    label="Help",
    menu=help_menu
)


root.config(
    menu=menu_bar
)



# START APPLICATION

root.mainloop()
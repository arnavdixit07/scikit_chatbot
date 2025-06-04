import tkinter as tk
from tkinter import Canvas
from tkinter import ttk
import threading
import time

from AI import predict_intent, responses  # type: ignore

# --- Theming ---
BG_COLOR = "#1a1a2e"
USER_BUBBLE = "#0f3460"
BOT_BUBBLE = "#16213e"
TEXT_COLOR = "#eaeaea"
ENTRY_BG = "#0f3460"
BUTTON_BG = "#533483"
BUTTON_HOVER = "#6c4cc4"
TYPING_COLOR = "#9ca3af"

FONT = ("Segoe UI", 11)
BUBBLE_RADIUS = 20

# --- Initialize App Window ---
root = tk.Tk()
root.title("🤖 Arnav's ChatBot")
root.geometry("600x650")
root.configure(bg=BG_COLOR)

# --- Chat Frame with Canvas Scroll ---
frame = tk.Frame(root, bg=BG_COLOR)
frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

canvas = Canvas(frame, bg=BG_COLOR, highlightthickness=0)
scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg=BG_COLOR)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"), yscrollincrement=10)
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# --- Chat Bubble Generator ---
def create_bubble(master, text, is_user):
    outer = tk.Frame(master, bg=BG_COLOR)
    outer.pack(anchor="e" if is_user else "w", pady=4, padx=5, fill=tk.X)

    bubble = tk.Label(
        outer,
        text=text,
        bg=USER_BUBBLE if is_user else BOT_BUBBLE,
        fg=TEXT_COLOR,
        font=FONT,
        wraplength=400,
        justify="left",
        anchor="w",
        padx=14,
        pady=8,
        bd=0,
        relief="flat"
    )
    bubble.pack(
        anchor="e" if is_user else "w",
        ipadx=8,
        ipady=2,
        padx=10,
    )

    # Rounded corners
    bubble.config(highlightbackground=BG_COLOR)
    bubble.after(10, lambda: bubble.config(highlightthickness=0))

# --- Typing Indicator ---
typing_label = tk.Label(
    scrollable_frame,
    text="Chatbot is typing...",
    fg=TYPING_COLOR,
    bg=BG_COLOR,
    font=(FONT[0], 10, "italic")
)

def show_typing():
    typing_label.pack(anchor="w", padx=15)
    canvas.yview_moveto(1.0)

def hide_typing():
    typing_label.pack_forget()

# --- Entry and Send Button Area ---
bottom_frame = tk.Frame(root, bg=BG_COLOR)
bottom_frame.pack(fill=tk.X, padx=10, pady=12)

entry_field = tk.Entry(
    bottom_frame,
    font=(FONT[0], 12),
    bg=ENTRY_BG,
    fg=TEXT_COLOR,
    insertbackground=TEXT_COLOR,
    relief=tk.FLAT,
    bd=8
)
entry_field.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=8, padx=(0, 12))

send_button = tk.Button(
    bottom_frame,
    text="Send",
    bg=BUTTON_BG,
    fg=TEXT_COLOR,
    activebackground=BUTTON_HOVER,
    font=(FONT[0], 11, "bold"),
    padx=20,
    pady=6,
    relief=tk.FLAT,
    cursor="hand2"
)
send_button.pack(side=tk.RIGHT)

# Hover effect for button
def on_enter(e): send_button.config(bg=BUTTON_HOVER)
def on_leave(e): send_button.config(bg=BUTTON_BG)

send_button.bind("<Enter>", on_enter)
send_button.bind("<Leave>", on_leave)

# --- Message Handling ---
def send_message():
    user_input = entry_field.get().strip()
    if not user_input:
        return
    entry_field.delete(0, tk.END)
    create_bubble(scrollable_frame, user_input, is_user=True)

    if user_input.lower() in ["exit", "quit"]:
        create_bubble(scrollable_frame, "Goodbye! 👋", is_user=False)
        root.after(1000, root.destroy)
        return

    threading.Thread(target=generate_response, args=(user_input,)).start()

def generate_response(user_input):
    show_typing()
    time.sleep(1.2)
    intent = predict_intent(user_input)
    response = responses.get(intent, "Sorry, I didn't understand that.")
    hide_typing()
    create_bubble(scrollable_frame, response, is_user=False)
    canvas.yview_moveto(1.0)

# --- Event Bindings ---
send_button.config(command=send_message)
root.bind("<Return>", lambda event: send_message())

# --- Run App ---
root.mainloop()

import tkinter as tk
from tkinter import scrolledtext
import requests

# === Configuration ===
WEBHOOK_URL = "https://eo50ibp0mhwd3eq.m.pipedream.net"  # <-- Replace this with your actual webhook or API URL
USE_JSON = True  # Set to False if the API expects form data instead

# === GUI Setup ===
root = tk.Tk()
root.title("Send me a message!")
root.geometry("400x300")

output_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10, state='disabled')
output_box.pack(pady=10)

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

# === Send Button Logic ===
def send_message():
    message = entry.get()
    if not message.strip():
        return

    # Send to webhook/API
    try:
        if USE_JSON:
            response = requests.post(WEBHOOK_URL, json={"content": message})
        else:
            response = requests.post(WEBHOOK_URL, data={"content": message})

        output_box.configure(state='normal')
        if response.ok:
            output_box.insert(tk.END, f"✅ Sent: {message}\n")
        else:
            output_box.insert(tk.END, f"❌ Error {response.status_code}: {response.text}\n")
        output_box.configure(state='disabled')
        output_box.see(tk.END)

    except Exception as e:
        output_box.configure(state='normal')
        output_box.insert(tk.END, f"⚠️ Exception: {e}\n")
        output_box.configure(state='disabled')

    entry.delete(0, tk.END)

# === Button ===
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=5)

root.mainloop()

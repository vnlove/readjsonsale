import tkinter as tk
import pyautogui
import time


def close_all_chrome_windows():
    # Lấy danh sách tiêu đề của tất cả các cửa sổ đang chạy
    window_titles = pyautogui.getAllTitles()

    # Kiểm tra từng tiêu đề
    for title in window_titles:
        # Kiểm tra xem tiêu đề có chứa từ "Google Chrome" không
        if "Google Chrome" in title:
            # Nếu có, tìm cửa sổ bằng tiêu đề
            chrome_window = pyautogui.getWindowsWithTitle(title)[0]
            # Đóng cửa sổ
            chrome_window.close()
            time.sleep(0.5)  # Đợi cửa sổ đóng


# Tạo giao diện tkinter
root = tk.Tk()
root.title("CLOSE ALL CHROME WINDOWS")

# Tạo nút "CLOSE"
button_close = tk.Button(root, text="CLOSE", command=close_all_chrome_windows)
button_close.pack()

# Chạy giao diện
root.mainloop()

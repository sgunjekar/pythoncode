from pywinauto import Application
from datetime import datetime, timedelta
import os
import time

EXPORT_DIR = r"C:\DiaryExports"
START_DATE = datetime(2023, 1, 1)
END_DATE = datetime(2023, 1, 3)

os.makedirs(EXPORT_DIR, exist_ok=True)

# Attach to running iDailyDiary instance
app = Application(backend="win32").connect(title="Diary - [Diary]")

# Focus the window
diary = app.window(title="Diary - [Diary]")
diary.set_focus()
time.sleep(1)

current_date = START_DATE
while current_date <= END_DATE:
    print(f"📅 Exporting: {current_date.strftime('%Y-%m-%d')}")

    # Navigate to date
    diary.type_keys("^g")  # Ctrl+G opens date selector
    time.sleep(1)
    diary.type_keys(current_date.strftime("%d/%m/%Y") + "{ENTER}")
    time.sleep(1)

    # Export via File menu
    diary.menu_select("File->Export->Entry...")
    time.sleep(2)

    # Export dialog
    export_dlg = app.window(title_re="Export Diary Entry.*")
    export_path = os.path.join(EXPORT_DIR, f"{current_date.strftime('%Y-%m-%d')}.txt")
    export_dlg['Edit'].set_text(export_path)
    export_dlg['Save'].click()
    time.sleep(1)

    current_date += timedelta(days=1)

print("✅ Export complete.")

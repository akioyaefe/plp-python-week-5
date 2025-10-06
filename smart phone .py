# ===========================
# PARENT CLASS: Device
# ===========================
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.power_status = False
    
    def power_on(self):
        if not self.power_status:
            self.power_status = True
            print(f"{self.brand} {self.model} is now ON.")
        else:
            print(f"{self.brand} {self.model} is already ON.")

    def power_off(self):
        if self.power_status:
            self.power_status = False
            print(f"{self.brand} {self.model} is now OFF.")
        else:
            print(f"{self.brand} {self.model} is already OFF.")


# ===========================
# CHILD CLASS: Smartphone
# ===========================
class Smartphone(Device):
    def __init__(self, brand, model, os, storage, battery=100):
        super().__init__(brand, model)
        self.__os = os             # Encapsulated attribute
        self.storage = storage     # Public attribute
        self.battery = battery     # Battery level (%)
        self.messages = []         # Store sent messages
    
    # Getter and Setter for OS
    def get_os(self):
        return self.__os

    def set_os(self, new_os):
        self.__os = new_os
        print(f"OS updated to {self.__os} ✅")

    # Show specifications
    def show_specs(self):
        print(f"\n📱 Smartphone Details:")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"OS: {self.__os}")
        print(f"Storage: {self.storage}GB")
        print(f"Battery: {self.battery}%")

    # Battery control
    def charge(self, amount):
        if amount < 0:
            print("❌ Invalid charge amount.")
            return
        self.battery = min(100, self.battery + amount)
        print(f"🔋 Charged! Battery is now {self.battery}%")

    def use_battery(self, amount):
        self.battery = max(0, self.battery - amount)
        if self.battery == 0:
            print("⚠️ Battery empty! Please charge your phone.")
        else:
            print(f"🔋 Battery remaining: {self.battery}%")

    # Communication
    def call(self, contact):
        if self.battery <= 5:
            print("⚠️ Not enough battery to make a call.")
            return
        print(f"📞 Calling {contact} using {self.brand} {self.model}...")
        self.use_battery(5)

    def send_message(self, contact, message):
        if self.battery <= 3:
            print("⚠️ Not enough battery to send a message.")
            return
        self.messages.append((contact, message))
        print(f"💬 Message sent to {contact}: '{message}'")
        self.use_battery(3)

    def view_messages(self):
        if not self.messages:
            print("📭 No messages yet.")
        else:
            print("\n💬 Message History:")
            for i, (contact, msg) in enumerate(self.messages, 1):
                print(f"{i}. To {contact}: {msg}")

    # Camera
    def take_photo(self, subject="a moment"):
        if self.battery <= 2:
            print("⚠️ Battery too low to take a photo.")
            return
        print(f"📸 You took a photo of {subject}.")
        self.use_battery(2)

    # App launcher simulation (polymorphism idea)
    def open_app(self, app_name):
        print(f"📲 Launching {app_name} app...")
        self.use_battery(4)

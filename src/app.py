from main import chatroom_main
import sys

print("=" * 40)
print("|| === SECURE CHATROOM === ||")
print("|| ===     v1.0.0      === ||")
print("=" * 40)

print("\n1. Launch Chatroom")
print("2. Exit")

choice = input("> ")

if choice == "1":
    chatroom_main()
elif choice == "2":
    print("Exiting...")
    sys.exit()

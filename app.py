import time

def main():
    print("==========================================")
    print("      C2C ELITE 101: LAUNCH CONSOLE       ")
    print("==========================================")
    
    user_name = input("Enter Commander Name: ")
    print(f"Welcome, Commander {user_name}. Systems initialized.")
    
    destination = input("Enter target mission destination: ")
    print(f"Coordinates locked for: {destination}")
    
    input("Press ENTER to authorize launch sequence...")
    
    for i in range(5, 0, -1):
        print(f"T-minus {i}...")
        time.sleep(1)
    
    print("🚀 LAUNCH SUCCESSFUL! Mission in progress.")

if __name__ == "__main__":
    main()
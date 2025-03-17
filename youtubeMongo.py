import pymongo
from bson import ObjectId

# Connect to MongoDB
client = pymongo.MongoClient(
    "mongodb+srv://youtubepy:youtubepy@cluster0.s5dln.mongodb.net/ytmanager",
    tlsAllowInvalidCertificates=True,
)

db = client["ytmanager"]
vediocollection = db["vedios"]
print(client)

# Color codes
GREEN = "\033[32m"
END = "\033[0m"

banner = f"""
  {GREEN}                   
_____.___.              ___________   ___.               _____                                             
\__  |   | ____  __ __  \__    ___/_ _\_ |__   ____     /     \ _____    ____ _____     ____   ___________ 
 /   |   |/  _ \|  |  \   |    | |  |  \ __ \_/ __ \   /  \ /  \\__  \  /    \\__  \   / ___\_/ __ \_  __ \
 \____   (  <_> )  |  /   |    | |  |  / \_\ \  ___/  /    Y    \/ __ \|   |  \/ __ \_/ /_/  >  ___/|  | \/
 / ______|\____/|____/    |____| |____/|___  /\___  > \____|__  (____  /___|  (____  /\___  / \___  >__|   
 \/                                        \/     \/          \/     \/     \/     \//_____/      \/       
"""
print(banner)

# Functions
def add_vedio(name, time):
    result = vediocollection.insert_one({"name": name, "time": time})
    print(f"Video added with ID: {result.inserted_id}")

def list_all_vedios():
    for vedio in vediocollection.find():
        print(f"ID: {vedio['_id']}, Name: {vedio['name']}, Time: {vedio['time']}")

def Update_vedio(vedio_id, name, time):
    try:
        vediocollection.update_one(
            {"_id": ObjectId(vedio_id)}, {"$set": {"name": name, "time": time}}
        )
        print("Video updated successfully.")
    except Exception as e:
        print("Error updating video:", e)

def Delete_Video(video_id):
    try:
        vediocollection.delete_one({"_id": ObjectId(video_id)})
        print("Video deleted successfully.")
    except Exception as e:
        print("Error deleting video:", e)

def main():
    while True:
        print("\n1. List all videos")
        print("2. Add video")
        print("3. Update video")
        print("4. Delete video")
        print("5. Exit the app")

        choice = input("Enter your choice: ")

        if choice == "1":
            list_all_vedios()
        elif choice == "2":
            Vname = input("Enter video name: ")
            Vtime = input("Enter video time: ")
            add_vedio(Vname, Vtime)
        elif choice == "3":
            Uid = input("Enter video ID to update: ")
            Uname = input("Enter updated name: ")
            Utime = input("Enter updated time: ")
            Update_vedio(Uid, Uname, Utime)
        elif choice == "4":
            video_id = input("Enter video ID to delete: ")
            Delete_Video(video_id)
        elif choice == "5":
            print("Exiting the app...")
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()

import json


def load_data():
    try:
        with open("youtube.txt", "r") as file:
            test = json.load(file)
            #    print(type(test))
            return test
    except FileNotFoundError:
        return []


def save_data_helper(videos):
    with open("youtube.txt", "w") as file:
        json.dump(videos, file)


def list_all_videos(videos):
    print("")
    print("*" * 70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration : {video['time']}")


def add_video(videos):
    name = input("Enter the name of the video: ")
    time = input("Enter the time of the video: ")
    videos.append({"name": name, "time": time})
    save_data_helper(videos)


def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the index of the video to update: ")) - 1
    if 0 <= index < len(videos):
        name = input("Enter the new name of the video: ")
        time = input("Enter the new time of the video: ")
        videos[index - 1 ] = {"name": name, "time": time}
        save_data_helper(videos)
    else:
        print("Invalid index.")



def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the index of the video to delete: "))

    if 1 <= index <= len(videos):
        del videos[index - 1]
        save_data_helper(videos)
    else:
        print("Invalid index.")


def main():
    videos = load_data()
    while True:
        print(" Welcome to the YouTube Video Manager! | Choose an option")
        print("1. List all videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")
        # print(videos)

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                print("Exiting the app...")
                break
            case _:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

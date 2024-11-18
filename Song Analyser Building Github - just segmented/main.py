# main.py
from api import fetch_song_details, search_song

def main():
    # Search for a song based on user input
    search_query = input("Enter Song Name: ")
    results = search_song(search_query)

    # Extract the hits from the results
    hits = results['hits']

    # Display song titles in enumerated form
    if hits:
        print(f"\nFound {len(hits)} songs:\n")
        for i, hit in enumerate(hits):
            song_title = hit['result']['full_title']
            song_id = hit['result']['id']
            print(f"{i + 1}. {song_title} (ID: {song_id})")  
        
    
        # Get user selection
        while True:
            try:
                song_choice = int(input("\nSelect a song by entering its number: ")) - 1
                if 0 <= song_choice < len(hits):
                    selected_song_id = hits[song_choice]['result']['id']
                    print(f"You selected the song with ID: {selected_song_id}")
                    break
                else:
                    print("Invalid selection. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Fetch song details using the selected song ID
        song_details = fetch_song_details(selected_song_id)
        if song_details:
            artist_name = song_details['primary_artist']['name']
            artist_song = song_details['title']
            print(f"{artist_song} by {artist_name}")
            lyrics = genius.search_song(artist_song, artist_name)
            print(lyrics.lyrics)
    else:
        print(f"No songs found for the search query '{search_query}'.")

if __name__ == "__main__":
    main()

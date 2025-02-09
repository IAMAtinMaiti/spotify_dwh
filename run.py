import streamlit as st
import requests
import base64
from configs import Config
config = Config()

# Spotify API credentials
CLIENT_ID = config.get('SECRETS.CLIENT_ID')
CLIENT_SECRET = config.get('SECRETS.CLIENT_SECRET')


def fetch_access_token(client_id, client_secret):
    # Concatenate client ID and client secret
    client_credentials = f"{client_id}:{client_secret}"
    # Encode client credentials in Base64
    encoded_credentials = base64.b64encode(client_credentials.encode()).decode()
    # Define headers
    headers = {
        'Authorization': f'Basic {encoded_credentials}'
    }
    # Define payload
    data = {
        'grant_type': 'client_credentials'
    }
    # Spotify token endpoint
    token_url = 'https://accounts.spotify.com/api/token'
    # Request access token
    response = requests.post(token_url, headers=headers, data=data)
    if response.status_code == 200:
        return response.json()['access_token']
    else:
        return None


def fetch_artist_details(artist_name, access_token):
    # Define Spotify API endpoint for artist search
    artist_search_endpoint = "https://api.spotify.com/v1/search"
    # Define query parameters for artist search
    artist_params = {
        "q": artist_name,
        "type": "artist",
        "limit": 1
    }
    # Define headers with access token
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    # Make the request to Spotify API for artist search
    response = requests.get(artist_search_endpoint, params=artist_params, headers=headers)
    if response.status_code == 200:
        artist_id = response.json()['artists']['items'][0]['id']
        # Define Spotify API endpoint for artist details
        artist_details_endpoint = f"https://api.spotify.com/v1/artists/{artist_id}"
        # Make the request to Spotify API for artist details
        response = requests.get(artist_details_endpoint, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    else:
        return None


def fetch_top_albums(artist_id, access_token):
    # Define Spotify API endpoint for artist's top tracks
    top_albums_endpoint = f"https://api.spotify.com/v1/artists/{artist_id}/albums"
    # Define query parameters for top tracks
    top_albums_params = {
        "limit": 10
    }
    # Define headers with access token
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    # Make the request to Spotify API for top tracks
    response = requests.get(top_albums_endpoint, params=top_albums_params, headers=headers)
    if response.status_code == 200:
        return response.json()['items']
    else:
        return None


def main():
    st.title("Spotify Artist Details")

    # Input field for artist name
    artist_name = st.text_input("Enter artist name:")

    if artist_name:
        # Fetch access token
        access_token = fetch_access_token(CLIENT_ID, CLIENT_SECRET)
        if access_token:
            # Fetch artist details from Spotify API
            artist_details = fetch_artist_details(artist_name, access_token)

            if artist_details:
                # Display artist details
                st.subheader("Artist Details:")
                st.write("Name:", artist_details['name'])
                st.write("Followers:", artist_details['followers']['total'])
                st.write("Genres:", ", ".join(artist_details['genres']))
                st.image(artist_details['images'][0]['url'], caption='Artist Image', use_column_width=True)

                # Fetch top albums of the artist
                top_albums = fetch_top_albums(artist_details['id'], access_token)
                if top_albums:
                    st.subheader("Top 10 Albums:")
                    for album in top_albums:
                        st.write("Name:", album['name'])
                        st.write("Release Date:", album['release_date'])
                        st.image(album['images'][0]['url'], caption='Album Image', use_column_width=True)
                        st.write("---")
                else:
                    st.error("Failed to fetch top albums. Please try again.")
            else:
                st.error("Failed to fetch artist details. Please try again.")
        else:
            st.error("Failed to fetch access token. Please check your credentials.")


if __name__ == "__main__":
    main()

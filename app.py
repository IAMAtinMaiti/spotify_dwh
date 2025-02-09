import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pprint

# Set up your credentials
client_id = '5ba8fc8e1ecd45d59bdb09bc6a01ecba'
client_secret = 'acc32b5847ee4457bcf8c7ab6248af78'

# Initialize Spotipy with your credentials
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Example: Search for an artist
# artist_name = 'Ed Sheeran'
# results = sp.search(q='artist:' + artist_name, type='artist')
# artist = results['artists']['items'][0]

# Get artist's ID
# artist_id = artist['id']

# Get artist's information including followers
artist_info = sp.track("6PCUP3dWmTjcTtXY02oFdT", "US")

# user_info = sp.user("259b2qh7yg5yvjgkg2fxlvi29")
#
# # Get a sample of followers' countries
# # followers_countries = sp.artist_followers(artist_id)['countries']
# #
# # print("Sample of followers' countries:", followers_countries)
pprint.pprint(artist_info)

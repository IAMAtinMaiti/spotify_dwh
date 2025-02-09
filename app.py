import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pprint
from configs import Config
config = Config()

# Set up your credentials
CLIENT_ID = config.get('SECRETS.CLIENT_ID')
CLIENT_SECRET = config.get('SECRETS.CLIENT_SECRET')

# Initialize Spotipy with your credentials
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Example: Search for an artist
# artist_name = 'Ed Sheeran'
# results = sp.search(q='artist:' + artist_name, type='artist')
# artist = results['artists']['items'][0]

# Get artist's ID
# artist_id = artist['id']

#Get artist's information including followers
# artist_info = sp.track("6PCUP3dWmTjcTtXY02oFdT", "US")
# pprint.pprint(artist_info)


# user_info = sp.user("259b2qh7yg5yvjgkg2fxlvi29")
#
# # Get a sample of followers' countries
# # followers_countries = sp.artist_followers(artist_id)['countries']
# #
# # print("Sample of followers' countries:", followers_countries)


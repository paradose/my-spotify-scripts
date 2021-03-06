from discover_script import DiscoverWeeklySaver
from auth import spotify_user_id, discover_weekly_id, discover_playlist_id

discover_weekly_token = DiscoverWeeklySaver(spotify_user_id, discover_playlist_id, discover_weekly_id)
discover_weekly_token.call_refresh()
discover_weekly_token.find_discovered_songs()
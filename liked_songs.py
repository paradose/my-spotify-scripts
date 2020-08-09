from discover_script import DiscoverWeeklySaver
from auth import spotify_user_id, discover_weekly_id, discover_playlist_id

new_task = DiscoverWeeklySaver(spotify_user_id, discover_playlist_id, discover_weekly_id)
new_task.call_refresh()
new_task.find_liked_discovered()

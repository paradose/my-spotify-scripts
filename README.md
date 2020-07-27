## Spotify Automation
So atm, this only works for my personal account (why ive left out all the token information) but for more information on how to setup refresh tokens look at https://developer.spotify.com/documentation/web-api/

### discover-script.py
I've been recently bothered @ how the discover playlist just gets refreshed and theres no way to look at past suggestions hence why this script can:
- add 'liked' songs in Discover Weekly to a playlist
- add all Discover Weekly songs to a single playlist

*all scheduled weekly before the Discover Weekly playlist gets refreshed

### to-dos
- [ ] documenting
- [ ] refactoring discover-script.py
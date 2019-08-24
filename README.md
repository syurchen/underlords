# Dota Underlords Helper
Email me(leprosy93 at gmail.com) if you are interesting in coding or helping me with probability theory!

Known limitations/bugs:
- Working only with between-rounds scoreboard (program needs player name to be white to detect it)
- Slow processing
- Working only with 16:9 (preferable 1080p)
- Some heroes are bugged. Program keeps finding them in empty spaces
- No UI
- Not counting blacklist (units that are shown at shop to player and opponents)
- No image for level 9
- Not detecting player gold

Plans:
- [x] Storing results in DB, so they can be accesed later
- [x] Adding queue system (added a bad db-based one)
- [X] Not relevant pictures are not parsed at all and freeze worker
- [ ] Implement blackist correctly
- [ ] Fixing bugged heroes
- [x] Using https://github.com/odota/underlordsconstants for hero data

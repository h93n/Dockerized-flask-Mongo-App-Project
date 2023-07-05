film catching application

Service that enables programmatic access via the internet to a database of images (movie posters). The database is based on MongoDB and stores movie files and information about the files (movie title, IMDB code, etc.). The software is based on Flask. Both the software and the database should be "wrapped in containers",we used docker-compose.

The software should implement the following options as a web API:

Search for a poster in the database (returns an image file). If the poster is not found in the database, the search should be redirected to TMDB.
Delete a poster from the database.
Update information about a poster.
Additionally, the software should allow searching using an HTML form accessible through a web browser.

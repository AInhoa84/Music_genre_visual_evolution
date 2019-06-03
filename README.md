# MUSIC GENRE: A VISUAL EVOLUTION - INSTRUCTIONS


**<u>1 - Technical requirements</u>**

Anaconda virtual environment with Python 3.7 and the following libraries/packages:

    - pandas & numpy
    - pygeocoder (pip install pygeocoder) & Google Maps API key *
    - time
    - tqdm
    - warnings
    - seaborn
    - matplotlib
    - reverse_geocoder (pip install reverse geocoder)
    - re
    - datetime
    - wikipedia (pip install wikipedia)
    - requests
    - json
    - pycountry

*The API key is not required if you don't intend to geocode the locations. The geocoded locations file will be provided.

**<u>2 - Data folders</u>**

Once you've downloaded/cloned the repository in your PC, download the two data folders (Data_in & Data_out) from XXXX and extract them into the repository folder.

**<u>3 - Notebook's order</u>**

In order to follow the whole process, there is a specific order to execute the notebooks:

1) Areas_Musicbrainz: this notebook prepares the area codes from Musicbrainz database and the resulting file is used in the next notebook.
2) Data_gathering_releases_origin: this notebook retrieves the origin for each release. The resulting file is used in the next notebook.
3) Data_gathering_music_genre: this notebook takes as input the output from the previous notebook and focuses on the music genre for each release.
4) Wikipedia_artist_information_retrieval: this is an auxiliary notebook. It assists notebooks 2 & 3 in their final steps.
5) Data analysis: this notebook analyzes the final dataframe and formats it before loading it with the visual tool.

**<u>4 -Frontend </u>**


**<u>5 -Project summary/conclusions </u>**


**<u>6 -Credits </u>**

This project is based mainly in MusicBrainz's database. It has been complemented by The Million Song Dataset, Wikidata and Wikipedia. The music genre list has been inspired from https://www.musicgenreslist.com/ and MusicBrainz's genre list.

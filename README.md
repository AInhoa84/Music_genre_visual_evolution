# MUSIC GENRE: A VISUAL EVOLUTION


Welcome to my first Data Science project!

This Data Science project is a data gathering challenge. In order to make the initial idea possible, many data sources and different tools were used to get the right amount of data and in a suitable format. 

This documents sums up in a very brief way all the work done. In order to really understand the different steps it's advised to look at the notebooks and Python scripts.

The main goal of this project was to show, in an interactive map, how the different music genres evolved over time and geography: where they started, and how they expanded over the years.

There are many websites/articles which explain the evolution of the different music genres over time, but they mainly focused on the relationships between genres and how the combination of some of them led to the inception of new ones. Only a few ones introduced the geographical factor and used it to make a visualization, but, as far as I have seen, they are limited to the US territory. 

A few online music databases were analyzed and tested (this process took about a month), before deciding that MusicBrainz would be the main data source for this project. MusicBrainz database seemed very complete and up-to-date and there were enough tables and records to retrieve:

- Music releases
- Their year
- Their author's origin
- Their main genre

The details about their database schema can be found at: https://beta.musicbrainz.org/doc/MusicBrainz_Database/Schema.

## PROCESS DESCRIPTION

You can see below the main steps that have been followed to retrieve all the data for each release:

### 1) Release year:

In order to select the first time a release was issued, a combination of the tables "release" & "release_country" was done (that last table provides us with the year and also the country). For each release group, only the earliest release_id was kept.

All the releases without year information were discarded, as there was already enough data (130 years of history).

### 2) Release origin:

The artist's origin was chosen as the geographical reference for each release, instead of the release production's location. The coordinates for each location were also retrieved, to be able to visualize it afterwards.

MusicBrainz's "artist" table was the main table for this part, especially the fields "start area 1" and "start area 2". The details about each area were merged with the artists table, including coordinates. Once the origins were retrieved for each artist, that information was extended to each release.

For all the releases or artists that had an unknown origin, the following complementary sources of information were used:

- Some tables from The Million Song Dataset
- Data from Wikidata Query
- Data from Wikipedia API

A total of 617.096 releases with origin were retrieved in this first step.

### 3) Release genre:

MusicBrainz uses their tag system to identify the music genre of each artist/release group: they consider that some of their tags are genres (https://beta.musicbrainz.org/genres).

As the intention was to show the evolution of the main music genres/categories, I manually classified MusicBrainz's genres and a complementary list of other possible tags/subgenres found in https://www.musicgenreslist.com/ into 14 categories that I wanted to focus on:

- Blues
- Classical
- Country
- Electronic
- Folk
- Hip Hop
- Jazz
- Latin
- Pop
- Punk
- Rythm & Blues (R&B) / Soul
- Rock
- World (local music genres from specific regions of the world)
- Others (This category contains all the subgenres I haven't been able to classify in the previous categories)

Of course, I wasn't familiar with all the genres appearing in the list so, in order to classify those, I looked at their definition online and chose the best main genre for them. If no definition was found, I searched for a representative song and listened to it in order to make a decision.

Once they were classified, MusicBrainz's "tags" table was used to identify, for each tag, its Main category/genre. Many tags weren't considered as subgenres (and therefore hadn't any Main genre assigned) but they did contain some words that could help identify their Main category. 

To do so, a pattern of words that could be assigned to each Main genre was used.

Once the tags were associated with their Main genre, the information was merged into the releases table. As each release and/or artist could have many tags associated with them, in order to be as objective as possible, only the tags whose number of counts was higher was kept. That way, the criteria of the majority of users who had tagged that artist/release was taken into consideration.

For all the releases that didn't have a genre, the following complementary sources of information were used:

- Some tables from The Million Song Dataset
- Data from Wikidata Query
- Data from Wikipedia API


At the end of this process, a total of 404.781 releases were retrieved with all the necessary information to visualize them.

## DESCRIPTION OF MAIN RESULTS


Rock is the dominant genre. I can't confirm if this is true in general or just in this dataset. It could be that my data sources (especially MusicBrainz) has more Rock related artists and therefore this is causing an umbalanced dataset, or it could be a reality that there are actually more Rock artists compared to other genres. It may also be due to the tag classification applied, which might have identified more rock subgenres than other categories.

A few countries produce the majority of the music: countries like USA, UK, Japan and a few others are the top producers of music/artists. This result isn't shocking to me, as the majority of the bands I know are either from the USA or the UK (even though I am Spanish). Again, this may or may not be true in the reality, it could have been biased by MusicBrainz's identity, as it is part of an NGO which is based in the USA and therefore, they may have more information about english-speaking artists. They do have, however, many Japanese artists in their database, and Japan is the third artist producer according to their records, which suggests that Musicbrainz tends to store data from all kids of artists, not only english-speaking ones.

In relation to the "oldest" genres, like Classical Music or Jazz: if we take into consideration that recorded music started rising around 1948 (first vynil LP), and that the releases table used contains only recorded music, the visualization doesn't really show the correct progress for these genres. Classical music, for instance, started before 1890 but, as the music wasn't recorded, those releases don't appear in the visualization. In order to show the real progress of all the genres that started before 1948, a more accurate way of gathering the data would be to look at each song/opera/etc and the year it was composed instead of released. This task could be really time consuming as it would involve searching song by song but it could be a way to improve the visualization.

Apart from the above genres, the visualization seems to be showing the results as they were intended to appear, as we can see how each genre expands over time and geography.


## FRONTEND/VISUALIZATION

I chose Tableau Public as my visualization tool, as it offers many options and is able to animate maps with a time feature, which was the main objective.

The link to the dashboard is: https://public.tableau.com/shared/N4N9Y99W5?:display_count=yes&:origin=viz_share_link (a copy of the workbook is attached to the repo too).

The dashboard consists of:

- Number of releases by genre and year: this is an areas graph, that simply shows the evolution of the different genres on time. The areas are sorted in decreasing order and they are stacked one on top of the other to avoid overlapping.

- Evolution of recorded music: this is a line graph showing the total number of releases per year. I added some key events which provide us with some information on how the different formats of recorded music have evolved in time. It seems that this could have had an impact on the volume of music produced, although proving this is out of the scope of the project.

- Top 5 artists by genre: this horizontal bar chart shows the artists that produced the most releases, for each genre.

- Top 10 countries and their predominant genre: this horizontal bar chart shows the contries that produce the most music/artists, and their main genre.

- The most relevant part: the interactive map, in which we can see the evolution. To run the animation, select the genre you want to visualize and press the "play" and stop buttons. You can change the speed of the visualization with the buttons next to "play".



## INSTRUCTIONS TO FOLLOW THE PROJECT


### 1 - Technical requirements

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

For the visualization, it is advised to download the latest version of Tableau Public (2019.2 or later) and run the dashboard locally in your computer (the interactive map doesn't render in the online version). You will need to have Tableau Public login details to be able to do that.

### 2 - Data folders

Once you've downloaded/cloned the repository in your PC, download the two data folders (Data_in & Data_out) from the following link:

https://drive.google.com/drive/folders/1PMlyqU2ruE8SyGH8qQNxXY29Cfvmg9jC?usp=sharing

Extract them into the repository folder.

### 3 - Notebook's order

In order to follow the whole process, there is a specific order to execute the notebooks:

- 1: Areas_Musicbrainz: this notebook prepares the area codes from Musicbrainz database and the resulting file is used in the next notebook.
- 2: Data_gathering_releases_origin: this notebook retrieves the origin for each release. The resulting file is used in the next notebook.
- 3: Data_gathering_music_genre: this notebook takes as input the output from the previous notebook and focuses on the music genre for each release.
- 4: Wikipedia_artist_information_retrieval: this is an auxiliary notebook. It assists notebooks 2 & 3 in their final steps.
- 5: Data analysis: this notebook analyzes the final dataframe and formats it before loading it with the visual tool.



## CREDITS

This project is based mainly in MusicBrainz's database. It has been complemented by The Million Song Dataset, Wikidata and Wikipedia. The music genre list has been inspired from https://www.musicgenreslist.com/ and MusicBrainz's genre list.


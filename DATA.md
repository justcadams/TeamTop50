# Introduction - Team Top 50

Eliot A. Heinrich, Owen D. Anderson, Matt J. Halligan, and Justin C. Adams chose the top 50 songs on Spotify as our data set for the Warm Up Project in UVM's Spring 2020 Software Engineering course taught by Dr. Jason Hibbeler. We named our team "Team Top 50" after the data set and this data will be incorporated in to a Command Line (CL) Application Programming Interface (API). This CL API will be turned in for class credit by 11:59PM 19 February 2020.

The CL API requires two relational databases with a common theme from a single data set. The theme is Top 50 Songs of 2019. The two Relational Databases (RDBs) are Song and Genre. The Song database contains the track name, artist name, and song length. The Genre database contains the Genre, Loudness, and Danceability. A summary of the data set and the relational database can be found below.

# Data Set - Top 50 Spotify Songs 2019

Leonardo Henrique is a Brazilian data scientist, who uses different popular media service apis to create useable data sets for competitions, work, and play. The Top 50 Songs on Spotify data set is a comma seperated value file containing the following meta data:

<ul>
  <li>ID - Signed Integer</li>
  <li>Track.Name - String</li>
  <li>Artist.Name - String</li>
  <li>Genre - String</li>
  <li>Beats.Per.Minute - Integer</li>
  <li>Energy - Integer</li>
  <li>Danceability - Integer</li>
  <li>Loudness in dB - Signed Integer</li>
  <li>Liveness - Integer</li>
  <li>Valence - Integer</li>
  <li>Length (s) - Integer</li>
  <li>Acousticness - Integer</li>
  <li>Speechiness - Integer</li>
  <li>Popularity - Integer</li>
</ul>

# Relational Databases - Song & Genre

### First RDB - Song
<ol>
  <li>ID</li>
  <li>Track.Name</li>
  <li>Artist.Name</li>
  <li>Length</li>
</ol>

### Second RDB - Genre
<ol>
  <li>ID</li>
  <li>Genre</li>
  <li>Loudness</li>
  <li>Danceability</li>
</ol>

<a id="1">[1]</a>
Henrique, L. Top 50 Spotify Songs - 2019. https://kaggle.com/leonardopena/top50spotify2019. Accessed 23 Jan. 2020.

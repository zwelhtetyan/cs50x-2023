SELECT avg(energy)
  FROM songs
  JOIN artists
    ON artists.id = artist_id
 WHERE artists.name = 'Drake';
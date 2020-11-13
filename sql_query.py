select_actors_director_note_by_film = '''
SELECT * FROM (
	SELECT  DISTINCT f.id as film_id,  
		pe.id as director_id, 
		nth_value(p.id, 1) over (partition by f.id) as actor_1,
		nth_value(p.id, 2) over (partition by f.id) as actor_2,
		nth_value(p.id, 3) over (partition by f.id) as actor_3,
		f.note_people as note
FROM films f
JOIN films_actors fa on fa.id_film = f.id
JOIN films_directors fd on fd.id_film = f.id
JOIN people p on p.id = fa.id_actor
JOIN people pe on pe.id = fd.id_director
WHERE f.note_people > 0
) as toto
WHERE toto.actor_2 is not null and toto.actor_3 is not null
ORDER BY toto.film_id;
'''
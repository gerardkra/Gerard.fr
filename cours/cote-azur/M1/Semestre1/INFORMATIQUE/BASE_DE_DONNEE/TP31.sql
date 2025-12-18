--EXERCICE 3.1: REQUETES SQL

--1. Liste des prénoms de la table. (1110019 lignes)--

SELECT *
FROM prenoms;

--2. Liste des années de la table. (1110019 lignes)--

SELECT annais
FROM prenoms;

--3. Département et année de naissance des personnes s’appelant Laetitia. (581 lignes)--

SELECT dpt, annais
FROM prenoms
WHERE preusuel="LAETITIA";

--4. Département et année de naissance des garçons prénommés Camille. (1438 lignes)--

SELECT dpt, annais
FROM prenoms
WHERE preusuel="CAMILLE" AND sexe="1";

--5. Liste des prénoms de garçons donnés en Corse en l’an 2000. (122 lignes)--

SELECT preusuel
FROM prenoms
WHERE annais="2000" AND sexe="1" AND dpt="20";

--6. Liste des prénoms donnés plus de 400 fois dans un département une année donnée, on affichera prénom,département, année. (4876 lignes)

SELECT preusuel, dpt, annais
FROM prenoms
WHERE nombre>400 AND preusuel<>"_PRENOMS_RARES";

--7. Liste des prénoms donnés strictement moins de 5 fois une année, avec l’année correspondante, dans les Alpes-Maritimes. (6650 lignes)

SELECT preusuel, annais
FROM prenoms
WHERE nombre<5 AND preusuel<>"_PRENOMS_RARES" AND dpt="06";

--8. Liste des prénoms de filles donnés strictement plus de 10 fois entre 2000 et 2004 dans les Alpes-de- Haute-Provence. Proposez deux requêtes. (16 lignes)

SELECT preusuel
FROM prenoms
WHERE nombre>10 AND preusuel<>"_PRENOMS_RARES" AND dpt=04 AND sexe=2 AND annais>=2000 AND annais<=2004;

--Méthode 2
SELECT preusuel
FROM prenoms
WHERE nombre>10 AND annais BETWEEN 2000 AND 2004  AND preusuel<>"_PRENOMS_RARES" AND dpt=04 AND sexe=2;

--9. Liste des prénoms donnés exactement 80 fois dans un département dont le numéro est strictement supérieur à 80 en 2005. (3 lignes)

SELECT preusuel
FROM prenoms
WHERE nombre=80 AND preusuel<>"_PRENOMS_RARES" AND dpt>80 AND annais=2005;

--10. Liste des prénoms de garçons commençant par Y donnés en 2000 dans les Alpes-Maritimes. Afficher prénom et nombre. (18 lignes)

SELECT preusuel, nombre
FROM prenoms
WHERE sexe=1  AND preusuel LIKE "Y%" AND annais=2000 AND dpt=06;

--11. Liste des prénoms commençant par « KHL ». Afficher les prénoms, départements et années. (28 lignes)

SELECT preusuel, dpt, annais
FROM prenoms
WHERE preusuel LIKE "KHL%";

--12. Liste des prénoms composés communs entre 2000 et 2003. Afficher les prénoms, départements, années et effectifs. (1932 lignes)

SELECT preusuel, dpt, annais, nombre
FROM prenoms
WHERE  preusuel LIKE "%-%" AND annais BETWEEN 2000 AND 2003;


--OPTION D'AFFICHAGE

--13. Liste des prénoms avec toutes les informations en renommant les colonnes : prénom, année, département,sexe, effectif. (1105864 lignes)

SELECT preusuel AS prénom, annais AS année, dpt AS département, sexe, nombre AS effectif
FROM prenoms;

--14. Afficher la liste des prénoms donnés en 2001 en Corse en triant par effectif croissant. (236 lignes)

SELECT preusuel
FROM prenoms
WHERE annais=2001 AND dpt=20
ORDER BY nombre;

--15. Afficher la liste des prénoms donnés en 2001 en Corse en triant par effectif décroissant. (236 lignes)

SELECT preusuel
FROM prenoms
WHERE annais=2001 AND dpt=20
ORDER BY nombre DESC;

-- 16. Afficher la liste des prénoms distincts de filles qui apparaissent dans la table. (20207 lignes)

SELECT DISTINCT preusuel
FROM prenoms
WHERE sexe=2 AND preusuel<>"_PRENOMS_RARES";

--17. Afficher la liste des prénoms distincts commençant par « Al » et terminant par « ce » apparaissant dans la table. (6 lignes)

SELECT DISTINCT preusuel
FROM prenoms
WHERE preusuel LIKE "Al%ce";


--18. Liste des prénoms de filles commençant par « C » donnés en 2000 en Corse. Afficher les prénoms et le nombre, trier par ordre croissant de nombre. (17 lignes)

SELECT preusuel
FROM prenoms
WHERE sexe=2  AND preusuel LIKE "C%" AND annais=2000 AND dpt=20;

--19. Liste des prénoms (distincts) communs donnés entre 2000 et 2020 qui ont deux caractères quelconques, puis terminent par « ice ». (3 lignes)


SELECT DISTINCT preusuel
FROM prenoms
WHERE preusuel LIKE "__ice" AND annais BETWEEN 2000 AND 2020;


--20. Liste des prénoms (distincts) communs entre 2000 et 2020 et qui comportement exactement 6 lettres. Afficher le prénom uniquement. (2746 lignes)

SELECT DISTINCT preusuel
FROM prenoms
WHERE preusuel LIKE "______" AND annais BETWEEN 2000 AND 2020;

--21. Liste des prénoms (distincts) communs entre 2000 et 2020 et qui comportement exactement 7 lettres, dont un Z. Afficher le prénom uniquement.

SELECT DISTINCT preusuel
FROM prenoms
WHERE preusuel LIKE "_______" AND preusuel LIKE "%Z%" AND annais BETWEEN 2000 AND 2020;

--22. Liste des prénoms (distincts) non composés communs entre 2000 et 2020 qui commencent par « Ab » et
--contiennent au moins deux fois la lettre A. Afficher le prénom, le département, l’année et l’effectif. Trié
--par année décroissante, par effectif croissant, puis par prénom dans l’ordre alphabétique.

SELECT DISTINCT preusuel, dpt, annais, nombre
FROM prenoms
WHERE preusuel LIKE "Ab%" AND preusuel LIKE "_%A%" AND annais BETWEEN 2000 AND 2020 
ORDER BY annais DESC,nombre,preusuel;

--23. Afficher la liste des prénoms distincts communs (pas rares) donnés entre 2000 et 2020

SELECT DISTINCT preusuel
FROM prenoms
WHERE annais BETWEEN 2000 AND 2020 AND preusuel<>"_PRENOMS_RARES";

--24. Afficher les prénoms communs (non rares) donnés à des garçons en région Provence-Alpes-Côte-d’Azur
--entre 2002 et 2006. On affichera prénom et nombre, on triera par ordre décroissant de nombre.

SELECT DISTINCT preusuel
FROM prenoms
WHERE annais BETWEEN 2002 AND 2006 AND preusuel<>"_PRENOMS_RARES" AND sexe=1 AND dpt=93;

																																																																																																																																																																																											
		--USAGE DE TABLE MULTIPLE		
--25. Afficher le prénom, le département, le nombre de naissances en 2017, le nombre de naissances en 2018
--pour les prénoms qui ont eu des naissances dans le même département en 2017 et en 2018		
SELECT p1.preusuel, p1.dpt, p1.nombre, p2.nombre
FROM prenoms p1, prenoms p2
WHERE p1.annais =2017 AND p2.annais=2018 AND p1.preusuel=p2.preusuel AND p1.dpt=p2.dpt AND p1.preusuel<>"_PRENOMS_RARES";	

--26. Afficher les départements et les prénoms correspondants pour lesquels le nombre de naissances en 2018
--est strictement supérieur à celui en 2017.																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																
SELECT p1.dpt, p1.preusuel
FROM prenoms p1, prenoms p2
WHERE p1.annais =2017 AND p2.annais=2018 AND p1.preusuel=p2.preusuel AND
 p1.dpt=p2.dpt AND p1.preusuel<>"_PRENOMS_RARES" AND p2.nombre>p1.nombre;																																																																																																																																																																																											
																																																																																																																																																																																											
--27. Afficher les départements pour lesquels il existe un prénom commençant par « K » tel que le nombre de
--naissances en 2018 dans le département est strictement supérieur à ce nombre en 2017.	

SELECT p1.dpt
FROM prenoms p1, prenoms p2
WHERE p1.annais =2017 AND p2.annais=2018 AND p1.preusuel=p2.preusuel AND
 p1.dpt=p2.dpt AND p1.preusuel<>"_PRENOMS_RARES" AND p2.nombre>p1.nombre AND p1.preusuel LIKE "K%";																																																																																																																																																																																																																																																																																																																																																																														

 
--	Afficher (sans répétition) les prénoms épicènes (l'un ou l'autre sex) donnés dans les Alpes-Maritimes en 2018.
SELECT p1.preusuel
FROM prenoms p1, prenoms p2
WHERE p1.sexe =1 OR p2.sexe=2 AND p2.annais=2018 AND p1.preusuel=p2.preusuel AND
 p1.dpt=p2.dpt AND p1.preusuel<>"_PRENOMS_RARES" AND p1.dpt="06";																																																																																																																																																																																																																																																																																																																																																																												
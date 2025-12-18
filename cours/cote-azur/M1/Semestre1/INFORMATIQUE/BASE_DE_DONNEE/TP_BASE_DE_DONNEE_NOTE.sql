--1)Toutes les infos du Chevale 1073

SELECT *
FROM Cheval
WHERE id_cheval=1073;

--2) Identifiants des Cheveaux
SELECT parent.id_cheval
FROM Cheval fils JOIN  Cheval parent 
ON fils.id_cheval = parent.id_cheval
WHERE parent.pere = 1118
ORDER BY parent.id_cheval DESC;

--3) 

SELECT DISTINCT c.id_cheval
FROM Cheval c
JOIN Participe p ON c.id_cheval =  p.id_cheval
JOIN Course cou ON cou.id_course = p.id_course
WHERE p.stalle= 1
ORDER BY c.id_cheval;

--4) Affichage annee de naissance
SELECT DISTINCT annee
FROM Cheval
WHERE nom_cheval LIKE"Bel%";

--5) Affichage de nom des chevaux

SELECT DISTINCT c.nom_cheval
FROM Cheval c
JOIN Participe p ON c.id_cheval =  p.id_cheval
JOIN Entraineur e ON e.id_e = p.id_e
WHERE e.id_e= 432;

--6) 

SELECT DISTINCT cou.nom_course, c.nom_cheval
FROM Cheval c
JOIN Participe p ON c.id_cheval =  p.id_cheval
JOIN Course cou ON cou.id_course = p.id_course
WHERE p.position= 3
ORDER BY c.id_cheval;

--7) 


--8) Nombre de ligne total
SELECT COUNT(*) AS nombre_de_lignes_total
FROM Jockey;

--9) Age des Chevaux
SELECT  c.nom_cheval, c.annee,(2020-c.annee) AS age_chevaux
FROM Cheval c
JOIN Participe p ON c.id_cheval =  p.id_cheval
JOIN Course cou ON cou.id_course = p.id_course
WHERE cou.obstacles= 0 AND cou.date LIKE '2020-01%'
ORDER BY age_chevaux;

--10) Age max
SELECT MAX(2020-c.annee) AS age_max
FROM Cheval c
JOIN Participe p ON c.id_cheval =  p.id_cheval
JOIN Course cou ON cou.id_course = p.id_course
JOIN Entraineur e ON e.id_e = p.id_e
WHERE cou.date LIKE '2020%' AND e.id_e= 201 OR e.id_e= 680
ORDER BY age_max;


-- 11) 
SELECT AVG(p.position) AS position_finale_moyenne
FROM Cheval c
JOIN Participe p ON c.id_cheval =  p.id_cheval
WHERE c.id_cheval=4126
ORDER BY position_finale_moyenne;

--12) 
SELECT enfant.nom_cheval AS nom, mere.mere AS id_mere, mere.nom_cheval AS nom_mere
FROM Cheval enfant JOIN  Cheval mere 
ON enfant.id_cheval = mere.id_cheval
WHERE enfant.id_cheval = 1364;

--13)
SELECT strftime('%m', Course.date) AS mois, COUNT(*) AS nombre_de_courses
FROM Course
WHERE Course.obstacles = 18
GROUP BY mois
ORDER BY mois;

--14) 
SELECT H.nom_h, COUNT(*)
FROM Hippodrome H 
JOIN Course cou ON cou.id_h =  H.id_h 
GROUP BY H.nom_h
HAVING COUNT(*)<=35;

-- 15)
SELECT J.nom_j, COUNT(DISTINCT p.id_cheval) AS nombre_chevaux
FROM Jockey J
JOIN Participe p ON p.id_j = J.id_j
JOIN Cheval c ON c.id_cheval =  p.id_cheval
GROUP BY J.nom_j
HAVING COUNT(DISTINCT p.id_cheval)>=30;

--16) 
SELECT DISTINCT p.stalle, COUNT(p.id_cheval) AS nombre_de_chevaux_gagnants
FROM Cheval c
JOIN Participe p ON c.id_cheval =  p.id_cheval
JOIN Course cou ON cou.id_course =  p.id_course
WHERE p.position = 1
GROUP BY p.stalle
ORDER BY nombre_de_chevaux_gagnants DESC;

--17)
SELECT p.stalle, AVG(p.position) AS position_moyenne
FROM Participe p
JOIN Cheval c ON p.id_cheval = c.id_cheval
WHERE c.pere = 93
GROUP BY p.stalle
ORDER BY p.stalle DESC;

--18)
SELECT J.id_j, J.nom_j, COUNT(DISTINCT c.classe) AS nombre_de_classes
FROM Jockey J
JOIN Participe p ON J.id_j = p.id_j
JOIN Course c ON p.id_course = c.id_course
GROUP BY J.id_j, J.nom_j
HAVING COUNT(DISTINCT c.classe) >= 4
ORDER BY nombre_de_classes DESC;

--19)
SELECT DISTINCT p.id_course
FROM Participe p
WHERE p.stalle = 3
  AND p.id_course NOT IN (
    SELECT id_course
    FROM Participe
    WHERE stalle = 2);
	
-- 24)-- CHATGPT--
SELECT Cheval.id_cheval, COUNT(DISTINCT Enfant.id_cheval) AS nombre_enfants
FROM Cheval
LEFT JOIN Cheval AS Enfant ON Cheval.id_cheval = Enfant.pere OR Cheval.id_cheval = Enfant.mere
GROUP BY Cheval.id_cheval
HAVING COUNT(DISTINCT Enfant.id_cheval) > 0
ORDER BY nombre_enfants DESC;
-- Source CHATGPT__


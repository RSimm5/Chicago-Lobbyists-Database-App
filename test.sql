SELECT l.Lobbyist_ID, l.First_Name, l.Last_Name, l.Phone,
    SUM(c.Compensation_Amount) AS Total_Compensation,
    GROUP_CONCAT(DISTINCT Client_Name ORDER BY Client_Name ASC)  AS Client_Names
FROM LobbyistInfo l
JOIN Compensation c ON c.Lobbyist_ID = l.Lobbyist_ID
JOIN ClientInfo ci ON c.Client_ID = ci.Client_ID
WHERE strftime('%Y', c.Period_Start) = ?
GROUP BY l.Lobbyist_ID
ORDER BY Total_Compensation DESC
LIMIT ?;

SELECT DISTINCT Client_Name
FROM ClientInfo ci
JOIN Compensation c ON c.Client_ID = ci.Client_ID
WHERE strftime('%Y', c.Period_Start) = ?
AND ;



SELECT l.Lobbyist_ID, l.First_Name, l.Last_Name, l.Phone,
    SUM(c.Compensation_Amount) AS Total_Compensation
FROM LobbyistInfo l
JOIN Compensation c ON c.Lobbyist_ID = l.Lobbyist_ID
JOIN ClientInfo ci ON c.Client_ID = ci.Client_ID
WHERE strftime('%Y', c.Period_Start) = '2020'
GROUP BY l.Lobbyist_ID
ORDER BY Total_Compensation DESC
LIMIT 3;


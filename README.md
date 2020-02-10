SNN-News

En textgenererande AI som hämtar nyhetsartiklar från flera olika sidor med hjälp av NewsAPI, https://newsapi.org. 

Relevant information sparas i en textfil som senare tränas med hjälp av GPT-2. Tanken är att den varje dag ska hämta nyheter som tillsammans med tidigare tränade vikten ska skapa ca. 10 egna artiklar. Tanken är även att genom NewsAPI hämta populära nyckelord som ska användas som prefix. 

Utöver detta tänker jag lägga upp artiklarna, som kommer bestå av en rubrik och en kort beskrivning, på Twitter. För detta kommer jag använda https://www.youtube.com/watch?v=RMQ4f6YXRTM.
Programmet hämtar bilderna för varje artikel med NewsAPI och sparar dessa med tillhörande text. Sedan ska programmet baserat på de genererade artiklarna välja den mest relevanta bilden till varje artikel. 

Jesper Jansson

SNN-News

En textgenererande AI som hämtar nyhetsartiklar från flera olika sidor med hjälp av NewsAPI, https://newsapi.org. 

Relevant information sparas i en textfil som senare tränas med hjälp av GPT-2. Tanken är att den varje dag ska hämta nyheter som tillsammans med tidigare tränade vikten ska skapa ca. 10 egna artiklar. Med hjälp av nltk, hittas nyckelord i de senaste texterna och använder de som prefix. 

Artiklarna genereras och läggs sedan ut på Twitter. 
Länk till twitterkonto: https://twitter.com/PmSvensk

Programmet hämtar bilderna för varje artikel med NewsAPI och sparar dessa med tillhörande text. Sedan väljer programmet baserat på de genererade artiklarna den mest relevanta bilden till varje artikel. 

Koden är uppdelad i två colabs:

Den första hämtar dataset och tränar en modell som läggs i google Drive,
https://colab.research.google.com/drive/1QMx8Q5Z3ddorHInnY4LGWm3ehzDFWxHz#scrollTo=P4jVFbiyavwu

Den andra använder den tränade modellen och genererar tweets som läggs ut,
https://colab.research.google.com/drive/1WXYVxzUSOyWam4ZqHB1aItDe6xL1rlXH#scrollTo=sJlbCdP3B2S6


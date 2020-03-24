# SNN-News

En textgenererande AI som hämtar nyhetsartiklar från flera olika sidor med hjälp av NewsAPI,  [https://newsapi.org](https://newsapi.org/).

Relevant information sparas i en textfil som senare tränas med hjälp av GPT-2. Tanken är att den varje dag ska hämta nyheter som tillsammans med tidigare tränade vikten ska skapa ca. 10 egna artiklar. Med hjälp av nltk, hittas nyckelord i de senaste texterna och använder de som prefix.

Artiklarna genereras och läggs sedan ut på Twitter. Länk till twitterkonto:  [https://twitter.com/PmSvensk](https://twitter.com/PmSvensk)

Programmet hämtar bilderna för varje artikel med NewsAPI och sparar dessa med tillhörande text. Sedan väljer programmet baserat på de genererade artiklarna den mest relevanta bilden till varje artikel. Detta görs genom att välja den bilden med den bildtext som stämmer bäst överens med den genererade texten. För att göra detta används Googles Universal Sentence Recorder som använer sig av tensorflow. Länk för mer info:  [https://tfhub.dev/google/universal-sentence-encoder/1](https://tfhub.dev/google/universal-sentence-encoder/1)  
Länk för exempelkod som används i projektet:  [https://colab.research.google.com/github/tensorflow/hub/blob/50bbebaa248cff13e82ddf0268ed1b149ef478f2/examples/colab/semantic_similarity_with_tf_hub_universal_encoder.ipynb](https://colab.research.google.com/github/tensorflow/hub/blob/50bbebaa248cff13e82ddf0268ed1b149ef478f2/examples/colab/semantic_similarity_with_tf_hub_universal_encoder.ipynb)

För att generara prefix för nyckelord i texterna användes denna guide:  [https://medium.com/analytics-vidhya/automated-keyword-extraction-from-articles-using-nlp-bfd864f41b34](https://medium.com/analytics-vidhya/automated-keyword-extraction-from-articles-using-nlp-bfd864f41b34)

# Komma igång med programmet

Koden är uppdelad i två colabs:

Alla instruktioner om hur programmen ska köras finns i colabfilerna.

Den första hämtar dataset och tränar en modell som läggs i google Drive:  [https://colab.research.google.com/drive/1QMx8Q5Z3ddorHInnY4LGWm3ehzDFWxHz#scrollTo=P4jVFbiyavwu](https://colab.research.google.com/drive/1QMx8Q5Z3ddorHInnY4LGWm3ehzDFWxHz#scrollTo=P4jVFbiyavwu) 
Med denna kan man träna upp en modell och ladda ned data till generering av tweets.

Den andra använder den tränade modellen och genererar tweets som läggs ut:  [https://colab.research.google.com/drive/1WXYVxzUSOyWam4ZqHB1aItDe6xL1rlXH#scrollTo=sJlbCdP3B2S6](https://colab.research.google.com/drive/1WXYVxzUSOyWam4ZqHB1aItDe6xL1rlXH#scrollTo=sJlbCdP3B2S6)  
Denna går att köra med min färdigtränade modell eller med en egen. För att köra med en egen modell behöver man träna en sådan i den första colabfilen och sedan spara den i sin Google Drive. Viktikt är då att byta ut så att programmet hämtar din modell istället för min. Mer inforamtion om det finns i filen.

## Heroku

Tanken var att köra programmet i Heroku så att det kunde generera tweets utan att något program behöver köras i colab eller på datorn. Eftersom Heroku har en hård minnesgräns går det inte att generera prefix och hitta bilder. Därför körs koden i nuläget enbart i colab. Som test har jag lagt med de filer som behövs för att köra ett enklare program som enbart postar tweets med text och utan prefixes i mappen "Heroku".



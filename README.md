# CeneoScraper
## Etap 1 - Pobranie składowych pojedynczej opinii o wybranym produkcie [Ceneo.pl](https://www.ceneo.pl/)
* Pobranie kodu pojedynczej strony z opiniami o produkcie
* Analiza kodu html pojedynczej opinii

+---------------+------------+--------------+----------+
|Składowa opinii|Selektor CSS|Nazwa zmiennej|Typ danych|
+===============+============+==============+==========+
|Opinia|.js_product-review|opinion|||
+---------------+------------+--------------+----------+
|Identyfikator opinii|['data-review-id']|opinion_id|||
+---------------+------------+--------------+----------+
|Autor|.user-post__author-name|author|||
+---------------+------------+--------------+----------+
|Rekomendacje|.user-post__author-recomendation|recomm|||
+---------------+------------+--------------+----------+
|Liczba gwiazdek|.user-post__score-count|stars|||
+---------------+------------+--------------+----------+
|Treść|.user-post__text|content|||
+---------------+------------+--------------+----------+
|Lista zalet|review-feature__col:has(> div.review-feature__title--positives) > .review-feature__item|pros|||
||review-feature__col:has(> div[class*="positives") > .review-feature__item|||
||div.review-feature__title--positives ~ .review-feature__item|||
+---------------+------------+--------------+----------+
|Lista wad|review-feature__col:has(> div.review-feature__title--negatives) > .review-feature__item|cons|||
||review-feature__col:has(> div[class*="negatives") > .review-feature__item|||
||div.review-feature__title--negatives ~ .review-feature__item|||
+---------------+------------+--------------+----------+
|Dla ilu osób użyteczna|span[id^="votes-yes"]|useful|||
+---------------+------------+--------------+----------+
|Dla ilu osób nieużyteczna|span[id^="votes-no"]|useless|||
+---------------+------------+--------------+----------+
|Czy opinia potwierdzona zakupem|.review-pz|purchased|||
+---------------+------------+--------------+----------+
|Data wystawienia opinii|.user-post__published > time:nth-child(1)`["datetime"]`|publish_date|||
+---------------+------------+--------------+----------+
|Data zakupu|.user-post__published > time:nth-child(2)`["datetime"]`|purchase_date|||
+---------------+------------+--------------+----------+

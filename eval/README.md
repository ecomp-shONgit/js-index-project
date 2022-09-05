
# Auswertung

## 1. Aufbau der Stichprobe / Evaluation
Es handelt sich um eine Stichprobe mit vielen sehr schwierigen Fällen, die die Grenzen der Software und des Referenzierens betrifft. Zum Beispiel müssen wir die Stichprobe in jene Fälle unterscheiden, die vollständig qualifizierte Referenzen darstellen und solle Fälle, die weitere Verkürzungen beinhalten. Außerdem ist die gesamte Stichprobe mehrsprachig ausgelegt und nicht nur auf Kurzformen beschränkt. Es wurden 5 Fachwissenschaftler mit der Beurteilung beauftragt (http://ecomparatio.net/~khk/indexprojte/). Die Auswertung ihrer Antworten wurde kumulativ erstellt. Die einzelnen Schritte sind als Python Skript hier zu finden (python3 eval1.py).

## 2. Überblick der Ergebnisse
Es wurden 188 strings untersucht. Davon konnten für 104 strings jeweils 116 richtige Referenzen hergestellt werden (unter den ersten 10 Vorschlägen, ohne Sortierung der Vorschläge). Manche strings konnten verkürzt werden und dennoch konnte die passende Referenz zugewiesen werden. Zu 84 strings konnte keine passende Referenz gefunden werden. Das heißt einwandfreie Zuordnung gelingt in 55% der Fälle. Für qualifizierte Angaben ist die Zuordnung deutlich besser von den 93 enthaltenden voll qualifizierten Referenzen konnten 16 % nicht richtig einem Eintrag in der Wissensbasis zugeordnet werden. Von den 15 nicht zugeordneten Angaben sind 2% Verschreibungen/keine klassischen Autoren, 6% stellen einen Fall extremer Informationsreduktion dar und 8% legen Lücken in der Wissensbasis nahe.

## 3. Beurteilung der korrekten Zuordnung
Hier müssen folgende Aspekte berücksichtigt werden: 27 der 104 Fälle sind nicht qualifizierte Referenzen.
Es existieren stark verkürzte strings und auch anderssprachige Angaben.
55 der 116 passenden Referenzen fallen in die Konfidenzgruppe 1 (Angaben können ohne Modifikationen oder mit leichten Modifikationen einem Eintrag in der Wissensbasis zugeordnet werden), 24 in die Konfidenzgruppe 2 (erhebliche Modifikationen erlauben eine Zuordnung zu einem Eintrag in der Wissensbasis) und 37 in die Konfidenzgruppe 3 (sicher keine vollständig qualifizierte Quellenangabe, aber es lassen sich Zuordungen herstellen). Das heißt die gesamte Konfidenzgruppe 3 und wenige Ergebnisse der Konfidenzgruppe 2 werden durch Fälle gebildet, die keine qualifizierten Referenzen angeben. Die Berücksichtigung mehrsprachige Angaben ist in Abhängigkeit von der Sprachfamilie und der resultierenden sting Veränderung möglich und werden für Augustinus richtig durchgeführt. Informationsverlust ist für sehr kurze Abkürzungen von 1-2 Buchstaben anzunehmen und somit Reduktion

## 4. Beurteilung der nicht korrekt zugeordneten strings
12 der 82 Fälle sind qualifiziert, davon sind drei absichtlich falsch geschrieben. 70 Fälle sind lediglich Wort (string repräsentiert die Abkürzung eines Autorennames oder Ähnliches) und Zahl Kombinationen.

Aufstellung der 16 voll qualifizierten Referenzen (http://ecomparatio.net/~khk/indexprojte/indexqualified.html):

- augustin. cd 2. 24; //Zu kurze Angabe des Werktitels.
- plut. mar. 10, 3 // Angabe konnte umgewandelt werden - übersehen.
- oic. div. 1. 72; 2. 65; // Falsche Schreibung der Abkürzung "Cic." ist kritisch.
- app. num frag. 4 // Zuweisbarkeit aufgrund der Angabe "frag." nicht möglich.
- plin. nh 8, 53. // Zu kurze Angabe des Werktitels.
- grueber crrbm 1. 459f. // Keine Referenz auf klassischen Autoren.
- app. bc 1. 7986; // Läng der Abkürzung des Werktitels.
- hes. th. 1 // Anpassung der Abkürzung in der Wissensbasis.
- hes. wd 1 // "
- pind. nem. 10, 61f. // Wissensbasis Lückenhaft
- aristot. en x 8, 1178 // Länge der Abkürzung des Werktitels.
- plat. theait. 173 // Wissensbasis Lückenhaft
- Euseb. praep. evang. 12, 29, 15, 2; // Abkürzung in der Wissensbasis

## 5. Anpassung
Die Software in Kombination mit der Wissensbasis liefert sehr tragfähige Ergebnisse. Die Vorschläge müssen nun noch so sortiert werden, dass die passendsten für den Nutzer an oberster Stelle genannt werden. Die Wissensbasis muss anhaltend auf Lücken und Unklarheiten hin untersucht werden.


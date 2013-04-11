DGS - DotLAN Galeriesauger
==========================

Dieses Skript saugt eine DotLAN-Galerie auf die lokale Platte.

Es setzt eine wget-Installation vorraus

Die Konstanten HOST, GALERY_ID und COUNT am Skriptanfang müssen gesetzt werden
Danach kann das Skript mit Python ausgeführt werden und lädt die Bilder in den
Ordner, von dem aus das Skript gestartet wurde.

Beispiel:

Wenn ein Bild aus der Galerie so aussieht:

http://meinelan.de/gallery/archive/20130908-C3D952/0001.jpg

und die Galerie 57 Bilder beinhaltet, dann müssen die Konstanten wie folgt
gesetzt sein:

HOST = "meinelan.de"
GALERY_ID = "20130908-C3D952"
COUNT = 57

Viel Spass mit dem Skript.


P.S.: Aktuell können nur Galerien mit nicht mehr als 999 Bildern gesaugt werden,
das duerfte aber kein Problem sein. Kommt nur sehr selten vor.

Inspiriert durch folgenden Forenpost von N3xu5:
http://1024lan.de/forum/?do=showthread&id=168
# Landwirtschaftliche Kontrolldaten
eCH Fachgruppe AgriFood
2026-10-07

- [<span class="toc-section-number">1</span>
  Einleitung](#sec-introduction)
  - [<span class="toc-section-number">1.1</span> Status](#sec-status)
  - [<span class="toc-section-number">1.2</span> Zielbild der
    Arbeitsgruppe](#sec-target-picture)
  - [<span class="toc-section-number">1.3</span> Landwirtschaftliche
    Kontrollen](#sec-agricultural-inspections)
  - [<span class="toc-section-number">1.4</span> Datenflüsse von
    Kontrolldaten](#sec-data-flows)
  - [<span class="toc-section-number">1.5</span> Hierarchie und
    Entstehung von Kontrollpunkten](#sec-control-point-hierarchy)
  - [<span class="toc-section-number">1.6</span> Kontrolldaten
    heute](#sec-inspection-data)
- [<span class="toc-section-number">2</span> Akteure und
  Anwendungsfälle](#sec-actors-use-cases)
  - [<span class="toc-section-number">2.1</span> Akteure](#sec-actors)
  - [<span class="toc-section-number">2.2</span>
    Anwendungsfälle](#sec-usecases)
  - [<span class="toc-section-number">2.3</span> Einschränkungen der
    heutigen Kontrolldaten](#sec-limitations)
- [<span class="toc-section-number">3</span> Fachglossar
  Kontrollwesen](#sec-glossary)
  - [<span class="toc-section-number">3.1</span> Aufbau des
    Glossars](#sec-glossary-structure)
  - [<span class="toc-section-number">3.2</span> Grundsätze der
    Terminologiearbeit](#sec-glossary-principles)
  - [<span class="toc-section-number">3.3</span>
    Governance](#sec-governance)
- [<span class="toc-section-number">4</span> Logisches
  Datenmodell](#sec-data-model)
- [<span class="toc-section-number">5</span>
  Haftungsausschluss](#sec-disclaimer)
- [<span class="toc-section-number">6</span>
  Urheberrechte](#sec-copyrights)
- [Anhang A - Referenzen](#sec-appendix-a)
- [Anhang B - Mitwirkung und Prüfung](#sec-appendix-b)
- [Anhang C - Abkürzungen und Glossar](#sec-appendix-c)
- [Anhang D - Änderungen gegenüber der Vorversion](#sec-appendix-d)
- [Anhang E - Abbildungsverzeichnis](#sec-appendix-e)
- [Anhang F - Tabellenverzeichnis](#sec-appendix-f)

# Hinweis

Im vorliegenden Dokument wird bei der Bezeichnung von Personen eine
geschlechtsneutrale Formulierung verwendet. Basis bildet der Leitfaden
der Bundeskanzlei. Je nach Situation kommen Paarformen (Bürgerinnen und
Bürger), geschlechtsabstrakte Formen (versicherte Person),
geschlechtsneutrale Formen (Versicherte) oder Umschreibungen ohne
Personenbezug zum Einsatz. Das generische Maskulin (Bürger) ist nicht
zulässig. Vollformen werden in fortlaufenden Texten verwendet, also in
Texten, die aus ausformulierten Sätzen bestehen. In verknappten
Textpassagen, namentlich in Tabellen, können Kurzformen verwendet
werden. Dabei wird die Kurzform mit Schrägstrich, aber ohne
Auslassungsstrich verwendet (Referent/in). Genderstern und ähnliche
Schreibweisen werden nicht verwendet.

# Einleitung

Die Weiterverwendung von Daten ist ein zentraler Bestandteil der
digitalen Transformation des Schweizer Agrar- und Ernährungssektors. Im
landwirtschaftlichen Kontrollwesen werden Daten in Form von Resultaten
und Eigenschaften von Kontrollen erhoben. Diese Daten dienen in erster
Linie der Oberaufsicht über den rechtskonformen Vollzug in den Kantonen
und der Festlegung risikobasierter Kontrollen. Zudem dienen sie der
Berichterstattung, der Unterstützung privatrechtlicher Kontrollen und
der Weiterentwicklung der Agrarpolitik.

## Status

In Arbeit: Der Gebrauch ist nur innerhalb der Fachgruppe,
beziehungsweise im Expertenausschuss zugelassen.

## Zielbild der Arbeitsgruppe

Der Aktionsplan Kontrollen auf Landwirtschaftsbetrieben hat ein klares
übergeordnetes Ziel: Die administrative Belastung der Landwirtinnen und
Landwirte durch Kontrollen soll sinken, konkret auf höchstens eine
Grund- oder Standardkontrolle pro Jahr und Betrieb \[BLW25\]. Dies kann
nur gelingen, wenn Doppelspurigkeiten zwischen öffentlich-rechtlichen
Kontrollen (Bund und Kantone) und privatrechtlichen Kontrollen (Labels
wie Bio Suisse, IP-Suisse oder SwissGAP) vermieden werden.

Damit eine Organisation auf eine eigene Kontrolle verzichten kann, muss
sie die Kontrollergebnisse einer anderen Organisation anerkennen und
nutzen können. Das funktioniert heute nicht reibungslos, weil die
Akteure unterschiedliche «Sprachen» sprechen – fachlich (Begriffe) und
technisch (Datenstrukturen).

Die eCH-Arbeitsgruppe Landwirtschaftliche Kontrolldaten kümmert sich
deshalb um die semantische und technische Interoperabilität von
Kontrolldaten. Sie erarbeitet das Wörterbuch (Fachglossar), die
Grammatik (Geschäftsobjekte), konkrete Anwendungen (Anwendungsfälle),
darauf basierend ein konzeptuelles und ein logisches Datenmodell und
eine Struktur für die langfristige Pflege (Governance). Die
Arbeitsgruppe hat sich am 4. März 2026 auf folgendes Hauptziel geeinigt:

> Das Ziel ist, Kontrolldaten auszutauschen und als Folge dessen auf
> Kontrollen verzichten zu können. Weiter soll für alle Beteiligten
> transparent sein, was genau kontrolliert wird und was die
> Anforderungen sind.

## Landwirtschaftliche Kontrollen

Betriebe, die Direktzahlungen beziehen, müssen den ökologischen
Leistungsnachweis (ÖLN) erfüllen und können sich zusätzlich für
freiwillige Direktzahlungsprogramme anmelden \[DZV\]. Darüber hinaus
können sich Betriebe bei privaten Label-Organisationen für
Produktionsweisen zertifizieren lassen, die über die
öffentlich-rechtlichen Anforderungen hinausgehen, zum Beispiel für die
integrierte Produktion (IP-Suisse) oder die biologisch-dynamische
Landwirtschaft (Demeter) \[Dem26; IPS26\]. Anforderungen an die
biologische Landwirtschaft werden sowohl öffentlich-rechtlich
(Bio-Verordnung) als auch privatrechtlich vorgegeben (Bio Suisse)
\[BioS26; BIOV\].

Die Einhaltung der gesetzlichen Anforderungen, des ÖLN und der
Direktzahlungsprogramme wird im Rahmen von Grundkontrollen und
risikobasierten Kontrollen überprüft \[VKKL\]. Ganzjahresbetriebe müssen
innerhalb von acht Jahren mindestens zweimal vor Ort kontrolliert
werden, Sömmerungsbetriebe mindestens einmal; für weitere
Direktzahlungsbereiche gilt in der Regel eine Mindesthäufigkeit von
einmal in acht Jahren \[VKKL\]. Zusätzlich werden risikobasierte
Kontrollen durchgeführt, etwa bei Mängeln in früheren Kontrollen, bei
begründetem Verdacht, bei wesentlichen betrieblichen Änderungen oder in
jährlich festgelegten Bereichen mit höherem Risiko \[VKKL\]. Zentraler
Bestandteil der Grundkontrollen ist ein Betriebsrundgang; hinzu kommen
die Prüfung von Aufzeichnungen und Dokumenten sowie Gespräche mit den
Bewirtschafterinnen und Bewirtschaftern \[VKKL\]. Werden Mängel
festgestellt, können je nach Art und Schwere die Direktzahlungen gekürzt
werden \[DZV\].

## Datenflüsse von Kontrolldaten

Die Daten öffentlich-rechtlicher Kontrollen fliessen im System Acontrol
zusammen, das vom Bundesamt für Landwirtschaft (BLW) und vom Bundesamt
für Lebensmittelsicherheit und Veterinärwesen (BLV) gemeinsam genutzt
wird \[BLW26a\]. Die Datenflüsse unterscheiden sich je nach Kanton:

- Kontrollpersonen erfassen die Resultate bei der Kontrolle auf dem
  Betrieb mit einer Tablet-Applikation, zum Beispiel ACmobile oder
  eControls. Je nach Kanton gehen die Daten zuerst in das kantonale
  Agrarinformationssystem (KAIS) und von dort an Acontrol. Sie können
  auch direkt von der Applikation an Acontrol gehen. Teilweise fehlen
  Schnittstellen, zum Beispiel im Wallis: eControls generiert für einen
  Teil der Kontrolldaten eine für Acontrol passende XML-Datei auf. Der
  Kanton lädt die Daten dann manuell herunter und importiert sie in
  Acontrol. Das kantonale System im Wallis speichert keine
  Kontrolldaten, nur die Beträge von Kürzungen. Der Kanton bezieht die
  Resultate für die Prüfung und die Bearbeitung von Mängeln aus
  Acontrol.
- Kontrollstellen im Auftrag der Kantone übermitteln ihre Resultate an
  die Kantone. Mängel sind meldepflichtig. Ein Teil dieser Angaben geht
  per E-Mail an bis zu 18 Kantone, weil das Acontrol-Schema nicht alle
  nötigen Felder enthält. Auch Kantonschemiker und Gewässerschutzstellen
  ohne KAIS-Zugriff, zum Beispiel im Tessin, erhalten meldepflichtige
  Daten per E-Mail.
- Bio-Kontrollstellen führen jährlich Kontrollen im privatrechtlichen
  und alle vier jahre im öffentlich-rechtlichen Auftrag durch. Die
  Kantone erhalten nur die öffentlich-rechtlichen und die
  meldepflichtigen Resultate. Einige Kontrollstellen, zum Beispiel Bio
  Test Agro, senden auch privatrechtliche Resultate an die Kantone. Im
  Wallis erfassen Bio-Kontrollstellen ihre Resultate direkt in Acontrol.
  Der Kanton wertet alle diese Resultate aus und bearbeitet so auch
  Mängel, die ausserhalb der kantonal beauftragten Kontrollen
  festgestellt wurden.
- Datenbezügerinnen und Datenbezüger können seit September 2026
  Acontrol-Daten mit Einverständnis der Bewirtschafterinnen und
  Bewirtschafter über agridata.ch (früher «Meine Agrardatenfreigabe»,
  MAF) beziehen.

Privatrechtliche Kontrolldaten werden nicht an Acontrol übermittelt.
Einige Kantone speichern sie trotzdem. Kontrollorganisationen müssen sie
deshalb bei jedem Kanton einzeln abholen. Auch kantonale Kontrollpunkte
der Landwirtschaftsämter, zum Beispiel zu Vernetzungs- und
Landschaftsqualitätsprojekten, gehen nicht an Acontrol. Die
Veterinärämter erfassen ihre Kontrollpunkte direkt in Acontrol.

## Hierarchie und Entstehung von Kontrollpunkten

Öffentlich-rechtliche Kontrollpunkte sind hierarchisch gegliedert:

- Kontrollbereich (zum Beispiel Lebensmittelsicherheit)
  - Kontrollrubrik (zum Beispiel Tierarzneimittel)
    - Punktegruppe (optional, zum Beispiel Schweinehaltung)
      - Kontrollpunkt (zum Beispiel «Aufbewahrungs- und
        Lagerungsvorschriften eingehalten»)

Das BLW legt die Kontrollrubriken und Kontrollpunkte des
Direktzahlungssystems fest, das BLV jene zu Tierschutz, Tiergesundheit
und Lebensmittelsicherheit. Zusätzlich führt das BLW seit 2020 eine
Kontrollrubrik «Gewässerschutz» für das Bundesamt für Umwelt (BAFU). Die
Rubriken und Punkte werden jeweils im Herbst mit Gültigkeit ab dem 1.
Januar des Folgejahres veröffentlicht. Kontrollpunkte können nicht zu
Rubriken hinzugefügt, oder entfernt werden. Kantonale Veterinärämter
erstellen zusätzliche kantonsspezifische Kontrollrubriken direkt in
Acontrol; die kantonsspezifischen Kontrollrubriken der
Landwirtschaftsämter werden nicht an Acontrol übermittelt.
Label-Organisationen erstellen ihre Kontrollpunkte selbständig und
passen Richtlinien und Ausnahmeregelungen bei Bedarf unterjährig an.
Führt eine Kontrollstelle öffentlich-rechtliche und privatrechtliche
Kontrollen gemeinsam durch, zum Beispiel bei Bio-Kontrollen, erhält sie
die öffentlich-rechtlichen Kontrollpunkte vom Kanton und die
privatrechtlichen von der Label-Organisation, zum Beispiel von Bio
Suisse. Sie führt dann eine Kontrolle mit allen Kontrollpunkten durch.
Bei der Kontrollplanung werden die Kontrollpunkte zusammengestellt und
die möglichen Ergebnisse, Massnahmen und Sanktionen definiert.

Damit bestehen vier Quellen von Kontrollpunkten: der Bund (BLW, BLV,
BAFU), die kantonalen Veterinärämter, die kantonalen
Landwirtschaftsämter und die Label-Organisationen. Die Anzahl der
Kontrollpunkte je Programm ist sehr unterschiedlich: Der Beitrag für den
Verzicht auf Pflanzenschutzmittel im Ackerbau umfasst einen
Kontrollpunkt, RAUS für Milchkühe rund zehn. Insgesamt gibt es in der
Schweiz mehrere tausend öffentlich-rechtliche und privatrechtliche
Kontrollpunkte; die Webanwendung Agricheck macht sie für
Bewirtschaftende zugänglich \[BLW26b\].

## Kontrolldaten heute

Daten aus öffentlich-rechtlichen Kontrollen sind für alle Betriebe,
deren Bewirtschafterinnen und Bewirtschafter der Weitergabe zustimmen,
über agridata.ch verfügbar. Pro Kontrollbereich wird ein Datenprodukt
angeboten; alle Datenprodukte haben dieselben Merkmale. Sie umfassen
Kontrollen aus dem laufenden und den drei vorangehenden Kalenderjahren
beziehungsweise seit dem letzten Bewirtschafterwechsel. Die tiefste
Ebene ist der Kontrollpunkt mit dem Kontrollergebnis und gegebenenfalls
der Mangelbeschreibung; Massnahmen sind nicht enthalten.

> [!IMPORTANT]
>
> Kontrolldaten enthalten keine Stammdaten von Betrieben und Personen,
> sondern nur Identifikatoren, die als Fremdschlüssel auf die Stammdaten
> im Agrarpolitischen Informationssystem (AGIS) verweisen. Dieser
> Grundsatz soll im künftigen Datenmodell
> (<a href="#sec-data-model" class="quarto-xref">Kapitel 4</a>)
> beibehalten werden.

# Akteure und Anwendungsfälle

## Akteure

<div id="tbl-actors">

Tabelle 1: Akteure des landwirtschaftlichen Kontrollwesens

| Akteur | Rolle im Kontrollwesen | Hauptinteresse an Kontrolldaten |
|:---|:---|:---|
| Bewirtschafterinnen und Bewirtschafter | Kontrollierte Personen, Datenproduzentinnen und Datenproduzenten | Weniger und besser koordinierte Kontrollen, Transparenz über die geltenden Anforderungen |
| BLW, BLV, BAFU | Herausgeber öffentlich-rechtlicher Kontrollpunkte, Oberaufsicht, Betrieb von Acontrol | Vergleichbare, vollständige und plausible Kontrolldaten |
| Kantonale Vollzugsbehörden und Kontrollkoordinationsstellen | Auftraggeber und Verwerter öffentlich-rechtlicher Kontrollen | Einheitliche Datenlieferungen, automatisierte Mängelmeldungen |
| Kontrollstellen (zum Beispiel bio.inspecta, Agrosolution, KUT, KOL) | Durchführung öffentlich-rechtlicher und privatrechtlicher Kontrollen | Ein nationales Schema statt vieler kantonaler Lösungen, Zugriff auf Basisinformationen |
| Label-Organisationen (zum Beispiel Bio Suisse, IP-Suisse, Mutterkuh Schweiz, QM Schweizer Fleisch) | Herausgeber privatrechtlicher Kontrollpunkte, Datenbezüger | Öffentlich-rechtliche Ergebnisse wiederverwenden und eigene Kontrollen reduzieren |
| agridata.ch | Datenübertragungsdienst | Klar beschriebene Datenprodukte, rechtlich abgestützte Einwilligungen |

</div>

## Anwendungsfälle

<div id="tbl-use-cases">

Tabelle 2: Anwendungsfälle des landwirtschaftlichen Kontrollwesens

| ID | Anwendungsfall | Akteure | Benötigte Geschäftsobjekte | Quelle |
|:---|:---|:---|:---|:---|
| UC-01 | Eine Label-Organisation bezieht mit Einwilligung der Bewirtschafterin oder des Bewirtschafters öffentlich-rechtliche Kontrolldaten, um auf eigene Kontrollen zu verzichten oder sie zu vereinfachen (zum Beispiel beef control für Mutterkuh Schweiz, IP-Suisse). | Label-Organisation, BLW, Bewirtschafter/in | Kontrolle, Kontrollumfang, Kontrollergebnis, Mangel, Programmteilnahme | Entwurf, Mutterkuh Schweiz, IP-Suisse |
| UC-02 | Eine Label-Organisation will wissen, ob ein öffentlich-rechtliches Programm (ÖLN, BTS, RAUS, GMF) erfüllt ist; ein Programm kann auch mit einzelnen Mängeln erfüllt sein (der ÖLN gilt zum Beispiel erst ab 110 Sanktionspunkten als nicht erfüllt). | Label-Organisation | Programmteilnahme mit Programmerfüllung, Zertifikat, Sanktion | Entwurf, erweitert (Mutterkuh Schweiz) |
| UC-03 | Eine Kontrollstelle meldet meldepflichtige Mängel strukturiert an die zuständigen Akteure (Landwirtschaftsamt, Kantonschemiker, Gewässerschutz) statt per E-Mail. Die Empfänger filtern die für sie relevanten Resultate. | Kontrollstelle, Kantone, Kantonschemiker, Gewässerschutz | Mangel, Massnahme, Organisation, Kontrollpunkt mit zu informierenden Akteuren | Entwurf, erweitert (Bio.Inspecta) |
| UC-04 | Eine Organisation prüft, welche ihrer Kontrollpunkte durch Kontrollpunkte einer anderen Herausgeberin bereits abgedeckt sind (zum Beispiel QM Schweizer Fleisch und Tierschutz, Demeter und Bio Suisse). | Label-Organisationen, Bund | Kontrollpunkt, Anforderung, Entsprechung von Kontrollpunkten | Entwurf, QM-SF |
| UC-05 | Kontrollergebnisse werden bei einem Bewirtschafterwechsel der verantwortlichen Person zugeordnet, damit Nachfolgerinnen und Nachfolger nicht mit Mängeln konfrontiert werden. | Kantone, Label-Organisationen | Kontrolle, Bewirtschafter/in | Entwurf, KIP |
| UC-06 | Kontrollergebnisse eines Betriebs mit Produktionsstätten in mehreren Kantonen werden der richtigen Produktionsstätte zugeordnet. | Kantone, Kontrollstellen | Betrieb, Produktionsstätte, Tierhaltung | Entwurf, KIP |
| UC-07 | Das BLW plausibilisiert die jährlich gelieferten Kontrolldaten und erkennt, welche Kontrollpunkte tatsächlich kontrolliert wurden. | BLW, Kantone | Kontrollumfang, Kontrollergebnis | Entwurf |
| UC-08 | Kontrollergebnisse werden durch Fotos, Dokumente oder Satellitenbilder belegt und automatisiert oder aufgrund von Selbstdeklarationen erzeugt. | Kontrollstellen, Kantone, BLV | Nachweis, Erhebungsmethode | Entwurf |
| UC-09 | Bewirtschafterinnen und Bewirtschafter und Kontrollstellen sehen, welche Kontrollpunkte für einen Betrieb gelten. | Bewirtschafter/in, Kontrollstellen | Kontrollpunkt, Programmteilnahme | Entwurf |
| UC-10 | Kantonale Landwirtschafts- und Veterinärämter koordinieren ihre öffentlich-rechtlichen Kontrollen, damit ein Betrieb nicht mehrmals pro Jahr von verschiedenen Kontrollpersonen kontrolliert wird. | Kantone (Landwirtschaftsämter, Veterinärämter), Kontrollstellen | Kontrolle, Kontrollumfang, Betrieb | IP-Suisse |
| UC-11 | Eine Label-Organisation bezieht Mängel, Tierzahlen und -kategorien sowie Tierwohlprogramme ohne Rückfrage beim Produzenten (setzt einen rechtlich erlaubten Austausch voraus). | Label-Organisation, Bewirtschafter/in | Mangel, Tierhaltung, Programmteilnahme | QM-SF |
| UC-12 | Eine Label-Organisation bezieht die Ergebnisse kontrollierter Nährstoffbilanzen für die wenigen Betriebe, die sie benötigt, heute per Post oder E-Mail. | Label-Organisation, Kantone | Kontrolle, Kontrollergebnis, Nachweis | Mutterkuh Schweiz |
| UC-13 | Eine Kontrollstelle führt öffentlich-rechtliche und privatrechtliche Kontrollpunkte in einer Kontrolle durch. Die Kantone erhalten nur die öffentlich-rechtlichen Resultate. | Kontrollstelle, Kantone, Label-Organisation | Kontrollpunkt, Kontrolle, Kontrollergebnis | Bio.Inspecta |
| UC-14 | Auf demselben Kontrollpunkt entstehen mehrere Sanktionsarten (zum Beispiel nach Bio-Verordnung und nach Bio Suisse), die getrennt ausgewiesen werden. | Kontrollstellen, Kantone, Label-Organisationen | Kontrollpunkt, Mangel, Sanktion | Bio.Inspecta |
| UC-15 | Kontrollorganisationen beziehen privatrechtliche Kontrolldaten, die Kantone speichern, zentral, standardisiert und tagesaktuell (agridata.ch) statt einzeln bei jedem Kanton. | Kontrollorganisationen, Kantone, BLW | Kontrolle, Kontrollergebnis, Mangel | Bio.Inspecta |
| UC-16 | Alle Kontrollresultate eines Betriebs aus allen Kontrollen sind an einer Stelle verfügbar. | Kantone, Kontrollstellen, Label-Organisationen | Betrieb, Kontrolle, Kontrollergebnis | Bio.Inspecta |
| UC-17 | Bei Feststellungen ausserhalb des Kontrollauftrags (zum Beispiel ungepflegte Klauen) ist erkennbar, ob die Kontrollperson dafür qualifiziert ist. So lässt sich beurteilen, ob eine Folgekontrolle (zum Beispiel durch Veterinärinnen und Veterinäre) nötig ist. | Kontrollstellen, Kantone | Kontrollperson mit Qualifikation, Kontrollergebnis | Bio.Inspecta |
| UC-18 | Kontrollorganisationen planen Kontrollen anhand aktueller Anmeldedaten für die Direktzahlungsprogramme. | Kontrollorganisationen, Kantone, BLW | Programmteilnahme, Kontrollpunkt, Kontrollumfang | Bio.Inspecta |
| UC-19 | Private Kontrollorganisationen melden Mängel zu Anforderungen der Direktzahlungsprogramme an Acontrol oder die Kantone, damit Kürzungen geprüft werden können (offen, ob und wie das heute geschieht). | Label-Organisationen, Kontrollstellen, Kantone | Mangel, Kontrollpunkt, Massnahme | Marie Zufferey |
| UC-20 | Acontrol setzt Kontrollpunkte von Programmen, für die ein Betrieb nicht angemeldet ist, anhand der AGIS-Anmeldedaten beim Import automatisch auf «nicht zutreffend». | BLW, Kantone | Kontrollpunkt, Programmteilnahme, Kontrollergebnis | Marie Zufferey |

</div>

## Einschränkungen der heutigen Kontrolldaten

Die Wiederverwendbarkeit öffentlich-rechtlicher Kontrolldaten entspricht
nicht den Bedürfnissen der Akteure. Das liegt teils an der Form der
Daten, die ihre Interpretation erschwert, teils am Umfang der erhobenen
Daten. Während die Form der bereits erhobenen Daten durch einheitliche
Begriffe und ein künftiges Datenmodell verbessert werden kann, lässt
sich die Datenerhebung selbst nur mit grossem Aufwand erweitern.

**Fehlende einheitliche Definitionen.** Datenbezügerinnen und
Datenbezüger haben Schwierigkeiten, Kontrolldaten zu interpretieren,
weil die Begriffe in den Kontrollpunkten nicht einheitlich definiert
sind. Semantische Interoperabilität setzt voraus, dass alle Akteure
Begriffsdefinitionen aus demselben Glossar verwenden
(<a href="#sec-glossary" class="quarto-xref">Kapitel 3</a>).

**Begrenzter Informationsgehalt der Kontrollergebnisse.** In Acontrol
können nur die Ergebnisse «Mangel», «nicht zutreffend» (NZ) und «nicht
kontrolliert» (NK) erfasst werden; fehlt ein Ergebnis, gilt der
Kontrollpunkt als «ohne Mangel». Bei Grundkontrollen müssen zudem nur
die Fokuskontrollpunkte geprüft werden, und nicht geprüfte übrige
Kontrollpunkte müssen nicht als «nicht kontrolliert» gekennzeichnet
werden. Das senkt den Erfassungsaufwand, führt aber dazu, dass nicht
erkennbar ist, welche Kontrollpunkte tatsächlich kontrolliert wurden. In
der Applikation eControls im Kanton Wallis wird für jeden Kontrollpunkt
ein explizites Ergebnis («in Ordnung», «Mangel», «nicht kontrolliert»
oder «nicht zutreffend») verlangtund setzen bei Fokuskontrollen nicht
gezielt geprüfte Kontrollpunkte automatisch auf «nicht kontrolliert». Es
gibt noch Fehlerquellen und teilweise werden Kontrollpunkte von
Programmen, für die ein Betrieb nicht angemeldet ist, mit «in Ordnung»
statt «nicht zutreffend» erfasst. Das betrifft insbesondere die
Tierwohlprogramme: Die Tierbestandsdaten für die Berechnung der
Direktzahlungen liegen ein Jahr zurück, und die Anmeldungen für
Direktzahlungsprogramme werden nicht immer geprüft.

> [!NOTE]
>
> ### Das Chüngeli-Problem
>
> Acontrol kennt die Kontrollrubriken nur als Ganzes. Planen Kantone
> Kontrollen mit einzelnen Kontrollpunkten und liefern nur diese,
> ergänzt Acontrol die übrigen Kontrollpunkte der Rubrik automatisch mit
> dem Ergebnis «ohne Mangel». So entstehen Ergebnisse zu
> Kontrollpunkten, die gar nicht kontrolliert wurden, zum Beispiel zur
> Haltung von Straussen auf Betrieben, die nur Hühner halten.

**Sammel-Kontrollpunkte.** Manche Kontrollpunkte fassen viele
Anforderungen zusammen, zum Beispiel «BFF-Auflagen eingehalten».
Label-Organisationen können dann nicht beurteilen, ob ihre spezifischen
Anforderungen geprüft wurden.

**Identifikation der Kontrollobjekte.** Kontrollergebnisse beziehen sich
je nach Bereich auf den Betrieb, die Produktionsstätte oder die
Tierhaltung. Label-Organisationen identifizieren ihre Mitglieder
teilweise nur über die TVD-Nummer, agridata.ch dagegen über UID und
BUR-Nummer; nicht bei jeder Tierhaltung ist eine TVD-Nummer hinterlegt.

**Limitierte historische Daten und Aktualität.** Über agridata.ch sind
höchstens die Kontrollen der letzten vier Kalenderjahre verfügbar, der
Kontrollrhythmus beträgt aber bis zu acht Jahre. Vor 2020 sind die Daten
lückenhaft. Zudem stehen Ergebnisse oft erst nach der Plausibilisierung
im Folgejahr zur Verfügung – für die Planung privatrechtlicher
Kontrollen häufig zu spät.

**Fehlende Angaben.** Fehlende Angaben in den heute verfügbaren
Kontrolldaten umfassen Massnahmen und Sanktionen, die Qualifikation der
Kontrollperson, die Erhebungsmethode und Nachweise wie Fotos. Auf einem
Kontrollpunkt können zudem verschiedene Massnahmen und Sanktionen
zutreffen, insbesondere wenn der Kontrollpunkt gleichzeitig im Rahmen
mehrerer Aufträge kontrolliert wurde (z.B. Bio-Verordnung und
Bio-Suisse). Die Qualifikation der Kontrollperson ist nötig, um bei
Feststellungen ausserhalb des Auftrags zu beurteilen, ob eine
Folgekontrolle ausgelöst werden muss.

# Fachglossar Kontrollwesen

Das Fachglossar Kontrollwesen definiert die für das landwirtschaftliche
Kontrollwesen relevanten Begriffe und ihre Beziehungen. Es dient als
*Single Source of Truth* für Begriffsdefinitionen und bildet die
Grundlage für das künftige logische Datenmodell
(<a href="#sec-data-model" class="quarto-xref">Kapitel 4</a>). Das
Glossar wird vom BLW gepflegt und kann aufgrund der Bedürfnisse des
Sektors erweitert und angepasst werden.

Die vollständige Liste der Begriffe findet sich in [Anhang
C](#sec-appendix-c).

## Aufbau des Glossars

Das Glossar ist wie in eCH-0265 als SKOS-Konzeptschema modelliert
\[MiBe09\]. Jeder Begriff ist ein `skos:Concept` mit einer dauerhaften
IRI im Namensraum `https://agriculture.ld.admin.ch/eCH-0264/1/term/` und
hat:

- eine Benennung (`schema:name`), wo verfügbar auch auf Französisch und
  Italienisch,
- Synonyme und Abkürzungen (`schema:alternateName`),
- eine Definition (`schema:description`),
- Anmerkungen und Kontextinformationen (`skos:scopeNote`),
- eine Quellenangabe (`schema:citation`), bei Rechtsbegriffen die
  Fundstelle auf fedlex.admin.ch,
- Beziehungen zu Ober-, Unter- und verwandten Begriffen (`skos:broader`,
  `skos:related`).

Die Begriffe sind in thematische Sammlungen (`skos:Collection`)
gegliedert: Akteure und Rollen; Kontrollobjekte und Identifikatoren;
Regelwerke, Programme und Anforderungen; Kontrollpunkte; Kontrolle und
Kontrollergebnis; Mängel, Massnahmen und Zertifizierung; Datenaustausch
und Systeme.

## Grundsätze der Terminologiearbeit

Die Definitionen folgen den Grundsätzen der Terminologiearbeit gemäss
ISO 704 und eCH-0128 \[eCH-0128\]:

- Wo vertrauenswürdige Definitionen bestehen, insbesondere in der
  Landwirtschaftlichen Begriffsverordnung \[LBV\] und der VKKL \[VKKL\],
  werden diese sinngemäss übernommen und mit ihrer Fundstelle angegeben.
- Definitionen nennen einen Oberbegriff und die abgrenzenden Merkmale;
  Aufzählungen von Unterarten sind abschliessend.
- Zirkelbezüge und Negativdefinitionen werden vermieden.
- Begriffe derselben Familie werden nach demselben Prinzip definiert.
- Informationen, die für das Verständnis wichtig, aber nicht Teil der
  Definition sind, stehen in den Anmerkungen.

Wo im Material für denselben Sachverhalt unterschiedliche Begriffe
verwendet werden, legt das Glossar eine Vorzugsbenennung fest und führt
die übrigen als Synonyme, zum Beispiel «Mangel» mit den Synonymen
«Beanstandung» und «Abweichung». Uneinheitlich verwendete Begriffe wie
«Teilbetrieb» werden mit einer Anmerkung auf die rechtlich definierten
Begriffe verwiesen.

## Governance

Damit das Glossar verlässlich bleibt, wird folgende Governance
umgesetzt:

- **Verantwortung:** Das BLW pflegt das Glossar im Rahmen der
  eCH-Fachgruppe AgriFood. Fachliche Entscheide werden in der
  Arbeitsgruppe Landwirtschaftliche Kontrolldaten vorbereitet.
- **Änderungsprozess:** Änderungsanträge werden als GitHub-Issue oder
  über <agridata.ch@blw.admin.ch> eingereicht, in der Arbeitsgruppe
  besprochen und als Pull Request umgesetzt. Automatisierte Tests
  stellen sicher, dass das Glossar konsistent bleibt.
- **Versionierung:** Das Glossar wird nach Semantic Versioning
  versioniert. Nur eine inkompatible Änderung erhöht die Hauptversion
  und damit den Namensraum
  (`https://agriculture.ld.admin.ch/eCH-0264/1/`).
- **Jahreszyklus:** Änderungen am Glossar werden auf die jährliche
  Veröffentlichung der öffentlich-rechtlichen Kontrollpunkte im Herbst
  abgestimmt.

# Logisches Datenmodell

> [!NOTE]
>
> ### In Erarbeitung
>
> Das logische Datenmodell ist noch in Erarbeitung, es wird in einer
> späteren Version ergänzt.

Das logische Datenmodell beschreibt die Geschäftsobjekte des
landwirtschaftlichen Kontrollwesens, ihre Merkmale und Beziehungen sowie
die zugehörigen Codelisten. Es baut auf den Begriffen des Fachglossars
(<a href="#sec-glossary" class="quarto-xref">Kapitel 3</a>) auf und
leitet sich aus den Anwendungsfällen und Bedürfnissen der Akteure ab
(**?@sec-use-cases**). Damit soll es insbesondere die heutigen
Einschränkungen der Kontrolldaten
(<a href="#sec-limitations" class="quarto-xref">Kapitel 2.3</a>)
adressieren, etwa die fehlende Unterscheidung zwischen kontrollierten
und nicht kontrollierten Kontrollpunkten.

Das Datenmodell legt fest, welche Objekte und Merkmale für den Austausch
von Kontrolldaten benötigt werden und was sie bedeuten. Es schreibt
nicht vor, wie einzelne Systeme ihre Daten intern speichern. Wie die
heutigen Kontrolldaten soll es keine Stammdaten von Betrieben und
Personen enthalten, sondern auf diese über Identifikatoren verweisen
(<a href="#sec-inspection-data" class="quarto-xref">Kapitel 1.6</a>).

# Haftungsausschluss

eCH-Standards, die der Verein eCH dem Anwender kostenlos zur Verfügung
stellt oder die auf eCH verweisen, haben nur den Status von
Empfehlungen. Der Verein eCH haftet in keinem Fall für Entscheidungen
oder Massnahmen, die der Anwender auf der Grundlage dieser Dokumente
trifft bzw. ergreift. Der Anwender ist dafür verantwortlich, die
Dokumente vor ihrer Verwendung selbst zu überprüfen und gegebenenfalls
fachlichen Rat einzuholen. eCH-Standards können und sollen die
technische, organisatorische oder rechtliche Beratung im Einzelfall
nicht ersetzen.

Dokumente, Verfahren, Methoden, Produkte und Standards, auf die in
eCH-Standards verwiesen wird, sind möglicherweise durch Marken-,
Urheber- oder Patentrechte geschützt. Es liegt in der ausschliesslichen
Verantwortung des Anwenders, die erforderlichen Lizenzen von den
berechtigten Personen und/oder Organisationen einzuholen.

Obwohl der Verein eCH bei der Erstellung der eCH-Standards mit
angemessener Sorgfalt vorgegangen ist, kann er keine Gewährleistung oder
Garantie dafür übernehmen, dass die bereitgestellten Informationen und
Dokumente aktuell, vollständig, richtig oder fehlerfrei sind. eCH behält
sich das Recht vor, die Inhalte der eCH-Standards jederzeit und ohne
vorherige Ankündigung zu ändern.

Jede Haftung für Schäden, die durch die Nutzung der eCH-Standards durch
den Anwender entstehen, wird im gesetzlich zulässigen Rahmen
ausgeschlossen.

# Urheberrechte

Personen, die eCH-Standards erarbeiten, bleiben Inhaber ihrer geistigen
Eigentumsrechte. Diese Personen verpflichten sich jedoch, ihre geistigen
Eigentumsrechte oder andere Rechte an geistigen Eigentumsrechten
Dritter, soweit möglich, den jeweiligen Fachgruppen und dem Verein eCH
kostenlos und zur uneingeschränkten Nutzung und Weiterentwicklung im
Rahmen des Vereinszwecks zur Verfügung zu stellen.

Die von den Fachgruppen erarbeiteten Standards dürfen unter Nennung des
jeweiligen Autors von eCH kostenlos und in uneingeschränktem Umfang
genutzt, verbreitet und weiterentwickelt werden.

eCH-Standards sind vollständig dokumentiert und frei von lizenz-
und/oder patentrechtlichen Einschränkungen. Die dazugehörige
Dokumentation kann kostenlos angefordert werden. Diese Bestimmungen
gelten jedoch nur für die von eCH erarbeiteten Standards, nicht aber für
Standards oder Produkte Dritter, die auf eCH-Standards verweisen. Die
Standards enthalten die entsprechenden Hinweise auf Rechte Dritter.

# Anhang A - Referenzen

<div id="refs" class="references csl-bib-body">

<div id="ref-biosuisse" class="csl-entry">

<span class="csl-left-margin">\[BioS26\]
</span><span class="csl-right-inline">Bio-Suisse:
[Bio-Suisse](https://www.bio-suisse.ch/de.html).</span>

</div>

<div id="ref-biov" class="csl-entry">

<span class="csl-left-margin">\[BIOV\]
</span><span class="csl-right-inline">Schweizerischer Bundesrat:
*[Verordnung über die biologische Landwirtschaft und die Kennzeichnung
biologisch produzierter Erzeugnisse und Lebensmittel (Bio-Verordnung,
BIOV; SR
910.18)](https://www.fedlex.admin.ch/eli/cc/1997/2498_2498_2498/de)* :
Schweizerische Eidgenossenschaft, 1997</span>

</div>

<div id="ref-blw2025aktionsplan" class="csl-entry">

<span class="csl-left-margin">\[BLW25\]
</span><span class="csl-right-inline"><span class="nocase">Bundesamt für
Landwirtschaft (BLW) u. a.</span>: [Aktionsplan Kontrollen auf
Landwirtschaftsbetrieben](https://www.blw.admin.ch/dam/de/sd-web/HtCH-BMgy5II/Aktionsplan%20Kontrollen%20Landwirtschaft%20-%20DE%20-%20von%20allen%20Teilnehmern%20unterzeichnet%2C%2004.09.25.pdf).</span>

</div>

<div id="ref-acontrol" class="csl-entry">

<span class="csl-left-margin">\[BLW26a\]
</span><span class="csl-right-inline">Bundesamt für Landwirtschaft
(BLW): [Anwendung
Acontrol](https://www.blw.admin.ch/de/anwendung-acontrol).</span>

</div>

<div id="ref-agricheck" class="csl-entry">

<span class="csl-left-margin">\[BLW26b\]
</span><span class="csl-right-inline">Bundesamt für Landwirtschaft
(BLW): [Agricheck – Kontrollpunkte der Schweizer
Landwirtschaft](https://blw-ofag-ufag.github.io/agricheck/).</span>

</div>

<div id="ref-demeter" class="csl-entry">

<span class="csl-left-margin">\[Dem26\]
</span><span class="csl-right-inline">Demeter: [Biologisch-dynamische
Landwirtschaft Demeter](https://demeter.ch/).</span>

</div>

<div id="ref-dzv" class="csl-entry">

<span class="csl-left-margin">\[DZV\]
</span><span class="csl-right-inline">Schweizerischer Bundesrat:
*[Verordnung vom 23. Oktober 2013 über die Direktzahlungen an die
Landwirtschaft (Direktzahlungsverordnung, DZV; SR
910.13)](https://www.fedlex.admin.ch/eli/cc/2013/765/de)* :
Schweizerische Eidgenossenschaft, 2013</span>

</div>

<div id="ref-eCH-0128:1.1" class="csl-entry">

<span class="csl-left-margin">\[eCH-0128\]
</span><span class="csl-right-inline"><span class="nocase">eCH-Fachgruppe
Terminologie</span>: *[eCH-0128 Fachsprachliche Glossare in
eCH-Dokumenten](https://www.ech.ch/de/ech/ech-0128/1.1)*
(eCH-Standard) : Verein eCH, 2016</span>

</div>

<div id="ref-ipsuisse" class="csl-entry">

<span class="csl-left-margin">\[IPS26\]
</span><span class="csl-right-inline">IP-Suisse: [Integrierte Produktion
IP-Suisse](https://www.ipsuisse.ch/).</span>

</div>

<div id="ref-lbv" class="csl-entry">

<span class="csl-left-margin">\[LBV\]
</span><span class="csl-right-inline">Schweizerischer Bundesrat:
*[Verordnung vom 7. Dezember 1998 über landwirtschaftliche Begriffe und
die Anerkennung von Betriebsformen (Landwirtschaftliche
Begriffsverordnung, LBV; SR
910.91)](https://www.fedlex.admin.ch/eli/cc/1999/13/de)* :
Schweizerische Eidgenossenschaft, 1998</span>

</div>

<div id="ref-skos" class="csl-entry">

<span class="csl-left-margin">\[MiBe09\]
</span><span class="csl-right-inline">Miles, Alistair ; Bechhofer, Sean:
*[SKOS Simple Knowledge Organization System
Reference](https://www.w3.org/TR/skos-reference/)* (W3C
Recommendation) : World Wide Web Consortium (W3C), 2009</span>

</div>

<div id="ref-vkkl" class="csl-entry">

<span class="csl-left-margin">\[VKKL\]
</span><span class="csl-right-inline">Schweizerischer Bundesrat:
*[Verordnung vom 31. Oktober 2018 über die Koordination der Kontrollen
auf Landwirtschaftsbetrieben (VKKL; SR
910.15)](https://www.fedlex.admin.ch/eli/cc/2018/673/de)* :
Schweizerische Eidgenossenschaft, 2018</span>

</div>

</div>

# Anhang B - Mitwirkung und Prüfung

Folgende Personen wirken in der Arbeitsgruppe Landwirtschaftliche
Kontrolldaten der eCH-Fachgruppe AgriFood mit.

<div id="tbl-authors">

Tabelle 3: Mitglieder der Arbeitsgruppe Landwirtschaftliche
Kontrolldaten

| Name | Organisation |
|:---|:---|
| Peter Althaus | IP-Suisse |
| Matthias Baumann | Bundesamt für Landwirtschaft BLW |
| Marc Beringer | Bundesamt für Landwirtschaft BLW |
| Claudia Blumenstein | Bundesamt für Landwirtschaft BLW |
| Daniel Bretscher | Agroscope |
| Egon Brüstle | Modan AG |
| Lorenz Escher | Koordinationsgruppe Integrierte Produktion KIP |
| Jonas Eyer | Schweizer Bauernverband SBV |
| Florian Frauchiger | Vereinigung der Schweizer Kantonstierärztinnen und Kantonstierärzte VSKT |
| Marcel Friedli | Prométerre |
| Sara Gomez | Bio Suisse |
| Sabine Grob | Agriquali Schweizer Bauernverband |
| Simon Hasler | Bundesamt für Landwirtschaft BLW |
| Christoph Keller | Vereinigung der Schweizer Kantonstierärztinnen und Kantonstierärzte VSKT |
| Daniel Meyer | Bundesamt für Landwirtschaft BLW |
| Daniel Moos | bio.inspecta AG |
| Damian Oswald | Bundesamt für Landwirtschaft BLW |
| Sara Schärrer | Bundesamt für Lebensmittelsicherheit und Veterinärwesen BLV |
| Rahel Schelbert | Bundesamt für Landwirtschaft BLW |
| Monika Schober | Agrosolution AG |
| Lea Stauber | Bundesamt für Landwirtschaft BLW |
| Roman Steiger | Kontrolldienst KUT |
| Yuval Tempelman | Bundesamt für Lebensmittelsicherheit und Veterinärwesen BLV |
| Fiorella Tettamanti | Bundesamt für Lebensmittelsicherheit und Veterinärwesen BLV |
| Christian Wilda | Bundesamt für Landwirtschaft BLW |
| Meike Wollenberg Martínez | Mutterkuh Schweiz |
| Marie Zufferey | Kanton Wallis |

</div>

# Anhang C - Abkürzungen und Glossar

<div id="tbl-glossary">

Tabelle 4: **Fachglossar Kontrollwesen:** Das Fachglossar Kontrollwesen
definiert die Begriffe des landwirtschaftlichen Kontrollwesens der
Schweiz, die für den Austausch und die Wiederverwendung von
Kontrolldaten zwischen Bund, Kantonen, Kontrollstellen und
Label-Organisationen benötigt werden. Es dient als Single Source of
Truth für die semantische Interoperabilität und als Grundlage für das
künftige logische Datenmodell von eCH-0264. Definitionen mit
Quellenangabe wurden sinngemäss aus der genannten Quelle übernommen.

<table>
<colgroup>
<col style="width: 35%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Begriff</th>
<th style="text-align: left;">Beschreibung</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><strong>ACmobile</strong></td>
<td style="text-align: left;"><p>Mobile Anwendung zur Erfassung von
Kontrollergebnissen auf dem Tablet, deren Checklisten auf den
Kontrollrubriken von Acontrol beruhen.</p>
<p><em>Oberbegriff</em>: Acontrol</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Acontrol</strong></td>
<td style="text-align: left;"><p>Informationssystem des Bundes, in dem
die Daten der öffentlich-rechtlichen Kontrollen in der
landwirtschaftlichen Primärproduktion zusammengeführt werden.</p>
<p><em>Verwandt</em>: Kantonales Agrarinformationssystem</p></td>
</tr>
<tr>
<td
style="text-align: left;"><strong>AGIS-Betriebsidentifikationsnummer</strong>
(AGIS_ID_B)</td>
<td style="text-align: left;"><p>Identifikationsnummer eines Betriebs im
Agrarpolitischen Informationssystem AGIS.</p>
<p><em>Oberbegriff</em>: Identifikator</p></td>
</tr>
<tr>
<td
style="text-align: left;"><strong>AGIS-Personenidentifikationsnummer</strong>
(AGIS_ID_P)</td>
<td style="text-align: left;"><p>Identifikationsnummer einer Person im
Agrarpolitischen Informationssystem AGIS.</p>
<p><em>Oberbegriff</em>: Identifikator</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Agrarpolitisches
Informationssystem</strong> (AGIS)</td>
<td style="text-align: left;"><p>Informationssystem des Bundes, in dem
die Kantone die Struktur- und Direktzahlungsdaten der Betriebe,
Personen, Flächen und Tiere zusammenführen.</p>
<p><em>Verwandt</em>: Identifikator, Kantonales
Agrarinformationssystem</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Agricheck</strong></td>
<td style="text-align: left;"><p>Webanwendung des BLW, mit der
Bewirtschafterinnen und Bewirtschafter die öffentlich-rechtlichen und
privatrechtlichen Kontrollpunkte abfragen können.</p>
<p><em>Verwandt</em>: Kontrollpunkt</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>agridata.ch</strong></td>
<td style="text-align: left;"><p>Nationaler Datenübertragungsdienst für
den sicheren und standardisierten Austausch landwirtschaftlicher Daten
mit Einverständnis der Datenproduzentinnen und Datenproduzenten.</p>
<p><em>Verwandt</em>: Once-Only-Prinzip</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Akkreditierung</strong></td>
<td style="text-align: left;"><p>Formelle Anerkennung der fachlichen
Kompetenz einer Kontroll- oder Zertifizierungsstelle, Kontrollen nach
einer bestimmten Norm durchzuführen.</p>
<p><em>Verwandt</em>: Kontrollstelle</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Aktionsplan Kontrollen auf
Landwirtschaftsbetrieben</strong></td>
<td style="text-align: left;"><p>Von Bund, Kantonen und
privatrechtlichen Organisationen am 4. September 2025 unterzeichneter
Plan mit Massnahmen, um die Zahl der Grund- oder Standardkontrollen auf
höchstens eine pro Jahr und Betrieb zu senken und öffentlich-rechtliche
und privatrechtliche Kontrollen zu optimieren.</p>
<p><em>Verwandt</em>: Kontrollkoordination</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Amtliche Fachassistentin oder
amtlicher Fachassistent</strong></td>
<td style="text-align: left;"><p>Qualifikation für Personen, die im
öffentlichen Veterinärwesen in einem bestimmten Fachbereich, zum
Beispiel Tierschutz, amtliche Kontrollen durchführen.</p>
<p><em>Oberbegriff</em>: Qualifikation</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Anforderung</strong>
(Vorgabe)</td>
<td style="text-align: left;"><p>Einzelne verbindliche Vorgabe aus einem
Regelwerk, die auf einem Kontrollobjekt einzuhalten ist.</p>
<p><em>Verwandt</em>: Kontrollpunkt, Regelwerk,
Sammel-Kontrollpunkt</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Begleitgruppe Landwirtschaftliche
Kontrollen</strong> (BG LaKo)</td>
<td style="text-align: left;"><p>Von BLW und Schweizer Bauernverband
gemeinsam geleitetes Gremium, das den Austausch zwischen den Akteuren
des landwirtschaftlichen Kontrollwesens etabliert und die Umsetzung des
Aktionsplans Kontrollen begleitet.</p>
<p><em>Oberbegriff</em>: Aktionsplan Kontrollen auf
Landwirtschaftsbetrieben</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Besonders tierfreundliche
Stallhaltungssysteme</strong> (BTS)</td>
<td style="text-align: left;"><p>Direktzahlungsprogramm des Tierwohls,
das Beiträge für die Haltung von Nutztieren in besonders
tierfreundlichen Stallhaltungssystemen ausrichtet.</p>
<p><em>Oberbegriff</em>: Direktzahlungsprogramm</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Betrieb</strong>
(Ganzjahresbetrieb)</td>
<td style="text-align: left;"><p>Landwirtschaftliches Unternehmen, das
Pflanzenbau, Nutztierhaltung oder beide Betriebszweige betreibt, eine
oder mehrere Produktionsstätten umfasst, rechtlich, wirtschaftlich,
organisatorisch und finanziell selbständig ist, ein eigenes
Betriebsergebnis ausweist und während des ganzen Jahres bewirtschaftet
wird.</p>
<p><em>Oberbegriff</em>: Kontrollobjekt</p>
<p><em>Verwandt</em>: Bewirtschafterin oder Bewirtschafter,
Produktionsstätte</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Bewegungsdaten</strong>
(Transaktionsdaten)</td>
<td style="text-align: left;"><p>Kontrolldaten, die bei einer einzelnen
Kontrolle entstehen, zum Beispiel Kontrollergebnisse, Mängel und
Massnahmen.</p>
<p><em>Oberbegriff</em>: Kontrolldaten</p>
<p><em>Verwandt</em>: Stammdaten</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Bewirtschafterin oder
Bewirtschafter</strong> (Bewirtschafter/in)</td>
<td style="text-align: left;"><p>Natürliche oder juristische Person oder
Personengesellschaft, die einen Betrieb auf eigene Rechnung und Gefahr
führt und damit das Geschäftsrisiko trägt.</p>
<p><em>Verwandt</em>: Betrieb, Datenproduzentin oder
Datenproduzent</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Bewirtschafterwechsel</strong>
(Betriebsleiterwechsel)</td>
<td style="text-align: left;"><p>Übergang der Bewirtschaftung eines
Betriebs von einer Bewirtschafterin oder einem Bewirtschafter auf eine
andere Person.</p>
<p><em>Oberbegriff</em>: Bewirtschafterin oder Bewirtschafter</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Bio-Verordnung</strong> (SR
910.18)</td>
<td style="text-align: left;"><p>Verordnung des Bundes über die
biologische Landwirtschaft und die Kennzeichnung biologisch produzierter
Erzeugnisse und Lebensmittel.</p>
<p><em>Oberbegriff</em>: Regelwerk</p></td>
</tr>
<tr>
<td
style="text-align: left;"><strong>Biodiversitätsförderfläche</strong>
(BFF)</td>
<td style="text-align: left;"><p>Landwirtschaftlich genutzte Fläche, die
nach den Anforderungen der Direktzahlungsverordnung zur Förderung der
Biodiversität bewirtschaftet wird und für die Biodiversitätsbeiträge
ausgerichtet werden.</p>
<p><em>Oberbegriff</em>: Direktzahlungsprogramm</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Bundesamt für
Landwirtschaft</strong> (BLW)</td>
<td style="text-align: left;"><p>Bundesamt, das die Kontrollrubriken und
Kontrollpunkte des Direktzahlungssystems festlegt, den Vollzug der VKKL
überwacht und das System Acontrol betreibt.</p>
<p><em>Oberbegriff</em>: Organisation</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Bundesamt für
Lebensmittelsicherheit und Veterinärwesen</strong> (BLV)</td>
<td style="text-align: left;"><p>Bundesamt, das die Kontrollrubriken und
Kontrollpunkte für die Bereiche Tierschutz, Tiergesundheit und
Lebensmittelsicherheit in der Primärproduktion festlegt.</p>
<p><em>Oberbegriff</em>: Organisation</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Bundesamt für Umwelt</strong>
(BAFU)</td>
<td style="text-align: left;"><p>Bundesamt, für das das BLW seit 2020
eine Kontrollrubrik zum Gewässerschutz in Acontrol führt.</p>
<p><em>Oberbegriff</em>: Organisation</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>BUR-Nummer</strong> (Nummer im
Betriebs- und Unternehmensregister)</td>
<td style="text-align: left;"><p>Identifikationsnummer eines Betriebs
oder einer Produktionsstätte im Betriebs- und Unternehmensregister (BUR)
des Bundesamts für Statistik.</p>
<p><em>Oberbegriff</em>: Identifikator</p>
<p><em>Verwandt</em>: Unternehmens-Identifikationsnummer</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Bürokontrolle</strong>
(Administrative Kontrolle)</td>
<td style="text-align: left;"><p>Kontrolle, die ohne Besuch des
Kontrollobjekts anhand von Unterlagen und digital verfügbaren Daten
durchgeführt wird.</p>
<p><em>Oberbegriff</em>: Kontrollart</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Chüngeli-Problem</strong></td>
<td style="text-align: left;"><p>Verfälschung von Kontrolldaten, die
entsteht, wenn ein System Kontrollpunkten, für die kein Ergebnis
übermittelt wurde, automatisch das Ergebnis «ohne Mangel» zuweist.</p>
<p><em>Oberbegriff</em>: Kontrollergebnis</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Codeliste</strong>
(Werteliste)</td>
<td style="text-align: left;">Abschliessende Liste der zulässigen Werte
eines Merkmals, in der jeder Wert einen eindeutigen Code und eine
Definition hat.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Datenanbieterin oder
Datenanbieter</strong> (Datenanbieter)</td>
<td style="text-align: left;"><p>Organisation oder System, das Daten
über agridata.ch bereitstellt.</p>
<p><em>Oberbegriff</em>: agridata.ch</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Datenbezügerin oder
Datenbezüger</strong> (Datenbezüger)</td>
<td style="text-align: left;"><p>Organisation, die Daten bei einer
Datenanbieterin anfordert und nutzt, zum Beispiel eine
Label-Organisation, die öffentlich-rechtliche Kontrolldaten bezieht.</p>
<p><em>Oberbegriff</em>: agridata.ch</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Datenprodukt</strong></td>
<td style="text-align: left;"><p>Standardisiertes Paket von Daten, das
eine Datenanbieterin über agridata.ch zum Bezug bereitstellt.</p>
<p><em>Oberbegriff</em>: agridata.ch</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Datenproduzentin oder
Datenproduzent</strong> (Datenproduzent)</td>
<td style="text-align: left;"><p>Bewirtschafterin, Bewirtschafter oder
Betrieb, deren oder dessen Daten nur mit Einverständnis weitergegeben
werden dürfen.</p>
<p><em>Oberbegriff</em>: agridata.ch</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Direktzahlungsprogramm</strong>
(Direktzahlungsart)</td>
<td style="text-align: left;"><p>Öffentlich-rechtliches Programm nach
der Direktzahlungsverordnung, für dessen Erfüllung ein Betrieb
Direktzahlungen erhält, zum Beispiel Tierwohlbeiträge oder
Biodiversitätsbeiträge.</p>
<p><em>Oberbegriff</em>: Programm</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Direktzahlungsverordnung</strong>
(SR 910.13)</td>
<td style="text-align: left;"><p>Verordnung des Bundes, welche die
Direktzahlungen an die Landwirtschaft, den ökologischen
Leistungsnachweis sowie die Kürzungen von Direktzahlungen bei Mängeln
regelt.</p>
<p><em>Oberbegriff</em>: Regelwerk</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Einverständnis</strong>
(Datenfreigabe)</td>
<td style="text-align: left;"><p>Zustimmung einer Datenproduzentin oder
eines Datenproduzenten zur Weitergabe bestimmter Daten an eine
Datenbezügerin.</p>
<p><em>Oberbegriff</em>: agridata.ch</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Entsprechung von
Kontrollpunkten</strong> (Kontrollpunkt-Mapping)</td>
<td style="text-align: left;"><p>Beziehung zwischen zwei Kontrollpunkten
verschiedener Herausgeberinnen, die angibt, ob sie dieselben,
weitergehende oder engere Anforderungen prüfen.</p>
<p><em>Oberbegriff</em>: Kontrollpunkt</p>
<p><em>Verwandt</em>: Anforderung</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Ergebnis Rubrik</strong>
(Rubrikergebnis)</td>
<td style="text-align: left;"><p>Zusammenfassendes Kontrollergebnis über
alle geprüften Kontrollpunkte einer Kontrollrubrik bei einer
Kontrolle.</p>
<p><em>Oberbegriff</em>: Kontrollergebnis</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Erhebungsmethode</strong>
(Kontrollmethode)</td>
<td style="text-align: left;"><p>Verfahren, mit dem ein Kontrollergebnis
ermittelt wird, nämlich Betriebsbegehung, Dokumentenprüfung, Befragung,
Fernerkundung, Selbstdeklaration oder automatisierte Datenprüfung.</p>
<p><em>Verwandt</em>: Nachweis</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Fokuskontrollpunkt</strong>
(FKP)</td>
<td style="text-align: left;"><p>Kontrollpunkt, der bei einer
Grundkontrolle zwingend geprüft werden muss.</p>
<p><em>Oberbegriff</em>: Kontrollpunkt</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Graslandbasierte Milch- und
Fleischproduktion</strong> (GMF)</td>
<td style="text-align: left;"><p>Direktzahlungsprogramm, das Beiträge
für eine Milch- und Fleischproduktion ausrichtet, die überwiegend auf
Wiesen- und Weidefutter beruht.</p>
<p><em>Oberbegriff</em>: Direktzahlungsprogramm</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Grundkontrolle</strong></td>
<td style="text-align: left;"><p>Kontrolle, mit der überprüft wird, ob
die Anforderungen auf dem ganzen Betrieb eingehalten werden, und die in
einer vorgeschriebenen Mindesthäufigkeit durchgeführt wird, in der Regel
mindestens einmal innerhalb von acht Jahren.</p>
<p><em>Oberbegriff</em>: Kontrolle</p>
<p><em>Verwandt</em>: Kontrollgrund</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Gültigkeitszeitraum</strong></td>
<td style="text-align: left;">Zeitspanne zwischen einem Anfangs- und
einem Enddatum, während der eine bestimmte Fassung eines Regelwerks,
einer Kontrollrubrik, eines Kontrollpunkts oder eines Zertifikats
anzuwenden ist.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Herausgeberin von
Kontrollpunkten</strong></td>
<td style="text-align: left;"><p>Organisation, die Kontrollpunkte
festlegt, veröffentlicht und für deren Inhalt verantwortlich ist.</p>
<p><em>Oberbegriff</em>: Organisation</p>
<p><em>Verwandt</em>: Kontrollpunkt</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Identifikator</strong>
(Identifikationsnummer)</td>
<td style="text-align: left;">Zeichenfolge, die ein Objekt innerhalb
eines bestimmten Registers oder Systems eindeutig bezeichnet.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Interoperabilität</strong></td>
<td style="text-align: left;">Fähigkeit von Organisationen und Systemen,
Daten auszutauschen und diese Daten ohne zusätzliche Absprachen
weiterzuverwenden.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Kantonale
Betriebsidentifikationsnummer</strong> (KT_ID_B)</td>
<td style="text-align: left;"><p>Identifikationsnummer eines Betriebs im
kantonalen Agrarinformationssystem.</p>
<p><em>Oberbegriff</em>: Identifikator</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Kantonale
Personenidentifikationsnummer</strong> (KT_ID_P)</td>
<td style="text-align: left;"><p>Identifikationsnummer einer Person im
kantonalen Agrarinformationssystem.</p>
<p><em>Oberbegriff</em>: Identifikator</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Kantonale Vollzugsbehörde</strong>
(Kantonale Vollzugsstelle)</td>
<td style="text-align: left;"><p>Kantonale Verwaltungseinheit, die für
den Vollzug bestimmter Verordnungen zuständig ist und dafür Kontrollen
in Auftrag gibt und deren Ergebnisse verwertet, zum Beispiel ein
Landwirtschaftsamt oder ein Veterinäramt.</p>
<p><em>Oberbegriff</em>: Organisation</p>
<p><em>Verwandt</em>: Kontrollkoordinationsstelle</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Kantonales
Agrarinformationssystem</strong> (KAIS)</td>
<td style="text-align: left;"><p>Informationssystem eines Kantons, in
dem Betriebs- und Strukturdaten erfasst und Kontrollergebnisse an
Acontrol übermittelt werden, zum Beispiel GELAN, Acorda oder LAWIS.</p>
<p><em>Verwandt</em>: Acontrol, Agrarpolitisches
Informationssystem</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Kantonsspezifischer
Kontrollpunkt</strong></td>
<td style="text-align: left;"><p>Kontrollpunkt, den eine kantonale
Vollzugsbehörde zusätzlich zu den Kontrollpunkten des Bundes
festlegt.</p>
<p><em>Oberbegriff</em>: Kontrollpunkt</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Kontrollart</strong></td>
<td style="text-align: left;"><p>Merkmal einer Kontrolle, das angibt, wo
sie durchgeführt wird, nämlich als Vor-Ort-Kontrolle auf dem
Kontrollobjekt oder als Bürokontrolle.</p>
<p><em>Verwandt</em>: Kontrollgrund, Unangemeldete Kontrolle</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Kontrollbereich</strong></td>
<td style="text-align: left;">Oberste Gliederungsebene der
öffentlich-rechtlichen Kontrollpunkte, die ein Rechtsgebiet oder eine
Gruppe von Programmen umfasst, zum Beispiel Lebensmittelsicherheit oder
Tierwohl.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Kontrollbericht</strong>
(Kontrollprotokoll)</td>
<td style="text-align: left;"><p>Dokument, das die Kontrollergebnisse
und festgestellten Mängel einer Kontrolle für die Bewirtschafterin oder
den Bewirtschafter und die Auftraggeberin zusammenfasst.</p>
<p><em>Oberbegriff</em>: Nachweis</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Kontrolldaten</strong></td>
<td style="text-align: left;"><p>Daten, die bei der Planung,
Durchführung und Auswertung von Kontrollen entstehen, nämlich
Kontrollgrunddaten, Kontrollergebnisse, Mängel und Massnahmen.</p>
<p><em>Verwandt</em>: Acontrol</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Kontrolldatum</strong></td>
<td style="text-align: left;"><p>Datum, an dem eine Kontrolle
durchgeführt wurde.</p>
<p><em>Oberbegriff</em>: Kontrolle</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Kontrolle</strong>
(Betriebskontrolle)</td>
<td style="text-align: left;"><p>Überprüfung der Einhaltung von
Anforderungen auf einem oder mehreren Kontrollobjekten durch eine
Kontrollstelle an einem bestimmten Datum.</p>
<p><em>Verwandt</em>: Kontrollobjekt, Kontrollstelle</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Kontrolleinheit</strong>
(Kontrollierte Einheit)</td>
<td style="text-align: left;"><p>Gesamtheit der Kontrollobjekte, die bei
einer Kontrolle gemeinsam kontrolliert werden.</p>
<p><em>Oberbegriff</em>: Kontrollobjekt</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Kontrollergebnis</strong>
(Testpunkt-Resultat)</td>
<td style="text-align: left;"><p>Feststellung zu einem Kontrollpunkt bei
einer Kontrolle, zum Beispiel «ohne Mangel», «Mangel», «nicht
zutreffend» oder «nicht kontrolliert».</p>
<p><em>Verwandt</em>: Kontrollpunkt, Mangel</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Kontrollgrund</strong></td>
<td style="text-align: left;"><p>Anlass, aus dem die Kontrollpunkte
einer Kontrollrubrik bei einer Kontrolle geprüft werden, nämlich eine
Grundkontrolle, eine der Arten risikobasierter Kontrollen oder eine
Zertifizierungskontrolle.</p>
<p><em>Verwandt</em>: Kontrollart, Kontrollumfang</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Kontrollgrunddaten</strong></td>
<td style="text-align: left;"><p>Kontrolldaten, die eine Kontrolle
beschreiben, ohne deren Ergebnisse zu enthalten, zum Beispiel der
Identifikator des Kontrollobjekts, das Kontrolldatum, die Kontrollstelle
und der Kontrollgrund.</p>
<p><em>Oberbegriff</em>: Kontrolldaten</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Kontrollkoordination</strong></td>
<td style="text-align: left;"><p>Abstimmung der Kontrollen verschiedener
Vollzugsbehörden und Kontrollstellen, sodass ein Betrieb in der Regel
nicht mehr als einmal pro Kalenderjahr kontrolliert wird.</p>
<p><em>Oberbegriff</em>: Kontrolle</p>
<p><em>Verwandt</em>: Begleitgruppe Landwirtschaftliche Kontrollen,
Kontrollkoordinationsstelle</p></td>
</tr>
<tr>
<td
style="text-align: left;"><strong>Kontrollkoordinationsstelle</strong></td>
<td style="text-align: left;"><p>Vom Kanton bezeichnete Stelle, welche
die Grundkontrollen auf den Betrieben koordiniert und den
Kontrollstellen vor Beginn einer Kontrollperiode mitteilt, auf welchen
Betrieben sie welche Bereiche wann und ob angemeldet oder unangemeldet
zu kontrollieren haben.</p>
<p><em>Oberbegriff</em>: Organisation</p>
<p><em>Verwandt</em>: Kantonale Vollzugsbehörde,
Kontrollkoordination</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Kontrollobjekt</strong></td>
<td style="text-align: left;"><p>Betrieb, Produktionsstätte oder
Tierhaltung, auf die sich eine Kontrolle bezieht.</p>
<p><em>Verwandt</em>: Kontrolle</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Kontrollperiode</strong></td>
<td style="text-align: left;"><p>Zeitraum, für den die
Kontrollkoordinationsstelle den Kontrollstellen die durchzuführenden
Kontrollen zuteilt, in der Regel ein Kalenderjahr.</p>
<p><em>Oberbegriff</em>: Kontrolle</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Kontrollperson</strong>
(Kontrolleur)</td>
<td style="text-align: left;"><p>Natürliche Person, die im Auftrag einer
Kontrollstelle Kontrollen durchführt.</p>
<p><em>Verwandt</em>: Kontrollstelle, Qualifikation</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Kontrollpunkt</strong>
(Checkpunkt)</td>
<td style="text-align: left;"><p>Prüfgegenstand einer Kontrolle, der
eine oder mehrere Anforderungen umfasst und für den bei einer Kontrolle
genau ein Kontrollergebnis festgehalten wird.</p>
<p><em>Oberbegriff</em>: Kontrollrubrik</p>
<p><em>Verwandt</em>: Anforderung, Herausgeberin von Kontrollpunkten,
Kontrollergebnis</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Kontrollrubrik</strong>
(Rubrik)</td>
<td style="text-align: left;"><p>Thematische Sammlung von
Kontrollpunkten innerhalb eines Kontrollbereichs, zum Beispiel
«Tierarzneimittel» im Kontrollbereich Lebensmittelsicherheit.</p>
<p><em>Oberbegriff</em>: Kontrollbereich</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Kontrollstelle</strong>
(Kontrollorganisation)</td>
<td style="text-align: left;"><p>Organisation, die im Auftrag einer
kantonalen Vollzugsbehörde oder einer Label-Organisation Kontrollen
durchführt.</p>
<p><em>Oberbegriff</em>: Organisation</p>
<p><em>Verwandt</em>: Akkreditierung, Kontrollperson,
Zertifizierungsstelle</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Kontrollumfang</strong></td>
<td style="text-align: left;"><p>Teil einer Kontrolle, der die aus einem
bestimmten Kontrollgrund geprüfte Kontrollrubrik und die Ergebnisse zu
deren Kontrollpunkten umfasst.</p>
<p><em>Oberbegriff</em>: Kontrolle</p>
<p><em>Verwandt</em>: Chüngeli-Problem, Kontrollgrund</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Kürzung von
Direktzahlungen</strong> (DZ-Kürzung)</td>
<td style="text-align: left;"><p>Öffentlich-rechtliche Massnahme, bei
der die Direktzahlungen eines Betriebs aufgrund von Mängeln nach den
Bestimmungen der Direktzahlungsverordnung reduziert werden.</p>
<p><em>Oberbegriff</em>: Massnahme</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Label-Organisation</strong>
(Labelinhaberin)</td>
<td style="text-align: left;"><p>Privatrechtliche Organisation, die in
Richtlinien Anforderungen an Produktionspraktiken festlegt, die über die
öffentlich-rechtlichen Anforderungen hinausgehen, und deren Einhaltung
durch Kontrollen und Zertifizierung prüfen lässt.</p>
<p><em>Oberbegriff</em>: Organisation</p>
<p><em>Verwandt</em>: Programm, Richtlinie</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Label-Programm</strong></td>
<td style="text-align: left;"><p>Privatrechtliches Programm einer
Label-Organisation, dessen Erfüllung zur Verwendung eines Labels
berechtigt.</p>
<p><em>Oberbegriff</em>: Programm</p>
<p><em>Verwandt</em>: Label-Organisation</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Landwirtschaftliche
Begriffsverordnung</strong> (SR 910.91)</td>
<td style="text-align: left;"><p>Verordnung des Bundes, die
landwirtschaftliche Begriffe wie Bewirtschafter, Betrieb,
Produktionsstätte und Tierhaltung rechtlich definiert.</p>
<p><em>Oberbegriff</em>: Regelwerk</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Mangel</strong>
(Nichtkonformität)</td>
<td style="text-align: left;"><p>Bei einer Kontrolle festgestellte
Nichteinhaltung einer oder mehrerer Anforderungen eines
Kontrollpunkts.</p>
<p><em>Verwandt</em>: Kontrollergebnis, Massnahme, Möglicher
Mangel</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Massnahme</strong> (Sanktion)</td>
<td style="text-align: left;"><p>Folge, die eine zuständige Organisation
aufgrund eines oder mehrerer Mängel anordnet, zum Beispiel eine Kürzung
von Direktzahlungen, eine Verwarnung, eine Auflage zur Mängelbehebung,
eine Nachkontrolle oder eine Label-Sanktion.</p>
<p><em>Verwandt</em>: Mangel</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Meine Agrardatenfreigabe</strong>
(MAF)</td>
<td style="text-align: left;"><p>Vorgängersystem von agridata.ch für die
Freigabe landwirtschaftlicher Daten an Dritte.</p>
<p><em>Oberbegriff</em>: agridata.ch</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Meldepflicht bei
Mängeln</strong></td>
<td style="text-align: left;"><p>Pflicht einer Kontrollperson oder
Kontrollstelle, einen festgestellten Verstoss der zuständigen
Vollzugsbehörde zu melden, auch wenn der Verstoss nicht Gegenstand ihres
Kontrollauftrags war.</p>
<p><em>Oberbegriff</em>: Mangel</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Merkmalskatalog
Acontrol</strong></td>
<td style="text-align: left;"><p>Technische Vorgabe, die zusammen mit
dem XSD-Schema und der Masterliste der Kontrollpunkte die Merkmale und
Wertebereiche für den Datenimport in Acontrol festlegt.</p>
<p><em>Oberbegriff</em>: Acontrol</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Möglicher Mangel</strong>
(Mangeltyp)</td>
<td style="text-align: left;"><p>Im Voraus festgelegte, typische
Abweichung zu einem Kontrollpunkt, auf die bei der Erfassung eines
Mangels verwiesen werden kann.</p>
<p><em>Oberbegriff</em>: Kontrollpunkt</p>
<p><em>Verwandt</em>: Mangel, Massnahme</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Nachkontrolle</strong></td>
<td style="text-align: left;"><p>Risikobasierte Kontrolle, die aufgrund
von Mängeln bei einer früheren Kontrolle durchgeführt wird.</p>
<p><em>Oberbegriff</em>: Risikobasierte Kontrolle</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Nachweis</strong>
(Mediendaten)</td>
<td style="text-align: left;">Datei, die eine Kontrolle, ein
Kontrollergebnis oder einen Mangel belegt, zum Beispiel ein Foto, ein
Dokument oder ein Satellitenbild.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Nicht kontrolliert</strong>
(NK)</td>
<td style="text-align: left;"><p>Wert eines Kontrollergebnisses, der
angibt, dass ein anwendbarer Kontrollpunkt bei der Kontrolle nicht
geprüft wurde.</p>
<p><em>Oberbegriff</em>: Kontrollergebnis</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Nicht zutreffend</strong>
(NZ)</td>
<td style="text-align: left;"><p>Wert eines Kontrollergebnisses, der
angibt, dass der Kontrollpunkt auf das Kontrollobjekt nicht anwendbar
ist, zum Beispiel weil die betreffende Tierkategorie nicht gehalten
wird.</p>
<p><em>Oberbegriff</em>: Kontrollergebnis</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Once-Only-Prinzip</strong></td>
<td style="text-align: left;">Grundsatz, nach dem Daten nur einmal
erfasst werden müssen und danach mehrfach genutzt werden können.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Organisation</strong></td>
<td style="text-align: left;">Behörde, Unternehmen oder Verein, das im
landwirtschaftlichen Kontrollwesen eine oder mehrere Rollen einnimmt,
zum Beispiel als Herausgeberin von Kontrollpunkten, Auftraggeberin,
Kontrollstelle, Zertifizierungsstelle, Datenanbieterin oder
Datenbezügerin.</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Privatrechtliche
Kontrolle</strong> (Labelkontrolle)</td>
<td style="text-align: left;"><p>Kontrolle, die im Auftrag einer
privatrechtlichen Organisation gestützt auf einen Vertrag und deren
Richtlinien durchgeführt wird.</p>
<p><em>Oberbegriff</em>: Kontrolle</p>
<p><em>Verwandt</em>: Label-Organisation, Rechtsnatur</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Produktionsstätte</strong></td>
<td style="text-align: left;"><p>Einheit von Land, Gebäuden und
Einrichtungen, die räumlich als solche erkennbar und von anderen
Produktionsstätten getrennt ist, auf der eine oder mehrere Personen
tätig sind und die eine oder mehrere Tierhaltungen umfasst.</p>
<p><em>Oberbegriff</em>: Kontrollobjekt</p>
<p><em>Verwandt</em>: BUR-Nummer, Betrieb, Tierhaltung</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Programm</strong></td>
<td style="text-align: left;"><p>Gesamtheit von Anforderungen, für deren
Einhaltung ein Betrieb Beiträge erhält oder ein Label verwenden darf und
an der er sich durch Anmeldung beteiligt.</p>
<p><em>Verwandt</em>: Label-Organisation</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Programmerfüllung</strong></td>
<td style="text-align: left;"><p>Gesamtbeurteilung, ob ein Betrieb die
Anforderungen eines Programms während eines Zeitraums erfüllt.</p>
<p><em>Oberbegriff</em>: Programm</p>
<p><em>Verwandt</em>: Programmteilnahme, Zertifikat</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Programmteilnahme</strong>
(Programmanmeldung)</td>
<td style="text-align: left;"><p>Beteiligung eines Betriebs an einem
Programm während eines bestimmten Zeitraums aufgrund einer
Anmeldung.</p>
<p><em>Oberbegriff</em>: Programm</p>
<p><em>Verwandt</em>: Programmerfüllung</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Punktegruppe</strong></td>
<td style="text-align: left;"><p>Optionale Gliederungsebene innerhalb
einer Kontrollrubrik, die zusammengehörende Kontrollpunkte bündelt, zum
Beispiel «Schweinehaltung».</p>
<p><em>Oberbegriff</em>: Kontrollrubrik</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Qualifikation</strong></td>
<td style="text-align: left;"><p>Nachgewiesene Befähigung einer
Kontrollperson, Kontrollen in einem bestimmten Bereich
durchzuführen.</p>
<p><em>Verwandt</em>: Kontrollperson</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Rechtliche
Interoperabilität</strong></td>
<td style="text-align: left;"><p>Interoperabilität, bei der
Organisationen aufgrund der Rechtsgrundlagen und Einwilligungen Daten
untereinander austauschen dürfen.</p>
<p><em>Oberbegriff</em>: Interoperabilität</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Rechtsnatur</strong></td>
<td style="text-align: left;"><p>Eigenschaft eines Regelwerks, einer
Kontrolle, eines Programms oder einer Massnahme, die angibt, ob sie auf
öffentlichem Recht oder auf privatrechtlichen Verträgen beruht.</p>
<p><em>Verwandt</em>: Privatrechtliche Kontrolle, Öffentlich-rechtliche
Kontrolle</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Regelmässiger Auslauf im
Freien</strong> (RAUS)</td>
<td style="text-align: left;"><p>Direktzahlungsprogramm des Tierwohls,
das Beiträge für den regelmässigen Auslauf von Nutztieren im Freien
ausrichtet.</p>
<p><em>Oberbegriff</em>: Direktzahlungsprogramm</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Regelwerk</strong></td>
<td style="text-align: left;"><p>Schriftlich festgelegte Sammlung von
Anforderungen, die von einer Organisation in einer bestimmten Fassung
erlassen wird, zum Beispiel ein Gesetz, eine Verordnung, eine Weisung,
eine Richtlinie oder ein Reglement.</p>
<p><em>Verwandt</em>: Anforderung, Rechtsnatur</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Richtlinie</strong>
(Reglement)</td>
<td style="text-align: left;"><p>Privatrechtliches Regelwerk einer
Label-Organisation, das die Anforderungen für die Verwendung eines
Labels festlegt.</p>
<p><em>Oberbegriff</em>: Regelwerk</p>
<p><em>Verwandt</em>: Label-Organisation</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Risikobasierte
Kontrolle</strong></td>
<td style="text-align: left;"><p>Kontrolle, die zusätzlich zu den
Grundkontrollen aufgrund von Mängeln bei früheren Kontrollen, eines
begründeten Verdachts, wesentlicher Änderungen auf dem Betrieb oder
jährlich festgelegter Risikobereiche durchgeführt wird.</p>
<p><em>Oberbegriff</em>: Kontrolle</p>
<p><em>Verwandt</em>: Kontrollgrund</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Sammel-Kontrollpunkt</strong></td>
<td style="text-align: left;"><p>Kontrollpunkt, der mehrere voneinander
unabhängige Anforderungen zu einem einzigen Kontrollergebnis
zusammenfasst.</p>
<p><em>Oberbegriff</em>: Kontrollpunkt</p>
<p><em>Verwandt</em>: Anforderung</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Sanktionspunkte</strong>
(Punkte)</td>
<td style="text-align: left;"><p>Masszahl, mit der ein Regelwerk die
Schwere eines Mangels bewertet und deren Summe über Art und Umfang einer
Massnahme entscheidet.</p>
<p><em>Oberbegriff</em>: Massnahme</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Selbstdeklaration</strong>
(Selbstcheckliste)</td>
<td style="text-align: left;"><p>Erhebungsmethode, bei der die
Bewirtschafterin oder der Bewirtschafter selbst Angaben zur Einhaltung
von Anforderungen macht, die von einer Kontrollstelle geprüft werden
können.</p>
<p><em>Oberbegriff</em>: Erhebungsmethode</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Semantische
Interoperabilität</strong></td>
<td style="text-align: left;"><p>Interoperabilität, bei der
Datenanbieter und Datenbezüger ausgetauschten Daten dieselbe Bedeutung
beimessen, weil sie Begriffe aus demselben Glossar verwenden.</p>
<p><em>Oberbegriff</em>: Interoperabilität</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Stammdaten</strong>
(Referenzdaten)</td>
<td style="text-align: left;"><p>Kontrolldaten, die über viele
Kontrollen hinweg unverändert gelten und auf die Bewegungsdaten
verweisen, zum Beispiel Kontrollpunkte, Kontrollrubriken,
Kontrollstellen und Codelisten.</p>
<p><em>Oberbegriff</em>: Kontrolldaten</p>
<p><em>Verwandt</em>: Bewegungsdaten, Codeliste</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Status der Kontrolle</strong>
(Kontrollstatus)</td>
<td style="text-align: left;"><p>Bearbeitungsstand einer Kontrolle von
der Erfassung der Ergebnisse über die Freigabe und die Massnahmen bis zu
einem allfälligen Rekurs.</p>
<p><em>Oberbegriff</em>: Kontrolle</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Sömmerungsbetrieb</strong></td>
<td style="text-align: left;"><p>Landwirtschaftliches Unternehmen, das
der Sömmerung von Tieren dient, von den Betrieben der Bestösser örtlich
getrennt ist, Sömmerungsweiden sowie die dafür nötigen Gebäude oder
Einrichtungen aufweist und während der Sömmerung bewirtschaftet
wird.</p>
<p><em>Oberbegriff</em>: Kontrollobjekt</p>
<p><em>Verwandt</em>: Betrieb, Kontrolleinheit</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Technische
Interoperabilität</strong></td>
<td style="text-align: left;"><p>Interoperabilität, bei der Systeme
Daten über gemeinsame Datenstrukturen, Formate und Schnittstellen
maschinell austauschen.</p>
<p><em>Oberbegriff</em>: Interoperabilität</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Teilbetrieb</strong></td>
<td style="text-align: left;"><p>Organisatorisch abgegrenzter Teil eines
Betriebs, der für eine Kontrolle, eine Programmteilnahme oder eine
Zertifizierung gesondert betrachtet wird.</p>
<p><em>Oberbegriff</em>: Kontrollobjekt</p>
<p><em>Verwandt</em>: Produktionsstätte, Tierhaltung</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Tierhaltung</strong></td>
<td style="text-align: left;"><p>Stallungen und Einrichtungen, ohne
Weideunterstände oder Weidstadel, zum regelmässigen Halten von Tieren
auf einer Produktionsstätte oder auf einem Sömmerungs- oder
Gemeinschaftsweidebetrieb.</p>
<p><em>Oberbegriff</em>: Kontrollobjekt</p>
<p><em>Verwandt</em>: Produktionsstätte, TVD-Nummer</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>TVD-Nummer</strong> (TVD ID)</td>
<td style="text-align: left;"><p>Identifikationsnummer einer Tierhaltung
in der Tierverkehrsdatenbank.</p>
<p><em>Oberbegriff</em>: Identifikator</p>
<p><em>Verwandt</em>: Tierhaltung</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Unangemeldete
Kontrolle</strong></td>
<td style="text-align: left;"><p>Kontrolle, die der Bewirtschafterin
oder dem Bewirtschafter nicht im Voraus angekündigt wird.</p>
<p><em>Oberbegriff</em>: Kontrolle</p></td>
</tr>
<tr>
<td
style="text-align: left;"><strong>Unternehmens-Identifikationsnummer</strong>
(UID)</td>
<td style="text-align: left;"><p>Vom Bundesamt für Statistik vergebene,
eindeutige Identifikationsnummer eines Unternehmens in der Schweiz im
Format CHE-123.456.789.</p>
<p><em>Oberbegriff</em>: Identifikator</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Verordnung über den mehrjährigen
nationalen Kontrollplan für die Lebensmittelkette und die
Gebrauchsgegenstände</strong> (SR 817.032)</td>
<td style="text-align: left;"><p>Verordnung des Bundes, welche die
Kontrollen entlang der Lebensmittelkette einschliesslich der
Primärproduktion regelt.</p>
<p><em>Oberbegriff</em>: Regelwerk</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Verordnung über die Koordination
der Kontrollen auf Landwirtschaftsbetrieben</strong> (SR 910.15)</td>
<td style="text-align: left;"><p>Verordnung des Bundes, welche die
allgemeinen Anforderungen an Grundkontrollen und risikobasierte
Kontrollen, an Kontrollstellen und an die Koordination der Kontrollen
auf Landwirtschaftsbetrieben regelt.</p>
<p><em>Oberbegriff</em>: Regelwerk</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Verordnung über
Informationssysteme im Bereich der Landwirtschaft</strong> (SR
919.117.71)</td>
<td style="text-align: left;"><p>Verordnung des Bundes, welche die
Informationssysteme der Landwirtschaft, darunter Acontrol, sowie die
Weitergabe der darin enthaltenen Daten regelt.</p>
<p><em>Oberbegriff</em>: Regelwerk</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Vor-Ort-Kontrolle</strong></td>
<td style="text-align: left;"><p>Kontrolle, bei der die Kontrollperson
das Kontrollobjekt aufsucht.</p>
<p><em>Oberbegriff</em>: Kontrollart</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Zertifikat</strong>
(Zertifizierungsbestätigung)</td>
<td style="text-align: left;"><p>Bestätigung einer
Zertifizierungsstelle, dass ein Kontrollobjekt die Anforderungen eines
Programms während eines Gültigkeitszeitraums erfüllt.</p>
<p><em>Oberbegriff</em>: Zertifizierung</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Zertifizierung</strong></td>
<td style="text-align: left;"><p>Verfahren, in dem eine
Zertifizierungsstelle auf Grundlage von Kontrollergebnissen bestätigt,
dass ein Kontrollobjekt die Anforderungen eines Programms erfüllt.</p>
<p><em>Verwandt</em>: Zertifizierungsstelle</p></td>
</tr>
<tr>
<td
style="text-align: left;"><strong>Zertifizierungsstelle</strong></td>
<td style="text-align: left;"><p>Organisation, die auf Grundlage von
Kontrollergebnissen entscheidet, ob ein Zertifikat erteilt,
aufrechterhalten, suspendiert oder entzogen wird.</p>
<p><em>Oberbegriff</em>: Organisation</p>
<p><em>Verwandt</em>: Zertifikat</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Öffentlich-rechtliche
Kontrolle</strong> (Amtliche Kontrolle)</td>
<td style="text-align: left;"><p>Kontrolle, die im Auftrag einer Behörde
gestützt auf Bundesrecht oder kantonales Recht durchgeführt wird.</p>
<p><em>Oberbegriff</em>: Kontrolle</p>
<p><em>Verwandt</em>: Privatrechtliche Kontrolle, Rechtsnatur</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Ökologischer
Leistungsnachweis</strong> (ÖLN)</td>
<td style="text-align: left;"><p>Gesamtheit der ökologischen
Anforderungen, die ein Betrieb als Voraussetzung für den Bezug von
Direktzahlungen erfüllen muss.</p>
<p><em>Oberbegriff</em>: Programm</p></td>
</tr>
</tbody>
</table>

</div>

# Anhang D - Änderungen gegenüber der Vorversion

Dies ist die erste Version des Standards. Der Standard ersetzt die
frühere Kurzbeschreibung «Dieser Standard soll dabei helfen, Begriffe
und Daten im öffentlich-rechtlichen und privatrechtlichen Bereich des
landwirtschaftlichen Kontrollwesens zu harmonisieren, so dass
Kontrolldaten besser ausgetauscht beziehungsweise wiederverwendet werden
können.»

# Anhang E - Abbildungsverzeichnis

# Anhang F - Tabellenverzeichnis

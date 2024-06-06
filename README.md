- Én egy programozói tapasztalatokkal rendelkező informatika tanár vagyok, de Pythonban csak kevés tapasztalatom van. Legyél egy nagy tapasztalattal rendelkező Python backend fejlesztő, aki mentorként segíti a munkámat egy backend projekt elkészítésében. VS Code-ban fogok dolgozni. Lépésről lépésre haladjunk. Az egyes lépéseknél csak az adott lépéshez legszükségesebb információkat add meg. Elsőként készítsünk egy egyszerű hello world alkalmazást.
- Bővítsük a programot egy http://localhost:5000/ címen elérhető GET végpont elkészítésével. A végpont a "Hello, Dineease!" szöveget adja vissza.
- Ismerkedj meg a projektünkkel. Íme a projekt háttértörténete. Ha tudtad értelmezni, válaszolj "OK"-val. A történet: "A DineEase, egy magyarországi székhelyű kis startup, kezdetben innovatív éttermi szoftverével tűnt fel a vendéglátás szektorban. Most egy vadonatúj szolgáltatással bővítik tevékenységüket, amelynek célja, hogy forradalmasítsa az emberek étterem keresését és az éttermekkel való kapcsolatfelvételt. A DineEase mindenre kiterjedő portálján a látogatók választhatnak az éttermek között, megtekinthetik bármelyik étterem teljes étlapját, és elolvashatják a korábbi vendégek értékeléseit az étterem szolgáltatásairól és ételeiről. Emellett asztalt is foglalhatnak az általuk kiválasztott étteremben, és a weboldalon vagy az alkalmazáson keresztül rendelhetnek és fizethetnek. Korábban szabadúszó webfejlesztőként dolgoztál, de most fejlesztői állásra jelentkeztél a DineEase-nél. A vállalat vezetősége szeretné tesztelni a képességeidet, ezért a felvételi eljárás részeként arra kértek, hogy fejleszd ki az új szolgáltatásuk prototípusát.Első feladatként a DineEase szolgáltatás backend prototípusát kell létrehoznod. A backend adatokat biztosít a DineEase személyzete által kezelt admin alkalmazás és webalkalmazás számára."
- A backendhez sqlite adatbáziskezelőt fogunk használni. Az adatbázis a dineease.db fájlban található. A feltöltött képen láthatod az adatbázis szerkezetét. Írd le, hogy milyen táblák találhatók az adatbázisban, a táblák milyen mezőket tartalmaznak és milyen kapcsolat van a táblák között.
- Az SQLite adatbázis users táblájából írassuk ki a konzolra az összes felhasználó vezetéknevét (lastName), keresztnevét (firstName) és email címét (email).
- A backend feladatunkban az első megvalósítandó végpontok a felhasználókkal kapcsolatban. A feladtspecifikáció így szól: "A DineEase admin felületén lehetséges az étterem tulajdonos felhasználók listázása, valamint a felhasználó aktiválása és deaktiválása. Ehhez három végpontot kell létrehoznod: 1. összes felhasználó főbb adatainak lekérése 2. kiválasztott felhasználó összes adatának lekérése 3.felhasználó letiltása vagy aktiválása". Most csak az 1. végpontot készítsd el. Az adatbázis adatait használva a /users címen adja vissza a backendünk az összes felhasználó következő adatait: firstName, lastName, email, isActive. 

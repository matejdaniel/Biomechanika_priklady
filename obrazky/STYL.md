# Stylová příručka obrázků

Všechny obrázky ve sbírce mají jednotný **kreslený, ručně vypadající styl**. Tahle příručka platí pro obrázky kreslené v Pythonu (grafy, schémata) i pro ilustrace vytvořené v AI nástroji.

## 1. Typy obrázků

| Typ | Co obsahuje | Kdo / čím |
|---|---|---|
| **A – graf** | závislosti x–t, v–t, σ–ε, F–x, sloupcové grafy | Python (`zdroje/styl.py`) |
| **B – schéma** | síly, páky, kóty, souřadnice, tyče, bloky | Python (`zdroje/styl.py`) |
| **C – ilustrace** | lidé, anatomie, sportovní scény | AI nástroj (bez textu a šipek) |
| **C+B – ilustrace s popisky** | ilustrace + síly, kóty, body | AI ilustrace, popisky dokreslí Python |
| **D – bez obrázku** | příklad obrázek nepotřebuje | – |

**Pravidlo:** AI nikdy nekreslí čísla, písmena, šipky sil ani kóty. Ty se vždy doplňují v Pythonu, aby byly přesné, česky a ve stejném fontu.

## 2. Formát

- **PNG**, bílé pozadí, šířka **1200 px**, základní poměr stran **3 : 2** (1200 × 800 px).
- Okraj kolem kresby alespoň 40 px, nic se nedotýká hrany.
- Velikost souboru ideálně pod 500 kB.
- Jeden obrázek = jedna myšlenka. Pokud příklad potřebuje víc obrázků, dostanou přípony `_a`, `_b`.

## 3. Pojmenování

```
NNN_kapitola_label[_a|_b].png
```

- `NNN` – pořadí příkladu v kapitole (3 číslice),
- `kapitola_label` – label příkladu bez `ex-`, pomlčky nahrazené `_`,
- příklad: `040_statika_kralik.png` ↔ `ex-statika-kralik`.

Zdrojový skript se jmenuje stejně, jen s příponou `.py` (`zdroje/040_statika_kralik.py`). Podklad z AI má příponu `_ilustrace.png`.

## 4. Barvy (pevný význam)

| Barva | Hex | Význam |
|---|---|---|
| tmavě šedá | `#222222` | obrysy, osy, běžný text |
| červená | `#d62828` | **síly** (šipka s plnou hlavičkou); hlavní křivka v grafu |
| oranžová | `#f77f00` | **momenty** (obloukové šipky) |
| fialová | `#7b2cbf` | **rychlost, zrychlení** |
| modrá | `#1d6fd1` | **kóty, úhly, vzdálenosti** |
| zelená | `#2a9d4b` | **těžiště, body, osy otáčení** |

Výplně těles: kost `#f1e3c8`, sval `#e07a7a`, kůže `#f6d5bf`, dřevo `#8b5a2b`.

Barvu nikdy nepoužívej jen pro ozdobu. Červená šipka vždy znamená sílu.

## 5. Písmo a popisky

- Font **Caveat** (`zdroje/Caveat-Regular.ttf`, licence OFL), velikost 20 pt (kóty 18 pt).
- Veličiny s indexy zapisuj přes LaTeX: `$F_m$`, `$G_1$`, `$T_2$`.
- Číslo a jednotka s mezerou, desetinná čárka: `0,6 m`, `3,5 cm`, `60°`.
- Popisek u síly stojí u hrotu šipky, popisek kóty uprostřed kóty.
- Žádné nadpisy v obrázku. Název a popis patří do textu příkladu.

## 6. Čáry a šipky

- Obrysy těles: 2,4 pt. Kóty a osy: 1,6 pt.
- Síla: plná hlavička (`-|>`). Kóta: oboustranná otevřená šipka (`<->`).
- Úhel: modrý oblouk s hodnotou.
- Těžiště a body: zelený plný kruh.
- Roztřesení čar zajišťuje `start()` v `styl.py`. Neměň jeho parametry, jinak obrázky přestanou ladit.

## 7. Grafy (typ A)

- Bez horního a pravého rámečku, jemná mřížka (`graf(ax)`).
- Popisky os ve tvaru `veličina [jednotka]`, např. `t [s]`, `σ [MPa]`.
- Hodnoty přesně podle zadání. Graf musí jít z obrázku odečíst.

## 8. Ilustrace z AI (typ C)

**Doporučený nástroj:** Google Gemini, model **Nano Banana Pro**. Umí pracovat s několika referenčními obrázky najednou a je silný v úpravách existujících obrázků.

**Stylová reference:** ke každému promptu přilož obrázek `obrazky/REF_styl_1.png` (Achillova šlacha – čistá linková kresba, tmavý obrys, světlá plochá výplň). Jedna společná reference drží vzhled celé sbírky jednotný. Text a šipky v referenci model ignoruje díky větě v promptu.

### Prompt – nová ilustrace

```
Hand-drawn educational illustration in the exact style of the attached
style reference image: clean dark ink outlines, light flat pastel fills
with minimal shading, plain white background.
Ignore any text, numbers or arrows in the reference image.

Subject: {POPIS SCÉNY}

Composition: side view, subject centered, generous empty space around it
for labels to be added later, aspect ratio 3:2.
Strictly NO text, NO letters, NO numbers, NO arrows, NO dimension lines,
NO watermark. Anatomically plausible proportions.
```

### Prompt – překreslení existujícího obrázku

```
Redraw image 1 in the exact style of image 2 (style reference):
clean dark ink outlines, light flat pastel fills with minimal shading,
plain white background. Ignore any text or arrows in image 2.

Keep the composition, pose, proportions and positions of all objects
exactly as in image 1. Remove all text, numbers, arrows and dimension
lines. Aspect ratio 3:2.
```

Obrázek 1 = předloha (stará verze nebo obrázek z PDF), obrázek 2 = `REF_styl_1.png`.

## 9. Postup u jednoho obrázku

1. Zjisti typ (A / B / C / C+B / D) a čísla ze zadání příkladu.
2. **A, B:** zkopíruj podobný skript ze `zdroje/`, uprav hodnoty a spusť ho:
   `python 040_statika_kralik.py`
3. **C:** vygeneruj ilustraci v Gemini podle promptu a ulož ji jako `…_ilustrace.png`.
4. **C+B:** skript načte `…_ilustrace.png` a dokreslí šipky, kóty a body.
5. Zkontroluj obrázek podle seznamu níže.

## 10. Kontrolní seznam

- [ ] Hodnoty a označení odpovídají textu zadání (veličiny, jednotky, úhly).
- [ ] Barvy odpovídají významu (síla červená, kóta modrá, …).
- [ ] Ve výplni ani na pozadí nejsou artefakty z AI (text, vodoznak, zkřivené ruce).
- [ ] 1200 px na šířku, bílé pozadí, název podle konvence.
- [ ] Obrázek nevyzrazuje řešení (např. výslednou sílu nebo výsledek).

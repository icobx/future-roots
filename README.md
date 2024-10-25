# future-roots


## Project preparation

### Layers

- **mestske pozemky**
- **mapa zelenych ploch ziskana analyzou satelitnych snimok**
- **cesty, budovy a ina infrastruktura obmedzujuca vysadbu**
- **tato vrstva bude mat 5 variantov (5 stromov)**
    - kazdy variant bude pre iny typ stromu
- **stromy**

*Prienik tychto vrstiev by mala byt plocha, kde sa mozu sadit stromy.*

### Co potrebujeme pripravit

- **frontend**, ktory bude schopny vizualizovat base mapu a vybrany set polygonov, interaktivne, idealne pridat drag and drop funkcionalitu, kde si moze user umiestnovat na mapu stromy prednastavenej velkosti (ale to je uz asi moc advanced)
- jednoduchy **python backend (flask)**, ktory bude servovat obrazky frontendu
    - toto teoreticky nepotrebujeme, ak jedine co budeme posielat na frontend su tie mapy. Ak ale budeme chciet nieco len trochu dynamickejsie pocitat, bolo by fajn to mat

#### Priprava dat pre vrstvy

- **mestske pozemky** - toto by sme mali dostat od mesta
- **mapa zelenych ploch** - musime pripravit
- **cesty, budovy a ina infrastruktura** - toto neviem ci dostaneme od mesta, ale predpokladam ze nie, takze tym padom by sme potrebovali natahat data z OpenStreetMaps??
- **stromy** - dostaneme od mesta
- **Nacitat STN a AR standardy**

### Linky

#### Anotovanie dat
- [https://pypi.org/project/anylabeling/](https://pypi.org/project/anylabeling/)
- [https://github.com/cvat-ai/cvat](https://github.com/cvat-ai/cvat)

#### Satelitne snimky
- [https://land.copernicus.eu/en/products/european-image-mosaic/very-high-resolution-image-mosaic-2021-true-colour-2m](https://land.copernicus.eu/en/products/european-image-mosaic/very-high-resolution-image-mosaic-2021-true-colour-2m)

#### Buffer okolo polygonov
- [https://shapely.readthedocs.io/en/stable/manual.html#object.buffer](https://shapely.readthedocs.io/en/stable/manual.html#object.buffer)

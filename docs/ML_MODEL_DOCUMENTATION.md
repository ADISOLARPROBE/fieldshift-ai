# ML Model Documentation
# Global Agricultural Climate Map: PRT

## 1. Overview

A world map of **73 agricultural reference points** across **21 countries**. Each point is tagged with its Köppen climate class and its main crops. Markers on the map are small and unlabelled to reduce clutter, so use the `point_id` in the dataset to identify each location.

- **Dataset:** `agricultural_locations_updated.csv`
- **Map:** Global Agricultural Climate Map (world outlines, one coloured marker per point)

## 2. Dataset Schema

| Column | Type | Description |
|---|---|---|
| `point_id` | Integer | Unique ID of the location (1–73) |
| `group` | String | Group the point belongs to (see section 3) |
| `country` | String | Country |
| `region` | String | Region or city, with state/province in brackets |
| `lat` | Float | Latitude (decimal degrees) |
| `lon` | Float | Longitude (decimal degrees) |
| `climate_koppen` | String | Köppen climate class (some points carry two, e.g. `Cwa/BSh`) |
| `main_crops` | String | Main crops, separated by hyphens |

## 3. Groups and Map Legend

| Group | Points | IDs | Countries | Points per country |
|---|---|---|---|---|
| `top5_5pts` | 25 | 1–25 | India, USA, Brazil, Russia, Indonesia | 5 |
| `farming20_3pts` | 42 | 26–37, 41–70 | Pakistan, Nigeria, Turkey, Argentina, Japan, Mexico, Thailand, Vietnam, Australia, Canada, Ukraine, Bangladesh, Germany, Iran | 3 |
| `farming20_3pts+UN5` | 3 | 38–40 | France | 3 |
| `UN5_3pts` | 3 | 71–73 | UK | 3 |
| **Total** | **73** | | **21 countries** | |

Marker colours on the map: red = `top5_5pts`, blue = `farming20_3pts`, purple = `farming20_3pts+UN5`, green = `UN5_3pts`.

## 4. Location Table

| ID | Group | Country | Region | Lat | Lon | Köppen | Main crops |
|---|---|---|---|---|---|---|---|
| 1 | top5_5pts | India | Ludhiana (Punjab) | 30.90 | 75.85 | Cwa/BSh | wheat-rice |
| 2 | top5_5pts | India | North East | 24.23 | 91.98 | Aw | rice-jute-potato |
| 3 | top5_5pts | India | Nagpur (Maharashtra) | 21.15 | 79.09 | Aw | cotton-soybean-orange |
| 4 | top5_5pts | India | Amaravati (Andhra Pradesh) | 16.51 | 80.51 | Aw/BSh | rice-chilli-cotton |
| 5 | top5_5pts | India | Jodhpur (Rajasthan) | 26.30 | 73.02 | BWh | millet-mustard-guar |
| 6 | top5_5pts | USA | Des Moines (Iowa) | 41.60 | -93.60 | Dfa | corn-soybean |
| 7 | top5_5pts | USA | Dodge City (Kansas) | 37.75 | -100.02 | BSk | winter wheat-sorghum |
| 8 | top5_5pts | USA | Fresno (California) | 36.74 | -119.79 | Csa | almond-grape-vegetables |
| 9 | top5_5pts | USA | Delta (Arkansas/Mississippi) | 34.50 | -91.00 | Cfa | rice-cotton-soybean |
| 10 | top5_5pts | USA | Fargo (North Dakota) | 46.88 | -96.79 | Dfb | spring wheat-canola |
| 11 | top5_5pts | Brazil | Sorriso (Mato Grosso) | -12.55 | -55.72 | Aw | soybean-maize |
| 12 | top5_5pts | Brazil | Londrina (Paraná) | -23.31 | -51.16 | Cfa | soybean-wheat-coffee |
| 13 | top5_5pts | Brazil | Passo Fundo (Rio Grande do Sul) | -28.26 | -52.41 | Cfa | soybean-wheat-rice |
| 14 | top5_5pts | Brazil | Barreiras (Bahia) | -12.15 | -44.99 | Aw/BSh | soybean-cotton-maize |
| 15 | top5_5pts | Brazil | Ribeirão Preto (São Paulo) | -21.18 | -47.81 | Cwa | sugarcane-orange-coffee |
| 16 | top5_5pts | Russia | Krasnodar | 45.04 | 38.98 | Cfa | wheat-sunflower |
| 17 | top5_5pts | Russia | Voronezh | 51.67 | 39.18 | Dfb | wheat-sugar beet |
| 18 | top5_5pts | Russia | Omsk (Siberia) | 54.99 | 73.37 | Dfb | spring wheat-barley |
| 19 | top5_5pts | Russia | Stavropol | 45.04 | 41.97 | BSk/Dfa | wheat-sunflower-barley |
| 20 | top5_5pts | Russia | Blagoveshchensk (Amur) | 50.27 | 127.53 | Dwb | soybean-wheat-maize |
| 21 | top5_5pts | Indonesia | Karawang (Java) | -6.32 | 107.34 | Am | rice |
| 22 | top5_5pts | Indonesia | Pekanbaru (Riau, Sumatra) | 0.51 | 101.45 | Af | oil palm-rubber |
| 23 | top5_5pts | Indonesia | Makassar (South Sulawesi) | -5.15 | 119.43 | Aw | rice-maize-cocoa |
| 24 | top5_5pts | Indonesia | Lampung (Sumatra) | -5.11 | 105.31 | Am | rice-cassava-maize |
| 25 | top5_5pts | Indonesia | Kupang (East Nusa Tenggara) | -10.18 | 123.60 | Aw | maize-sorghum |
| 26 | farming20_3pts | Pakistan | Faisalabad (Punjab) | 31.42 | 73.08 | BWh/BSh | wheat-cotton-rice |
| 27 | farming20_3pts | Pakistan | Larkana (Sindh) | 27.56 | 68.21 | BWh | rice-sugarcane-cotton |
| 28 | farming20_3pts | Pakistan | Peshawar (KP) | 34.01 | 71.52 | BSh | wheat-maize-tobacco |
| 29 | farming20_3pts | Nigeria | Kano | 12.00 | 8.52 | BSh/Aw | millet-sorghum-groundnut |
| 30 | farming20_3pts | Nigeria | Makurdi (Benue) | 7.73 | 8.52 | Aw | yam-rice-soybean |
| 31 | farming20_3pts | Nigeria | Ibadan | 7.38 | 3.90 | Aw/Am | cassava-cocoa-maize |
| 32 | farming20_3pts | Turkey | Konya | 37.87 | 32.48 | BSk | wheat-barley-sugar beet |
| 33 | farming20_3pts | Turkey | Adana (Çukurova) | 37.00 | 35.32 | Csa | cotton-citrus-maize |
| 34 | farming20_3pts | Turkey | Samsun (Black Sea) | 41.29 | 36.33 | Cfa | hazelnut-tea-maize |
| 35 | farming20_3pts | Argentina | Rosario (Pampas) | -32.95 | -60.65 | Cfa | soybean-maize-wheat |
| 36 | farming20_3pts | Argentina | Tucumán | -26.82 | -65.22 | Cwa | sugarcane-citrus-soybean |
| 37 | farming20_3pts | Argentina | Mendoza | -32.89 | -68.84 | BWk | grape-olive-fruit |
| 38 | farming20_3pts+UN5 | France | Chartres (Beauce) | 48.45 | 1.49 | Cfb | wheat-rapeseed-barley |
| 39 | farming20_3pts+UN5 | France | Bordeaux | 44.84 | -0.58 | Cfb | vineyards-maize |
| 40 | farming20_3pts+UN5 | France | Montpellier | 43.61 | 3.88 | Csa | vineyards-durum wheat-fruit |
| 41 | farming20_3pts | Japan | Obihiro (Hokkaido) | 42.92 | 143.20 | Dfb | wheat-potato-sugar beet-beans |
| 42 | farming20_3pts | Japan | Niigata (Honshu) | 37.92 | 139.04 | Cfa | rice-soybean-vegetables |
| 43 | farming20_3pts | Japan | Kumamoto (Kyushu) | 32.80 | 130.71 | Cfa | rice-wheat-vegetables-citrus |
| 44 | farming20_3pts | Mexico | Culiacán (Sinaloa) | 24.80 | -107.39 | BSh | maize-vegetables-wheat |
| 45 | farming20_3pts | Mexico | Celaya (Bajío) | 20.52 | -100.81 | BSh/Cwb | sorghum-wheat-maize |
| 46 | farming20_3pts | Mexico | Tapachula (Chiapas) | 14.91 | -92.26 | Am | coffee-maize-banana |
| 47 | farming20_3pts | Thailand | Suphan Buri | 14.47 | 100.12 | Aw | rice-sugarcane |
| 48 | farming20_3pts | Thailand | Khon Kaen | 16.44 | 102.84 | Aw | cassava-sugarcane-rice |
| 49 | farming20_3pts | Thailand | Surat Thani | 9.14 | 99.33 | Am | oil palm-rubber |
| 50 | farming20_3pts | Vietnam | Can Tho (Mekong Delta) | 10.04 | 105.78 | Aw | rice-fruit |
| 51 | farming20_3pts | Vietnam | Buon Ma Thuot | 12.67 | 108.04 | Aw | coffee-pepper |
| 52 | farming20_3pts | Vietnam | Thai Binh (Red River Delta) | 20.45 | 106.34 | Cwa | rice-vegetables |
| 53 | farming20_3pts | Australia | Dubbo (NSW) | -32.25 | 148.60 | Cfa | wheat-canola-barley |
| 54 | farming20_3pts | Australia | Toowoomba (Queensland) | -27.56 | 151.95 | Cfa | sorghum-cotton-wheat |
| 55 | farming20_3pts | Australia | Merredin (Western Australia) | -31.48 | 118.28 | BSk | wheat-barley-lupin |
| 56 | farming20_3pts | Canada | Saskatoon (Saskatchewan) | 52.13 | -106.67 | Dfb | wheat-canola-lentil |
| 57 | farming20_3pts | Canada | Lethbridge (Alberta) | 49.69 | -112.84 | BSk | wheat-barley-potato |
| 58 | farming20_3pts | Canada | Chatham-Kent (Ontario) | 42.40 | -82.19 | Dfb | corn-soybean-wheat |
| 59 | farming20_3pts | Ukraine | Poltava | 49.59 | 34.55 | Dfb | wheat-sunflower-maize |
| 60 | farming20_3pts | Ukraine | Vinnytsia | 49.23 | 28.47 | Dfb | sugar beet-wheat |
| 61 | farming20_3pts | Ukraine | Odesa | 46.48 | 30.73 | BSk | wheat-sunflower-barley |
| 62 | farming20_3pts | Bangladesh | Rajshahi | 24.37 | 88.60 | Aw | rice-wheat-mango |
| 63 | farming20_3pts | Bangladesh | Mymensingh | 24.75 | 90.41 | Aw/Cwa | rice-jute |
| 64 | farming20_3pts | Bangladesh | Barishal | 22.70 | 90.37 | Am/Aw | rice-pulses |
| 65 | farming20_3pts | Germany | Magdeburg Börde | 52.12 | 11.63 | Cfb | wheat-sugar beet-rapeseed |
| 66 | farming20_3pts | Germany | Cloppenburg (Lower Saxony) | 52.85 | 8.05 | Cfb | maize-potato |
| 67 | farming20_3pts | Germany | Munich (Bavaria) | 48.14 | 11.58 | Cfb/Dfb | barley-hops-maize |
| 68 | farming20_3pts | Iran | Ahvaz (Khuzestan) | 31.32 | 48.67 | BWh | wheat-sugarcane |
| 69 | farming20_3pts | Iran | Mashhad (Khorasan) | 36.30 | 59.60 | BSk | wheat-saffron |
| 70 | farming20_3pts | Iran | Rasht (Gilan) | 37.28 | 49.58 | Cfa | rice-tea |
| 71 | UN5_3pts | UK | Norfolk (East Anglia) | 52.63 | 1.30 | Cfb | wheat-barley-sugar beet |
| 72 | UN5_3pts | UK | Devon (South West) | 50.72 | -3.53 | Cfb | grassland-dairy |
| 73 | UN5_3pts | UK | Aberdeenshire | 57.30 | -2.60 | Cfb | barley-oats-potato |

## 5. Notes

- Köppen classes with a slash (e.g. `Aw/BSh`) mark points on the boundary between two climate zones.
- Negative latitude = Southern Hemisphere; negative longitude = Western Hemisphere.
- Country outlines on the map are general reference geography.


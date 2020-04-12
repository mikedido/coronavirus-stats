# COVID-19 stats

![python](https://img.shields.io/badge/v3.7-Python3-green)
![flask](https://img.shields.io/badge/v1.1-flask-green)
![jinja](https://img.shields.io/badge/v2.10.3-jinja-green)
![javascirpt](https://img.shields.io/badge/v1.5-javascript-yellow)
![d3js](https://img.shields.io/badge/v5-d3js-yellow)
![spinner](https://img.shields.io/badge/v2-spinner-yellow)

## About

An app to analysis data about the corona virus / COVID-19 on the world by giving the number of deaths, confirmed and recovered person. 

Also a charts and histogrammes available to evaluate the number of deaths, confirmed and recovered by country.

The app is avalable by clicking on the following link : https://corona-stats-world.herokuapp.com/

## Screenshot

<img src="images/map.png">
<img src="images/charts.png" >
<img src="images/histo.png" >


## Features
* __Data__: Shows the most recent data.
* __Distribution map__ with two levels of details:
  * __Countries__: When the user mouse over country on the map. Fewer details show the number of deaths, confirmed, recovered and active are shown.
  * __List__ : list of the countries regrouped by deaths, confirmed and recovered+.
* __Charts__:
   * __Confirmed chart__ for all countries.
   * __Deaths chart__ for all countries.
   * __Recovered chart__ for all country.
   * __Confirmed Histogramme__ the number of confirmed by day and by country
   * __Deaths Histogramme__ the number of deaths by day and by country
   * __Recovered Histogramme__ the number of recovered by day and by country
* __Red color scale__: Reflects the number of confirmed and death cases.

## How to Use
#### Build from source code
```
1. Clone/Download the repo.
2. Install the requiremenet : `make install`
2. Execute & run! : `make run`
3. Visit your browser : http://localhost:5000
4. Enjoy ;)
```
#### Runing tests
```
make test
```

#### Runing linter
```
make lint
```

## TODO

* __Search__ for countries & cities.
* __Cities__ add détails of the cities
* __Chart__ add map by country and their détails by city
* __Share__ stats & charts as images.
* __Statistics__: Including the number of confirmed, recovered, and deaths, in addition to percents.

 ## Data
 The data of coronavirus are retrieve from the api of the github project : https://github.com/ExpDev07/coronavirus-tracker-api

 This API used the data from : jhu - https://github.com/CSSEGISandData/COVID-19 - Worldwide Data repository operated by the Johns Hopkins University Center for Systems Science and Engineering (JHU CSSE).

 ## The map
 The used map are the same used on d3dataviz. Visit the website : https://www.datavis.fr/index.php?page=map-improve


## Contribute
Please feel free to contribute pull requests or create issues for bugs and feature requests.

## License
The app is available for personal/non-commercial use. It's not allowed to publish, distribute, or use the app in a commercial way.

## Author
Mahdi Gueffaz (mahdi.gueffaz@gmail.com)
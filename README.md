# airflow-etl-crypto-analytics
Automated ETL pipeline using Apache Airflow, Python, PostgreSQL, Docker, and Grafana for cryptocurrency market analytics.

# Airflow ETL Crypto Analytics Platform

## Overview

Built and orchestrated automated ETL workflows using Apache Airflow, Python, PostgreSQL, Docker, and Grafana.

The platform extracts cryptocurrency market data from the CoinGecko API, loads records into PostgreSQL, schedules recurring ETL jobs through Airflow, and visualizes market trends using Grafana dashboards.

## Architecture

CoinGecko API

↓

Python ETL

↓

Apache Airflow

↓

PostgreSQL

↓

Grafana

## Technology Stack

* Apache Airflow
* Python
* PostgreSQL
* Docker
* Grafana
* CoinGecko API

## Features

* Automated ETL scheduling
* API data ingestion
* PostgreSQL analytical storage
* Grafana dashboards
* Dockerized deployment

## Dashboard Metrics

* Cryptocurrency Prices
* Market Capitalization
* Price Trends

<img width="1807" height="872" alt="Screenshot 2026-06-11 003528" src="https://github.com/user-attachments/assets/3dac6524-b1e7-457b-b575-5c999399f461" />


## Scheduling

Airflow DAG executes every 5 minutes and loads fresh cryptocurrency market data into PostgreSQL.

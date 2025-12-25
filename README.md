# TaskAPI
A Simple API I made using FastAPI in Python. (My first FastAPI project) 

<img width="1011" height="123" alt="Bildschirmfoto 2025-12-25 um 21 44 02" src="https://github.com/user-attachments/assets/8c2f815a-17ab-4886-92a5-34e678e20c3d" />

## Instructions

### Installation + Setup

```bash
# Installation
$ git clone https://github.com/Timhongphuc/TaskAPI
```

```bash
# Install FastAPI
$ pip install fastapi
```

```bash
# Install Pydantic
$ pip install pydantic
```

```bash
# Start the FastAPI Server
$ fastapi dev learnfastapi.py
```

### GET, POST, DELETE
 
```bash
# How to do a GET Call
$ curl -X GET "http://128.0.0.1:8000/"
```

```bash
# How to do a POST Call
$ curl -X POST "http://128.0.0.1:8000/" -H "Content-Type: application/json" -d '{"taskname": "YOURTASK"}'
```

```bash
# How to do a DELETE Call
$ curl -X DELETE "http://128.0.0.1:8000/" -H "Content-Type: application/json" -d '{"taskname": "YOURTASK"}'
```

## Hosting on the Web + UI will come soon (Hopefully)

## Project information

- Duration of the Project (Beginnging - End): 20. December 2025 - 25. October 2025
- Sticky notes used: ≈ 0
- Hours I spend building this Project: ≈ 4h


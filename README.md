# Calculator

# Frontend setup
```
1) cd frontend
2) npm install
3) npm run serve - compiles and hot-reloads for development
npm run build - compiles and minifies for production
npm run lint - lints and fixes files
```

# DB setup 
```
1) cd db
2) docker compose up
```

# Backend setup
```
1) Should to install python 3.9 and pipenv to the global scope
https://www.python.org/dev/peps/pep-0596/
https://docs.pipenv.org/
2) pipenv shell - create a virtual environment
3) pipenv install --ignore-pipfile - install dependencies
4) uvicorn main:app --reload - server start
```
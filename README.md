<p align="center">
    <img src="/poketest/core/static/assets/images/logo.png" alt="Logo" width="350"/><br><br>
    PokéAPI RESTful API endpoint.<br>
</p>

------------
<h2>📖 About</h2>

PokéAPI RESTful API endpoint for discovering Pokémon skills in json, created during the ZRP Applications test in April 2021.

------------
<h2>🧪 Technology</h2>

The project was developed with:

&rarr; <a href="https://www.djangoproject.com/" target="_blank">DJango</a> <br>
&rarr; <a href="https://www.python.org/" target="_blank">Python</a> <br>

------------
<h2>🔌 Getting started</h2>
Clone the project:

```bash
$ git clone https://github.com/gesielrios/poketest.git
```

Acess the folder and install dependencies:

```bash
$ cd poketest

# Create a virtual env for the dependencies
$ python -m venv .venv
$ source .venv/bin/activate

# Install the dependencies
$ pip install -r requirements.txt

# Creating the project database
$ python manage.py makemigrations
$ python manage.py migrate
```

Starting the development server:
```bash
# Start the project
$ python manage.py runserver
```

------------
<h2>📕 Using the endpoint</h2>

Accessing via terminal, with curl for example:
```bash
$ curl http://localhost:8000/api/pokemon/ditto

# Response
{"imposter": "This Pok\u00e9mon transforms into a random opponent upon entering battle.  This effect is identical to the move transform.", "limber": "This Pok\u00e9mon cannot be paralyzed.\n\nIf a Pok\u00e9mon is paralyzed and acquires this ability, its paralysis is healed; this includes when regaining a lost ability upon leaving battle."}
```

Accessing via browser. Just access via url http://localhost:8000 and in the form specify the pokemon, as shown below.<br><br>

<img src="/poketest/core/static/assets/images/app-1.png" alt="app-1" width="400"/><br><br>
<img src="/poketest/core/static/assets/images/app-2.png" alt="app-2" width="400"/><br><br>
<img src="/poketest/core/static/assets/images/app-3.png" alt="app-3" width="400"/><br><br>

------------
<h2>🔖 Proposed solution to the challenge</h2>
<p>
    In addition to the development of an endpoint for PokéAPI RESTful API, the challenge of optimizing the search for the effect of the pokemon skill based on the URL returned from the skill itself, was assumed, assuming a pokemon might have several skills.
</p>
<p>
    Assuming we have a server with n cores available, a possible solution would be to parallelize the search requests for the effect of the pokemon skill on each core in a pool through the multiprocessing library.
</p>

------------
<h2>🎓 Thanks</h2>

👨‍🏫 Rafael Trostli Costella from 🚀 <a href="https://zrp.com.br/" target="_blank">ZRP - Consultoria Tecnológica e de Produtos Digitais</a>.

------------
<h2>📝 License</h2>
This project is licensed under the MIT License.
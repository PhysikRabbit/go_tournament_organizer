# Go Tournament Organizer

The goal of this project is to provide a simple way of organizing tournaments for games like Go, Chess or similar. 
It was created because we saw the need of a simpler way to record results in a tournament than to have several people write their result down on a piece of paper just that another person has to type all result into the computer. 
So this project wants to create an easy way for participants of such an event to insert their results immediately to the system.

## Installation
### Requirements for developement
* [Django](https://docs.djangoproject.com/en/4.0/topics/install/#installing-official-release)
* [Python](https://www.python.org/downloads/)
* [PostgreSQL](https://www.postgresql.org/download/)

#### Database
I decided on a PostgrSQL-database. 
After installation of PostgreSQL, start the pgAdmin-tool and create a new database named 'go-tournament-organizer'.
Username and password need to be inserted in the [settings.py](/go_tournament_organizer/go_tournament_organizer/settings.py).
Make sure, to not push any password into VCS!

### Python virtual environment
To create a virtual environment for this project run following commands.

On Windows:

Create virtual environment
```
py -m venv venvGTO
```

Activate environment
```
.\venvGTO\Scripts\activate
```
You might have to change your execution policy, to be able to activate the virtual environment.
But be aware of security risks.
```
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
```

Deactivate environment
```
deactivate
```

You should see the name of your virtual environment now in your console prompt.
To check for sure, if the environment is activated, start the python console and run this:

```python
import sys

def get_base_prefix_compat():
    """Get base/real prefix, or sys.prefix if there is none."""
    return getattr(sys, "base_prefix", None) or getattr(sys, "real_prefix", None) or sys.prefix

def in_virtualenv():
    return get_base_prefix_compat() != sys.prefix

in_virtualenv()
```

### Django

In your activated virtual environment run
```
python -m pip install Django
```

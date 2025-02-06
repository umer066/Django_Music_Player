# Django Music Player Web Application

This is a web-based music player application built with Django. It allows users to upload, manage, and play music files directly from their browser.

## Features

- **Play Music**: Stream and play uploaded music files.
- **Organize Music**: Manage music files with associated metadata like title and duration.
- **User Authentication**: Secure user registration and login system.

## Installation

1. **Clone the Repository**:

   git clone https://github.com/yourusername/django-music-player.git

   cd django-music-player

- Create a Virtual Environment:

python3 -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`

- Install Dependencies:

pip install -r requirements.txt

- Apply Migrations:

python manage.py makemigrations
python manage.py migrate

- Create a Superuser:

python manage.py createsuperuser

- Run the Development Server:

python manage.py runserver

Access the Application: Open your browser and navigate to http://127.0.0.1:8000/.

- Project Structure :-

django-music-player/
├── music_player_project/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── musicplayer/
│   ├── migrations/
│   ├── templates/
│   │       ├── main.html
│   │       └── index.html
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── script.js
│   ├── models.py
│   ├── views.py
│   └── ...
├── media/
│   ├── images/
│   └── audio/
└── manage.py


music_player_project/: Contains project-level settings and configurations.
musicapp/: Contains the main application code, including models, views, templates, and static files.
media/: Directory for storing uploaded media files like images and audio.

 Configuration :-

Ensure the following settings are configured in settings.py:

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Media files (Uploaded content)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
In urls.py, add the following to serve media files during development:


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... your url patterns ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

 Usage :-

Uploading Music: Navigate to the upload section to add new music files.
Playing Music: Browse the library and select a track to play.
Managing Music: Edit or delete tracks from your library as needed.

 Contributing :-

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

 License :-
This project is licensed under the MIT License. See the LICENSE file for details.


Feel free to customize this `README.md` to fit the specific details and features of your application.
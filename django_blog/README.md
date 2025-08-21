## Blog Post CRUD

### URLs
- `/posts/` — list all posts
- `/posts/new/` — create a new post (auth required)
- `/posts/<pk>/` — view a post
- `/posts/<pk>/edit/` — edit a post (author only)
- `/posts/<pk>/delete/` — delete a post (author only)
- `/login/`, `/logout/`, `/register/` — auth

### Permissions
- Anyone can read list/detail.
- Only authenticated users can create posts.
- Only the post author can edit/delete (LoginRequiredMixin + UserPassesTestMixin).

### Templates & Static
- Base template: `blog/templates/blog/base.html` includes
  - `{% static 'blog/css/style.css' %}`
  - `{% static 'blog/js/script.js' %}`
- All pages extend `base.html` so styling is applied.
- Static files live in `blog/static/blog/...`.

### Setup
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

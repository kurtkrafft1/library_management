
from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = "libraryapp"

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    path('', home, name='home'),
    path('books/', book_list, name='books'),
    path('librarians/', list_librarians, name='librarians'),
    path('libraries/', library_list, name="libraries"),
    path('book/form', book_form, name='book_form'),
    path('library/form', library_form, name='library_form'),
    path('books/<int:book_id>/', book_details, name='book'),
    path('libraries/<int:library_id>/', library_details, name="library"),
    path('librarians/<int:librarian_id>/', librarian_details, name="librarian"),
    path('books/<int:book_id>/form/', book_edit_form, name='book_edit_form'),
]

static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
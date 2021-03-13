from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre
from django.views import generic

def index(request):

	num_books = Book.objects.all().count()
	num_instances = BookInstance.objects.all().count()

	num_instances_available = BookInstance.objects.filter(status__exact = 'a').count()

	num_authors = Author.objects.count()

	num_genres = Genre.objects.count()
	num_books_searched_word = Book.objects.filter(title__icontains = "Best").count()



	context = {
		'num_books': num_books,
		'num_instances': num_instances,
		'num_instances_available': num_instances_available,
		'num_authors': num_authors,
		'num_genres': num_genres,
		'num_books_searched_word': num_books_searched_word,
	}

	return render(request, 'index.html', context = context)

class BookListView(generic.ListView):
	model = Book
	paginate_by = 3
	# context_object_name = 'my_book_list'
	# queryset = Book.objects.filter(title__icontains = 'de')[:5]
	# template_name = 'books/my_arbitrary_template_name_list.html'

	def get_queryset(self):
		return Book.objects.all()

	def get_context_data(self, **kwargs):
		context = super(BookListView, self).get_context_data(**kwargs)
		context['some_date'] = 'This is just some data'
		return context

class BookDetailView(generic.DetailView):
	model = Book

class AuthorListView(generic.ListView):
	model = Author

	def get_queryset(self):
		return Author.objects.all()

class AuthorDetailView(generic.DetailView):
	model = Author
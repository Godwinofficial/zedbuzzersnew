from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Ads
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.


def home_list_view(request):
  if request.method == 'GET':
    trending_posts = Post.objects.all().order_by('-post_views')
    category_links = Category.objects.all()
    posts = Post.objects.all().order_by('-time_stamp')
    ads = Ads.objects.all().order_by('-id')


    paginator = Paginator(posts, 15)
    page = request.GET.get('page')

    try:
      posts = paginator.get_page(page)
    except PageNotAnInteger:
      posts = paginator.page(1)
    except EmptyPage:
      posts = paginator.page(paginator.num_pages)

    index       = posts.number 
    max_index   = len(paginator.page_range)
    start_index = index - 3 if index >= 5 else 0
    end_index   = index + 3 if index <= max_index - 1 else max_index
    page_range  = paginator.page_range[start_index:end_index]


    context = {
      'posts': posts,
      'category_links': category_links,
      'trending_posts': trending_posts,
      'page_range': page_range,
      'ads': ads,

    }

  return render(request, 'home.html', context)



def post_detail_view(request, slug):
  if request.method == 'GET':
    videos = Category.objects.get(slug='videos')
    related_posts_videos = Post.objects.filter(category=videos).order_by('-time_stamp')
    news_posts = Category.objects.get(slug='news')
    news = Post.objects.filter(category=news_posts)
    related_posts = Post.objects.all().order_by('-time_stamp')
    category_links = Category.objects.all()
    post_details = get_object_or_404(Post, slug=slug)
    details_trending_posts = Post.objects.all().order_by('-post_views')
    post_details.post_views += 1
    post_details.save()
    ads = Ads.objects.all().order_by('-id')


    context = {
      'news_posts': news_posts,
      'news': news,
      'post_details': post_details,
      'category_links': category_links,
      'details_trending_posts':details_trending_posts,
      'related_posts': related_posts,
      'related_posts_videos': related_posts_videos,
      'ads': ads,
    }
  return render(request, 'details.html', context)



def category_list_view(request, slug):
  if request.method == 'GET':
    category_links = Category.objects.all()
    categories = get_object_or_404(Category, slug=slug)
    category_posts = Post.objects.filter(category=categories).order_by('-time_stamp')
    posts = category_posts
    category_trending_posts = Post.objects.filter(category=categories).order_by('-post_views')
    ads = Ads.objects.all().order_by('-id')

    paginator = Paginator(posts, 15)
    page = request.GET.get('page')

    try:
      posts = paginator.get_page(page)
    except PageNotAnInteger:
      posts = paginator.page(1)
    except EmptyPage:
      posts = paginator.page(paginator.num_pages)

    index       = posts.number 
    max_index   = len(paginator.page_range)
    start_index = index - 3 if index >= 5 else 0
    end_index   = index + 3 if index <= max_index - 1 else max_index
    page_range  = paginator.page_range[start_index:end_index]


  

    context = {
      'categories': categories,
      'category_posts': category_posts,
      'category_links': category_links, 
      'category_trending_posts': category_trending_posts,
      'posts': posts,
      'page_range': page_range,
      'ads': ads,
    }

  return render(request, 'category.html', context)



def search_list_view(request):
  if request.method == 'GET':
    category_links = Category.objects.all()
    search = request.GET.get('search')
    search_data = Post.objects.all().filter(name__icontains=search).order_by('-time_stamp')
    search_trending_posts = Post.objects.all().order_by('-post_views')
    posts = search_data

    paginator = Paginator(posts, 1)
    page = request.GET.get('page')

    try:
      posts = paginator.get_page(page)
    except PageNotAnInteger:
      posts = paginator.page(1)
    except EmptyPage:
      posts = paginator.page(paginator.num_pages)

    index       = posts.number 
    max_index   = len(paginator.page_range)
    start_index = index - 3 if index >= 5 else 0
    end_index   = index + 3 if index <= max_index - 1 else max_index
    page_range  = paginator.page_range[start_index:end_index]


    context = {
      'search_data': search_data,
      'category_links': category_links,
      'search': search,
      'search_trending_posts': search_trending_posts,
      'posts': posts,
      'page_range': page_range,
    }

  return render(request, 'search.html', context)




def about_us_list_view(request):
  if request.method == 'GET':
    category_links = Category.objects.all()

    context = {
      'category_links': category_links,    
    }
  return render(request, 'about_us.html', context)



def privacy_policy_list_view(request):
  if request.method == 'GET':
    category_links = Category.objects.all()

    context = {
      'category_links': category_links,    
    }
  return render(request, 'privacy_policy.html', context)




def terms_and_conditions_list_view(request):
  if request.method == 'GET':
    category_links = Category.objects.all()

    context = {
      'category_links': category_links,    
    }
  return render(request, 'terms_and_conditions.html', context)




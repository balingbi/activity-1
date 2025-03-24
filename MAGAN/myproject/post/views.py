from django.shortcuts import render

def posts_list(request):
    # Example data for posts
    """Render the post list page."""
    return render(request, 'posts_list.html')
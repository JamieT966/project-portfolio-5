from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, Review, UserProfile
from .forms import ProductForm, ReviewForm


def all_products(request):
    """
    Displays a page with all products
    """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You did not enter anything to search,"
                                        "please try again.")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    A view to show individual product details
    Also displays all reviews for the specific product
    """

    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product=product_id)
    user = UserProfile.objects.all()
    category = Category.objects.all()

    context = {
        'product': product,
        'reviews': reviews,
        'user': user,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """
    Allows admin user to add product to store.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only an admin is allowed to do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Try again with a vaild product.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    Allows admin user to edit a product in store.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only an admin is allowed to do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure all details are valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """
    Allows admin user to delete a product from store.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only an admin is allowed to do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def add_review(request, product_id):
    """
    Allows user to submit a product review
    """

    if request.method == 'POST':

        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)

            review.product = Product.objects.get(pk=product_id)
            review.user = UserProfile.objects.get(user__username=request.user.username)
            review.save()
            reviews = Review.objects.filter(product=product_id)
            messages.success(request, 'Thank you! Your review has been submitted.')

        return redirect(reverse('product_detail', kwargs={'product_id':product_id,}))


@login_required
def edit_review(request, review_id):
    """
    Allows admin user to edit a review in store.
    """
    review = get_object_or_404(Review, pk=review_id)
    review_id = Review.objects.get(pk=review_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = UserProfile.objects.get(user__username=request.user.username)
            review.save()
            messages.success(request, 'Review updated successfully')
            return redirect(reverse('product_detail', kwargs={'product_id': review_id.product.id}))

        else:
            messages.error(request, 'Failed to update review. Please ensure all details are valid.')
    else:
        form = ReviewForm(instance=review)
        review.user = UserProfile.objects.get(user__username=request.user.username)
        messages.info(request, f'You are editing a review by {review.user}')

    template = 'products/edit_review.html'
    context = {
        'form': form,
        'review': review,
    }

    return render(request, template, context)


@login_required
def delete_review(request, review_id):
    """
    Allows admin user to delete a product from store.
    """
    review = get_object_or_404(Review, pk=review_id)
    product_id = review.product.id
    review.delete()
    messages.success(request, 'Review deleted!')
    return redirect(reverse('products'))


# def verify_purchase(user_profile, order_model, product):
#     """
#     Verify user has purchased a product, return boolean.
#     """
#     user_orders = order_model.objects.filter(user_profile=user_profile)
#     for order in user_orders:
#         for item in order.lineitems.all():
#             if item.product == product:
#                 return True
#     return False

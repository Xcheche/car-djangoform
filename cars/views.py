from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from cars.forms import ReviewForm
from cars.models import Review


# Create your views here.
def rental_review(request):
    if request.method == "POST":
        print(request.POST)
        form = ReviewForm(request.POST)

        if form.is_valid():
            # Extract data after form validation
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            review = form.cleaned_data["review"]

            # Manually create and save the model instance
            new_review = Review(name=name, email=email, review=review)
            new_review.save()

            messages.success(request, "Review successfully submitted!")
            return redirect(reverse("thank_you"))
        else:
            # Handle the case where the form is invalid
            messages.error(request, "There was an error in your submission.")
    else:
        form = ReviewForm()

    return render(request, "cars/rental_review.html", {"form": form})


def thank_you(request):
    return render(request, "cars/thank_you.html")

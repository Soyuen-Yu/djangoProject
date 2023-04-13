from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorators import profile_ownership_decorator
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile
import logging

# Create your views here.
logger = logging.getLogger(__name__)


class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'targetProfile'
    form_class = ProfileCreationForm
    template_name = 'profileapp/create.html'
    logger.error('create 호출')
    def form_valid(self, form):
        temp_profile = form.save(commit=False)
        temp_profile.user = self.request.user
        temp_profile.save()
        logger.error('save완료')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})


@method_decorator(profile_ownership_decorator, 'get')
@method_decorator(profile_ownership_decorator, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'targetProfile'
    form_class = ProfileCreationForm
    template_name = 'profileapp/update.html'

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})

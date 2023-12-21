from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import FeedbackForms
from .models import Feedback
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, FormView, CreateView
from datetime import datetime
# Create your views here.


# class FeedbackView(View):
#     def get(self, request):
#         form = FeedbackForms()
#         return render(request, 'form/index.html', {'form': form})
#
#     def post(self, request):
#         form = FeedbackForms(request.POST)
#         if request.method == 'POST':
#             if form.is_valid():
#                 form.save()
#                 return HttpResponseRedirect('/done')
#         return render(request, 'form/index.html', {'form': form})

# class FeedbackView(FormView):
#     form_class = FeedbackForms
#     template_name = 'form/index.html'
#     success_url = 'done'
#     def form_valid(self, form):
#         form.save()
#         return super(FeedbackView, self).form_valid()

class FeedbackView(CreateView):
    model = Feedback
    form_class = FeedbackForms
    template_name = 'form/index.html'
    success_url = 'done'


class UpdateView(View):
    def get(self, request, id_feedback):
        feed = Feedback.objects.get(id=id_feedback)
        form = FeedbackForms(instance=feed)
        return render(request, 'form/index.html', {'form': form})
    def post(self, request, id_feedback):
        feed = Feedback.objects.get(id=id_feedback)
        form = FeedbackForms(request.POST, instance=feed)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/done')
        return render(request, 'form/index.html', {'form': form})


class DoneView(TemplateView):
   template_name = 'form/done.html'

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['name'] = 'Ivan'
       context['data'] = datetime.now().strftime('%Y-%m-%d')
       return context

# class ListFeedBack(TemplateView):
#     template_name = 'form/list_feedback.html'
#     list_data = list(map(lambda x: (x.id, x.name, x.surname, x.feedback),Feedback.objects.all()))
#     print(list_data)
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['feedback'] = self.list_data
#         print(context)
#         return context

# class DetailFeedBack(TemplateView):
#     template_name = 'form/detail_feedback.html'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['current'] = Feedback.objects.get(id=kwargs['id_feedback'])
#         return context


class ListFeedBack(ListView):
    template_name = 'form/list_feedback.html'
    model = Feedback
    context_object_name = 'feedbacks'

class DetailFeedBack(DetailView):
    template_name = 'form/detail_feedback.html'
    model = Feedback
    context_object_name = 'feed'

# class DoneView(View):
#     def get(self, request):
#         return render(request, 'form/done.html')

# def index(request):
#     if request.method == 'POST':
#         form = FeedbackForms(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/done')
#     else:
#         form = FeedbackForms()
#     return render(request, 'form/index.html', {'form': form})

# def update_data(request, id_feedback):
#     feed = Feedback.objects.get(id=id_feedback)
#     if request.method == 'POST':
#         form = FeedbackForms(request.POST, instance=feed)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/done')
#     else:
#         form = FeedbackForms(instance=feed)
#     return render(request, 'form/index.html', {'form': form})
# def done(request):
#     return render(request, 'form/done.html')

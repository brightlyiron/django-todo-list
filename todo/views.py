from django.views import generic


class TodoListTemplateView(generic.TemplateView):
    template_name = "todo/list.html"


todo_list_view = TodoListTemplateView.as_view()

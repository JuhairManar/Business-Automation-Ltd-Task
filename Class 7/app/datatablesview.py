from django_datatables_view.base_datatable_view import BaseDatatableView
from .models import Person

class PersonListJson(BaseDatatableView):
    model = Person
    columns = ['name', 'email', 'status']

    def get_initial_queryset(self):
        return Person.objects.all()

    def render_column(self, row, column):
        # We want to display status as 'Active' or 'Inactive'
        if column == 'status':
            return row.get_status_display()
        else:
            return super(PersonListJson, self).render_column(row, column)

"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from app import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from tasks import views as taskViews


urlpatterns = [
    path('admin/', admin.site.urls),

    path("",views.login,name="login"),
    path("logout",views.logout,name="logout"),

    path("home",views.home,name="home"),
    path("new-building-form",views.building_form,name="building-form"),
    path("delete-building/<int:id>",views.delete_building,name="delete-building"),

    path("apartments/<int:id>",views.apartments,name="apartments"),
    path("new-apartment-form/<int:id>/<str:prev_id>",views.apartment_form,name="apartment-form"),
    path("edit-apartment-form/<int:id>",views.edit_apartment_form,name="edit-apartment-form"),
    path("delete-apartment/<int:id>",views.delete_apartment,name="delete-apartment"),

    path("invoices/<int:id>",views.invoices,name="invoices"),
    path("other-invoices/<int:id>",views.other_invoices,name="other-invoices"),
    path("new-invoice-form/<int:id>",views.invoice_form,name="invoice-form"),
    path("new-other-invoice-form/<int:id>",views.other_invoice_form,name="other-invoice-form"),

    path("print-invoice/<int:id>",views.print_invoice,name="print-invoice"),
    path("delete-invoice/<int:id>",views.delete_invoice,name="delete-invoice"),
    path("actual-delete-invoice/<int:id>",views.actual_delete_invoice,name="actual-delete-invoice"),

    #path("owner-invoices/<str:id>",views.owner_invoices,name="owner-invoices"),

    path("maintenance-invoices/<int:id>",views.maintenance_invoices,name="maintenance-invoices"),
    path("new-maintenance-invoice-form/<int:id>",views.maintenance_invoice_form,name="maintenance-invoice-form"),
    path("delete-maintenance-invoice/<int:id>",views.delete_maintenance_invoice,name="delete-maintenance-invoice"),
    path("actual-delete-maintenance-invoice/<int:id>",views.actual_delete_maintenance_invoice,name="actual-delete-maintenance-invoice"),
    path("owner-maintenance-invoices/<str:id>",views.owner_maintenance_invoices,name="owner-maintenance-invoices"),

    path("owner-report/<int:id>",views.owner_report,name="owner-report"),

    path("check-download-allowed/<int:id>",views.check_download_allowed),
    path("check-delete-allowed/<int:id>/<str:type_of>",views.check_delete_allowed),

    path("receive-invoice/<int:id>",views.receive_invoice,name="receive-invoice"),

    path("deleted-invoices",views.deleted_invoices,name="deleted-invoices"),
    path("deleted-maintenance-invoices",views.deleted_maintenance_invoices,name="deleted-maintenance-invoices"),

    path("new-tenant-form/<int:id>/<str:sel>",views.new_tenant_form,name="new-tenant-form"),
    path("previous-tenants/<int:id>/<str:sel>",views.previous_tenants,name="previous-tenants"),
    path("tenant-invoices/<int:aid>/<int:id>",views.tenant_invoices,name="tenant-invoices"),
    path("tenant-maintenance-invoices/<int:aid>/<int:id>",views.tenant_maintenance_invoices,name="tenant-maintenance-invoices"),

    path("move-up-apartment/<int:bid>/<int:aid>",views.move_up_apartment,name='move-up-apartment'),
    path("move-down-apartment/<int:bid>/<int:aid>",views.move_down_apartment,name='move-down-apartment'),
    path("search-apartment-by-phone",views.search_apartment_by_phone,name='search-apartment-by-phone'),
    path("search-apartment-by-contract",views.search_apartment_by_contract,name='search-apartment-by-contract'),

    path("get-to-date-for-invoice/<int:id>/<int:amt>",views.get_to_date_for_invoice),

    path("task-dashboard/<int:show>",taskViews.home,name="task-dashboard"),
    path("create-task",taskViews.create_task,name="create-task"),
    path("task-detail/<int:id>/<int:show>",taskViews.task_detail,name="task-detail"),
    path("task-close/<int:id>/<int:show>",taskViews.task_close,name="task-close"),
    path('requests/', views.requests_view, name='requests_page'),
    path('owner-invoices/<str:id>/', views.owner_invoices, name='owner-invoices'),
    #path('owner-invoices/<str:id>/', views.owner_invoices, name='owner-invoices')

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
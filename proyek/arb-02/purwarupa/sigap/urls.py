from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from penjualan import views

urlpatterns = [
    path("", TemplateView.as_view(template_name="sales.html"), name="sales"),
    path("panel/", TemplateView.as_view(template_name="panel.html"), name="panel"),
    path("admin/", admin.site.urls),
    path("api/versi", views.versi),
    path("api/katalog", views.katalog),
    path("api/pesanan", views.pesanan_baru),
    path("api/pesanan/<int:pesanan_id>/batal", views.pesanan_batal),
    path("api/pesanan/<int:pesanan_id>/kirim", views.pesanan_kirim),
    path("api/penyesuaian", views.penyesuaian),
    path("api/ringkasan", views.ringkasan),
    path("api/telusur-batch/<str:no_batch>", views.telusur_batch),
    path("api/reset", views.reset),
]

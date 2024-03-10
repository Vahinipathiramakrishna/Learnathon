from django.urls import path
from.import views

urlpatterns = [

    path("ttmhome", views.ttmhome, name="ttmhome"),
    path("checkadminlogin",views.checkadminlogin,name="checkadminlogin"),
    path("checkregistration",views.checkregistration,name="checkregistration"),
    path("checkpackages",views.checkpackages,name="checkpackages"),
    path("checkchangepassword",views.checkchangepassword,name="checkchangepassword"),
    path("homepage",views.homepage,name="homepage"),
    path("about",views.about,name="about"),
    path("buy",views.buy,name="buy"),
    path("logout",views.logout,name="logout"),
    path("houses",views.houses,name="houses"),
    path("lands",views.lands,name="lands"),
    path("contact",views.contact,name="contact"),
    path("apartments",views.apartments,name="apartments"),
    path("villas",views.villas,name="villas"),
    path("house1",views.house1,name="house1"),
    path("house2",views.house2,name="house2"),
    path("house3",views.house3,name="house3"),
    path("house4",views.house4,name="house4"),
    path("agents",views.agents,name="agents"),
    path("terms",views.terms,name="terms"),
    path("apartment1",views.apartment1,name="apartment1"),
    path("apartment2",views.apartment2,name="apartment2"),
    path("apartment3",views.apartment3,name="apartment3"),
    path("apartment4",views.apartment4,name="apartment4"),
    path("",views.homepage,name=""),
]

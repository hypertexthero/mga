from django.conf.urls import *
from portfolio.models import *
from portfolio.views import *

urlpatterns = patterns("portfolio.views",
   (r"^category/(?P<dpk>\d+)/(?P<show>\S+)/" , CategoryView.as_view(), {}, "category"),
   (r"^category/(?P<dpk>\d+)/"               , CategoryView.as_view(), {}, "category"),
   (r"^add-images/(?P<dpk>\d+)/"          , AddImages.as_view(), {}, "add_images"),
   (r"^slideshow/(?P<dpk>\d+)/"           , SlideshowView.as_view(), {}, "slideshow"),
   (r"^image/(?P<mfpk>\d+)/"              , ImageView.as_view(), {}, "image"),
   (r"^image/"                            , ImageView.as_view(), {}, "image"),
   (r""                                   , Main.as_view(), {}, "portfolio"),
)

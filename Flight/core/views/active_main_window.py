from django.views.generic import TemplateView
import re
import urllib.parse, urllib.request

# destination = ""
# is_site = ""
# recommendations = []
# def get_data_from_user(d):
#     global destination
#     global is_site
#
#     if d['destination'] != '':
#         destination = d['destination']
#         recommendations.clear()
#
#     if d['is_a_tourist_site'] != '':
#         is_site = True

    # recommendations.append(f"SEAT {d['seat']}:    " + d['text'])
from core.models import Dest, Facts


class Active_view(TemplateView):
    template_name = 'active_main.html'

    def dispatch(self, request, *args, **kwargs):
        self.dest = Dest.objects.order_by("?").first()
        self.recs = Facts.objects.get(dest=self.dest.name)
        return super().dispatch(request, *args, **kwargs)

    def get_url(self):
        place = self.dest.dest
        query_string = urllib.parse.urlencode({"search_query": place})
        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
        return f"https://www.youtube.com/embed/{search_results[0]}"

    def get_topic(self):
        return self.dest.dest

    def get_recognization(self):
        str_recs = [rec['content'] for rec in self.recs]
        return '\n\n'.join(str_recs) # the \n does'nt work!!!

    def is_site(self):
        return self.dest.is_site

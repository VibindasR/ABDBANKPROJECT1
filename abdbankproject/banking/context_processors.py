from banking.models import Branch, District


def menu_links(request):
    links = Branch.objects.all()
    return dict(links=links)

def menu_link(request):
    link = District.objects.all()
    return dict(link=link)
from webapp.models import Site


def serve(request, path):
    site = Site.objects.first()
    path_components = [component for component in path.split('/') if component]
    return site.root_page.specific.route(request, path_components)

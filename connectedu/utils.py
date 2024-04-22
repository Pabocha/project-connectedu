def extract_domain_from_request(request):
    """ Extrait le nom de domaine de la requête.
        Par défaut, supprime le port et le préfixe 'www'.
    """
    host = request.get_host().split(':')[0]  # Récupère le nom de domaine sans le port
    if host.startswith('www.'):  # Vérifie si le nom de domaine commence par 'www.'
        return host[4:]  # Retourne le nom de domaine sans le préfixe 'www.'
    return host  # Retourne le nom de domaine tel quel s'il n'y a pas de préfixe 'www.'

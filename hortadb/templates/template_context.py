def context(request):
    return {
        'title': 'HortaDB',
        'navigation': [
            {
                'title': 'Plants',
                'url': '/plants',
                'icon': 'leaf'
            },

            {
                'title': 'Collections',
                'url': '/hortadb/species',
                'icon': 'warehouse'
            },

            {
                'title': 'Resources',
                'url': '/hortadb/resources',
                'icon': 'book-open'
            }
        ]
    }
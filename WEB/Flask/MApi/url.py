from apps.user.user import register

urls = [
    {
        "url": '/register',
        "name": register.__name__,
        "fun": register,
        "methods": ["POST"]
    }
]


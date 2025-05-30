from backend.auth.security import get_password_hash, verify_password

# Simulação de banco de dados
fake_users_db = {
    "admin": {
        "username": "admin",
        "full_name": "Administrador",
        "email": "admin@example.com",
        "hashed_password": get_password_hash("admin123"),
        "disabled": False
    }
}

def get_user(username: str):
    user = fake_users_db.get(username)
    return user

def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False
    if not verify_password(password, user["hashed_password"]):
        return False
    return user

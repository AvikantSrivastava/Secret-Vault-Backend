from fastapi import APIRouter

router = APIRouter()

@router.post("/signup")
async def signup(user: User):
    user_id = hash(user.username, os.environ.get('USER_ID_HASH_SECRET'))

    try:
        if not user_db.fetch(user_id):
            user.id = user_id
            # user.password_hash = auth_handler.get_password_hash(user.password)
            user_db.add(
                user_id,
                user.dict(exclude={'password'})
            )
            token = generate_token(user.username)
            return {
                'status': 'success',
                'token': token
            }

        else:
            return Response("User already exists", status_code=401)
    except:
        return Response("Internal server error", status_code=500)

@router.post("/login")
async def login(user: User):
    user_id = hash(user.username,
                   os.environ.get('USER_ID_HASH_SECRET'))

    try:
        user_from_db = user_db.fetch(user_id)

        if auth_handler.verify_password(user.password, user_from_db['password_hash']):
            token = generate_token(user.username)
            return {
                'status': 'success',
                'token': token
            }

        return Response("Failed login", status_code=401)

    except:
        return Response("User not found", status_code=404)
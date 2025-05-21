from fastapi import APIRouter, HTTPException, Depends
from database.mongodb import get_db
from dto.user import UserCreate, UserResponse
from repository.user_repository import UserRepository
from service.user_service import UserService

router = APIRouter(prefix='/users',tags=["Users"])

def get_user_service(db=Depends(get_db)):
    user_repo = UserRepository(db)
    return UserService(user_repo)
@router.post("/", response_model=UserResponse)
async def register_user(user: UserCreate, service: UserService = Depends(get_user_service)):
    new_user = await service.register_user(user)
    return UserResponse(username=new_user['username'], email=new_user['email'])

@router.get("/{user_id}", response_model=UserResponse)
async def read_user(user_id: str, service: UserService = Depends(get_user_service)):
    user = await service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
from fastapi import APIRouter
from database import member_db
from pydantic_classes import members
from logs.logger_config import get_logger

logger = get_logger(__name__)

member = member_db.MemberDB()

router = APIRouter()
@router.post("/")
def create_member(data: members.Member):
    return member.create_member(data)


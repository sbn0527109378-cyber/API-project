from fastapi import APIRouter, HTTPException
from database import member_db
from pydantic_classes import members
from logs.logger_config import get_logger

logger = get_logger(__name__)

member = member_db.MemberDB()

router = APIRouter()
@router.post("/")
def create_member(data: members.Member):
    return member.create_member(data)

@router.get("/")
def all_members():
    return member.get_all_members()

@router.get("/{id}")
def member_by_id(id):
    try:
        return member.get_member_by_id(id)
    except KeyError:
        logger.error("id not found")
        raise HTTPException(status_code=404, detail="id not found")
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=400, detail=f"{e}")
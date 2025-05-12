from litestar import get, post, delete, patch
from sqlalchemy.ext.asyncio import AsyncSession

import u_database
from u_validation import UserCreate, UserUpdate, UserShow


@get("/user/")
async def get_user_list(
        db_session: AsyncSession
) -> list[UserShow]:
    repos = u_database.UserRepository(session=db_session)
    mlist = await repos.list()
    res_list = [UserShow.model_validate(it) for it in mlist]
    return res_list


@get("/user/{user_id:int}")
async def get_user(user_id: int,
                   db_session: AsyncSession
                   ) -> UserShow:
    repos = u_database.UserRepository(session=db_session)
    user = await repos.get(user_id)
    return UserShow.model_validate(user)


@post("/user/")
async def create_user(
        data: UserCreate,
        db_session: AsyncSession
) -> u_database.UserTable:
    repos = u_database.UserRepository(session=db_session)
    raw_obj = data.model_dump(exclude_none=True)
    us = u_database.UserTable(**raw_obj)
    user = await repos.add(us)
    await db_session.commit()
    return user


@patch("/user/{user_id:int}")
async def update_user(
        user_id: int,
        data: UserUpdate,
        db_session: AsyncSession
) -> u_database.UserTable:
    raw_obj = data.model_dump(exclude_none=True)
    raw_obj["id"] = user_id
    user = u_database.UserTable(**raw_obj)
    repos = u_database.UserRepository(session=db_session)
    updated_user = await repos.update(user)
    await repos.session.commit()
    return updated_user


@delete("/user/{user_id:int}")
async def delete_user(
        db_session: AsyncSession,
        user_id: int
) -> None:
    repos = u_database.UserRepository(session=db_session)
    await repos.delete(user_id)
    await repos.session.commit()
    return None

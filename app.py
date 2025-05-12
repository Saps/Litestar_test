from litestar import Litestar, get, post, delete, patch

import u_database
import u_controller


# ----------------------------------------------------------
@get("/")
async def index() -> str:
    return "Defalut page, no functions"


app = Litestar([index
                   , u_controller.get_user_list
                   , u_controller.get_user
                   , u_controller.create_user
                   , u_controller.update_user
                   , u_controller.delete_user
                ],
               plugins=[u_database.sql_plugin])

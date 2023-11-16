from .question_and_answer_objects import *


from fastapi import APIRouter, FastAPI, Request
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os


class Service_question_and_answer:
    async def about(self, headers: dict[str, str], item: About_Request) -> About_Response:
        default_response = About_Response()

        try:
            pass
        except Exception as e:
            print(f"Error: {e}")
            #default_response.error = str(e)
            #default_response.success = False

        return default_response

    async def ask_yingshaoxo_ai(self, headers: dict[str, str], item: Ask_Yingshaoxo_Ai_Request) -> Ask_Yingshaoxo_Ai_Response:
        default_response = Ask_Yingshaoxo_Ai_Response()

        try:
            pass
        except Exception as e:
            print(f"Error: {e}")
            #default_response.error = str(e)
            #default_response.success = False

        return default_response

    async def visitor_search(self, headers: dict[str, str], item: Search_Request) -> Search_Response:
        default_response = Search_Response()

        try:
            pass
        except Exception as e:
            print(f"Error: {e}")
            #default_response.error = str(e)
            #default_response.success = False

        return default_response

    async def visitor_get_a_post(self, headers: dict[str, str], item: Get_A_Post_Request) -> Get_A_Post_Response:
        default_response = Get_A_Post_Response()

        try:
            pass
        except Exception as e:
            print(f"Error: {e}")
            #default_response.error = str(e)
            #default_response.success = False

        return default_response

    async def visitor_get_comment_list_by_id_list(self, headers: dict[str, str], item: Get_Comment_List_By_Id_List_Request) -> Get_Comment_List_By_Id_List_Response:
        default_response = Get_Comment_List_By_Id_List_Response()

        try:
            pass
        except Exception as e:
            print(f"Error: {e}")
            #default_response.error = str(e)
            #default_response.success = False

        return default_response

    async def user_add_post(self, headers: dict[str, str], item: Add_Post_Request) -> Add_Post_Response:
        default_response = Add_Post_Response()

        try:
            pass
        except Exception as e:
            print(f"Error: {e}")
            #default_response.error = str(e)
            #default_response.success = False

        return default_response

    async def user_comment_post(self, headers: dict[str, str], item: Comment_Post_Request) -> Comment_Post_Response:
        default_response = Comment_Post_Response()

        try:
            pass
        except Exception as e:
            print(f"Error: {e}")
            #default_response.error = str(e)
            #default_response.success = False

        return default_response

    async def user_download_backup_data(self, headers: dict[str, str], item: Download_Backup_Data_Request) -> Download_Backup_Data_Response:
        default_response = Download_Backup_Data_Response()

        try:
            pass
        except Exception as e:
            print(f"Error: {e}")
            #default_response.error = str(e)
            #default_response.success = False

        return default_response

    async def admin_download_backup_data(self, headers: dict[str, str], item: Admin_Download_Backup_Data_Request) -> Admin_Download_Backup_Data_Response:
        default_response = Admin_Download_Backup_Data_Response()

        try:
            pass
        except Exception as e:
            print(f"Error: {e}")
            #default_response.error = str(e)
            #default_response.success = False

        return default_response

    async def admin_upload_backup_data(self, headers: dict[str, str], item: Admin_Upload_Backup_Data_Request) -> Admin_Upload_Backup_Data_Response:
        default_response = Admin_Upload_Backup_Data_Response()

        try:
            pass
        except Exception as e:
            print(f"Error: {e}")
            #default_response.error = str(e)
            #default_response.success = False

        return default_response


def init(service_instance: Any, router: Any):
    @router.post("/about/", tags=["question_and_answer"])
    async def about(request: Request, item: About_Request) -> About_Response:
        item = About_Request().from_dict(item.to_dict())
        headers = dict(request.headers.items())
        return (await service_instance.about(headers, item)).to_dict()

    @router.post("/ask_yingshaoxo_ai/", tags=["question_and_answer"])
    async def ask_yingshaoxo_ai(request: Request, item: Ask_Yingshaoxo_Ai_Request) -> Ask_Yingshaoxo_Ai_Response:
        item = Ask_Yingshaoxo_Ai_Request().from_dict(item.to_dict())
        headers = dict(request.headers.items())
        return (await service_instance.ask_yingshaoxo_ai(headers, item)).to_dict()

    @router.post("/visitor_search/", tags=["question_and_answer"])
    async def visitor_search(request: Request, item: Search_Request) -> Search_Response:
        item = Search_Request().from_dict(item.to_dict())
        headers = dict(request.headers.items())
        return (await service_instance.visitor_search(headers, item)).to_dict()

    @router.post("/visitor_get_a_post/", tags=["question_and_answer"])
    async def visitor_get_a_post(request: Request, item: Get_A_Post_Request) -> Get_A_Post_Response:
        item = Get_A_Post_Request().from_dict(item.to_dict())
        headers = dict(request.headers.items())
        return (await service_instance.visitor_get_a_post(headers, item)).to_dict()

    @router.post("/visitor_get_comment_list_by_id_list/", tags=["question_and_answer"])
    async def visitor_get_comment_list_by_id_list(request: Request, item: Get_Comment_List_By_Id_List_Request) -> Get_Comment_List_By_Id_List_Response:
        item = Get_Comment_List_By_Id_List_Request().from_dict(item.to_dict())
        headers = dict(request.headers.items())
        return (await service_instance.visitor_get_comment_list_by_id_list(headers, item)).to_dict()

    @router.post("/user_add_post/", tags=["question_and_answer"])
    async def user_add_post(request: Request, item: Add_Post_Request) -> Add_Post_Response:
        item = Add_Post_Request().from_dict(item.to_dict())
        headers = dict(request.headers.items())
        return (await service_instance.user_add_post(headers, item)).to_dict()

    @router.post("/user_comment_post/", tags=["question_and_answer"])
    async def user_comment_post(request: Request, item: Comment_Post_Request) -> Comment_Post_Response:
        item = Comment_Post_Request().from_dict(item.to_dict())
        headers = dict(request.headers.items())
        return (await service_instance.user_comment_post(headers, item)).to_dict()

    @router.post("/user_download_backup_data/", tags=["question_and_answer"])
    async def user_download_backup_data(request: Request, item: Download_Backup_Data_Request) -> Download_Backup_Data_Response:
        item = Download_Backup_Data_Request().from_dict(item.to_dict())
        headers = dict(request.headers.items())
        return (await service_instance.user_download_backup_data(headers, item)).to_dict()

    @router.post("/admin_download_backup_data/", tags=["question_and_answer"])
    async def admin_download_backup_data(request: Request, item: Admin_Download_Backup_Data_Request) -> Admin_Download_Backup_Data_Response:
        item = Admin_Download_Backup_Data_Request().from_dict(item.to_dict())
        headers = dict(request.headers.items())
        return (await service_instance.admin_download_backup_data(headers, item)).to_dict()

    @router.post("/admin_upload_backup_data/", tags=["question_and_answer"])
    async def admin_upload_backup_data(request: Request, item: Admin_Upload_Backup_Data_Request) -> Admin_Upload_Backup_Data_Response:
        item = Admin_Upload_Backup_Data_Request().from_dict(item.to_dict())
        headers = dict(request.headers.items())
        return (await service_instance.admin_upload_backup_data(headers, item)).to_dict()


def run(service_instance: Any, port: str, html_folder_path: str="", serve_html_under_which_url: str="/", only_return_app: bool = False):
    router = APIRouter()

    init(service_instance=service_instance, router=router)

    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(
        router,
        prefix="/question_and_answer",
    )

    if (html_folder_path != ""):
        if os.path.exists(html_folder_path) and os.path.isdir(html_folder_path):
            app.mount(serve_html_under_which_url, StaticFiles(directory=html_folder_path, html = True), name="web")
            @app.get(serve_html_under_which_url, response_model=str)
            async def index_page():
                return FileResponse(os.path.join(html_folder_path, 'index.html'))
            @app.exception_handler(404) #type: ignore
            async def custom_404_handler(_, __): #type: ignore
                return FileResponse(os.path.join(html_folder_path, 'index.html'))
            print(f"The website is running at: http://127.0.0.1:{port}/")
        else:
            print(f"Error: You should give me an absolute html_folder_path than {html_folder_path}")

    if only_return_app == True:
        return app

    print(f"You can see the docs here: http://127.0.0.1:{port}/docs")
    uvicorn.run( #type: ignore
        app=app,
        host="0.0.0.0",
        port=int(port)
    )


if __name__ == "__main__":
    service_instance = Service_question_and_answer()
    run(service_instance, port="6060")
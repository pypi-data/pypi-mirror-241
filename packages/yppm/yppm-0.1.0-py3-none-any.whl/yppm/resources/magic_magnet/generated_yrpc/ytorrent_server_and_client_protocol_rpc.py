from .ytorrent_server_and_client_protocol_objects import *


from fastapi import APIRouter, FastAPI, Request
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os


class Service_ytorrent_server_and_client_protocol:
    async def seed(self, headers: dict[str, str], item: Seed_Request) -> Seed_Response:
        default_response = Seed_Response()

        try:
            pass
        except Exception as e:
            print(f"Error: {e}")
            #default_response.error = str(e)
            #default_response.success = False

        return default_response

    async def search(self, headers: dict[str, str], item: Search_Request) -> Search_Response:
        default_response = Search_Response()

        try:
            pass
        except Exception as e:
            print(f"Error: {e}")
            #default_response.error = str(e)
            #default_response.success = False

        return default_response

    async def download_resource_info(self, headers: dict[str, str], item: Download_Resource_Info_Request) -> Download_Resource_Info_Response:
        default_response = Download_Resource_Info_Response()

        try:
            pass
        except Exception as e:
            print(f"Error: {e}")
            #default_response.error = str(e)
            #default_response.success = False

        return default_response

    async def download(self, headers: dict[str, str], item: Download_Request) -> Download_Response:
        default_response = Download_Response()

        try:
            pass
        except Exception as e:
            print(f"Error: {e}")
            #default_response.error = str(e)
            #default_response.success = False

        return default_response

    async def upload(self, headers: dict[str, str], item: Upload_Request) -> Upload_Response:
        default_response = Upload_Response()

        try:
            pass
        except Exception as e:
            print(f"Error: {e}")
            #default_response.error = str(e)
            #default_response.success = False

        return default_response

    async def get_shared_tracker_list(self, headers: dict[str, str], item: Get_Shared_Tracker_List_Request) -> Get_Shared_Tracker_List_Response:
        default_response = Get_Shared_Tracker_List_Response()

        try:
            pass
        except Exception as e:
            print(f"Error: {e}")
            #default_response.error = str(e)
            #default_response.success = False

        return default_response

    async def version(self, headers: dict[str, str], item: Version_Request) -> Version_Response:
        default_response = Version_Response()

        try:
            pass
        except Exception as e:
            print(f"Error: {e}")
            #default_response.error = str(e)
            #default_response.success = False

        return default_response


def init(service_instance: Any, router: Any):
    @router.post("/seed/", tags=["ytorrent_server_and_client_protocol"])
    async def seed(request: Request, item: Seed_Request) -> Seed_Response:
        item = Seed_Request().from_dict(item.to_dict())
        headers = dict(request.headers.items())
        return (await service_instance.seed(headers, item)).to_dict()

    @router.post("/search/", tags=["ytorrent_server_and_client_protocol"])
    async def search(request: Request, item: Search_Request) -> Search_Response:
        item = Search_Request().from_dict(item.to_dict())
        headers = dict(request.headers.items())
        return (await service_instance.search(headers, item)).to_dict()

    @router.post("/download_resource_info/", tags=["ytorrent_server_and_client_protocol"])
    async def download_resource_info(request: Request, item: Download_Resource_Info_Request) -> Download_Resource_Info_Response:
        item = Download_Resource_Info_Request().from_dict(item.to_dict())
        headers = dict(request.headers.items())
        return (await service_instance.download_resource_info(headers, item)).to_dict()

    @router.post("/download/", tags=["ytorrent_server_and_client_protocol"])
    async def download(request: Request, item: Download_Request) -> Download_Response:
        item = Download_Request().from_dict(item.to_dict())
        headers = dict(request.headers.items())
        return (await service_instance.download(headers, item)).to_dict()

    @router.post("/upload/", tags=["ytorrent_server_and_client_protocol"])
    async def upload(request: Request, item: Upload_Request) -> Upload_Response:
        item = Upload_Request().from_dict(item.to_dict())
        headers = dict(request.headers.items())
        return (await service_instance.upload(headers, item)).to_dict()

    @router.post("/get_shared_tracker_list/", tags=["ytorrent_server_and_client_protocol"])
    async def get_shared_tracker_list(request: Request, item: Get_Shared_Tracker_List_Request) -> Get_Shared_Tracker_List_Response:
        item = Get_Shared_Tracker_List_Request().from_dict(item.to_dict())
        headers = dict(request.headers.items())
        return (await service_instance.get_shared_tracker_list(headers, item)).to_dict()

    @router.post("/version/", tags=["ytorrent_server_and_client_protocol"])
    async def version(request: Request, item: Version_Request) -> Version_Response:
        item = Version_Request().from_dict(item.to_dict())
        headers = dict(request.headers.items())
        return (await service_instance.version(headers, item)).to_dict()


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
        prefix="/ytorrent_server_and_client_protocol",
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
    service_instance = Service_ytorrent_server_and_client_protocol()
    run(service_instance, port="6060")
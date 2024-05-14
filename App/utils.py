from pathlib import Path


def get_upload_path(filename):
    home_path = Path(__file__).parent
    upload_path = home_path.joinpath("static", "upload")
    # 创建上传目录（如果不存在）
    upload_path.mkdir(parents=True, exist_ok=True)
    # 返回完整的文件路径
    return upload_path.joinpath(filename)

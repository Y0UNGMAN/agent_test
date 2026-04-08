import os
from huggingface_hub import snapshot_download

def download_model():
    # Hugging Face 上的模型仓库 ID
    model_id = "openai/gpt-oss-20b"
    # 指定您想保存模型的本地目录
    save_dir = "./models/gpt-oss-20b"
    
    # 确保保存目录存在
    os.makedirs(save_dir, exist_ok=True)
    
    print(f"正在准备下载 {model_id}...")
    print("由于 20B 模型文件体积较大，下载可能需要较长时间。")
    print("（提示：脚本默认支持断点续传，如果意外中断，重新运行即可）")
    
    # 开始下载
    snapshot_download(
        repo_id=model_id,
        local_dir=save_dir,
        max_workers=8  # 设置多线程数量以加速下载
    )
    
    print(f"\n🎉 下载完成！模型已保存在: {os.path.abspath(save_dir)}")

if __name__ == "__main__":
    download_model()
import yt_dlp

video_url = "https://cn.pornhub.com/view_video.php?viewkey=660f28d950cb4"

# 配置下载参数
ydl_opts = {
    "format": "best",  # 选择最佳质量
    "outtmpl": "%(title)s.%(ext)s",  # 输出文件格式
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])
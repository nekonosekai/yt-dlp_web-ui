import gradio as gr
from yt_dlp import YoutubeDL

def video_download(video_url,video_format,audio_format):
  url_list = list(map(str,video_url.split()))
  option = {
      'outtmpl':'/content/%(title)s.%(ext)s',
      'format' : 'bv{}+ba{}/bv+ba'.format(video_format,audio_format)
  }
  ydl=YoutubeDL(option)
  result = ydl.download(url_list)
  return "ダウンロードが開始されました　詳しくはGoogle Colabの出力欄を御覧ください"

with gr.Blocks() as app:
  gr.Markdown(
      """
      <h1 style="text-align: center;">Youtube Download</h1>
      <div style="text-align: center;">動画/音声をダウンロードする 広告はもちろんなし </div>
      <div style="text-align:center;">ちなみに対応しているのはYoutubeだけではありません 詳しくは
        <a href="https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md" target="_blank">こちら</a>
      </div>
      """
  )

  with gr.Tab("動画をダウンロードする"):
    #コンポーネント
    gr.Markdown(
        """
        <div style="text-align: center;"> ここではURLから動画をダウンロードできます</div>
        """
    )
    url = gr.Textbox(label="動画のURLをここに入力してください(複数指定可能です)")
    with gr.Row():
      submit_btn = gr.Button("ダウンロードする",scale=3)
      clear_input = gr.ClearButton([url],value="URL欄をクリアする(全消し)",scale=1)

    with gr.Row():
      video_format = gr.Dropdown(["mp4","webm"],label="動画の保存形式を選択してください",value="mp4")
      audio_format = gr.Dropdown(["m4a","wav","mp3"],label="音声の保存形式を選択してください",value="m4a")

    #イベントリスナー
    output = gr.Textbox(label="ここに出力が表示されます")
    submit_btn.click(fn=video_download,inputs=[url,video_format,audio_format],outputs=output)

app.launch(share=True)

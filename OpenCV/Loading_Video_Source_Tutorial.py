import numpy as np
import cv2

# こちらはwebcam(0番目)からの映像を流します。
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while(True):
    # このコードでは継続的に映像を撮り続ける
    ret, frame = cap.read()
    # ここで画面をグレーに変換してくれる変数を指定します。
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # outとして指定された映像にframeを書き込みます。
    out.write(frame)
    # ビデオストリームにも関わらずimshowで画面をみれます。
    cv2.imshow('frame', gray)
    # この文章はビデオストリーム中に一回だけ実行されます。
    # もし、qを推したらloopがbreakされるように設定するソースです。
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break;

# Webcamをreleaseします。
cap.release()
# out作用をreleaseします。
out.release()
# すべてのビデオウィンドウを終了します。
cv2.destroyAllWindows()

# yolotinyv4_custom_dataset
---

Helper repository to train tiny yolo v4 on custom data in Google Colaboratory notebook.

## How to use
1. Fork this repository and rename it(eg. yolotinyv4_robocon2021).
2. Clone the repository on your local PC and put images(.jpg) and annotations(.txt) into _obj_ folder in the cloned repository.
3. Push the repository containing images and annotations of objects you want to detect.
4. Clone the updated repository in Google Colaboratory notebook.

## Caution
Please avoid to edit obj.data or obj.names directly, or it may cause errors.

---

カスタムデータセットを用いた，Yolov4-tinyのファインチューニング用Google Colaboratory notebookに用いる補助リポジトリです．

## 使用方法
1. このリポジトリをフォークして，名前を変更する(例. yolotinyv4_robocon2021).
2. ローカルPCにリポジトリをクローンし，画像ファイル(.jpg)とアノテーションファイル(.txt)を，クローンしたリポジトリ内にある _obj_ フォルダーに入れる．
3. 検出したい物体の画像やアノテーションファイルが入ったリポジトリをプッシュ．
4. 更新したリポジトリを，Google Colaboratory notebook内でクローンする．

## 注意
エラーの原因になる可能性があるため，obj.dataやobj.namesファイルの直接的な編集は避けてください．

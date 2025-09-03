# 作成開始日：2025年9月1日
# 作成完了日：2025年9月3日
# 著作者名：yuuki-hiroshima
# All rights reserved.

# ChatGPT 「数当てゲーム作成方法」を参照
# 予定：スタートを準備する。エンターキーで「予想する」ボタンを押せるようにする。

# -------------------------------
# 1. 必要なモジュールやフォントを追加
# -------------------------------

# GUIを作るTkinterモジュールをインポート
import tkinter as tk

# randomモジュール（ライブラリ）をインポート
import random

# グラフ描画ライブラリを読み込む
import matplotlib.pyplot as plt

# グラフ描画ライブラリを読み込む（文字化けしたため追加）
import matplotlib as mpl

# Macで日本語が文字化けしないようにフォントを追加
mpl.rcParams['font.family'] = 'Hiragino Sans'

# -------------------------------
# 2. ゲームの初期設定
# -------------------------------

LOW,HIGH = 1, 100 # 数字の範囲（難易度によって変更）
LIMIT = 10 # 最大挑戦回数
answer = None # 正解の数字（ゲーム開始時に設定）
count = 0 # 入力回数のカウント
history = [] # 予想した履歴の保存

# -------------------------------
# 3. ゲーム開始・リセット処理
# -------------------------------

def start_game(mode=None): # ゲームを初期化する関数（modeは難易度選択）
    global LOW, HIGH, LIMIT, answer, count, history

    if mode == "1": # かんたんモード
        LOW, HIGH = 1, 50 # 範囲を指定
    elif mode == "2": # ふつうモード
        LOW, HIGH = 1, 100 # 範囲を指定
    elif mode == "3": # むずかしいモード
        LOW, HIGH = 1, 500 # 範囲を指定
    else: # デフォルトとして判定
        LOW, HIGH = 1, 100 # 範囲を指定

    # 選んだ難易度に応じた数字をゲームに当てはめる
    answer = random.randint(LOW, HIGH) # randint関数はランダムな小数・整数を生成する。randint関数はrandomモジュールのなかに含まれるため、randomモジュールのインポートが必要
    count = 0 # 回数をリセット
    history = [] # 履歴をリセット

    # ラベルを初期化
    info_label.config(text=f"{LOW}〜{HIGH}の数字を当ててください。最大{LIMIT}回です。")
    msg_label.config(text="")
    history_label.config(text="")
    entry.delete(0, tk.END)
    guess_button.config(state=tk.NORMAL)  # ボタン有効化

# -------------------------------
# 4. 予想チェック処理
# -------------------------------

def check_guess(): # 入力した数字を判定してメッセージと履歴を更新する
    global count, history

    guess_text = entry.get() # 入力取得
    entry.delete(0, tk.END) # 入力欄クリア

    try:
        guess = int(guess_text) # 入力を整数に変換（小数や文字列が入力されるなど、エラーが出る可能性のあるコード）
    except ValueError: # 変換できない場合（文字列や小数など）
        msg_label.config(text="整数を入力してください") # エラーメッセージ
        return
    
    # 範囲チェック
    if guess < LOW or guess > HIGH:
        msg_label.config(text=f"{LOW}〜{HIGH}の範囲で入力してください。")
        return # カウント増えずに再入力


    # ここから先は有効な入力だけが通る
    count += 1 # 入力がおこなわれるごと（ループするごと）にカウントを1増やす
    history.append(guess) # 入力した予想を履歴リストに追加
    remaining = LIMIT - count # 残り回数を計算する

    # 判定の処理
    if guess == answer:
        msg_label.config(text=f"おめでとう！正解は{answer}です。{count}回で当たりました！")
        guess_button.config(state=tk.DISABLED)
        show_history()
        show_graph()
    elif count >= LIMIT:
        msg_label.config(f"残念！ゲームオーバーです。正解は{answer}でした。")
        guess_button.config(state=tk.DISABLED)
        show_history()
        show_graph()
    elif guess < answer:
        msg_label.config(text=f"もっと大きい数字です。残り{remaining}回")
    else:
        msg_label.config(text=f"もっと小さい数字です。残り{remaining}回")

# -------------------------------
# 5. 履歴表示処理
# -------------------------------

def show_history(): # 正解までの予想履歴を表示
    hist_text = "これまでの予想: " + ", ".join(f"{i+1}回目:{v}" for i,v in enumerate(history))
    history_label.config(text=hist_text)

# -------------------------------
# 6. グラフ表示処理
# -------------------------------

def show_graph(): # 正解までの履歴を折れ線グラフで表示
    turns = list(range(1, len(history) + 1)) # 1回目,2回目と結果をリスト化
    plt.plot(turns, history, marker="o", label="予想した数字") # 折れ線グラフを描画
    plt.axhline(y=answer, color="r", linestyle="--", label="正解") # 正解の位置に横線を引く
    plt.xlabel("回数") # x軸ラベル
    plt.ylabel("予想した数字") # y軸ラベル
    plt.title("数当てゲームの履歴") # グラフタイトル
    plt.legend() # 凡例を表示
    plt.grid(True) # グリッド線を表示
    plt.show() # グラフを表示

# -------------------------------
# 7. GUIウィンドウ作成
# -------------------------------

root = tk.Tk()
root.title("数当てゲーム for Python")

# --- 難易度選択ボタン ---
difficulty_fame = tk.Frame(root)
difficulty_fame.pack(pady=10)
tk.Label(difficulty_fame, text="難易度選択:").pack(side=tk.LEFT)
tk.Button(difficulty_fame, text="簡単", command=lambda: start_game("1")).pack(side=tk.LEFT)
tk.Button(difficulty_fame, text="普通", command=lambda: start_game("2")).pack(side=tk.LEFT)
tk.Button(difficulty_fame, text="難しい", command=lambda: start_game("3")).pack(side=tk.LEFT)

# --- 説明ラベル---
info_label = tk.Label(root, text="")
info_label.pack(pady=5)

# --- 入力欄 ---
entry = tk.Entry(root)
entry.pack(pady=5)

# --- 予想ボタン ---
guess_button = tk.Button(root, text="予想する", command=check_guess)
guess_button.pack(pady=5)

# --- メッセージラベル ---
msg_label = tk.Label(root, text="")
msg_label.pack(pady=5)

# --- 履歴ラベル ---
history_label = tk.Label(root, text="")
history_label.pack(pady=5)

# --- リプレイボタン ---
repay_button = tk.Button(root, text="ゲームリセット", command=lambda: start_game())
repay_button.pack(pady=10)

# --- 初回ゲーム開始 ---
start_game()

# --- GUI開始 ---
root.mainloop()
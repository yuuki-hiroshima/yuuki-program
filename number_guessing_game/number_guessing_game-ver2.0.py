# 作成開始日：2025年9月1日
# 作成完了日：2025年9月1日
# 著作者名：yuuki-hiroshima
# All rights reserved.

# ChatGPT 「数当てゲーム作成方法」を参照
# 正解するまでに回答した回数を表示できるようアップデート

# randomモジュール（ライブラリ）をインポート
import random

# 1〜100のなかから、ランダムに数字を決める
answer = random.randint(1, 100) # randint関数はランダムな小数・整数を生成する。randint関数はrandomモジュールのなかに含まれるため、randomモジュールのインポートが必要

# 上記は冒頭で「from random import randint」としている場合、answer = randint(1, 100)と記述しても動作する。

print("数当てゲームを始めます！") # ゲーム開始のメッセージ
print("1〜100の数字を当ててください。") # ユーザーへのルール説明

# 挑戦回数を超える変数（最初は0回）
count = 0

# 正解するまで入力を繰り返す
while True:
    guess = input("あなたの予想は？：") # ユーザーに入力してもらう
    guess = int(guess) #入力された文字を数値に変換
    count += 1 # 入力がおこなわれるごと（ループするごと）にカウントを1増やす

    # 答えと比較
    if guess == answer:
        print("おめでとう！正解です！")
        print(f"{count}回目で当たりました！") # f文字列で回数を表示
        break # 正解したらループを終了
    elif guess > answer: # 入力された数値より小さい場合
        print("もっと小さい数字です。")
    else: # 入力された数値より小さい場合以外（入力された数字より大きい場合）
        print("もっと大きい数字です")